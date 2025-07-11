from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import os

pdfs_directory = 'pdfs/'
os.makedirs(pdfs_directory, exist_ok=True)

ollama_model_name = "nomic-embed-text"

# Save uploaded file to local directory
def upload_pdf(file):
    file_path = os.path.join(pdfs_directory, file.name)
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())
    return file_path

# Load PDF contents
def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    return loader.load()

# Split into chunks
def create_chunks(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    return splitter.split_documents(documents)

# Get embedding model
def get_embedding_model():
    return OllamaEmbeddings(model=ollama_model_name)

# Create FAISS index from uploaded file
def create_faiss_index_from_uploaded_pdf(file):
    file_path = upload_pdf(file)
    docs = load_pdf(file_path)
    chunks = create_chunks(docs)
    embeddings = get_embedding_model()
    return FAISS.from_documents(chunks, embeddings)
