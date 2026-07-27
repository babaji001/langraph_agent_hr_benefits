import chromadb
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path="./chroma_db")

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.get_collection(
    "hr_docs",
    embedding_function=embedding_function
)

results = collection.query(
    query_texts=[
        "Who is eligible for FMLA?"
    ],
    n_results=2
)

print(results["documents"])
