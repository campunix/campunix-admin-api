class RoutineTeacher:
    id: int
    full_name: str
    email: str
    designation: str
    status: str

    def __init__(self, id: int, full_name: str, email: str, designation: str, status):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.designation = designation
        self.status = status