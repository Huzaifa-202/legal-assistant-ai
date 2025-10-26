# ⚖️ AI Lawyer – Legal Document Q&A Assistant

AI Lawyer is a legal chatbot built using Retrieval-Augmented Generation (RAG) and the DeepSeek R1 model. It allows users to upload legal PDF documents and interactively ask questions, receiving context-aware, accurate answers grounded in the uploaded text.

---

## 🚀 Features

- 📄 Upload any legal PDF document  
- 🧠 Semantic search using FAISS vector store  
- 🔍 Retrieve relevant context using LangChain  
- 💬 Ask legal questions in natural language  
- ✅ Accurate responses with reduced hallucination  
- 🖥️ Interactive UI powered by Streamlit  
- ⚙️ Uses local embedding via Ollama and LLM via GROQ (DeepSeek R1)  

---


## 🖥️ User Interface Preview

Here’s a glimpse of the AI Lawyer web interface built using Streamlit:

### 📄 Upload Section

<img width="956" height="268" alt="upload" src="https://github.com/user-attachments/assets/227ec523-f0db-4316-93be-a29e992058b5" />


### 💬 Ask Legal Questions

<img width="882" height="175" alt="question" src="https://github.com/user-attachments/assets/ae3b0b8e-bb8f-4406-a407-6e627020314e" />


### 🤖 AI Response

<img width="852" height="436" alt="answers" src="https://github.com/user-attachments/assets/226a4cf9-0366-4f01-b8ea-6e5d10dc662f" />


---


## 🧱 Project Architecture

User Uploads PDF  
  ↓  
PDF → Text → Chunks  
  ↓  
Chunks → Embeddings → FAISS Index  
  ↓  
Query → Similarity Search → Retrieved Docs  
  ↓  
Prompt + Docs → DeepSeek LLM → Final Answer  

---

## 🛠️ Tech Stack

| Layer               | Tool/Library              |
|--------------------|---------------------------|
| LLM                | DeepSeek R1 (via Groq)     |
| Embeddings         | Ollama (DeepSeek R1 1.5b)  |
| Framework          | LangChain                 |
| Vector Store       | FAISS                     |
| PDF Parsing        | PDFPlumber + LangChain    |
| UI                 | Streamlit                 |
| Deployment         | Docker                    |

---

## 🧪 How to Use

### Prerequisites

- Python 3.10+
- Docker (for containerized deployment)
- GROQ API Key
- Ollama installed with `nomic-embed-text` model pulled

### Setup (Local)

1. Clone the repo:  
   git clone https://github.com/your-username/legal-assistant-ai.git  
   cd legal-assistant-ai  

2. Create `.env` file and add your API key:  
   GROQ_API_KEY=your_api_key_here  

3. Install dependencies:  
   pip install -r requirements.txt  

4. Start the app:  
   streamlit run frontend.py  

---

## 🐳 Docker Instructions

### Build the Docker image  
docker build -t ai-lawyer-app .

### Run the container  
docker run -p 8501:8501  
-e GROQ_API_KEY=your_api_key_here  
-v ${PWD}/pdfs:/app/pdfs  
-v ${PWD}/vectorstore:/app/vectorstore  
ai-lawyer-app

### Or use docker-compose  
docker compose up

---

## 🐳 Docker Image

You can directly pull and run the prebuilt image from Docker Hub:

👉 [View on Docker Hub](https://hub.docker.com/r/huzaifaasad/ai-lawyer-app)
https://claude.ai/oauth/authorize?code=true&client_id=9d1c250a-e61b-44d9-88ed-5944d1962f5e&response_type=code&scope=org%3Acreate_api_key+user%3Aprofile+user%3Ainference&code_challenge=9a0FoT3tjNqaMv1m6BPP_BE6cy84Gfr7N-O_KlaEd2A&code_challenge_method=S256&state=PoXei2ilcWsTMoC9_-RHyaGFDf6PKYcVMAGe4F3p0hs&redirect_uri=https%3A%2F%2Fconsole.anthropic.com%2Foauth%2Fcode%2Fcallback
### Pull the image:  
docker pull huzaifaasad/ai-lawyer-app:latest

### Run the container:  
docker run -p 8501:8501 -e GROQ_API_KEY=your_api_key_here huzaifaasad/ai-lawyer-app:latest

---

## 📂 Project Structure

legal-assistant-ai/  
├── frontend.py             → Streamlit UI  
├── vector_database.py      → PDF loader, splitter, embeddings, FAISS setup  
├── rag_pipeline.py         → LLM setup, doc retrieval, prompt chaining  
├── requirements.txt  
├── dockerfile  
├── docker-compose.yml  
├── .env                    → GROQ API Key (not committed)  
├── .gitignore  
├── .gitattributes  
├── pdfs/                   → Uploaded PDFs  
└── vectorstore/            → FAISS vector database  

---

## 📚 What is RAG?

RAG (Retrieval-Augmented Generation) enhances LLMs by retrieving contextually relevant information from custom knowledge bases (like PDFs) before generating a response. This helps:  
- 📌 Reduce hallucinations  
- 📌 Improve factual accuracy  
- 📌 Enable private/custom document Q&A  

---

## 🔐 Security Note

Make sure your `.env` file containing the API key is excluded from version control. The `.gitignore` already handles this.

---

## 📎 Credits

- DeepSeek R1 – Groq-hosted reasoning LLM  
- Ollama – Local model serving for embeddings  
- LangChain – Framework for chaining retrieval & generation  
- Streamlit – UI for real-time legal chat  
- FAISS – Fast vector search for document similarity  

---

## 📄 License

This project is open source and available under the MIT License.
