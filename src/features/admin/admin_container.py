from dependency_injector import containers, providers
from src.core.repositories.admin_groups_repository import AdminGroupsRepository
from src.core.repositories.organizations_repository import OrganizationsRepository
from src.features.admin.services.admin_service import AdminService
from src.features.admin.services.organization_service import OrganizationService
from src.infrastructure.base_container import BaseContainer


class AdminContainer(BaseContainer):
    wiring_config = containers.WiringConfiguration(modules=[".routes.admin_routes", ".routes.organization_routes"])

    organizations_repository = providers.Factory(
        OrganizationsRepository, db_session=BaseContainer.db_session
    )

    admin_groups_repository = providers.Factory(
        AdminGroupsRepository, db_session=BaseContainer.db_session
    )

    admin_service = providers.Factory(
        AdminService,
        organizations_repository=organizations_repository,
        admin_groups_repository=admin_groups_repository,
    )

    organization_service = providers.Factory(
        OrganizationService,
        organizations_repository=organizations_repository,
    )
