from dependency_injector import containers, providers

from src.core.repositories.syllabus_repository import SyllabusRepository
from src.features.syllabus.services.syllabus_service import SyllabusService
from src.infrastructure.base_container import BaseContainer


class SyllabusContainer(BaseContainer):
    wiring_config = containers.WiringConfiguration(modules=[".syllabus_routes"])
    syllabus_repository = providers.Factory(SyllabusRepository, db_session=BaseContainer.db_session)
    syllabus_service = providers.Factory(SyllabusService, syllabus_repository=syllabus_repository)
