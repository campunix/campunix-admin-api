from src.features.routine.models.gene import Gene
from src.features.routine.models.routine_course import RoutineCourse
from src.features.routine.models.routine_out import RoutineOut
from src.features.routine.models.routine_semester import RoutineSemester
from src.features.routine.services.routine_generator_contract import RoutineGeneratorContract
from src.features.routine.services.routine_service_contract import RoutineServiceContract
from src.features.syllabus.services.syllabus_service_contract import SyllabusServiceContract


class RoutineService(RoutineServiceContract):
    def __init__(self, routine_generator: RoutineGeneratorContract, syllabus_service: SyllabusServiceContract):
        self.routine_generator = routine_generator
        self.syllabus_service = syllabus_service

    async def generate_routine_async(self, total_slots: int):
        syllabus_courses = await self.syllabus_service.get_course_list(1)

        course_dict = self.get_courses_from_syllabus(syllabus_courses)
        semester_dict = self.get_semesters_from_syllabus(syllabus_courses)
        available_genes = self.get_genes_from_syllabus(syllabus_courses, course_dict, semester_dict)

        chromosome = await self.routine_generator.generate_async(
            total_slots=total_slots,
            total_semesters=len(semester_dict),
            available_genes=available_genes)
        
        return RoutineOut(
            courses=list(course_dict.values()),
            semesters=list(semester_dict.values()),
            routine=chromosome
        )

    def get_genes_from_syllabus(self, syllabus_courses, course_dict, semester_dict):

        available_genes = []
        for x in syllabus_courses:
            course = course_dict[x["course"].code]
            semester = semester_dict[x["semester"].id]

            available_genes.append(Gene(
                course_code=course.code,
                is_lab=course.is_lab,
                course_teacher=x["teacher"].full_name,
                semester=semester.id,
                semester_number=semester.serial_number))
        
        return available_genes

    def get_courses_from_syllabus(self, syllabus_courses):
        course_dict: dict[str, RoutineCourse] = dict()

        for x in syllabus_courses:
            if x["course"].code not in course_dict:
                course_dict[x["course"].code] = RoutineCourse(
                    id=x["course"].id,
                    code=x["course"].code,
                    title=x["course"].title,
                    course_type=x["course"].course_type
                )

        return course_dict
    
    def get_semesters_from_syllabus(self, syllabus_courses):
        semester_dict: dict[int, RoutineSemester] = dict()

        for x in syllabus_courses:
            if x["semester"].id not in semester_dict:
                semester_dict[x["semester"].id] = RoutineSemester(
                    id=x["semester"].id,
                    year=x["semester"].year,
                    number=x["semester"].number
                )

        sorted_semesters = sorted(
            semester_dict.values(),
              key=lambda semester: semester.number) or []
        
        semester_code_dict = {x.id: idx + 1 for idx, x in enumerate(sorted_semesters)}
        for key, value in semester_dict.items():
            value.serial_number = semester_code_dict[value.id]

        return semester_dict