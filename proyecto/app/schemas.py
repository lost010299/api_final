from pydantic import BaseModel, Field, ConfigDict

# ✅ Definimos primero el esquema de entrada
class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1)
    value: float

# ✅ Luego el esquema de salida que hereda del anterior
class ItemOut(ItemCreate):
    id: int
    # Versión moderna para Pydantic v2
    model_config = ConfigDict(from_attributes=True)