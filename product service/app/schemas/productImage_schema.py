from pydantic import BaseModel, Field, HttpUrl
from uuid import UUID
from typing import Optional


class ProductImageBase(BaseModel):
    product_id: UUID
    image_url: HttpUrl


class ProductImageCreate(ProductImageBase):
    pass


class ProductImageUpdate(BaseModel):
    image_url: Optional[HttpUrl]


class ProductImageInDB(ProductImageBase):
    _id: UUID = Field(default_factory=UUID)

    class Config:
        orm_mode = True