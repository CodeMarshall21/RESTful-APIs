from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Root endpoint
@app.get("/")
def welcome():
    return {"message": "Welcome to the FastAPI App!"}

@app.get("/user")
def user_profile():
    return {
        "name": "John Doe",
        "age": 30,
        "occupation": "Software Developer"
    }

@app.get("/user/{user_id}")
def user_profile(user_id:int):
    if user_id == 1:
        return {
            "name": "ROOT User",
            "age": 999,
            "occupation": "ALPHA BEING"
        }
    else:
        return {
            "name": f"User {user_id}",
            "age": 25 + user_id,
            "occupation": "NPC"
        }

class User(BaseModel):
    name: str
    age: int
    occupation: str

users = []
        
@app.post("/user")
def create_user(user: User):
    users.append(user.dict())
    count = len(users)
    
    return{
        "message": "User Created",
        "total_users": count
    }