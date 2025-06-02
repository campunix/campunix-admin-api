from sqlmodel import Field, SQLModel

from src.core.entities.base_entity import BaseEntity


class OrganizationBase(SQLModel):
    name: str = Field(default=None, nullable=False)


class Organization(BaseEntity, OrganizationBase, table=True):
    __tablename__ = "organizations"
