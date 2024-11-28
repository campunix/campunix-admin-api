from abc import ABC, abstractmethod

from src.features.routine.models.gene import Gene

class RoutineGeneratorContract(ABC):

    @abstractmethod
    async def generate_async(self, total_slots: int, total_semesters: int, available_genes: list[Gene]):
        pass