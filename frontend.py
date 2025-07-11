import streamlit as st
from rag_pipeline import answer_query, retrieve_docs, llm_model

# ----------------- Page Setup -----------------
st.set_page_config(page_title="⚖️ AI Lawyer", page_icon="📘", layout="centered")

# ----------------- CSS Styling -----------------
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }

    .main {
        background-color: #f0f2f6;
    }

    .stButton > button {
        background-color: #1f4e79;
        color: white;
        font-weight: 600;
        font-size: 16px;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        transition: 0.3s ease-in-out;
        border: none;
    }

    .stButton > button:hover {
        background-color: #163d5c;
    }

    .stTextArea textarea {
        border-radius: 10px;
        border: 1px solid #ccc;
        font-size: 15px;
    }

    .stFileUploader {
        border-radius: 8px;
    }

    .chat-bubble-user {
        background-color: #e8f4fd;
        color: #154360;
        padding: 15px 20px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .chat-bubble-ai {
        background-color: #e6f9ed;
        color: #0b5345;
        padding: 15px 20px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .header {
        text-align: center;
        color: #1f4e79;
        font-size: 36px;
        margin-bottom: 0;
        font-weight: 700;
    }

    .subheader {
        text-align: center;
        color: #6c757d;
        font-size: 16px;
        margin-top: 0;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- Header -----------------
st.markdown("<h1 class='header'>⚖️ AI Lawyer</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Upload a legal PDF and consult your AI-powered legal assistant</p>", unsafe_allow_html=True)

st.divider()

# ----------------- PDF Upload -----------------
uploaded_file = st.file_uploader("📄 Upload your legal PDF", type="pdf", accept_multiple_files=False)

# ----------------- User Input -----------------
user_query = st.text_area("💬 Your Legal Question:", height=150, placeholder="e.g., What does Article 19 guarantee?")
ask_question = st.button("🔍 Ask AI Lawyer")

# ----------------- RAG Pipeline -----------------
if ask_question:
    if uploaded_file and user_query.strip() != "":
        st.markdown(f"<div class='chat-bubble-user'><b>🧑‍💼 You:</b><br>{user_query}</div>", unsafe_allow_html=True)

        retrieved_docs = retrieve_docs(user_query)
        response = answer_query(documents=retrieved_docs, model=llm_model, query=user_query)

        st.markdown(f"<div class='chat-bubble-ai'><b>🤖 AI Lawyer:</b><br>{response}</div>", unsafe_allow_html=True)

    else:
        st.error("📌 Please upload a valid PDF and enter your question.")

# ----------------- Footer -----------------
st.divider()
st.markdown("<p style='text-align: center; font-size: 13px;'>🧠 Powered by <b>LangChain</b>, <b>Ollama</b>, <b>Groq</b>, and <b>Streamlit</b></p>", unsafe_allow_html=True)
