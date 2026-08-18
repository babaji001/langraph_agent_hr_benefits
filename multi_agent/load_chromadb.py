from pathlib import Path

import chromadb

from langchain_ollama import OllamaEmbeddings

from config import (
    CHROMA_PATH,
    OLLAMA_URL
)


embedding = OllamaEmbeddings(

    model="nomic-embed-text",

    base_url=OLLAMA_URL

)


client = chromadb.PersistentClient(

    path=CHROMA_PATH

)


collection = client.get_or_create_collection(

    name="hr_policies"

)


policy_folder = Path(

    "docs"

)


existing = collection.get()

if existing["ids"]:

    collection.delete(

        ids=existing["ids"]

    )


for file in policy_folder.glob("*.md"):

    text = file.read_text(

        encoding="utf-8"

    )

    vector = embedding.embed_query(

        text

    )

    collection.add(

        ids=[file.stem],

        documents=[text],

        embeddings=[vector],

        metadatas=[

            {

                "title": file.stem,

                "source": str(file)

            }

        ]

    )


print()

print("=" * 60)

print("Policies Loaded")

print("Documents :", collection.count())

print("=" * 60)
