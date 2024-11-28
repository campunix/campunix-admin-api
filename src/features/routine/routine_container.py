from dependency_injector import containers, providers
from src.core.repositories.users_repository import UsersRepository
from src.features.auth.services.auth_service import AuthService
from src.features.routine.services.routine_generator import RoutineGenerator
from src.features.routine.services.routine_service import RoutineService
from src.features.syllabus.syllabus_container import SyllabusContainer
from src.infrastructure.base_container import BaseContainer


class RoutineContainer(BaseContainer):
    wiring_config = containers.WiringConfiguration(modules=[".routine_routes"])

    routine_generator = providers.Factory(RoutineGenerator)
    routine_service = providers.Factory(RoutineService, routine_generator, SyllabusContainer.syllabus_service)
