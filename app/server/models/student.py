#optional type allows for data to be None or specified data
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
#in this file we define the schema, representing how our data is stored in MongoDB
#Pydantic's schema's are used for validating data, serializing data (Json -> Python), and deserializing data (Python -> Json)

class StudentSchema(BaseModel):
  #Ellipsis means a field is required
  fullname: str = Field(...)
  email : EmailStr = Field(...)
  major : str = Field(...)
  #gt sets rule that data must be greater than 0, lt sets rule that data must be less than 9 
  year : int = Field(..., gt = 0 , lt = 9)
  #le sets rule that data must be less than or equal to 4.0
  gpa : float = Field(..., le = 4.0)

  class Config:
    schema_extra = {
      "example": {
        "fullname" : "Tom White", 
        "email" : "Tom21White@gmail.com",
        "major" : "Visual Art",
        "year" : 4,
        "gpa" : 2.7,
      }

    }
class UpdateStudentModel(BaseModel):
  fullname : Optional[str]
  email : Optional[EmailStr]
  major  : Optional[str]
  gpa : Optional[float]

  class Config:
    schema_extra = {
      "example": {
        "fullname" : "Tom White", 
        "email" : "Tom21White@gmail.com",
        "major" : "Visual Art",
        "year" : 5,
        "gpa" : 3.2,
      }

    }
def ResponseModel(data, message):
  return{
    "data" : [data],
    "code" : 200,
    "message" : message
  }
def ErrorrResponseModel(error,code, message):
  return {"error" : error, "code": code, "message" : message}

