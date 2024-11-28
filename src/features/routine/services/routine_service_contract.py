from abc import ABC


class RoutineServiceContract(ABC):
    
    async def generate_routine_async(self, total_slots: int):
        pass