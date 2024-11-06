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
  ]
}
