from pprint import pprint
import inquirer
import qdrant_client
from ollama import Client
import ollama

EMBEDDING_MODEL_NAME="nomic-embed-text"
MODEL="llama3.2"

def list_collections():
    try:
        client = qdrant_client.QdrantClient(host="localhost", port=6333, timeout=1000)
        collections_list = []
        collections = client.get_collections()
        for collection in collections:
            for c in list(collection[1]):
                collections_list.append(c.name)
        return collections_list
    except Exception as e:
        print(f"Error fetching collections from Qdrant: {e}")


def prompt(collection_name, prompt="What is the purpose of this document?"):

    client = qdrant_client.QdrantClient(host="localhost", port=6333, timeout=1000)

    prompt_with_prefix = f"search_query: {prompt}"
    matching_vectors = ollama.embeddings(model=EMBEDDING_MODEL_NAME, prompt=prompt_with_prefix)

    result = client.search(
        collection_name=collection_name,
        query_vector=matching_vectors["embedding"],
    )

    # extract hits  from search result
    text_list = [ text.payload["text"] for text in result]
    print(text_list)

    client = Client(host='http://localhost:11434')

    print(f"Using data from {text_list} with prompt: {prompt}")

    text_list = [ text.payload["text"] for text in result]

    output = ollama.generate(
        prompt=f"Using data from {text_list} with prompt: {prompt}",
        model="llama3.2"
    )

    return output


if __name__ == "__main__":
    
    collections = list_collections()
    questions = [
        inquirer.List(
            "collection",
            message="Which collection would you like to query?",
            choices=collections,
        ),
    ]

    answers = inquirer.prompt(questions)
    pprint(answers)
    while True:
        query = input(">>> ")
        output = prompt(collection_name=answers["collection"], prompt=query)
        print(output["response"])