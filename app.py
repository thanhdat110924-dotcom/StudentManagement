from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from database import get_all_students, insert_student, update_student_score, delete_student, search_student_id

app = FastAPI()

class StudentOut(BaseModel):
    id: int
    name: str
    age: int
    score: float

    class Config:
        from_attributes = True

class StudentCreate(BaseModel):
    name: str
    age: int
    score: float
    

@app.get("/students", response_model=List[StudentOut])
def read_students():
    students = get_all_students()
    return students

@app.post("/students")
def create_student(student: StudentCreate):
    insert_student(student.name, student.age, student.score)
    return {"message": "Student added successfully"}

@app.put("/students/{student_id}")
def update_student(student_id: int, new_score: float):
    if new_score < 0 or new_score > 100:
        return {"error": "Score must be between 0 and 100"}
    student = search_student_id(student_id)  
    if not student:
        return {"error": "Student not found"}
    update_student_score(student_id, new_score)
    return {"message": "Student score updated successfully"}

@app.delete("/students/{student_id}")
def remove_student(student_id: int):
    result = delete_student(student_id)
    if result:
        return {"message": "Student deleted successfully"}
    else:
        return {"error": "Failed to delete student"}
    