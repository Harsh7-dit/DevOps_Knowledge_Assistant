from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

db = Chroma(
    persist_directory="./vectorstore",
    embedding_function=OllamaEmbeddings(model="nomic-embed-text")
)

data = db.get(include=["embeddings", "documents", "metadatas"])

print("Total Documents:", len(data['documents']))
print("Embedding Dimension:", len(data['embeddings'][0]))

print("")

print("\nSample Document:\n", data['documents'][0])
print("\nSample Embedding:\n", data['embeddings'][0][:10])

embeddings = data['embeddings']

print(len(embeddings))       # number of vectors
print(len(embeddings[0]))    # dimension (e.g., 384/768)
print(embeddings[0])    # first 10 values
