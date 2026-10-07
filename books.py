from fastapi import Body,FastAPI

app = FastAPI()

books = [
    {"book_name":"Twelfth fail","author":"Anurag Pathak","category":"biography"},
    {"book_name":"War and Peace","author":"Leo Tolstoy","category":"Historical Fiction"},
    {"book_name":"Atomic Habits","author":"James Clear","category":"Self-Help / Psychology"},
     {"book_name":"MS Dhoni","author":"Bharat Sundaresan","category":"biography"},
]

@app.get("/all-books")
def book_details():
    return books

#order matters with path parameters bcoz if we have similar parameters path one is static and dynamic and first we have dynamic parameters endpoing then it will execute that instead of static and it will never be called so place static parameters related endpoint first and then dynamic parameters endpoint.
@app.get("/books/mybook")
def read_book():
    return {"book_title":"Twelfth fail"}

@app.get("/books/{book_name}")
def get_book_details(book_name: str):
    for book in books:
        print("book_name=", book_name)
        print(book.get(book_name))
        if book.get('book_name').casefold() == book_name.casefold():
            return book

#http://localhost:8000/books/Twelfth%20fail
""" 
    In API url it won't accept empty space so encoding that empty space and using %20
"""

@app.get("/books")
def get_category_books(category:str):
    books_to_return = []
    for book in books:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{author}/")
def get_book_by_path_query_parameter(author:str, category: str):
    books_details = []
    for book in books:
        if book.get('author').casefold() == author.casefold() and book.get('category').casefold()  == category.casefold():
            books_details.append(book)
    return books_details


#GET cannot have a body but POST can have.
@app.post("/books/create_book")
def create_book(new_book=Body()):
    books.append(new_book)
    return new_book