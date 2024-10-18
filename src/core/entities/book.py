from sqlmodel import Field

from src.core.entities.base_entity import BaseEntity

class Book(BaseEntity, table=True):
    title: str = Field(default=None, nullable=True)
    author: str = Field(default=None, nullable=True)