from typing import Any, Dict, Optional

from src.core.contracts.organizations_repository_contract import OrganizationsRepositoryContract
from src.core.entities.organization import Organization, OrganizationBase
from src.features.admin.services.organization_service_contract import OrganizationServiceContract
from src.models.organization import OrganizationIn, OrganizationOut


class OrganizationService(OrganizationServiceContract):
    def __init__(
            self,
            organizations_repository: OrganizationsRepositoryContract,
    ):
        self.organizations_repository = organizations_repository

    async def create_organization(self, organization: OrganizationIn) -> Optional[OrganizationOut]:
        new_organization = await self.organizations_repository.create(Organization(name=organization.name))
        return OrganizationOut(id=new_organization.id, name=new_organization.name)

    async def get_organizations(self, page: int = 1, page_size: int = 10, paginate: bool = False) -> Dict[str, Any]:
        data = await self.organizations_repository.get_all()

        organizations = {
            "organizations": [
                {key: value for key, value in item.items() if key not in ["created_at", "updated_at"]}
                for item in data["items"]
            ]
        }
        return organizations

    async def update_organization(self, id: int, organization: OrganizationIn) -> Optional[OrganizationOut]:
        return await self.organizations_repository.update(id, Organization(id = id, name=organization.name))

    async def delete_organization(self, id: int) -> bool:
        return await self.organizations_repository.delete(id)

    async def get_organization_by_id(self, id: int) -> Optional[OrganizationOut]:
        return await self.organizations_repository.get_by_id(id)
