from src.features.routine.models.routine_teacher import RoutineTeacher


class RoutineCourse:
    id: int
    title: str
    code: str
    course_type: str
    is_lab: bool
    teachers: list[RoutineTeacher] = []

    def __init__(self, id: int, title: str, code: str, course_type: str, teachers: list[any] = None):
        self.id = id
        self.title = title
        self.code = code
        self.course_type = course_type
        self.is_lab = course_type is 'LAB'
        self.teachers = []
        for teacher in teachers or []:
            self.teachers.append(
                RoutineTeacher(
                    id=teacher.id,
                    full_name=teacher.full_name,
                    email=teacher.email,
                    designation=teacher.designation,
                    status=teacher.status
                )
            )