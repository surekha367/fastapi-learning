from fastapi import FastAPI, HTTPException
import psycopg

app = FastAPI()

DATABASE_URL = "postgresql://postgres:password@localhost:5432/fastapi_learning"

@app.get("/")
def home():
    return {"message":"FastAPI is running successfully"}

@app.get("/users")
def get_users():
    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute("select * from users")
            rows = cursor.fetchall()

    return [{"user_id":row[0],"name":row[1],"email":row[2],"age":row[3]} for row in rows]

@app.get("/users/{user_id}")
def get_user_details(user_id:int):
    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute("select * from users where user_id = %s",(user_id,))
            row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="user_id not found")
    return {"user_id":row[0],"name":row[1],"email":row[2],"age":row[3]}