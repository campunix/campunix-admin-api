from dependency_injector import containers, providers

from src.auth.repositories.auth_repository import AuthRepository
from src.auth.services.auth_service import AuthService
from src.auth.services.auth_service_contract import AuthServiceContract
from src.infrastructure.base_container import BaseContainer
from src.infrastructure.database import Database
from src.core.config import settings
from src.infrastructure.database2 import Database2


class AuthContainer(BaseContainer):
    wiring_config = containers.WiringConfiguration(modules=["..routes.auth_routes"])

    db = providers.Singleton(Database2)
    db_session = providers.Resource(db.provided.get_session())

    auth_repository = providers.Factory(AuthRepository, db_session=db_session)
    auth_service = providers.Factory(AuthService, repository=auth_repository)
