from dependency_injector import containers, providers

from src.auth.repositories.auth_repository import AuthRepository
from src.auth.services.auth_service import AuthService
from src.auth.services.auth_service_contract import AuthServiceContract
from src.infrastructure.database import Database
from src.core.config import settings


class AuthContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["..routes.auth_routes"]
    )

    db_session = providers.Singleton(Database, db_url=str(settings.DATABASE_URL))

    auth_repository = providers.Factory(AuthRepository, session_factory=db_session)
    auth_service = providers.Factory(AuthService, repository=auth_repository)
