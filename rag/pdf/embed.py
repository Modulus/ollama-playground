from typing import List
from chunkify import chunkify
import ollama
MODEL_NAME="nomic-embed-text"
import time

import os
import json
import qdrant_client
from qdrant_client.models import Batch, Distance, VectorParams

from helper import get_root_folder

import sys

root_folder = get_root_folder()
print(f"Root folder: {root_folder}")
core_folder = os.path.join(root_folder, "core")
print(f"Core folder: {core_folder}")

sys.path.insert(0, core_folder)

import meta

def list_files(dir: str, postfix: str = ".pdf") -> List[str]:
    files = []
    for file in os.listdir(dir):
        if file.endswith(postfix):
            files.append(os.path.join(dir, file))
    return files

def embed(file):
    chunks = chunkify(file=file, size=150, overlap=10)

    print(f"Length of chunks {len(chunks)}")

    print("Embedding into model")
    start = time.time()
    collection_name = meta.extract_collection_name(file)
    print(f"Creating collection: {collection_name}")

    client = qdrant_client.QdrantClient(host="localhost", port=6333, timeout=1000)

    if not client.collection_exists(collection_name=collection_name):
        client.create_collection(collection_name=collection_name, vectors_config=VectorParams(size=768, distance=Distance.COSINE),)

        for index, chunk in enumerate(chunks):
            # Embed into model and store vectors with text as payload
            print("Embedding chunk into model with payload")
            chunck_with_prefix = f"search_document: {chunk}"
            embeddings = ollama.embeddings(model=MODEL_NAME, prompt=chunck_with_prefix)["embedding"]

            client = qdrant_client.QdrantClient(host="localhost", port=6333, timeout=1000)
        
            # Upsert the embedding into Qdrant
            client.upsert(
                collection_name=collection_name,
                points=Batch(
                    ids=[index],
                    vectors=[embeddings],
                    payloads=[{"text": chunk}]
                    )
            )



        end = time.time() - start


        print(f"Embeddings took: {end}")
        print(f"embeddings length is {len(embeddings)}")


if __name__ == "__main__":
    files = list_files("files", postfix=".pdf")

    for file in files:
      embed(file)


