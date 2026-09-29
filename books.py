from fastapi import FastAPI

app = FastAPI()

books = [
    {"book_name":"Twelfth fail","author":"Anurag Pathak","category":"biography"},
    {"book_name":"War and Peace","author":"Leo Tolstoy","category":"Historical Fiction"},
    {"book_name":"Atomic Habits","author":"James Clear","category":"Self-Help / Psychology"},
]
@app.get("/books")
def book_details():
    return books