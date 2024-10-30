from src.core.contracts.admin_groups_repository_contract import (
    AdminGroupsRepositoryContract,
)
from src.core.contracts.organizations_repository_contract import (
    OrganizationsRepositoryContract,
)
from src.features.admin.admin_service_contract import AdminServiceContract


class AdminService(AdminServiceContract):
    def __init__(
        self,
        organizations_repository: OrganizationsRepositoryContract,
        admin_groups_repository: AdminGroupsRepositoryContract,
    ):
        self.organizations_repository = organizations_repository
        self.admin_groups_repository = admin_groups_repository
