import ollama
from ollama import generate
import random


question = random.choice([
    "Why is the sky blue?",
    "How many of the letter r, are there in the word 'Strawberry'?",
    "Can you tell me a joke?",
    "Can you write java code to print the 10 first fibonacci numbers?",
])

print(f"Asking llama3.2: {question}")
response = ollama.chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': question,
  },
])
print(response['message']['content'])

print(f"Asking phi3.5: {question}")
response = generate('phi3.5', question)
print(response['response'])