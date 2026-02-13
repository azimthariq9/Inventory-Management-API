from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel, Field

app = FastAPI(
    title="Inventory Management API",
    version="1.1.0"
)

items = []

class Item(BaseModel):
    id: int
    name: str
    stock: int = Field(..., ge=0, description="Stock cannot be negative")
    price: float = Field(..., gt=0, description="Price must be greater than 0")
    category: Optional[str] = None

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    stock: Optional[int] = Field(None, ge=0)
    price: Optional[float] = Field(None, gt=0)
    category: Optional[str] = None

@app.get("/")
def root():
    return {"message": "Inventory API Running", "version": "1.1.0"}

@app.get("/items", response_model=List[Item])
def list_items(category: Optional[str] = None):
    if category:
        return [item for item in items if item.category == category]
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    for existing in items:
        if existing.id == item.id:
            raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items.append(item)
    return item

@app.patch("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_fields: ItemUpdate):
    for index, item in enumerate(items):
        if item.id == item_id:
            updated_data = item.model_dump()
            patch_data = updated_fields.model_dump(exclude_unset=True)
            updated_data.update(patch_data)
            items[index] = Item(**updated_data)
            return items[index]
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            deleted = items.pop(index)
            return {"message": f"Item '{deleted.name}' deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")