#adding in routing for database operations
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
  add_student,
  delete_student,
  retrieve_student,
  retrieve_students,
  update_student,

)
from app.server.models.student import (
  ErrorrResponseModel,
  ResponseModel,
  StudentSchema,
  UpdateStudentModel,
)
router = APIRouter()

#create a handler for POST requests that create a new student
@router.post("/", response_description = "New student added!")
async def add_student_data(student : StudentSchema = Body(...)):
  student = jsonable_encoder(student)
  new_student = await add_student(student)
  return ResponseModel(new_student, "Student added successfully")