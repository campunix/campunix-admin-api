from sqlalchemy import Column, Enum
from sqlmodel import Field, SQLModel

from src.core.entities.base_entity import BaseEntity
from src.core.entities.enums.room_type import RoomType


class RoomBase(SQLModel):
    name: str = Field(
        default=None,
        nullable=False,
    )
    department_id: int = Field(
        default=None,
        foreign_key="departments.id",
        nullable=False,
    )
    room_type: RoomType = Field(
        sa_column=Column(Enum(RoomType, name="room_type", create_type=False))
    )


class Room(BaseEntity, RoomBase, table=True):
    __tablename__ = "rooms"
