import ollama
from ollama import generate
print("llama3.2 chat:")
response = ollama.chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])

print("phi3.5 chat:")
response = generate('phi3.5', 'why is the sky blue?')
print(response['response'])