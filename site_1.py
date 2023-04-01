from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Classe modelo para definir o formato de dados do item
class Item(BaseModel):
    id: int
    name: str
    price: float
    is_offer: bool = None

# Lista simulando um banco de dados
items = []

# Rota GET para obter todos os itens
@app.get("/items/")
async def read_items():
    return items

# Rota GET para obter um item por ID
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"message": "Item not found"}

# Rota POST para criar um novo item
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    item_dict["id"] = len(items) + 1
    items.append(item_dict)
    return {"message": "Item created successfully", "item": item_dict}

# Rota PUT para atualizar um item existente
@app.put("/items/{item_id}/")
async def update_item(item_id: int, item: Item):
    for index, item_dict in enumerate(items):
        if item_dict["id"] == item_id:
            items[index] = item.dict()
            items[index]["id"] = item_id
            return {"message": "Item updated successfully", "item": items[index]}
    return {"message": "Item not found"}

# Rota DELETE para deletar um item existente
@app.delete("/items/{item_id}/")
async def delete_item(item_id: int):
    for index, item_dict in enumerate(items):
        if item_dict["id"] == item_id:
            itens.pop(index)
            return {"message": "Item deleted successfully"}
    return {"message": "Item not found"}
