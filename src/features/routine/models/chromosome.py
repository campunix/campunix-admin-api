import random
from typing import List

from src.features.routine.models.gene import Gene

class Chromosome:
    total_slots = 5
    total_semesters = 2
    
    def __init__(self, total_slots: int, available_genes: List[Gene] = None):
        self.genes = []
        self.conflicts = 0
        self.fitness = 0.0
        self.total_slots = total_slots
        
        if available_genes:
            for gene in available_genes:
                gene.cell_number = self.calculate_cell_number(gene)
                self.genes.append(gene)

    def calculate_fitness(self):
        conflicts = 0

        for i in range(len(self.genes)):
            for j in range(len(self.genes)):
                if i == j:
                    continue

                if self.genes[i].cell_number == self.genes[j].cell_number:
                    conflicts += 1

                if ((self.genes[i].is_lab and self.genes[i].is_last_slot(self.total_slots)) or
                    (self.genes[j].is_lab and self.genes[j].is_last_slot(self.total_slots))):
                    conflicts += 1

                if (self.genes[i].has_same_course_teacher_of(self.genes[j]) and
                    self.genes[i].is_in_same_slot_on_same_day_of(self.genes[j], self.total_slots, self.total_semesters)):
                    conflicts += 1

                if (self.genes[i].is_lab and
                    self.genes[i].has_same_course_teacher_of(self.genes[j]) and
                    self.genes[i].is_in_previous_slot_on_same_day_of(self.genes[j], self.total_slots, self.total_semesters)):
                    conflicts += 1

                if (self.genes[i].is_lab and
                    self.genes[i].has_same_semester_of(self.genes[j]) and
                    self.genes[i].is_in_previous_slot_on_same_day_of(self.genes[j], self.total_slots, self.total_semesters)):
                    conflicts += 1

        self.conflicts = conflicts
        self.fitness = 1.0 / (1 + conflicts)

    def crossover(self, other: 'Chromosome') -> 'Chromosome':
        child = Chromosome(self.total_slots)

        for i in range(len(self.genes)):
            gene = self.genes[i] if random.random() < 0.5 else other.genes[i]
            child.genes.append(gene)

        return child

    def mutate(self):
        index = random.randint(0, len(self.genes) - 1)
        self.genes[index].cell_number = self.calculate_cell_number(self.genes[index])

    def calculate_cell_number(self, gene: Gene) -> int:
        total_cells_in_a_day = self.total_semesters * self.total_slots
        current_semester = gene.semester_number

        cell_number = (random.randint(0, 4) + ((current_semester - 1) * self.total_slots)) + \
                      (random.randint(0, 4) * total_cells_in_a_day)

        return cell_number