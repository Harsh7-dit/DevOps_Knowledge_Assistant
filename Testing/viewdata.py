from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

# Load existing DB
db = Chroma(
    persist_directory="./vectorstore",
    embedding_function=OllamaEmbeddings(model="nomic-embed-text")
)

docs = db.get()

print(docs.keys())

print(docs['documents'][:3])

print("")

embeddings = docs['embeddings']

#print(len(embeddings))       # number of vectors
#print(len(embeddings[0]))    # dimension (e.g., 384/768)
print(embeddings[0][:10])    # first 10 values
