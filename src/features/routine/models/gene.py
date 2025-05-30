from src.features.routine.models.routine_course import RoutineCourse
from src.features.routine.models.routine_semester import RoutineSemester


class Gene():
    def __init__(self, course: RoutineCourse, semester: RoutineSemester):
        self.course = course
        self.semester = semester
        self.cell_number = None

    def has_same_course_code_of(self, gene: 'Gene') -> bool:
        return self.course.code == gene.course.code

    def has_same_course_teacher_of(self, gene: 'Gene') -> bool:
        for item1 in self.course.teachers:
            for item2 in gene.course.teachers:
                if item1.id == item2.id:
                    return True

    def has_same_semester_of(self, gene: 'Gene') -> bool:
        return self.semester.number == gene.semester.number

    def is_in_same_slot_on_same_day_of(self, gene: 'Gene', total_slots: int, total_semesters: int) -> bool:
        return self.is_in_same_day_of(gene, total_slots, total_semesters) and self.is_in_same_slot_of(gene, total_slots)

    def is_in_previous_slot_on_same_day_of(self, gene: 'Gene', total_slots: int, total_semesters: int) -> bool:
        return self.is_in_same_day_of(gene, total_slots, total_semesters) and self.is_in_previous_slot_of(gene, total_slots)

    def is_in_next_slot_on_same_day(self, gene: 'Gene', total_slots: int, total_semesters: int) -> bool:
        return self.is_in_same_day_of(gene, total_slots, total_semesters) and self.is_in_next_slot_of(gene, total_slots)

    def is_in_same_slot_of(self, gene: 'Gene', total_slots: int) -> bool:
        return self.get_slot_no(total_slots) == gene.get_slot_no(total_slots)

    def is_in_previous_slot_of(self, gene: 'Gene', total_slots: int) -> bool:
        return self.get_slot_no(total_slots) == gene.get_slot_no(total_slots) - 1

    def is_in_next_slot_of(self, gene: 'Gene', total_slots: int) -> bool:
        return self.get_slot_no(total_slots) == gene.get_slot_no(total_slots) + 1

    def is_last_slot(self, total_slots: int) -> bool:
        return self.get_slot_no(total_slots) == (total_slots - 1)

    def is_in_same_day_of(self, gene: 'Gene', total_slots: int, total_semesters: int) -> bool:
        cell1_day = self.get_day_no(total_slots, total_semesters)
        cell2_day = gene.get_day_no(total_slots, total_semesters)
        return cell1_day == cell2_day
    
    def get_slot_no(self, total_slots: int) -> int:
        return self.cell_number % total_slots
    
    def get_day_no(self, total_slots: int, total_semesters: int) -> int:
        total_cells_in_a_day = total_slots * total_semesters
        return self.cell_number // total_cells_in_a_day