##  Overview
This project implements a **Retrieval-Augmented Generation (RAG)** system that acts as a **Prerequisite & Course Planning Assistant**. It answers student queries using academic catalog documents and ensures responses are **grounded, citation-based, and reliable**.

The system retrieves relevant course and program information from documents and uses a Large Language Model (LLM) to generate structured, context-aware answers.
[Data Used in this task](https://erp.iitkgp.ac.in/ERPWebServices/curricula/CurriculaSubjectsList.jsp?stuType=UG&splCode=CS)
[Data used in this task](https://www.iitkgp.ac.in/assets/pdf/stu_ad.pdf)

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

##  Project Structure
```
RAG_Project/
├── main.py
├── app.py
├── RAG_Data/
├── requirements.txt
├── README.md
└── .env
```

##  Setup Instructions

### 1️ Clone the Repository
```
git clone https://github.com/your-username/rag-course-assistant.git
cd rag-course-assistant
```

### 2. Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
```

### Install Dependencies
```
pip install -r requirements.txt
```

### 4. Environment Variable 
```
GEMINI_API_KEY=your_api_key_here
```

### 5. Add Data
```
RAG_DATA
```

### 6. Run the application
```
streamlit run app.py
```

## Usage
1. Open the app in your browser
2. Click "Process Documents"
3. Wait until the vector database is created
4. Enter your query (e.g., prerequisites, course planning)
5. View:
   - Answer
   - Supporting documnets chunks

## Future Improvements
- Save/load FAISS index (faster startup)
- Multi-agent architecture (retriever + planner + verifier)
- Chat-based UI
- Support for live web data

## Tech Stack 
- Python
- Streamlit
- LangChain
- FAISS
- HuggingFace Embeddings
- Google Gemini API
