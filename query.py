from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os

load_dotenv()

# Loading vector DB
def load_vectorstore():
    return Chroma(
        persist_directory="./vectorstore",
        embedding_function=OllamaEmbeddings(model="nomic-embed-text")
    )

#Create Retriever with k = 3 for top 3 relevant chunks
def get_retriever(db):
    return db.as_retriever(search_kwargs={"k": 3})

# Load the LLM

def load_llm():
    return OllamaLLM(model="tinyllama")

# Query Function
def ask_question(query):
    db = load_vectorstore()
    retriever = get_retriever(db)
    llm = load_llm()

    # Retrieve relevant docs
    docs = retriever.get_relevant_documents(query)

    # Combine context
    context = "\n\n".join([doc.page_content for doc in docs])

    # Prompt
    prompt = f"""
    Answer the question based only on the context below.

    Context:
    {context}

    Question:
    {query}
    """

    # Generate response
    response = llm.invoke(prompt)

    return response

if __name__ == "__main__":
    question = "What is Kubernetes master node?"
    answer = ask_question(question)

    print("\nAnswer:\n", answer)
