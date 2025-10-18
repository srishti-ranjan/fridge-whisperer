from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    quantity: int

# In-memory "database"
items = [
    {"id": 1, "name": "Milk", "quantity": 2},
    {"id": 2, "name": "Eggs", "quantity": 12}
]

@app.get("/")
def read_root():
    return {"message": "Hello from PantryPal!"}

@app.get("/items")
def get_items():
    return {"items": items}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items")
def add_item(item: Item):
    new_id = max(i["id"] for i in items) + 1 if items else 1
    obj = {"id": new_id, "name": item.name, "quantity": item.quantity}
    items.append(obj)
    return obj

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    for obj in items:
        if obj["id"] == item_id:
            obj["name"] = item.name
            obj["quantity"] = item.quantity
            return obj
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, obj in enumerate(items):
        if obj["id"] == item_id:
            deleted = items.pop(idx)
            return {"deleted": deleted}
    raise HTTPException(status_code=404, detail="Item not found")
