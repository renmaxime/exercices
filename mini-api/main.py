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
    # 1. fabriquer un nouveau dict : {"id": ..., "name": ...}
    d = {"id":len(items)+1, "name": item.name}
    #    - id : le suivant (pense à len(items))
    #    - name : vient de l'objet reçu, item.name
    # 2. l'ajouter à la liste items (append)
    items.append(d)
    # 3. renvoyer le nouvel item
    return items