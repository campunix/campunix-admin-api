from datetime import datetime, UTC

from sqlmodel import Column, DateTime, Field, SQLModel, func


class BaseEntity(SQLModel):
    id: int = Field(default=None, nullable=False, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.utcnow(), nullable=False)
    updated_at: datetime = Field(default_factory=lambda: datetime.utcnow(), nullable=False)
