from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid

router = APIRouter()

class Item(BaseModel):
    id: Optional[str]
    name: str
    description: Optional[str] = None

DB = {}

@router.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    item_id = str(uuid.uuid4())
    item.id = item_id
    DB[item_id] = item.dict()
    return item

@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: str):
    item = DB.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/items", response_model=list[Item])
def list_items():
    return list(DB.values())

@router.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: str):
    if item_id in DB:
        del DB[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")