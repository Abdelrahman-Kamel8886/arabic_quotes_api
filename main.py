from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("arabic_Q.jsonl", "r", encoding="utf-8") as f:
    quotes = [json.loads(line.strip()) for line in f]

@app.get("/")
def root():
    return {"message": "مرحبًا بك في Arabic Quotes API 💬"}

@app.get("/quote")
def get_random_quote():
    quote = random.choice(quotes)
    return {
        "quote": quote["quote"],
        "author": quote["author"],
        "tags": quote["tags"]
    }

@app.get("/quotes")
def get_multiple_quotes():
    selected = quotes
    return [
        {
            "quote": q["quote"],
            "author": q["author"],
            "tags": q["tags"]
        }
        for q in selected
    ]

