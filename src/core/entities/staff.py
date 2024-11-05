from sqlalchemy import Column, Enum
from sqlmodel import Field, SQLModel

from src.core.entities.base_entity import BaseEntity
from src.core.entities.enums.staff_designation import StaffDesignation
from src.core.entities.enums.staff_status import StaffStatus


class StaffBase(SQLModel):
    user_id: int = Field(
        default=None,
        foreign_key="users.id",
        nullable=False,
    )
    department_id: int = Field(
        default=None,
        foreign_key="departments.id",
        nullable=True,
    )
    designation: StaffDesignation = Field(
        sa_column=Column(Enum(StaffDesignation, name="staff_designation", create_type=False))
    )
    status: StaffStatus = Field(
        sa_column=Column(Enum(StaffStatus, name="staff_status", create_type=False))
    )


class Staff(BaseEntity, StaffBase, table=True):
    __tablename__ = "staff"
