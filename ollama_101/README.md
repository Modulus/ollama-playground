
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
