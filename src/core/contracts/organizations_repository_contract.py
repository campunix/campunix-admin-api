from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from src.core.entities.organization import Organization, OrganizationBase


class OrganizationsRepositoryContract(ABC):
    @abstractmethod
    async def createOrganization(self, organization: OrganizationBase) -> Organization:
        pass

    @abstractmethod
    async def get_organization_by_id(self, id: int) -> Optional[Organization]:
        pass

    @abstractmethod
    async def get_all_organizations(
        self,
        page: int = 1,
        page_size: int = 10,
        paginate: bool = False,
        filters: Optional[List[Any]] = None, 
    ) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def update_organization(self, id: id, organization: OrganizationBase) -> Organization:
        pass

    @abstractmethod
    async def delete_organization(self, id: id) -> bool:
        pass
