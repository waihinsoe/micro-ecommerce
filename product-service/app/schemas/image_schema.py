from pydantic import BaseModel, Field # type: ignore
from typing import Optional
from datetime import datetime


class ProductImageBase(BaseModel):
    product_id: str
    image_url: str # get from cloudinary
    public_id: str # get from cloudinary
    position: int
    format: str # get from cloudinary
    created_at: datetime = Field(default_factory=datetime.utcnow)
    delete_flag: bool = False

class ProductImageCreate(ProductImageBase):
    pass

class ProductImageInDB(ProductImageBase):
    _id: str
    created_at: datetime

    class Config:
        from_attribute = True