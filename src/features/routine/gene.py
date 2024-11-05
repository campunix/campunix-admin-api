class Gene():
    def __init__(self, course_code: str, course_teacher: str, semester: str, semester_number: int, is_lab: bool):
        self.course_code = course_code
        self.course_teacher = course_teacher
        self.semester = semester
        self.semester_number = semester_number
        self.is_lab = is_lab
        self.cell_number = None

    def has_same_course_code_of(self, gene: 'Gene') -> bool:
        return self.course_code == gene.course_code

    def has_same_course_teacher_of(self, gene: 'Gene') -> bool:
        return self.course_teacher == gene.course_teacher

    def has_same_semester_of(self, gene: 'Gene') -> bool:
        return self.semester_number == gene.semester_number

    def is_in_same_slot_on_same_day_of(self, gene: 'Gene', total_slot: int, total_semester: int) -> bool:
        return self.is_in_same_day_of(gene, total_slot, total_semester) and self.is_in_same_slot_of(gene, total_slot)

    def is_in_previous_slot_on_same_day_of(self, gene: 'Gene', total_slot: int, total_semester: int) -> bool:
        return self.is_in_same_day_of(gene, total_slot, total_semester) and self.is_in_previous_slot_of(gene, total_slot)

    def is_in_next_slot_on_same_day(self, gene: 'Gene', total_slot: int, total_semester: int) -> bool:
        return self.is_in_same_day_of(gene, total_slot, total_semester) and self.is_in_next_slot_of(gene, total_slot)

    def is_in_same_slot_of(self, gene: 'Gene', total_slot: int) -> bool:
        return self.cell_number % total_slot == gene.cell_number % total_slot

    def is_in_previous_slot_of(self, gene: 'Gene', total_slot: int) -> bool:
        return self.cell_number % total_slot == (gene.cell_number % total_slot) - 1

    def is_in_next_slot_of(self, gene: 'Gene', total_slot: int) -> bool:
        return self.cell_number % total_slot == (gene.cell_number % total_slot) + 1

    def is_last_slot(self, total_slot: int) -> bool:
        return self.cell_number % total_slot == (total_slot - 1)

    def is_in_same_day_of(self, gene: 'Gene', total_slot: int, total_semester: int) -> bool:
        total_cell_in_a_day = total_slot * total_semester
        cell1_day = self.cell_number // total_cell_in_a_day
        cell2_day = gene.cell_number // total_cell_in_a_day
        return cell1_day == cell2_day