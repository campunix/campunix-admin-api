from pydantic import BaseModel, Field


class DepartmentOut(BaseModel):
    id: int
    name: str
    code: str


class DepartmentIn(BaseModel):
    name: str
    code: str
    organization_id: int
    created_by: int


class DepartmentCreate(BaseModel):
    name: str
    code: str
    organization_id: int
