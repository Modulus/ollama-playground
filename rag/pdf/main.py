from chunkify import chunkify
import ollama
MODEL_NAME="nomic-embed-text"
import time

import os
import json
if __name__ == "__main__":
    chunks = chunkify("my.pdf")

    print("Embedding into model")
    start = time.time()
    embeddings = [ollama.embeddings(model=MODEL_NAME, prompt=chunk)["embedding"] for chunk in chunks ]
    end = time.time() - start

    filename = "dnd.json"
    if not os.path.exists("embeddings"):
        os.makedirs("embeddings")
    with open(f"embeddings/{filename}.json", mode="w") as file:
        json.dump(embeddings, file, indent=4)

    print(f"Embeddings took: {end}")
    print(f"embeddings length is {len(embeddings)}")
