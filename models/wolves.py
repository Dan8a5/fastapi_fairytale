from sqlmodel import Field, SQLModel
from .base import Base

class WolfBase(SQLModel):
    wolf_name: str = Field(index=True)
    wolf_power: int

class Wolf(WolfBase, Base, table=True):
    __tablename__ = "wolves"

class WolfCreate(WolfBase):
    pass