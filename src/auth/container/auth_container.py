from dependency_injector import containers, providers
from src.auth.repositories.fake_users_repository import FakeUsersRepository
from src.auth.services.auth_service import AuthService
from src.auth.services.auth_service_contract import AuthServiceContract
from src.core.repositories.users_repository import UsersRepository
from src.infrastructure.base_container import BaseContainer
from src.infrastructure.database import Database
from src.core.config import settings
from src.infrastructure.database2 import Database2


class AuthContainer(BaseContainer):
    wiring_config = containers.WiringConfiguration(modules=["..routes.auth_routes"])

    db = providers.Singleton(Database2)
    db_session = providers.Resource(db.provided.get_session())

    users_repository = providers.Factory(UsersRepository, db_session=db_session)
    # users_repository = providers.Factory(FakeUsersRepository, db_session=db_session)
    auth_service = providers.Factory(AuthService, users_repository=users_repository)
