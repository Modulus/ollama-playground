from dataclasses import dataclass
from faker import Faker
from pydantic import BaseModel
import json
import os

from fastapi.responses import (
    FileResponse,
    HTMLResponse,
    JSONResponse,
    ORJSONResponse,
    PlainTextResponse,
    RedirectResponse,
    Response,
    StreamingResponse,
    UJSONResponse,
)
from fastapi import FastAPI
import ollama
from ollama import generate
from ollama import Client
import random
# from fastapi import FastAPI, StreamingResponse

app = FastAPI()
faker = Faker()

class Question(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str

def generate_names():
    for _ in range(10000):
        yield faker.name() + '\n'

def generate_answers(question: Question):
    OLLAMA_URL = os.environ.get('OLLAMA_BASE_URL', 'http://localhost:11434')

    client = Client(host=OLLAMA_URL)

    print(f"Talking to ollama on url: {OLLAMA_URL}")

    print(f"Asking llama3.2: {question}")
    response = client.chat(
        model='llama3.2', messages=[
            {
                'role': 'user',
                'content': question.question,
            },
        ],
        stream=False
    )


        
    return response['message']['content'] 

@app.get("/stream")
async def read_stream():
    return StreamingResponse(generate_names())

@app.get("/q")   
async def get_q():
    return Question(question="Hello, World!")

@app.post("/ask")
async def ask_question(question: Question):
    return StreamingResponse(json.dumps({"msg": generate_answers(question)} ))

