from pydantic import BaseModel, Field # type: ignore
from typing import Optional
from datetime import datetime


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    parent_id: Optional[str] = None
    delete_flag: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    parent_id: Optional[str]
    delete_flag: Optional[bool]
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class CategoryInDB(CategoryBase):
    _id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


