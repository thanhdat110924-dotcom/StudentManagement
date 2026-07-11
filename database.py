import os

import mysql.connector
from dotenv import load_dotenv

from student import Student


load_dotenv()

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

def insert_student(name, age, score):
    connection = connect_database()
    if not connection:
        return
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO students (name, age, score) VALUES (%s, %s, %s)",
            (name, age, score),
        )
        connection.commit()
        print("Student added successfully!")
    except mysql.connector.Error as err:
        print(err)
    finally:
        cursor.close()
        connection.close()

def delete_student(name):
    connection = connect_database()
    if not connection:
        return
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM students WHERE name = %s", (name,))
        connection.commit()
        if cursor.rowcount > 0:
            print("Student removed successfully!")
        else:
            print("Student not found.")
    except mysql.connector.Error as err:
        print(err)
    finally:
        cursor.close()
        connection.close()

def get_all_students():
    connection = connect_database()
    if not connection:
        return []

    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        students = []

        for row in rows:
            student = Student(row[1], row[2], row[3])
            students.append(student)

        return students

    except mysql.connector.Error as err:
        print(err)
        return []

    finally:
        cursor.close()
        connection.close()

def update_student_score(name, new_score):
    connection = connect_database()
    if not connection:
        return
    cursor = connection.cursor()
    try:
        cursor.execute(
            "UPDATE students SET score = %s WHERE name = %s", (new_score, name)
        )
        connection.commit()

        if cursor.rowcount > 0:
            print("Score updated successfully!")
        else:
            print("Student not found.")
    except mysql.connector.Error as err:
            print(err)
    finally:
        cursor.close()
        connection.close()


def search_student(name):
    connection = connect_database()
    if not connection:
        return None
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM students WHERE name = %s", (name,))
        row = cursor.fetchone()

        if row:
            return Student(row[1], row[2], row[3])
        else:
            return None

    except mysql.connector.Error as err:
        print(err)
        return None

    finally:
        cursor.close()
        connection.close()

def get_top_student():
    connection = connect_database()
    if not connection:
        return None
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM students ORDER BY score DESC LIMIT 1")
        row = cursor.fetchone()

        if row:
            return Student(row[1], row[2], row[3])
        else:
            return None

    except mysql.connector.Error as err:
        print(err)
        return None

    finally:
        cursor.close()
        connection.close()

def get_lowest_student():
    connection = connect_database()
    if not connection:
        return None
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM students ORDER BY score ASC LIMIT 1")
        row = cursor.fetchone()

        if row:
            return Student(row[1], row[2], row[3])
        else:
            return None

    except mysql.connector.Error as err:
        print(err)
        return None

    finally:
        cursor.close()
        connection.close()