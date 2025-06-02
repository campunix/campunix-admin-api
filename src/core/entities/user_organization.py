from setuptools.command.alias import alias
from sqlalchemy import Column, Enum
from sqlmodel import Field, SQLModel

from src.core.entities.base_entity import BaseEntity
from src.core.entities.enums.user_role import UserRole


class UserOrganizationBase(SQLModel):
    model_config = {
        "arbitrary_types_allowed": True,
    }

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
        sa_column=Column(Enum(UserRole, name="user_role", create_type=False))
    )


class UserOrganization(BaseEntity, UserOrganizationBase, table=True):
    __tablename__ = "user_organizations"
