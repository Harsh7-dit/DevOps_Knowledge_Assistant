from ingestion.loader import load_documents
from ingestion.chunker import split_documents
from ingestion.embedder import get_embeddings
from ingestion.langchain.vectorstores import Chroma

def run_pipeline(file_path):
    docs = load_documents(file_path)
    chunks = split_documents(docs)

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory="./vectorstore"
    )

    vectorstore.persist()
    print("Ingestion complete!")