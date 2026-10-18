from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

class ItemCreate(BaseModel):
    name: str

app = FastAPI()

items = {
    1: {"id": 1, "name": "Jean"},
    2: {"id": 2, "name": "Benoit"},
}
next_id = 3

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items")
def get_items():
    return list(items.values())

@app.post("/items", status_code=201)
def create_item(item: ItemCreate):
    global next_id
    d = {"id":next_id, "name": item.name}
    items[next_id] = d
    next_id +=1
    return d

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemCreate):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id]["name"] = item.name
    return items[item_id]

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]

