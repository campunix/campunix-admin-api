from sqlmodel import Field, SQLModel

from src.core.entities.base_entity import BaseEntity


class DepartmentBase(SQLModel):
    name: str = Field(
        default=None,
        nullable=False,
    )
    admin_group: int = Field(
        default=None,
        foreign_key="admin_groups.id",
        nullable=False,
    )
    created_by: int = Field(
        default=None,
        foreign_key="users.id",
        nullable=False,
    )


class Department(BaseEntity, DepartmentBase, table=True):
    __tablename__ = "departments"
