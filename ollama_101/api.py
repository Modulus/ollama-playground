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

# from fastapi import FastAPI, StreamingResponse

app = FastAPI()
faker = Faker()

class Question(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str
    person: str

def generate_names():
    for _ in range(10000):
        yield faker.name() + '\n'

def generate_answers(question: Question):
    for _ in range(10000):
        yield Answer(answer=faker.sentence(), person=faker.name())

@app.get("/stream")
async def read_stream():
    return StreamingResponse(generate_names())

@app.get("/q")   
async def get_q():
    return Question(question="Hello, World!")

@app.post("/ask")
async def ask_question(question: Question):
    return generate_answers(question)
