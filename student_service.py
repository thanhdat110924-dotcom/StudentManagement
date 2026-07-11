

from database import (
    get_lowest_student,
    get_top_student,
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

def update_score():
    print("-" * 20)

    name = input("Enter name: ").strip()
    new_score = enter_number("Enter new score: ")

    update_student_score(name, new_score)

    print("-" * 20)

def add_student():
    print("-" * 20)

    name = input("Enter name: ").strip().title()
    age = enter_number("Enter age: ")
    score = enter_number("Enter score: ")

    insert_student(name, age, score)

    print("-" * 20)


def remove_student():
    print("-" * 20)
    name = input("Enter student name to delete: ").strip()
    delete_student(name)
    print("-" * 20)

def find_student():
    print("-" * 20)
    name = input("Enter student name: ").strip()
    student = search_student(name)
    if student:
        student.show_info()
    else:
        print("Student not found")
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

