import chromadb
from langchain_ollama import OllamaEmbeddings

from config import CHROMA_PATH, OLLAMA_URL

embedding_model = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url=OLLAMA_URL
)

client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = client.get_collection("hr_policies")


class PolicyService:

    def search(self, query):

        embedding = embedding_model.embed_query(query)

        results = collection.query(
            query_embeddings=[embedding],
            n_results=3
        )

        return results
