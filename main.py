from database import connect_database, get_all_students
connection = connect_database()

if connection:
    print("Connected to MySQL!")
else:
    print("Connection failed!")
    

from student_service import *

while True:
    print("=" * 10 + " STUDENT MANAGEMENT " + "=" * 10)
    print("1. Show all students")
    print("2. Add student")
    print("3. Update score")
    print("4. Delete student")
    print("5. Find student")
    print("6. Top student")
    print("7. Lowest student")
    print("8. Students with courses")
    print("9. Add course")
    print("10. Enroll student in course")
    print("11. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        students = get_all_students()
        show_students(students)
    elif choice == "2":
        add_student()
    elif choice == "3":
        update_score()
    elif choice == "4":
        remove_student()
    elif choice == "5":
        find_student()
    elif choice == "6":
        top_student()
    elif choice == "7":
        lowest_student()
    elif choice == "8":
        rows = get_students_with_courses()
        show_students_with_courses(rows)
    elif choice == "9":
        add_course()
    elif choice == "10":
        enroll_student()
    elif choice == "11":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
