from student_service import *
students = [
    Student("steve", 26, 10),
    Student("jack", 21, 70),
    Student("Olivia", 22, 80),
    Student("Sophia", 24, 30),
]
# Bảng menu
while True:
    print("=" * 10 + " STUDENT MANAGEMENT " + "=" * 10)
    print("1. Show all students")
    print("2. Add student")
    print("3. Update score")
    print("4. Delete student")
    print("5. Find student")
    print("6. Top student")
    print("7. Lowest student")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        show_students(students)
    elif choice == "2":
        add_student(students)
    elif choice == "3":
        update_score(students)
    elif choice == "4":
        delete_student(students)
    elif choice == "5":
        find_student(students)
    elif choice == "6":
        top_student(students)
    elif choice == "7":
        lowest_student(students)
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
