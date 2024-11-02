from typing import Optional, Any

from src.core.contracts.admin_groups_repository_contract import (
    AdminGroupsRepositoryContract,
)
from src.core.contracts.user_organizations_repository_contract import UserOrganizationsRepositoryContract
from src.core.entities.admin_group import AdminGroup
from src.core.entities.enums.user_role import UserRole
from src.core.entities.user_organization import UserOrganization
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.services.admin_service_contract import AdminServiceContract
from src.features.auth.services.auth_service_contract import AuthServiceContract
from src.models.user_organization import UserOrganizationIn


class AdminService(AdminServiceContract):
    def __init__(
            self,
            user_organizations_repository: UserOrganizationsRepositoryContract,
            admin_groups_repository: AdminGroupsRepositoryContract,
            auth_service: AuthServiceContract
    ):
        self.user_organizations_repository = user_organizations_repository
        self.admin_groups_repository = admin_groups_repository
        self.auth_service = auth_service

    async def map_user_to_organization(self, organization_id: int, user_id: int, role: UserRole):
        await self.user_organizations_repository.create(
            UserOrganization(
                user_id=user_id,
                organization_id=organization_id,
                role=role
            )
        )

    async def _create_default_admin_group(self, name: str, organization_id: int, user_id: int):
        await self.admin_groups_repository.create(
            AdminGroup(name=name, organization_id=organization_id, created_by=user_id))

    async def initiate_organization_for_current_user(self, token: str, organization_id: int):
        user = await  self.auth_service.get_current_user(token)

        if not user:
            NotFoundException()

        await self.map_user_to_organization(
            user_id=user.id,
            organization_id=organization_id,
            role=UserRole.ADMIN
        )

        await self._create_default_admin_group(
            name="default",
            organization_id=organization_id,
            user_id=user.id
        )
