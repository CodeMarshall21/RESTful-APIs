from fastapi import FastAPI

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