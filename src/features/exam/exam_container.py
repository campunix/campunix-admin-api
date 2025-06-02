from dependency_injector import containers, providers

from src.features.exam.services.exam_routine_service import ExamRoutineService
from src.infrastructure.base_container import BaseContainer


class ExamContainer(BaseContainer):
    wiring_config = containers.WiringConfiguration(modules=[".exam_routes"])

    exam_routine_service = providers.Factory(
        ExamRoutineService,
        exam_routines_repository=BaseContainer.exam_routines_repository,
    )
