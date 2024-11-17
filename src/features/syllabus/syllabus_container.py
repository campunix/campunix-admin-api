from dependency_injector import containers, providers

from src.core.repositories.syllabus_repository import SyllabusRepository
from src.features.admin.services.TeacherService import TeacherService
from src.features.admin.services.course_service import CourseService
from src.features.admin.services.teacher_course_service import TeacherCourseService
from src.features.syllabus.services.syllabus_service import SyllabusService
from src.infrastructure.base_container import BaseContainer


class SyllabusContainer(BaseContainer):
    wiring_config = containers.WiringConfiguration(modules=[".syllabus_routes"])

    syllabus_repository = providers.Factory(SyllabusRepository, db_session=BaseContainer.db_session)

    course_service = providers.Factory(
        CourseService,
        course_repository=BaseContainer.courses_repository
    )

    teacher_service = providers.Factory(
        TeacherService,
        teachers_repository=BaseContainer.teachers_repository,
        users_repository=BaseContainer.users_repository,
    )

    teacher_course_service = providers.Factory(
        TeacherCourseService,
        teacher_course_repository=BaseContainer.teacher_courses_repository,
        teacher_service=teacher_service,
        course_service=course_service
    )


    syllabus_service = providers.Factory(
        SyllabusService,
        syllabus_repository=syllabus_repository,
        departments_repository=BaseContainer.departments_repository,
        courses_repository=BaseContainer.courses_repository,
        semesters_repository=BaseContainer.semesters_repository,
        teachers_course_service=teacher_course_service
    )
