from dependency_injector import containers, providers

from src.core.repositories.exam_routine_course_teachers_repository import ExamRoutineCourseTeachersRepository
from src.core.repositories.exam_routine_courses_repository import ExamRoutineCoursesRepository
from src.core.repositories.exam_routines_repository import ExamRoutinesRepository
from src.features.exam.services.exam_routine_service import ExamRoutineService
from src.infrastructure.base_container import BaseContainer


class ExamContainer(BaseContainer):
    wiring_config = containers.WiringConfiguration(modules=[".exam_routes"])

    exam_routines_repository = providers.Factory(
        ExamRoutinesRepository,
        db_session=BaseContainer.db_session
    )

    exam_routine_courses_repository = providers.Factory(
        ExamRoutineCoursesRepository,
        db_session=BaseContainer.db_session)

    exam_routine_course_teachers_repository = providers.Factory(
        ExamRoutineCourseTeachersRepository,
        db_session=BaseContainer.db_session
    )

    exam_routine_service = providers.Factory(
        ExamRoutineService,
        exam_routines_repository=exam_routines_repository,
        exam_routine_courses_repository=exam_routine_courses_repository,
        exam_routine_course_teachers_repository=exam_routine_course_teachers_repository
    )
