from src.features.routine.models.routine_preference import RoutinePreference


class RoutineTeacher:
    id: int
    full_name: str
    email: str
    designation: str
    status: str
    preferences: list[RoutinePreference] = []

    def __init__(self, id: int, full_name: str, email: str, designation: str, status: str, preferences: list[any] = None):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.designation = designation
        self.status = status
        self.preferences = []
        for item in preferences or []:
            self.preferences.append(
                RoutinePreference(
                    id=item.id,
                    day=item.day,
                    slot_no=item.slot_no,
                )
            )