import random
from typing import List

from src.features.routine.models.gene import Gene

class Chromosome:
    def __init__(self, total_slots: int, total_semesters: int, available_genes: List[Gene] = None):
        self.genes = []
        self.conflicts = 0
        self.fitness = 0.0
        self.total_slots = total_slots
        self.total_semesters = total_semesters
        self.total_days = 5  # TODO: have to set dynamically
        
        if available_genes:
            for gene in available_genes:
                gene.set_cell_number(self.calculate_cell_number(gene))
                self.genes.append(gene)

    def calculate_fitness(self):
        conflicts = 0

        for i in range(len(self.genes)):
            conflicts += 2*(1 - self.genes[i].get_preference_satisfication_ratio(self.total_slots, self.total_semesters))

            if (self.genes[i].course.is_lab and self.genes[i].is_last_slot(self.total_slots)):
                conflicts += 5

            for j in range(i + 1, len(self.genes)):
                if i == j:
                    continue

                if self.genes[i].cell_number == self.genes[j].cell_number:
                    conflicts += 10

                if (self.genes[i].has_same_course_teacher_of(self.genes[j]) and
                    self.genes[i].is_in_same_slot_on_same_day_of(self.genes[j], self.total_slots, self.total_semesters)):
                    conflicts += 3

                if (self.genes[i].course.is_lab and
                    self.genes[i].has_same_course_teacher_of(self.genes[j]) and
                    self.genes[i].is_in_previous_slot_on_same_day_of(self.genes[j], self.total_slots, self.total_semesters)):
                    conflicts += 3
                
                if (self.genes[i].course.is_lab and
                    self.genes[i].has_same_semester_of(self.genes[j]) and
                    self.genes[i].is_in_previous_slot_on_same_day_of(self.genes[j], self.total_slots, self.total_semesters)):
                    conflicts += 3

        self.conflicts = conflicts
        self.fitness = 1.0 / (1 + conflicts)

    def crossover(self, other: 'Chromosome') -> 'Chromosome':
        child = Chromosome(self.total_slots, self.total_semesters)

        for i in range(len(self.genes)):
            gene = self.genes[i] if random.random() < 0.5 else other.genes[i]
            child.genes.append(gene)

        return child

    def mutate(self):
        index = random.randint(0, len(self.genes) - 1)

        # TODO: what if we only assign empty cell numbers? and this section must be improved using hash map or something
        max_attempt = 10
        while(max_attempt > 0):
            max_attempt -= 1
            new_cell_number = self.calculate_cell_number(self.genes[index])

            is_same_cell_number = False
            for gene in self.genes:
                if gene.cell_number == new_cell_number:
                    is_same_cell_number = True
                    break

            if not is_same_cell_number:
                break

        self.genes[index].set_cell_number(new_cell_number)

    def calculate_cell_number(self, gene: Gene) -> int:
        current_semester = gene.semester.number
        total_cells_in_a_day = self.total_semesters * self.total_slots

        total_slots = self.total_slots - 1 if gene.course.is_lab else self.total_slots # since lab takes 2 slots so it should not be slot
        cell_number = (random.randint(0, total_slots - 1) + ((current_semester - 1) * self.total_slots)) + \
                      (random.randint(0, self.total_days - 1) * total_cells_in_a_day)

        return cell_number