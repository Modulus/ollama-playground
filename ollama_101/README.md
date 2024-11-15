
# API
curl -XPOST -H "Content-Type: application/json" http://localhost:11434/v1/chat/completions -d '{"model": "llama3.2", "messages": [{"role": "users", "content": "How are you today?"}]}'
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Why is the sky blue?",
  "stream": false
}'

# Python api 
https://github.com/ollama/ollama-python


# modelfiles for ollama
ollama create mario -f modelfile.mario
ollama run mario



## Code
fastapi dev api.py

curl --header "Content-Type: application/json" -X POST -d '{"question": "how much is the fish?"}' http://localhost:8000/ask

## TODO 
Add ollama access from inside container