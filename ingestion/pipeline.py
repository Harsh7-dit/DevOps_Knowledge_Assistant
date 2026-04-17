from ingestion.loader import load_documents
from ingestion.chunker import split_documents
from ingestion.embedder import get_embeddings
from langchain_community.vectorstores import Chroma

def run_pipeline(file_path):
    #Step 1: Load documents
    docs = load_documents(file_path)

    #Step 2: Add metadata (VERY IMPORTANT)
    for doc in docs:
        doc.metadata["source"] = file_path

    #Step 3: Chunk documents
    chunks = split_documents(docs)

    #Step 4: Load existing vector DB
    vectorstore = Chroma(
        persist_directory="../vectorstore",
        embedding_function=get_embeddings()
    )

    #Step 5: Add new documents (APPEND, not overwrite)
    vectorstore.add_documents(chunks)

    print(f"✅ {file_path} ingested successfully!")
