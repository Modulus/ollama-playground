import pandas as pd
import numpy as np
import json
import ollama
from qdrant_client import QdrantClient
from qdrant_client.models import CollectionDescription, Distance, VectorParams

client = QdrantClient(host="127.0.0.1", port=6333)
ollama_client = ollama.Client("http://127.0.0.1:11434")
dataset = pd.read_excel("./dataset/processed_anime.xlsx")

# Define collection schema
collection_name = "anime_db"
client.recreate_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(size=2560, distance=Distance.COSINE),
)

# Prepare and index data
for index, row in dataset.iterrows():
    vector = ollama_client.embeddings(model="qwen", prompt=row["text_vectors"])["embedding"]
    client.upsert(
        collection_name=collection_name,
        points=[{
            "id": index,
            "vector": vector,
        }]
    )