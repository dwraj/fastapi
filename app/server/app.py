from fastapi import FastAPI

from app.server.routes.student import router as StudentRouter

app = FastAPI()
 
app.include_router(StudentRouter, tags = ["Student"], prefix = "/student")
# now setting our base route 
@app.get("/", tags = ["Root"])
async def read_root():
  return {"Greeting": "Tutorial for FastAPI :)"}