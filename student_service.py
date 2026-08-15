

from database import (
    get_all_courses,
    get_all_students,
    get_lowest_student,
    get_students_with_courses,
    get_top_student,
    insert_course,
    insert_enrollment,
    search_student,
    update_student_score,
    insert_student,
    delete_student
)
from student import *
from utils import *

def show_students(students):
    print("-" * 20)
    if not students:
        print("No students.")
        return
    for student in students:
        student.show_info()
    print("-" * 20)


def add_student():
    print("-" * 20)
    name = input("Enter name: ").strip()
    age = enter_number("Enter age: ")
    score = enter_score("Enter score: ")
    insert_student(name, age, score)
    print("-" * 20)

def update_score():
    print("-" * 20)
    students = search_student(input("Enter student name to update score: ").strip())
    if not students:
        print("No students found.")
    elif len(students) == 1:
        student = students[0]
        student.show_info()
        new_score = enter_score(f"Enter new score for {student.name}: ")
        update_student_score(student.id, new_score)
    else:
        print(f"Found {len(students)} students matching the name:")
        for s in students:
            print(f"ID: {s.id}, Name: {s.name}, Age: {s.age}, Score: {s.score}")
        student_id = enter_number("Enter student ID to update score: ")
        new_score = enter_score("Enter new score: ")
        update_student_score(student_id, new_score)


def remove_student():
    print("-" * 20)
    students = search_student(input("Enter student name to delete: ").strip())
    if not students:
        print("No students found.")
    elif len(students) == 1:
        student = students[0]
        student.show_info()
        confirm = input(f"Are you sure you want to delete {student.name}? (y/n): ").strip().lower()
        if confirm == 'y':
            delete_student(student.id)
        else:
            print("Deletion cancelled.")
    else:
        print(f"Found {len(students)} students matching the name:")
        for s in students:
            print(f"ID: {s.id}, Name: {s.name}, Age: {s.age}, Score: {s.score}")
        student_id = enter_number("Enter student ID to delete: ")
        confirm = input(f"Are you sure you want to delete student with ID {student_id}? (y/n): ").strip().lower()
        if confirm == 'y':
            delete_student(student_id)

def find_student():
    print("-" * 20)
    name = input("Enter student name to search: ").strip()
    students = search_student(name)
    if not students:
        print("No students found.")
    elif len(students) == 1:
        students[0].show_info()
    else:
        print(f"Found {len(students)} students matching '{name}':")
        for s in students:
            print(f"ID: {s.id}, Name: {s.name}, Age: {s.age}, Score: {s.score} \n")
    print("-" * 20)


def top_student():
    print("-" * 20)
    student = get_top_student()
    if not student:
        print("No students.")
        return
    student.show_info()
    print(f"Top student: {student.name}")
    print("-" * 20)


def lowest_student():
    print("-" * 20)
    student = get_lowest_student()
    if not student:
        print("No students.")
        return
    student.show_info()
    print(f"Lowest student: {student.name}")
    print("-" * 20)

def group_students_courses(rows):
    if not rows:
        return {}
    result = {}
    for row in rows:
        sid = row["id"]
        if sid not in result:
            result[sid] = {"name": row["name"], "courses": []}
        if row["course_name"] is not None:
            result[sid]["courses"].append(row["course_name"])
    return result


def show_students_with_courses(rows):
    grouped_students = group_students_courses(rows)
    if not grouped_students:
        print("No students.")
        return
    for student_id, student_info in grouped_students.items():
        print(f"Student ID: {student_id}, Name: {student_info['name']}")
        if student_info["courses"]:
            print("Courses:", ", ".join(student_info["courses"]))
        else:
            print("Courses: None")
        print("-" * 20)

def add_course():
    print("-" * 20)
    course_name = input("Enter course name: ").strip()
    insert_course(course_name)
    print("-" * 20)

def enroll_student():
    print("-" * 20)
    students = get_all_students()
    print("Students:")
    for s in students:
        print(f"ID: {s.id}, Name: {s.name}")

    courses = get_all_courses()
    print("Courses:")
    for c in courses:
        print(f"ID: {c[0]}, Name: {c[1]}")    

    student_id = enter_number("Enter student ID: ")
    course_id = enter_number("Enter course ID: ")
    insert_enrollment(student_id, course_id) 
    print("-" * 20)
    