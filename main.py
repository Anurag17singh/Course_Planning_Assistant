import streamlit as st
import os
import time

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader

# Load environment variables
load_dotenv()

# LLM setup
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.0,
    api_key=os.getenv("GEMINI_API_KEY")
)

# Fast embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Prompt template
prompt = ChatPromptTemplate.from_template("""
You are an academic course planning assistant.

STRICT RULES:
- Use ONLY provided context
- Always include citations
- If missing info → ask questions
- If not found → say "I don’t have that information"

<context>
{context}
<context>

Question: {input}
""")

# Function to create vector DB
def create_vector_embedding():
    loader = PyPDFDirectoryLoader("RAG_Data")
    docs = loader.load()[:50]

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    final_docs = splitter.split_documents(docs)

    vectors = FAISS.from_documents(final_docs, embeddings)
    return vectors

# UI
st.title("RAG With Gemini (Main)")

user_prompt = st.text_input("Enter your query")

# Button to process documents
if st.button("Process Documents"):
    with st.spinner("Processing documents..."):
        st.session_state.vectors = create_vector_embedding()
    st.success("Vector Database is ready ")

# Query handling
if user_prompt:
    if "vectors" not in st.session_state:
        st.error(" Please click 'Process Documents' first")
        st.stop()

    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever(search_kwargs={"k": 4})
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    with st.spinner("Generating response..."):
        start = time.process_time()
        response = retrieval_chain.invoke({'input': user_prompt})
        end = time.process_time()

    st.write(response['answer'])
    st.write(f"⏱️ Response time: {end - start:.2f} sec")

    with st.expander("Document similarity Search"):
        for doc in response['context']:
            st.write(doc.page_content)
            st.write("------------------------")