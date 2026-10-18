from fastapi import FastAPI
from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str

app = FastAPI()

items = [{"id":1, "name": "Jean"}, {"id":2, "name": "Benoit"},{"id":3, "name": "Arthur"},]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items")
def get_items():
    return items

@app.post("/items", status_code=201)
def create_item(item: ItemCreate):
    d = {"id":len(items)+1, "name": item.name}
    items.append(d)
    return d