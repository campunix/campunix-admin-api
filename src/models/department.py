from pydantic import BaseModel, Field


class DepartmentOut(BaseModel):
    id: int
    name: str


class DepartmentIn(BaseModel):
    name: str
    organization_id: int
    created_by: int


class DepartmentCreate(BaseModel):
    name: str
    organization_id: int
