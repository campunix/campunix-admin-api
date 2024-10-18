
from typing import Any
from sqlalchemy import (
    DateTime
)

from pydantic import BaseModel

class QueryResponse(BaseModel):
    total_count: int
    records: list[Any]

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    publication_year: int
    summary: str
    created_at: Any
    updated_at: Any