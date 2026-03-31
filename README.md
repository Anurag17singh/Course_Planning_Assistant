##  Overview
This project implements a **Retrieval-Augmented Generation (RAG)** system that acts as a **Prerequisite & Course Planning Assistant**. It answers student queries using academic catalog documents and ensures responses are **grounded, citation-based, and reliable**.

The system retrieves relevant course and program information from documents and uses a Large Language Model (LLM) to generate structured, context-aware answers.

---
##  Features
-  Answers prerequisite-related queries  
-  Generates course planning suggestions  
-  Provides **citations for every response**  
-  Handles missing information with clarifying questions  
-  Avoids hallucination (safe “don’t know” responses)  
-  Built using **LangChain + FAISS + Streamlit**

---
## Architecture

### RAG Pipeline:
1. **Document Ingestion**
   - Loads PDF catalog documents

2. **Text Chunking**
   - Chunk size: `500`  
   - Overlap: `50`  

3. **Embeddings**
   - Model: `all-MiniLM-L6-v2` (fast + efficient)

4. **Vector Store**
   - FAISS for similarity search

5. **Retriever**
   - Top-k = `4` relevant chunks

6. **LLM**
   - Google Gemini (`gemini-2.5-flash`)

7. **Prompt Design**
   - Enforces:
     - grounded answers
     - citations
     - safe abstention
     - structured output

---

 
