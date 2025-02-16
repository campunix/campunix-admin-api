from src.core.contracts.exam_routine_course_teachers_repository_contract import \
    ExamRoutineCourseTeachersRepositoryContract
from src.core.contracts.exam_routine_courses_repository_contract import ExamRoutineCoursesRepositoryContract
from src.core.contracts.exam_routines_repository_contract import ExamRoutinesRepositoryContract
from src.features.exam.services.exam_routine_service_contract import ExamRoutineServiceContract


class ExamRoutineService(ExamRoutineServiceContract):
    def __init__(
            self,
            exam_routines_repository: ExamRoutinesRepositoryContract,
            exam_routine_courses_repository: ExamRoutineCoursesRepositoryContract,
            exam_routine_course_teachers_repository: ExamRoutineCourseTeachersRepositoryContract,
    ):
        self.exam_routines_repository = exam_routines_repository
        self.exam_routine_courses_repository = exam_routine_courses_repository
        self.exam_routine_course_teachers_repository = exam_routine_course_teachers_repository
