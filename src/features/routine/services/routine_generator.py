import random
from typing import List

from src.features.routine.models.chromosome import Chromosome
from src.features.routine.models.gene import Gene

class RoutineGenerator:
    def __init__(self):
        self.available_genes = [
            Gene("CSE-203", "EI", "2-1", 2, True),
            Gene("CSE-205", "NAR", "2-1", 2, False),
            Gene("CSE-206", "GM", "2-1", 2, False),
            Gene("CSE-207", "MMB", "2-1", 2, False),
            Gene("CSE-208", "MZR", "2-1", 2, False),
            Gene("CSE-209", "MAI", "2-1", 2, False),
            Gene("CSE-210", "MAI", "2-1", 2, True),
            Gene("CSE-212", "EI", "2-1", 2, True),
            Gene("CSE-303", "SKS", "3-1", 3, False),
            Gene("CSE-304", "SKS", "3-1", 3, True),
            Gene("CSE-305", "BA", "3-1", 3, False),
            Gene("CSE-307", "JKD", "3-1", 3, False),
            Gene("CSE-309", "AKA", "3-1", 3, False),
            Gene("CSE-314", "SB", "3-1", 3, True),
        ]
        self.total_population = 10
        self._random = random.Random()

    def generate(self, total_slots: int):
        self.total_slots = total_slots
        chromosomes = self.initialize_population()

        generation = 0
        while generation < 1500:  # max generations
            # Evaluate fitness
            for chromosome in chromosomes:
                chromosome.calculate_fitness()

            # Sort population by fitness
            chromosomes = sorted(chromosomes, key=lambda x: x.fitness, reverse=True)

            # If best solution found, break
            if chromosomes[0].fitness == 1.0:
                print("Optimal schedule found:")
                self.print_schedule(chromosomes[0])
                chromosomes[0].calculate_fitness()
                return chromosomes[0]

            # Selection
            new_chromosomes = self.select_best_population(chromosomes)

            new_chromosomes = self.perform_crossover(new_chromosomes)

            new_chromosomes = self.perform_mutation(new_chromosomes)

            chromosomes = new_chromosomes
            generation += 1

        return chromosomes[0]

    def initialize_population(self) -> List[Chromosome]:
        chromosomes = []
        for _ in range(self.total_population):
            chromosomes.append(Chromosome(
                total_slots = self.total_slots,
                  available_genes=self.available_genes))
        return chromosomes
    
    @staticmethod
    def select_best_population(population: List[Chromosome]) -> List['Chromosome']:
        return population[:5]  # Select top 5 schedules

    @staticmethod
    def perform_crossover(population: List[Chromosome]) -> List['Chromosome']:
        new_population = population.copy()
        for i in range(0, len(population) - 1, 2):
            parent1 = population[i]
            parent2 = population[i + 1]
            child = parent1.crossover(parent2)
            new_population.append(child)
        return new_population

    def perform_mutation(self, population: List[Chromosome]) -> List['Chromosome']:
        for schedule in population:
            if self._random.random() < 0.1:  # Mutation rate of 10%
                schedule.mutate()
        return population

    @staticmethod
    def print_schedule(schedule: Chromosome):
        print(f"Conflicts: {schedule.conflicts}")
        
        ordered_genes = sorted(schedule.genes, key=lambda x: x.cell_number)
        for i, gene in enumerate(ordered_genes, start=1):
            print(f"Time Slot {i}: Class - {gene.course_code}, Teacher - {gene.course_teacher}, CellNumber - {gene.cell_number}, (row, col) = ({gene.cell_number // 5}, {gene.cell_number % 5})")
