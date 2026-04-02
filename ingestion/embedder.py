from langchain.embeddings import OllamaEmbeddings

def get_embeddings():
    return OllamaEmbeddings(model="nomic-embed-text")