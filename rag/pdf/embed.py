from chunkify import chunkify
import ollama
MODEL_NAME="nomic-embed-text"
import time

import os
import json
import qdrant_client
from qdrant_client.models import Batch, Distance, VectorParams
if __name__ == "__main__":

    # if not os.path.exists("embeddings/nasjonal-digitaliseringsstrategi_ny.json"):
    chunks = chunkify(file="files/nasjonal-digitaliseringsstrategi_ny.pdf", size=200, overlap=50)

    print(f"Length of chunks {len(chunks)}")

    print("Embedding into model")
    start = time.time()
    collection_name = "nasjonal_digitaliseringsstrategi_ny"

    client = qdrant_client.QdrantClient(host="localhost", port=6333, timeout=1000)

    if not client.collection_exists(collection_name=collection_name):
        client.create_collection(collection_name=collection_name, vectors_config=VectorParams(size=768, distance=Distance.COSINE),)

    for index, chunk in enumerate(chunks):
        # Embed into model and store vectors with text as payload
        print("Embedding chunk into model with payload")
        embeddings = ollama.embeddings(model=MODEL_NAME, prompt=chunk)["embedding"]

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

        # filename = "nasjonal-digitaliseringsstrategi_ny"
        # if not os.path.exists("embeddings"):
        #     os.makedirs("embeddings")
        # with open(f"embeddings/{filename}.json", mode="w") as file:
        #     json.dump(embeddings, file, indent=4)

    print(f"Embeddings took: {end}")
    print(f"embeddings length is {len(embeddings)}")
    # else:
        # print("Embeddings already exists, loading jsonfile")
        # with open(f"embeddings/nasjonal-digitaliseringsstrategi_ny.json", mode="r") as file:
        #     embeddings = json.load(file)
        # print(f"embeddings length is {len(embeddings)}")

        # # Initialize Qdrant client
        # qdrant_client = qdrant_client.QdrantClient(host="localhost", port=6333, timeout=1000)

        # # Upsert the embedding into Qdrant
        # qdrant_client.upsert(
        #     collection_name="nasjonal-digitaliseringsstrategi_ny",
        #     points=Batch(
        #         ids=[1],
        #         vectors=[embeddings],
        #         )

        # )

