from sqlalchemy import Column, Enum
from sqlmodel import Field, SQLModel

from src.core.entities.base_entity import BaseEntity
from src.core.entities.enums.teacher_designation import TeacherDesignation
from src.core.entities.enums.teacher_status import TeacherStatus


class TeacherBase(SQLModel):
    user_id: int = Field(
        default=None,
        foreign_key="users.id",
        nullable=False,
    )
    department_id: int = Field(
        default=None,
        foreign_key="departments.id",
        nullable=False,
    )
    designation: TeacherDesignation = Field(
        sa_column=Column(Enum(TeacherDesignation, name="teacher_designation", create_type=False))
    )
    status: TeacherStatus = Field(
        sa_column=Column(Enum(TeacherStatus, name="teacher_status", create_type=False))
    )


class Teacher(BaseEntity, TeacherBase, table=True):
    __tablename__ = "teachers"
