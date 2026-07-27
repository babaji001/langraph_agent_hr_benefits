from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(

    persist_directory="chroma_db",

    embedding_function=embeddings

)


def search_policy(question):

    docs = db.similarity_search(question, k=3)

    answer = ""

    for doc in docs:

        answer += doc.page_content
        answer += "\n\n"

    return answer
