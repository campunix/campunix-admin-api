from src.utils.oauth2_utils import pwd_context

data = {
    "users": [
        {
            "username": "cedas",
            "email": "cedas@juniv.edu",
            "full_name": "Dr. Jugal Krishna Das, B.Sc(Donetsk), MSc.(Donetsk), PhD(Kiev)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "shorifuddin",
            "email": "shorifuddin@juniv.edu",
            "full_name": "Dr. Mohammad Shorif Uddin, B.Sc. Engg. (BUET), M.Tech.Ed.(Japan), Ph.D.(Japan)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "rmzahid",
            "email": "rmzahid@juniv.edu",
            "full_name": "Dr. Mohammad Zahidur Rahman, B.Sc(BUET), MSc.(BUET), PhD(Malaysia)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "imdad",
            "email": "imdad@juniv.edu",
            "full_name": "Dr. Md. Imdadul Islam, B.Sc. Engg. (BUET), MSc. Engg. (BUET), PhD (JU)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "litonrozario",
            "email": "litonrozario@juniv.edu",
            "full_name": "Dr. Liton Jude Rozario, B.Sc(JU), MS(JU), PhD(JU)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "khokan",
            "email": "khokan@juniv.edu",
            "full_name": "Dr. Md. Golam Moazzam, B.Sc(JU), MS(JU), PhD(JU)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "israt",
            "email": "israt@juniv.edu",
            "full_name": "Dr. Israt Jahan, B.Sc(BUET), MSc.(BUET), PhD(JU)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "hkabir",
            "email": "hkabir@juniv.edu",
            "full_name": "Dr. Md. Humayun Kabir, B.Sc(DU), MSc.(DU), PhD(Ireland)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "makazad",
            "email": "makazad@juniv.edu",
            "full_name": "Dr. Md Abul Kalam Azad, BSc(JU), MSc(KTH, Sweden), PhD(JU), PhD(UoU, South Korea)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "asmmr",
            "email": "asmmr@juniv.edu",
            "full_name": "Dr. Abu Sayed Md. Mostafizur Rahaman, B.Sc(JU), MSc.(Germany) PhD(JU)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "ezharul.islam",
            "email": "ezharul.islam@juniv.edu",
            "full_name": "Dr. Md. Ezharul Islam, B.SC.(JU), M.ENGG.(JAPAN), PHD(JAPAN)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "morium.akter",
            "email": "morium.akter@juniv.edu",
            "full_name": "Dr. Morium Akter",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "sanjit",
            "email": "sanjit@juniv.edu",
            "full_name": "Dr.-Ing. Sanjit Kumar Saha",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "manwar",
            "email": "manwar@juniv.edu",
            "full_name": "Dr. Md. Musfique Anwar B.Sc (JU), MSc. (Japan), PhD (Australia)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "sarnali.cse",
            "email": "sarnali.cse@juniv.edu",
            "full_name": "Sarnali Basak, BSc(JU), MSc (The University of Edinburgh, UK)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "tahsina.hashem",
            "email": "tahsina.hashem@juniv.edu",
            "full_name": "Tahsina Hashem, B.Sc. (JU), M.Sc. Engg. (BUET)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "tanzila.rahman",
            "email": "tanzila.rahman@juniv.edu",
            "full_name": "Tanzila Rahman, B.Sc. (JU), M.Sc. (U of M)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "rafsan",
            "email": "rafsan@juniv.edu",
            "full_name": "Md. Rafsan Jani",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "hafsa.moontari.ali",
            "email": "hafsa.moontari.ali@juniv.edu",
            "full_name": "Hafsa Moontari Ali",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "ashraful.islam",
            "email": "ashraful.islam@juniv.edu",
            "full_name": "Mohammad Ashraful Islam",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "bulbul",
            "email": "bulbul@juniv.edu",
            "full_name": "Bulbul Ahammad",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "anupmajumder",
            "email": "anupmajumder@juniv.edu",
            "full_name": "Anup Majumder, B.SC.(JU), MS(JU)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "nadiaritu",
            "email": "nadiaritu@juniv.edu",
            "full_name": "Nadia Afrin Ritu, B.Sc (JU), MSc. (JU)",
            "password_hash": pwd_context.hash("1234")
        },
        {
            "username": "admin",
            "email": "adminu@juniv.edu",
            "full_name": "CSE Admin",
            "password_hash": pwd_context.hash("1234")
        }
    ],
    "organizations": [
        {
            "name": "Jahangirnagar University",

        }
    ],
    "departments": [
        {
            "name": "Computer Science and Engineering",
            "code": "CSE",
            "organization_id": 1,
            "created_by": 24
        }
    ],
    "user_organizations": [
        {
            "user_id": 1,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 2,
            "organization_id": 1,
            "role": "TEACHER"
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
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 6,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 7,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 8,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 9,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 10,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 11,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 12,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 13,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 14,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 15,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 16,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 17,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 18,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 19,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 20,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 21,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 22,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 23,
            "organization_id": 1,
            "role": "TEACHER"
        },
        {
            "user_id": 24,
            "organization_id": 1,
            "role": "ADMIN"
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
            "title": "Viva-Voce",
            "code": "CSE-100",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Mathematics I (Matrix, Differential Calculus and Coordinate Geometry)",
            "code": "MATH-101",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Communicative English",
            "code": "ENG-103",
            "department_id": 1,
            "course_type": "THEORY"
        },
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
        {
            "title": "Physics",
            "code": "PHY-109",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Computer Aided Engineering Drawing Laboratory",
            "code": "URP-112",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Viva-Voce",
            "code": "CSE-150",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Mathematics II (Integral Calculus, Differential Equations and Series Solution)",
            "code": "MATH-151",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Discrete Mathematics",
            "code": "CSE-153",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Data Structures",
            "code": "CSE-155",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Data Structures Laboratory",
            "code": "CSE-156",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Electronic Devices and Circuits-I",
            "code": "CSE-157",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Electronic Devices and Circuits-I Laboratory",
            "code": "CSE-158",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Object Oriented Programming (C++)",
            "code": "CSE-159",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Object Oriented Programming (C++) Laboratory",
            "code": "CSE-160",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Technical Writing and Presentation Laboratory",
            "code": "CSE-162",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Viva-Voce",
            "code": "CSE-200",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Mathematics III (Vector, Complex Variable, Fourier Analysis, and Laplace Transformation)",
            "code": "MATH-201",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Computer Ethics and Cyber Law",
            "code": "CSE-203",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Numerical Methods",
            "code": "CSE-205",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Numerical Methods Laboratory",
            "code": "CSE-206",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Electronic Devices and Circuits-II",
            "code": "CSE-207",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Electronic Devices and Circuits-II Laboratory",
            "code": "CSE-208",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Algorithms-I",
            "code": "CSE-209",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Algorithms-I Laboratory",
            "code": "CSE-210",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Object Oriented Programming (JAVA) Laboratory",
            "code": "CSE-212",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Viva-Voce",
            "code": "CSE-250",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Introduction to Probability and Statistics",
            "code": "STAT-251",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Digital Logic Design",
            "code": "CSE-253",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Digital Logic Design Laboratory",
            "code": "CSE-254",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Database Systems",
            "code": "CSE-255",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Database Systems Laboratory",
            "code": "CSE-256",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Algorithms-II",
            "code": "CSE-257",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Algorithms-II Laboratory",
            "code": "CSE-258",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Data and Telecommunication",
            "code": "CSE-259",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Data and Telecommunication Laboratory",
            "code": "CSE-260",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Viva-Voce",
            "code": "CSE-300",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Economics",
            "code": "ECO-301",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Computer Graphics",
            "code": "CSE-303",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Computer Graphics Laboratory",
            "code": "CSE-304",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Computational Geometry",
            "code": "CSE-305",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Computer Architecture and Organization",
            "code": "CSE-307",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Operating Systems",
            "code": "CSE-309",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Operating Systems Laboratory",
            "code": "CSE-310",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Web Design and Programming Laboratory-I (PHP/C#)",
            "code": "CSE-312",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "OOAD Laboratory",
            "code": "CSE-314",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Viva-Voce",
            "code": "CSE-350",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Management and Accounting",
            "code": "BIS-351",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Human Computer Interaction",
            "code": "CSE-353",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Introduction to Bioinformatics",
            "code": "CSE-355",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Microprocessors",
            "code": "CSE-357",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Microprocessors and Assembly Language Laboratory",
            "code": "CSE-358",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Computer Networks",
            "code": "CSE-359",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Computer Networks Laboratory",
            "code": "CSE-360",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Web Design and Programming Laboratory-II (JSP/Python)",
            "code": "CSE-362",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Viva-Voce",
            "code": "CSE-400",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Theory of Computation and Compiler Design",
            "code": "CSE-401",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Software Engineering and Information System Design",
            "code": "CSE-403",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Software Engineering and ISD Laboratory",
            "code": "CSE-404",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Digital Image Processing",
            "code": "CSE-405",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Digital Image Processing Laboratory",
            "code": "CSE-406",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Wireless Networks",
            "code": "CSE-407",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Mobile Application Development Laboratory",
            "code": "CSE-410",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Research Project",
            "code": "CSE-440",
            "department_id": 1,
            "course_type": "RESEARCH"
        },
        {
            "title": "Viva-Voce",
            "code": "CSE-450",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Data Mining and Big Data Analysis",
            "code": "CSE-451",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Data Mining and Big Data Analysis Laboratory",
            "code": "CSE-452",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Artificial Intelligence",
            "code": "CSE-453",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Artificial Intelligence Laboratory",
            "code": "CSE-454",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Software Quality Assurance",
            "code": "CSE-455",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Machine Learning",
            "code": "CSE-457",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Machine Learning Laboratory",
            "code": "CSE-458",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "IoT Laboratory",
            "code": "CSE-460",
            "department_id": 1,
            "course_type": "LAB"
        },
        {
            "title": "Research Project",
            "code": "CSE-480",
            "department_id": 1,
            "course_type": "RESEARCH"
        }
    ],
    "teachers": [
        {
            "user_id": 1,
            "designation": "PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 2,
            "designation": "PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
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
        },
        {
            "user_id": 5,
            "designation": "PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 6,
            "designation": "PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 7,
            "designation": "PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 8,
            "designation": "PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 9,
            "designation": "ASSOCIATE_PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 10,
            "designation": "PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 11,
            "designation": "ASSOCIATE_PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 12,
            "designation": "ASSISTANT_PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 13,
            "designation": "ASSISTANT_PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 14,
            "designation": "ASSISTANT_PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 15,
            "designation": "ASSISTANT_PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 16,
            "designation": "ASSISTANT_PROFESSOR",
            "status": "LEAVE",
            "department_id": 1
        },
        {
            "user_id": 17,
            "designation": "LECTURER",
            "status": "LEAVE",
            "department_id": 1
        },
        {
            "user_id": 18,
            "designation": "LECTURER",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 19,
            "designation": "ASSISTANT_PROFESSOR",
            "status": "LEAVE",
            "department_id": 1
        },
        {
            "user_id": 20,
            "designation": "ASSISTANT_PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 21,
            "designation": "ASSISTANT_PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 22,
            "designation": "ASSISTANT_PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        },
        {
            "user_id": 23,
            "designation": "ASSISTANT_PROFESSOR",
            "status": "ACTIVE",
            "department_id": 1
        }
    ],
    "teacher_courses": [
        {
            "teacher_id": 1,
            "course_id": 2
        },
        {
            "teacher_id": 2,
            "course_id": 3
        },
        {
            "teacher_id": 3,
            "course_id": 4
        },
        {
            "teacher_id": 4,
            "course_id": 5
        },
        {
            "teacher_id": 5,
            "course_id": 6
        },
        {
            "teacher_id": 6,
            "course_id": 7
        },
        {
            "teacher_id": 7,
            "course_id": 8
        },
        {
            "teacher_id": 8,
            "course_id": 9
        },
        {
            "teacher_id": 9,
            "course_id": 10
        },
        {
            "teacher_id": 10,
            "course_id": 11
        },
        {
            "teacher_id": 11,
            "course_id": 12
        },
        {
            "teacher_id": 12,
            "course_id": 13
        },
        {
            "teacher_id": 13,
            "course_id": 14
        },
        {
            "teacher_id": 14,
            "course_id": 15
        },
        {
            "teacher_id": 15,
            "course_id": 16
        },
        {
            "teacher_id": 18,
            "course_id": 17
        },
        {
            "teacher_id": 20,
            "course_id": 18
        },
        {
            "teacher_id": 21,
            "course_id": 19
        },
        {
            "teacher_id": 22,
            "course_id": 20
        },
        {
            "teacher_id": 23,
            "course_id": 21
        },
        {
            "teacher_id": 1,
            "course_id": 22
        },
        {
            "teacher_id": 2,
            "course_id": 23
        },
        {
            "teacher_id": 3,
            "course_id": 24
        },
        {
            "teacher_id": 4,
            "course_id": 25
        },
        {
            "teacher_id": 5,
            "course_id": 26
        },
        {
            "teacher_id": 6,
            "course_id": 27
        },
        {
            "teacher_id": 7,
            "course_id": 28
        },
        {
            "teacher_id": 8,
            "course_id": 29
        },
        {
            "teacher_id": 9,
            "course_id": 30
        },
        {
            "teacher_id": 10,
            "course_id": 31
        },
        {
            "teacher_id": 11,
            "course_id": 32
        },
        {
            "teacher_id": 12,
            "course_id": 33
        },
        {
            "teacher_id": 13,
            "course_id": 34
        },
        {
            "teacher_id": 14,
            "course_id": 35
        },
        {
            "teacher_id": 18,
            "course_id": 36
        },
        {
            "teacher_id": 20,
            "course_id": 37
        },
        {
            "teacher_id": 21,
            "course_id": 38
        },
        {
            "teacher_id": 22,
            "course_id": 39
        },
        {
            "teacher_id": 23,
            "course_id": 40
        },
        {
            "teacher_id": 1,
            "course_id": 41
        },
        {
            "teacher_id": 2,
            "course_id": 42
        },
        {
            "teacher_id": 3,
            "course_id": 43
        },
        {
            "teacher_id": 4,
            "course_id": 44
        },
        {
            "teacher_id": 5,
            "course_id": 45
        },
        {
            "teacher_id": 6,
            "course_id": 46
        },
        {
            "teacher_id": 7,
            "course_id": 47
        },
        {
            "teacher_id": 8,
            "course_id": 48
        },
        {
            "teacher_id": 9,
            "course_id": 49
        },
        {
            "teacher_id": 10,
            "course_id": 51
        },
        {
            "teacher_id": 11,
            "course_id": 52
        },
        {
            "teacher_id": 12,
            "course_id": 53
        },
        {
            "teacher_id": 13,
            "course_id": 54
        },
        {
            "teacher_id": 14,
            "course_id": 55
        },
        {
            "teacher_id": 18,
            "course_id": 56
        },
        {
            "teacher_id": 20,
            "course_id": 57
        },
        {
            "teacher_id": 21,
            "course_id": 58
        },
        {
            "teacher_id": 22,
            "course_id": 60
        },
        {
            "teacher_id": 23,
            "course_id": 61
        },
        {
            "teacher_id": 1,
            "course_id": 62
        },
        {
            "teacher_id": 2,
            "course_id": 63
        },
        {
            "teacher_id": 3,
            "course_id": 64
        },
        {
            "teacher_id": 4,
            "course_id": 65
        },
        {
            "teacher_id": 5,
            "course_id": 66
        },
        {
            "teacher_id": 6,
            "course_id": 70
        },
        {
            "teacher_id": 7,
            "course_id": 71
        },
        {
            "teacher_id": 8,
            "course_id": 72
        },
        {
            "teacher_id": 9,
            "course_id": 73
        },
        {
            "teacher_id": 10,
            "course_id": 74
        },
        {
            "teacher_id": 11,
            "course_id": 75
        }
    ],
    "rooms": [
        {
            "name": "R-101",
            "code": "R-101",
            "department_id": 1,
            "room_type": "LECTURE"
        },
        {
            "name": "R-102",
            "code": "R-102",
            "department_id": 1,
            "room_type": "LECTURE"
        },
        {
            "name": "Lab-302",
            "code": "Lab-302",
            "department_id": 1,
            "room_type": "LAB"
        },
        {
            "name": "Lab-201",
            "code": "Lab-201",
            "department_id": 1,
            "room_type": "LAB"
        },
        {
            "name": "R-103",
            "code": "R-103",
            "department_id": 1,
            "room_type": "LECTURE"
        },
        {
            "name": "R-202",
            "code": "R-202",
            "department_id": 1,
            "room_type": "LECTURE"
        }
    ]
}
