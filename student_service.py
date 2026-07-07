from student import *
from utils import *
def show_students(students):
    print("-" * 20)
    if not students:
        print("No students found.")
        return
    total_score = 0
    for index, student in enumerate(students, start=1):
        print(f"Student {index}")
        student.show_info()
        student.is_pass()
        total_score += student.score
    average = total_score / len(students)
    print(f"Average score: {average:.2f}")
    print(f"Total students: {len(students)}")
    print("-" * 20)

def add_student(students):
    print("-" * 20)
    name = input("Enter name: ").strip().title()
    age = enter_number("Enter age: ")
    score = enter_number("Enter score: ")
    students.append(Student(name, age, score))
    print("Student added successfully!")
    print("-" * 20)

def update_score(students):
    print("-" * 20)
    name = input("Enter name: ").strip().lower()
    found = False
    for student in students:
        if student.name.lower() == name:
            new_score = enter_number("Enter new score: ")
            student.update_score(new_score)
            print("Score updated successfully!")
            found = True
            break
    if not found:
        print("Student not found")
    print("-" * 20)

def delete_student(students):
    print("-" * 20)
    name = input("Enter student name: ").strip().lower()
    found = False
    for student in students:
        if student.name.lower() == name:
            students.remove(student)
            print("Student removed successfully!")
            found = True
            break
    if not found:
        print("Student not found")
    print("-" * 20)

def find_student(students):
    print("-" * 20)
    name = input("Enter student name: ").strip().lower()
    found = False
    for student in students:
        if student.name.lower() == name:
            student.show_info()
            found = True
            break
    if not found:
        print("Student not found")
    print("-" * 20)

def top_student(students):
    print("-" * 20)
    if not students:
        print("No students.")
        return
    top_student = max(students, key=lambda student: student.score)
    top_student.show_info()
    print(f"Top student: {top_student.name}")
    print("-" * 20)

def lowest_student(students):
    print("-" * 20)
    if not students:
        print("No students.")
        return
    lowest_student = min(students, key=lambda student: student.score)
    lowest_student.show_info()
    print(f"Top student: {lowest_student.name}")
    print("-" * 20)

