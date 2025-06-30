from pydantic import BaseModel, Field # type: ignore
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    category_id: Optional[str] = None
    status: bool = True
    delete_flag: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    stock: Optional[int]
    category_id: Optional[str]
    status: Optional[bool]
    updated_at: datetime
    delete_flag: Optional[bool]


class ProductInDB(ProductBase):
    _id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
