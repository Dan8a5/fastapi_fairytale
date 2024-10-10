from sqlmodel import SQLModel, Field
from typing import Optional
from .base import Base

class HouseBase(SQLModel):
    type: str
    sturdiness: int
    pig_id: Optional[int] = Field(default=None, foreign_key="pigs.id")

class House(HouseBase, Base, table=True):
    __tablename__ = "houses"

class HouseCreate(HouseBase):
    pass