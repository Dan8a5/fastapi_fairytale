from sqlmodel import Field, SQLModel
from .base import Base

class PigBase(SQLModel):
    pig_name: str = Field(index=True)
    pig_house: str

class Pig(PigBase, Base, table=True):
    __tablename__ = "pigs"

class PigCreate(PigBase):
    pass