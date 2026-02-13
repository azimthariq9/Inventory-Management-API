from fastapi import FastAPI
from typing import List

app = FastAPI()

items = []

@app.get("/items")
def list_items():
    return items
