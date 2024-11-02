from abc import ABC, abstractmethod
from typing import Optional, Any

from src.models.user_organization import UserOrganizationIn


class AdminServiceContract(ABC):
    @abstractmethod
    async def initiate_organization_for_current_user(self, token: str, organization_id: int):
        pass