from pydantic import BaseModel


class DepartmentOut(BaseModel):
    id: int
    name: str


class DepartmentIn(BaseModel):
    name: str