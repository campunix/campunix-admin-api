from abc import ABC, abstractmethod

from src.core.entities.enums.user_role import UserRole


class AdminServiceContract(ABC):
    @abstractmethod
    async def initiate_organization_for_current_user(self, token: str, organization_id: int):
        pass

    @abstractmethod
    async def map_user_to_organization(self, organization_id: int, user_id: int, role: UserRole):
        pass