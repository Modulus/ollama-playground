from chunkify import chunkify
import ollama
MODEL_NAME="nomic-embed-text"


if __name__ == "__main__":
    chunks = chunkify("jada.pdf")

    print("Embedding into model")
    embeddings = [ollama.embeddings(model=MODEL_NAME, prompt=chunk)["embedding"] for chunk in chunks ]

    print(f"embeddings length is {len(embeddings)}")
