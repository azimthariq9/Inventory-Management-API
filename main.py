from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

items = []

class Item(BaseModel):
    id: int
    name: str
    stock: int

@app.get("/")
def root():
    return {"message": "Inventory API Running"}

@app.get("/items")
def list_items():
    return items

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item
