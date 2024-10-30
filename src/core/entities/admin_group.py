from sqlmodel import Field, SQLModel

from src.core.entities.base_entity import BaseEntity


class AdminGroupBase(SQLModel):
    name: str = Field(
        default=None,
        nullable=False,
    )
    organization_id: int = Field(
        default=None,
        foreign_key="organizations.id",
        nullable=False,
    )
    created_by: int = Field(
        default=None,
        foreign_key="users.id",
        nullable=False,
    )


class AdminGroup(BaseEntity, AdminGroupBase, table=True):
    __tablename__ = "admin_groups"
