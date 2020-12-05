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

@router.get("/", response_description = "all students retrieved")
async def get_students():
  students = await retrieve_students()
  if students:
    return ResponseModel(students, "Student data retrieved")
  return ErrorrResponseModel("An error occured", 404, "Students don't exist")

#handling a get request with an ID as the parameter
@router.get("/{id}", response_description = "Single student retrieved")
async def get_student_data(id):
  student = await retrieve_student(id)
  if student:
    return ResponseModel(student, "student data retrieved")
  return ErrorrResponseModel("An error occured", 404, "Student doesn't exist")

@router.put("/{id}")
async def update_student_data(id: str, req: UpdateStudentModel = Body(...)):
  req = {k: v for k,v in req.dict().items() if v is not None}
  updated_student = await update_student(id, req)
  if updated_student:
    return ResponseModel(
      "Student with ID {} has been updated".format(id),
      "Student name updated succcesfully"
    )
  return ErrorrResponseModel("An error occured", 404, "Error updating student data")

@router.delete("/{id}", response_description = "Student data deleted from the database")
async def delete_student_data(id: str):
  deleted_student = await delete_student(id)
  if deleted_student:
    return ResponseModel( "Student with ID: {} removed".format(id), "Student deleted succesfully")
  else:
    return ErrorrResponseModel("An error occurred", 404, "Student with id {0} doesn't exist".format(id))
