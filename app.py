import streamlit as st
from langchain.chains import RetrievalQA
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_core.prompts import PromptTemplate
import os

groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM and Embeddings
llm = ChatGroq(model="llama3-8b-8192", api_key=groq_api_key)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load dataset
file_path = "mobile_packages.csv"
loader = CSVLoader(file_path=file_path)
docs = loader.load()

# Split documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
splits = text_splitter.split_documents(docs)

# Create an in-memory vector store
vectorstore = InMemoryVectorStore.from_documents(documents=splits, embedding=embeddings)
retriever = vectorstore.as_retriever()

# Define Prompt Template
prompt_template = PromptTemplate(
    template="""
    You are an assistant that helps with mobile packages. Use the following retrieved documents to answer the question:
    {context}
    Question: {question}
    Answer:
    """,
    input_variables=["context", "question"]
)

# Define QA Chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff", chain_type_kwargs={"prompt": prompt_template})

# Streamlit UI
st.set_page_config(page_title="Mobile Packages Assistant", page_icon="📱", layout="centered")
st.title("📱 Mobile Package Finder")
st.write("Ask about mobile packages based on your needs!")

# User input
query = st.text_input("Enter your query:")

if query:
    response = qa_chain.invoke({"query": query})
    st.subheader("Response:")
    st.write(response["result"])
