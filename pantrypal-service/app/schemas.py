from pydantic import BaseModel, Field
from typing import Optional

class PantryItemBase(BaseModel):
    name: str = Field(..., examples=["Milk"])
    quantity: int = Field(..., examples=[2])

class PantryItemCreate(PantryItemBase):
    """
    Schema for creating a PantryItem
    """
    pass

class PantryItemUpdate(BaseModel):
    name: Optional[str] = Field(None, examples=["Eggs"])
    quantity: Optional[int] = Field(None, examples=[12])

class PantryItem(PantryItemBase):
    id: int = Field(..., examples=[1])
    # Pydantic v2 ORM support:
    model_config = {"from_attributes": True}
