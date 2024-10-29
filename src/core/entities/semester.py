from sqlmodel import Field, SQLModel

from src.core.entities.base_entity import BaseEntity


class SemesterBase(SQLModel):
    year: int = Field(
        default=None,
        nullable=False,
    )
    number: int = Field(
        default=None,
        nullable=False,
    )
    department_id: int = Field(
        default=None,
        foreign_key="departments.id",
        nullable=False,
    )


class Semester(BaseEntity, SemesterBase, table=True):
    __tablename__ = "semesters"