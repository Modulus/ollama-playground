import ollama

# Step 1. Data prepartion
documents = [
    "Llamas are members of the camelid family, meaning they're closely related to vicuñas and camels.",
    "Llamas were first domesticated and used as pack animals 4,000 to 5,000 years ago in the Peruvian highlands.",
    "Llamas can grow as much as 6 feet tall, though the average llama is between 5 feet 6 inches and 5 feet 9 inches tall.",
    "Llamas weigh between 280 and 450 pounds and can carry 25 to 30 percent of their body weight.",
    "Llamas are vegetarians and have very efficient digestive systems.",
    "Llamas live to be about 20 years old, though some live up to 30 years."
]

# Generate embeddings
# Initialize the Ollama client
client = ollama.Client()

# Step 2. Generate embeddings
embeddings = []
for doc in documents:
    response = client.embeddings(model="mxbai-embed-large", prompt=doc)
    embeddings.append(response["embedding"])

# Display the embeddings
for i, emb in enumerate(embeddings):
    print(f"Document {i+1}: {emb[:5]}...")  # Print the first 5 dimensions of each embedding


# Step 3. Store embeddings in db
import chromadb

# Initialize the ChromaDB client
chroma_client = chromadb.Client()

# Create a collection to store documents and embeddings
collection = chromadb.create_collection(name="document_collection")

# Store documents and their embeddings in the collection
for i, (doc, emb) in enumerate(zip(documents, embeddings)):
    collection.add(ids=[str(i)], embeddings=[emb], documents=[doc])

print("Documents and embeddings stored successfully.")


# Step 4: Implementing the Retrieval Component

query = "What animals are llamas related to?"

# Generate embedding for the query
query_embedding = client.embeddings(model="mxbai-embed-large", prompt=query)["embedding"]

# Retrieve the most relevant document
results = collection.query(query_embeddings=[query_embedding], n_results=1)
retrieved_document = results['documents'][0][0]

print(f"Retrieved Document: {retrieved_document}")


# Step 5: Generating Responses with Llama 3
# Generate a response using the retrieved document and the query
response_prompt = f"Using this information: {retrieved_document}, respond to the query: {query}"
response = client.chat(model="llama3", prompt=response_prompt)

print(f"Generated Response: {response['response']}")

# Step 6: Integrating All Components into a RAG Pipeline
class RAGPipeline:
    def __init__(self, retriever, generator):
        self.retriever = retriever
        self.generator = generator

    def __call__(self, query):
        # Step 1: Generate query embedding
        query_embedding = self.retriever.embeddings(model="mxbai-embed-large", prompt=query)["embedding"]

        # Step 2: Retrieve the most relevant document
        results = collection.query(query_embeddings=[query_embedding], n_results=1)
        retrieved_document = results['documents'][0][0]

        # Step 3: Generate a response
        response_prompt = f"Using this information: {retrieved_document}, respond to the query: {query}"
        response = self.generator.chat(model="llama3", prompt=response_prompt)

        return response['response']

# Initialize the RAG pipeline
rag_pipeline = RAGPipeline(retriever=client, generator=client)

# Example usage
query = "Tell me about the dietary habits of llamas."
response = rag_pipeline(query)
print(f"RAG Response: {response}")
