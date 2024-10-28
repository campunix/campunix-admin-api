import xml.etree.ElementTree as ET
from typing import Dict, Any


def parse_syllabus(xml_root: ET.Element) -> Dict[str, Any]:
    departmentID = int(xml_root.find("DepartmentID").text)
    departmentCode = xml_root.find("DepartmentCode").text
    departmentName = xml_root.find("DepartmentName").text
    semester = int(xml_root.find("Semester").text)

    courses = [parse_course(course) for course in xml_root.findall(".//Course")]

    return {
        "departmentID": departmentID,
        "departmentCode": departmentCode,
        "departmentName": departmentName,
        "semester": semester,
        "courses": courses
    }


def parse_course(course_element: ET.Element) -> Dict[str, Any]:
    course_code = course_element.find("CourseCode").text
    title = course_element.find("Title").text
    credit = float(course_element.find("Credit").text)
    prerequisite = course_element.find("Prerequisite").text
    course_type = course_element.find("Type").text
    contact_hours = int(course_element.find("ContactHours").text)

    objectives = [obj.text for obj in course_element.findall(".//Objective")]
    outcomes = [out.text for out in course_element.findall(".//Outcome")]

    books = [
        {
            "title": book.find("Title").text,
            "author": book.find("Author").text,
            "publisher": book.find("Publisher").text,
            "year": int(book.find("Year").text),
        }
        for book in course_element.findall(".//Book")
    ]

    modules = [
        {
            "module": module.text,
            "content": module.find("Content").text if module.find("Content") else "N/A"
        }
        for module in course_element.findall(".//Module")
    ]

    return {
        "course_code": course_code,
        "title": title,
        "credit": credit,
        "prerequisite": prerequisite,
        "type": course_type,
        "contact_hours": contact_hours,
        "objectives": objectives,
        "outcomes": outcomes,
        "books": books,
        "modules": modules,
    }
