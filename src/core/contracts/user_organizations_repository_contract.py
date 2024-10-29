from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from src.core.entities.user_organization import UserOrganization, UserOrganizationBase


class UserOrganizationsRepositoryContract(ABC):
    @abstractmethod
    async def createOrganization(
        self, userOrganization: UserOrganizationBase
    ) -> UserOrganization:
        pass

    @abstractmethod
    async def get_user_organization_by_id(self, id: int) -> Optional[UserOrganization]:
        pass

    @abstractmethod
    async def get_all_user_organizations(
        self,
        page: int = 1,
        page_size: int = 10,
        paginate: bool = False,
        filters: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def update_user_organization(
        self, id: id, organization: UserOrganizationBase
    ) -> UserOrganization:
        pass

    @abstractmethod
    async def delete_user_organization(self, id: id) -> bool:
        pass
