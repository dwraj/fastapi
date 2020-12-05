#forming the database connection
import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "MONGO URI"
#create a client connection
client  = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
#reference a database called students
database = client.testDB
#reference a collection called student_collection
#these are just references so await isn't neccesary
student_collection = database.get_collection("students_collection")

#helper function to parse results from database query, return as dictionary
#takes in a student object and converts json into dictionary
def student_helper(student) -> dict:
  return{
    "id" : str(student["_id"]),
    "fullname" : student["fullname"],
    "email" : student["email"],
    "major" : student["major"],
    "year" : student["year"],
    "GPA" : student["gpa"],
  }
 #CRUD functions

 #gets all students in the database
async def retrieve_students():
  students = []
  async for student in student_collection.find():
    students.append(student_helper(student))
  return students

  #add new student to database
async def add_student(student_data: dict) -> dict:
  student = await student_collection.insert_one(student_data)
  new_student = await student_collection.find_one({"_id": student.inserted_id})
  return student_helper(new_student)

  #retrieve student with matching ID
async def retrieve_student(id:str) -> dict:
  student = await student_collection.find_one({"_id" : ObjectId(id)})
  if student:
    return student_helper(student)

  #update a student with matching ID
async def update_student(id: str, data: dict):
  if len(data) < 1:
    return False
  student = await student_collection.find_one({"_id" : ObjectId(id)})
  if student:
    updated_student = await student_collection.update_one(
      {"_id" : ObjectId(id)}, {"$set" : data}
    )
    if updated_student:
      return True
    return False

async def delete_student(id: str):
  student = await student_collection.find_one({"_id" : ObjectId(id)})
  if student:
    await student_collection.delete_one({"_id" : ObjectId(id)})
    return True