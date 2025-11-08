from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1)
    value: float

class ItemOut(ItemCreate):
    id: int

    class Config:
        orm_mode = True  # permite devolver objetos SQLAlchemy