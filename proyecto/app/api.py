from fastapi import APIRouter, HTTPException
from .schemas import ItemCreate, ItemOut
from .db import create_item, get_item

router = APIRouter()

@router.post("/items", response_model=ItemOut, status_code=201)
def create(item: ItemCreate):
    saved = create_item(item.dict())
    return saved

@router.get("/items/{item_id}", response_model=ItemOut)
def read(item_id: int):
    item = get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail={"error":"not_found","message":"Item no encontrado"})
    return item
