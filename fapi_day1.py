from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello world."}

@app.get("/users")
def users():
    return {"users":["Snoopy","karthik","siva"]}

@app.get("/departments")
def departments():
    return {"departments":("Accounts","Development","Data Engineer")}

@app.get("/health")
def health_check():
    return {"status":"ok"}