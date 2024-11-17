from src.utils.oauth2_utils import pwd_context

data = {
    "users": [
        {
            "username": "admin1",
            "email": "admin1@campunix.com",
            "full_name": "Admin 1",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "admin2",
            "email": "admin2@campunix.com",
            "full_name": "Admin 2",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "teacher1",
            "email": "teacher1@campunix.com",
            "full_name": "Teacher 1",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "teacher2",
            "email": "teacher2@campunix.com",
            "full_name": "Teacher 2",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "teacher3",
            "email": "teacher3@campunix.com",
            "full_name": "Teacher 3",
            "password_hash": pwd_context.hash("1234")
        }
    ],
    "organizations": [
        {
            "name": "JU"
        },
        {
            "name": "DU"
        }
    ],
    "departments": [
        {
            "name": "Computer Science and Engineering",
            "code": "CSE",
            "organization_id": 1,
            "created_by": 1
        },
        {
            "name": "Bangla",
            "code": "BNG",
            "organization_id": 1,
            "created_by": 1
        },
        {
            "name": "Mathematics",
            "code": "MATH",
            "organization_id": 1,
            "created_by": 1
        },
        {
            "name": "Physics",
            "code": "PHY",
            "organization_id": 1,
            "created_by": 1
        }
    ],
    "user_organizations": [
        {
            "user_id": 1,
            "organization_id": 1,
            "role": "ADMIN"
        },
        {
            "user_id": 2,
            "organization_id": 2,
            "role": "ADMIN"
        },
        {
            "user_id": 3,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 4,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 5,
            "organization_id": 2,
            "role": "TEACHER"
        }
    ],
    "semesters": [
        {
            "year": 1,
            "number": 1,
            "disabled": False,
            "department_id": 1
        },
        {
            "year": 1,
            "number": 2,
            "disabled": False,
            "department_id": 1
        },
        {
            "year": 2,
            "number": 1,
            "disabled": False,
            "department_id": 1
        },
        {
            "year": 2,
            "number": 2,
            "disabled": False,
            "department_id": 1
        },
        {
            "year": 3,
            "number": 1,
            "disabled": False,
            "department_id": 1
        },
        {
            "year": 3,
            "number": 2,
            "disabled": False,
            "department_id": 1
        },
        {
            "year": 4,
            "number": 1,
            "disabled": False,
            "department_id": 1
        },
        {
            "year": 4,
            "number": 2,
            "disabled": False,
            "department_id": 1
        }
    ],
    "courses": [
        {
            "title": "Structured Programming",
            "code": "CSE-105",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Structured Programming Laboratory",
            "code": "CSE-106",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Electrical Circuits",
            "code": "CSE-107",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Electrical Circuits Laboratory",
            "code": "CSE-108",
            "department_id": 1,
            "course_type": "LAB"
        },
    ],
    "teachers": [
        {
            "user_id": 3,
            "designation": "PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 4,
            "designation": "PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        }
    ],
    "teacher_courses": [
        {
            "teacher_id": 1,
            "course_id": 1
        },
        {
            "teacher_id": 1,
            "course_id": 2,
        },
        {
            "teacher_id": 2,
            "course_id": 3,
        },
        {
            "teacher_id": 2,
            "course_id": 4,
        }
    ]
}
