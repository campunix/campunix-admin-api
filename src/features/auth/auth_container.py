from dependency_injector import containers, providers
from src.core.repositories.users_repository import UsersRepository
from src.features.auth.services.auth_service import AuthService
from src.infrastructure.base_container import BaseContainer


class AuthContainer(BaseContainer):
    wiring_config = containers.WiringConfiguration(modules=[".auth_routes"])

    users_repository = providers.Factory(UsersRepository, db_session=BaseContainer.db_session)
    # users_repository = providers.Factory(FakeUsersRepository, db_session=BaseContainer.db_session)
    auth_service = providers.Factory(AuthService, users_repository=users_repository)
