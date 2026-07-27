import os

from langchain_community.document_loaders import TextLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings


############################################################
# Embedding Model
############################################################

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

############################################################
# Read all txt files
############################################################

documents = []

docs_folder = "docs"

for file in os.listdir(docs_folder):

    if file.endswith(".txt"):

        loader = TextLoader(
            os.path.join(docs_folder, file),
            encoding="utf-8"
        )

        documents.extend(loader.load())

############################################################
# Split Documents
############################################################

splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,
    chunk_overlap=50

)

docs = splitter.split_documents(documents)

############################################################
# Create ChromaDB
############################################################

db = Chroma.from_documents(

    documents=docs,

    embedding=embeddings,

    persist_directory="chroma_db"

)

print("Knowledge Base Created Successfully")

print("Documents Loaded :", len(documents))

print("Chunks Created :", len(docs))
