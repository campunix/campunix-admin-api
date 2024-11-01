from abc import ABC, abstractmethod
from typing import Optional

from src.models.organization import OrganizationIn, OrganizationOut


class OrganizationServiceContract(ABC):
    @abstractmethod
    async def create_organization(self, organization: OrganizationIn) -> Optional[OrganizationOut]:
        pass

    @abstractmethod
    async def get_organizations(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        pass

    @abstractmethod
    async def update_organization(self, id: int, organization: OrganizationIn) -> Optional[OrganizationOut]:
        pass

    @abstractmethod
    async def delete_organization(self, id: int) -> bool:
        pass

    @abstractmethod
    async def get_organization_by_id(self, id: int) -> Optional[OrganizationOut]:
        pass
