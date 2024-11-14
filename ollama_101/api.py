from dataclasses import dataclass
from faker import Faker
from pydantic import BaseModel

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
    print(f"Asking llama3.2: {question}")
    response = ollama.chat(model='llama3.2', messages=[
    {
        'role': 'user',
        'content': question.question,
    },
    ])
    print(response['message']['content'])

    return Answer(answer=response['message']['content'])

@app.get("/stream")
async def read_stream():
    return StreamingResponse(generate_names())

@app.get("/q")   
async def get_q():
    return Question(question="Hello, World!")

@app.post("/ask")
async def ask_question(question: Question):
    return generate_answers(question)
