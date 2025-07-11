from langchain_groq import ChatGroq
from vector_database import create_faiss_index_from_uploaded_pdf
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm_model = ChatGroq(model="deepseek-r1-distill-llama-70b")

# Prompt template
custom_prompt_template = """
Use the information below to answer the user's legal question.
If the answer is not in the context, say "I don’t know".
Don't make up answers or go beyond the context.

Question: {question}
Context: {context}
Answer:
"""

def get_context(documents):
    return "\n\n".join([doc.page_content for doc in documents])

# Retrieve docs from uploaded PDF
def retrieve_docs(query, vectorstore):
    return vectorstore.similarity_search(query)

# Main RAG logic
def answer_query(uploaded_file, query):
    vectorstore = create_faiss_index_from_uploaded_pdf(uploaded_file)
    documents = retrieve_docs(query, vectorstore)
    context = get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    chain = prompt | llm_model
    return chain.invoke({"question": query, "context": context})
