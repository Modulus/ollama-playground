from chunkify import chunkify
import ollama
MODEL_NAME="nomic-embed-text"
import time

import os
import json
import qdrant_client
from qdrant_client.models import Batch, Distance, VectorParams

MODEL_NAME="nomic-embed-text"

collection_name = "nasjonal_digitaliseringsstrategi_ny"

client = qdrant_client.QdrantClient(host="localhost", port=6333, timeout=1000)

prompt="What is the purpose of this document?"
matching_vectors = ollama.embeddings(model=MODEL_NAME, prompt=prompt)


result = client.search(
    collection_name="nasjonal_digitaliseringsstrategi_ny",
    query_vector=matching_vectors["embedding"],
)

# extract hits  from search result
text_list = [ text.payload["text"] for text in result]

output = ollama.generate(
    prompt=f"Using data from {text_list} with prompt: {prompt}",
    model="llama3.2"
)

print(output["response"])