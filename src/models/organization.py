from typing import Optional
from pydantic import BaseModel

class OrganizationOut(BaseModel):
    id: int
    name: str
    
class OrganizationIn(BaseModel):
    name: str
    admin_group: int
    created_by: int
