from sqlalchemy import Column, Enum
from sqlmodel import Field, SQLModel

from src.core.entities.base_entity import BaseEntity
from src.core.entities.enums.user_role import UserRole


class UserOrganizationBase(SQLModel):
    user_id: int = Field(
        default=None,
        foreign_key="users.id",
        nullable=False,
    )
    organization_id: int = Field(
        default=None,
        foreign_key="organizations.id",
        nullable=False,
    )
    role: UserRole = Field(
        default=None,
        sa_column=Column(Enum(UserRole)),
        nullable=False,
    )


class UserOrganization(BaseEntity, UserOrganizationBase, table=True):
    __tablename__ = "user_organizations"
