# Found here

https://decoder.sh/videos/rag-from-the-ground-up-with-python-and-ollama


# set up environment
ollama pull nomic-embed-text
ollama pull llama3.2
python -m venv .venv
source .venv/bin/activate
python -m pip install ollama numpy


## Note
Current setup uses nomic-embed-text model to create embeddings
Then we use llama3.2 to chat with. 

If you want to change models, remember to delete the embeddings folder


## Use this as inspiration for qdrant
https://ollama.com/blog/embedding-models

http://localhost:6333/dashboard