import ollama
import os
import json
import numpy as np
from numpy.linalg import norm
# MODEL_NAME = "ollama3.2"
MODEL_NAME="nomic-embed-text"
# MODEL_NAME = "mistral"






def parse_file(filename):
    with open(filename, mode="r", encoding="utf-8-sig") as file:
        paragraphs = []
        buffer = []
        for line in file.readlines():
            line = line.strip()
            if line:
                buffer.append(line)
            elif len(buffer):
                paragraphs.append((" ").join(buffer))
                buffer = []
        if len(buffer):
            paragraphs.append((" ").join(buffer))
        return paragraphs

def save_embeddings(filename, embeddings):
    if not os.path.exists("embeddings"):
        os.makedirs("embeddings")
    with open(f"embeddings/{filename}.json", mode="w") as file:
        json.dump(embeddings, file, indent=4)

def load_embeddings(filename):
    if not os.path.exists(f"embeddings/{filename}.json"):
        return False
    with open(f"embeddings/{filename}.json", mode="r") as file:
        return json.load(file)

def get_embeddings(filename, chunks):
    if (embeddings := load_embeddings(filename)) is not False:
        return embeddings
    embeddings = [
        embed_into_model(chunk=chunk)
        for chunk in chunks
    ]
    save_embeddings(filename, embeddings)
    return embeddings

def embed_into_model(chunk):
    print("embedding chunk")
    return ollama.embeddings(model=MODEL_NAME, prompt=chunk)["embedding"]


# find cosine similarity of every chunk to a given embedding
def find_most_similar(needle, haystack):
    needle_norm = norm(needle)
    similarity_scores = [
        np.dot(needle, item) / (needle_norm * norm(item)) for item in haystack
    ]
    return sorted(zip(similarity_scores, range(len(haystack))), reverse=True)


def main () :
    import time

    SYSTEM_PROMPT = """You are a helpful reading assistant who answers questions 
        based on snippets of text provided in context. Answer only using the context provided, 
        being as concise as possible. If you're unsure, just say that you don't know.
        Context:
    """

    start = time.perf_counter()
    filename = "peterpan.txt"
    paragraphs = parse_file(filename)
    # join multiple paragraphs to meet a minimum length

    ## Remember to delete embeddings folder if you mess with this
    paragraphs = ["".join(paragraphs[i : i + 2]) for i in range(0, len(paragraphs), 2)]

    # Overlapping chunks Ended

    embeddings = get_embeddings(filename, paragraphs)

    print(time.perf_counter() - start)
    print(len(embeddings))

    while True:
        prompt = input(">>> ")
        promt_embedding = ollama.embeddings(model=MODEL_NAME, prompt=prompt)["embedding"]


        most_similar_chunks = find_most_similar(needle=promt_embedding, haystack=embeddings)[:5]

        response = ollama.chat(
            model="mistral", 
            messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT + "\n".join( paragraphs[item[1]] for item in most_similar_chunks),
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        )
        print(response["message"]["content"])

if __name__ == "__main__":
    main()