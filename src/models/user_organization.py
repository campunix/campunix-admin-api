from pydantic import BaseModel

from src.models.organization import OrganizationOut
from src.models.user import UserPublic


class UserOrganizationIn(BaseModel):
    user_id: int
    role: str


class UserOrganizationOut(BaseModel):
    user: UserPublic
    organization: OrganizationOut
