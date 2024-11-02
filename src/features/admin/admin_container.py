from dependency_injector import containers, providers

from src.features.admin.services.admin_service import AdminService
from src.features.auth.services.auth_service import AuthService
from src.infrastructure.base_container import BaseContainer


class AdminContainer(BaseContainer):
    wiring_config = containers.WiringConfiguration(packages=["."])

    auth_service = providers.Factory(
        AuthService,
        users_repository=BaseContainer.users_repository,
    )

    admin_service = providers.Factory(
        AdminService,
        user_organizations_repository=BaseContainer.user_organizations_repository,
        admin_groups_repository=BaseContainer.admin_groups_repository,
        auth_service=auth_service,
    )


