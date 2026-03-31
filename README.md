# __Overview__
### This project implements a Retrieval-Augmented Generation (RAG) system that acts as a Prerequisite & Course Planning Assistant. It answers student queries using academic catalog documents and ensures responses are grounded, citation-based, and reliable. The system retrieves relevant course and program information from documents and uses an LLM to generate structured, context-aware answers.
# __Features__
. Answers prerequisite-related queries
. Generates course planning suggestions
. Provides citations for every response
. Handles missing information with clarifying questions
. Avoids hallucination (safe “don’t know” responses)
. Built using LangChain + FAISS + Streamlit
