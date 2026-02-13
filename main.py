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

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            deleted = items.pop(index)
            return deleted_item   # <- BUG DISINI
    return {"error": "Item not found"}


