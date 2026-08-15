import os

import mysql.connector
from dotenv import load_dotenv

from student import Student


load_dotenv()

# Function to execute a query and return the result
def execute_query(sql, params=None, fetch=None):
    connection = connect_database()
    if not connection:
        return None
    cursor = connection.cursor()
    try:
        cursor.execute(sql, params)
        if fetch == "one":
            result = cursor.fetchone()          
        elif fetch == "all":
            result = cursor.fetchall()          
        else:
            connection.commit()   
            result = cursor.rowcount   
        return result
    except mysql.connector.Error as err:
        print(err)
        return None
    finally:
        cursor.close()
        connection.close()

# Function to establish a connection to the database
def connect_database():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )

        return connection

    except mysql.connector.Error as err:
        print(f"Connection failed: {err}")
        return None
    
# Function to create the database if it doesn't exist
def create_database():
    connection = connect_database()

    if not connection:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS student_management")
        print("Database created successfully!")

    except mysql.connector.Error as err:
        print(err)

    finally:
        cursor.close()
        connection.close()

# Function to insert a new student into the database
def insert_student(name, age, score):
    name = name.strip().title()
    result = execute_query(
        "INSERT INTO students (name, age, score) VALUES (%s, %s, %s)",
        (name, age, score),
    )
    if result:
        print("Student added successfully!")
    else:
        print("Failed to add student.")

# Function to delete a student from the database
def delete_student(student_id):
    result = execute_query(
        "DELETE FROM students WHERE id = %s", (student_id,)
    )
    if result:
        print("Student deleted successfully!")
    else:
        print("Failed to delete student.")

# Function to get all students from the database
def get_all_students():
    rows = execute_query("SELECT * FROM students", fetch="all")
    if not rows:
        return []
    students = []
    for row in rows:
        student = Student(row[0], row[1], row[2], row[3])
        students.append(student)
    return students

# Function to update a student's score
def update_student_score(student_id, new_score):
    result = execute_query(
        "UPDATE students SET score = %s WHERE id = %s", (new_score, student_id)
    )
    if result:
        print("Student score updated successfully!")
    else:
        print("Failed to update student score.")

# Function to search for students by name
def search_student(name):
    rows = execute_query(
        "SELECT * FROM students " 
        "WHERE name LIKE %s", (f"%{name}%",), fetch="all"
    )
    if not rows:
        return []
    students = []
    for r in rows:
        student = Student(r[0], r[1], r[2], r[3])
        students.append(student)
    return students

# Function to get the top student based on score
def get_top_student():
    result = execute_query(
        "SELECT * FROM students ORDER BY score DESC LIMIT 1", fetch="one"
    )
    if result:
        return Student(result[0], result[1], result[2], result[3])
    return None

# Function to get the student with the lowest score
def get_lowest_student():
    result = execute_query(
        "SELECT * FROM students ORDER BY score ASC LIMIT 1", fetch="one"
    )
    if result:
        return Student(result[0], result[1], result[2], result[3])
    return None

# Function to insert a new enrollment into the database
def insert_enrollment(student_id, course_id):
    result = execute_query(
        "INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)",
        (student_id, course_id),
    )
    if result:
        print("Enrollment added successfully!")
    else:
        print("Failed to add enrollment.")

# Function to add a new course to the database
def insert_course(course_name):
    result = execute_query(
        "INSERT INTO courses (course_name) VALUES (%s)", (course_name,)
    )
    if result:
        print("Course added successfully!")
    else:
        print("Failed to add course.")

# Function to get all courses
def get_all_courses():
    connection = connect_database()
    if not connection:
        return []
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM courses")
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(err)
        return []
    finally:
        cursor.close()
        connection.close()

# Function to get courses by student ID
def insert_enrollment(student_id, course_id):
    result = execute_query(
        "INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)",
        (student_id, course_id),
    )
    if result:
        print("Enrollment added successfully!")
    else:
        print("Failed to add enrollment.")

# Function to get courses by student ID
def get_courses_by_student(student_id):
    connection = connect_database()
    if not connection:
        return []
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            SELECT c.id, c.course_name
            FROM enrollments e
            JOIN courses c ON e.course_id = c.id
            WHERE e.student_id = %s
            """,
            (student_id,),
        )
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(err)
        return []
    finally:
        cursor.close()
        connection.close()

# Function to get students with their courses
def get_students_with_courses():
    connection = connect_database()
    if not connection:
        return []
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(
            """
            SELECT s.id, s.name, s.age, s.score, c.course_name
            FROM students s
            LEFT JOIN enrollments e ON s.id = e.student_id
            LEFT JOIN courses c ON e.course_id = c.id
            """
        )
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(err)
        return []
    finally:
        cursor.close()
        connection.close()

# Last function to search student by ID
def search_student_id(student_id):
    result = execute_query(
        "SELECT * FROM students WHERE id = %s", (student_id,), fetch="one"
    )
    if result:
        return Student(result[0], result[1], result[2], result[3])
    return None