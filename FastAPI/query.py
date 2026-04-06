from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import OllamaLLM

def load_vectorstore():
    return Chroma(
        persist_directory="./vectorstore",
        embedding_function=OllamaEmbeddings(model="nomic-embed-text")
    )


# Load the LLM

def load_llm():
    return OllamaLLM(model="tinyllama")

def ask_question(query):
    db = load_vectorstore()
    retriever = db.as_retriever(search_kwargs={"k": 3})
    llm = load_llm()

    # Step 1: Retrieve documents
    docs = retriever.get_relevant_documents(query)

    # Step 2: Extract context (chunks)
    context_chunks = [doc.page_content for doc in docs]

    context_text = "\n\n".join(context_chunks)

    # Step 3: Extract sources
    sources = list(set([
        doc.metadata.get("source", "Unknown")
        for doc in docs
    ]))

    # Step 4: Prompt
    prompt = f"""
    You are a DevOps expert.

    Answer ONLY based on the context below.
    If the answer is not present, say "I don't know".

    Context:
    {context_text}

    Question:
    {query}
    """

    # Step 5: Generate answer
    response = llm.invoke(prompt)

    return {
        "answer": str(response),
        "sources": sources,
        "context": context_chunks
    }
