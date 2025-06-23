from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    parent_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    name: Optional[str]
    description: Optional[str]
    parent_id: Optional[str]


class CategoryInDB(CategoryBase):
    _id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


