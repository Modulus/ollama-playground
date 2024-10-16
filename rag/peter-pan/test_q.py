import qdrant_client
from qdrant_client.models import Batch
from qdrant_client import models
import ollama 

# Initialize Ollama model

# Generate embeddings for niche applications
text = "Ollama excels in niche applications with specific embeddings."
embeddings = ollama.embeddings(model="nomic-embed-text", prompt=text)["embedding"]

# Initialize Qdrant client
client = qdrant_client.QdrantClient(host="localhost", port=6333)

name = "NicheApplications"

try:
    client.get_collection(collection_name=name)
except qdrant_client.http.exceptions.UnexpectedResponse as e:
    response = client.create_collection(collection_name=name, 
                                            vectors_config=models.VectorParams(
                                                size=768,
                                                distance=models.Distance.COSINE,

                                            )   
                                        )

# Upsert the embedding into Qdrant


client.upsert(
    collection_name=name,
    points=Batch(
        ids=[1],
        vectors=[embeddings],
    )
)

client.add(
    collection_name=name,
    points=Batch(
        ids=[2],
        vectors=[ollama.embeddings(model="nomic-embed-text", prompt="Ollama excels in niche applications with specific embeddings.")["embedding"]],
    )
)


prompt = "What does Ollama excel in?"

response = ollama.embeddings(
  prompt=prompt,
  model="nomic-embed-text" #mxbai-embed-large
)


result = client.search(
    collection_name=name,
    query_vector=response["embedding"],
    with_payload=True,
    with_vectors=True,
    limit=1
)

print(result)

