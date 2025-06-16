from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    parent_id: Optional[UUID] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    name: Optional[str]
    description: Optional[str]
    parent_id: Optional[UUID]


class CategoryInDB(CategoryBase):
    id: UUID = Field(default_factory=UUID)
    # created_at: datetime
    # updated_at: datetime

    class Config:
        orm_mode = True


