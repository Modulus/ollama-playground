from qdrant_client import QdrantClient
from ollama import Ollama
# Initialize the client
client = QdrantClient("localhost", port=6333) # For production
# client = QdrantClient(":memory:") # For small experiments

# Prepare your documents, metadata, and IDs
docs = ["Qdrant has Langchain integrations", "Qdrant also has Llama Index integrations"]
metadata = [
    {"source": "Langchain-docs"},
    {"source": "Llama-index-docs"},
]
ids = [42, 2]

# If you want to change the model:
# client.set_model("sentence-transformers/all-MiniLM-L6-v2")
# List of supported models: https://qdrant.github.io/fastembed/examples/Supported_Models

# Use the new add() instead of upsert()
# This internally calls embed() of the configured embedding model
# client.add(
#     collection_name="demo_collection",
#     documents=docs,
#     metadata=metadata,
#     ids=ids
# )

# Initialize Ollama model
model = Ollama("nomic-embed-text")

# Generate embeddings for niche applications
text = "Ollama excels in niche applications with specific embeddings."
embeddings = model.embed(text)


qdrant_client.upsert(
    collection_name="demo_collection",
    points=Batch(
        ids=[1],
        vectors=[embeddings],
    )
)

search_result = client.query(
    collection_name="demo_collection",
    query_text="This is a query document"
)
print(search_result)