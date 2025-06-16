from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    category_id: UUID
    is_active: bool = True


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    stock: Optional[int]
    category_id: Optional[UUID]
    is_active: Optional[bool]


class ProductInDB(ProductBase):
    id: UUID = Field(default_factory=UUID)
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
