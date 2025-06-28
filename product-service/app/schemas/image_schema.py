from pydantic import BaseModel, Field # type: ignore
from typing import Optional
from datetime import datetime


class ProductImageBase(BaseModel):
    product_id: str
    image_url: str # get from cloudinary
    public_id: str # get from cloudinary
    position: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    delete_flag: bool = False

class ProductImageCreate(ProductImageBase):
    pass


class ProductImageUpdate(BaseModel):
    image_url: Optional[str]
    public_id: Optional[str]
    position: Optional[int]


class ProductImageInDB(ProductImageBase):
    _id: str
    created_at: datetime

    class Config:
        from_attribute = True