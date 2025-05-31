import random
from typing import List

from src.features.routine.models.chromosome import Chromosome
from src.features.routine.models.gene import Gene
from src.features.routine.services.routine_generator_contract import RoutineGeneratorContract
from src.features.syllabus.services.syllabus_service_contract import SyllabusServiceContract

class RoutineGenerator(RoutineGeneratorContract):
    total_semesters: int
    total_slots: int = 2
    total_population: int = 15
    available_genes: list[Gene] = []

    def __init__(self):
        self._random = random.Random()

    async def generate_async(self, total_slots: int, total_semesters: int, available_genes: list[Gene]):

        self.total_slots = total_slots
        self.total_semesters = total_semesters
        self.available_genes = available_genes or []

        chromosomes = self.initialize_population()

        generation = 0
        max_generations = 3000

        while generation < max_generations:  # max generations
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
                total_slots=self.total_slots,
                total_semesters=self.total_semesters,
                available_genes=self.available_genes))
        return chromosomes
    
    def select_best_population(self, population: List[Chromosome]) -> List['Chromosome']:
        best_population_size = 6
        return population[:best_population_size]

    @staticmethod
    def perform_crossover(population: List[Chromosome]) -> List['Chromosome']:
        length = len(population)
        for i in range(0, length - 1, 2):
            parent1 = population[i]
            parent2 = population[i + 1]
            child = parent1.crossover(parent2)
            population.append(child)
        return population

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
            print(f"Time Slot {i}: Class - {gene.course.code}, Teacher - {gene.course.teachers}, CellNumber - {gene.cell_number}, (row, col) = ({gene.cell_number // 5}, {gene.cell_number % 5})")
