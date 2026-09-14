# What is FastAPI ?
"""
    
"""
first install fastapi and uvicorn.
pip install fastapi uvicorn

for running FastAPI application run this command.
uvicorn main:app --reload
main -> main.py
app -> app = FastAPI() (object creation for FastAPI class)
: -> look inside that file
--reload  -> reload application when changes are made.

flow of a request process:
browser -> url path -> Uvicorn(ASGI) -> fastapi -> checks registered route with same http method and path if exists -> execute that func -> provides that response (python format /json structure format) -> uvicorn -> browser but here one point i didn't get where i am mentioning the http method ?
ex: http://127.0.0.1:8000/users

we don't type GET But the browser interprets navigating to a URL as a request, and for normal page navigation it sends:(GET /users)

when we type this http://127.0.0.1:8000/users  the browser consider it as
GET /users HTTP/1.1
Host: 127.0.0.1:8000

You didn't manually specify GET; the browser selected it because you're navigating to a resource.

Then how do we send POST?

This is where tools such as:

FastAPI /docs
Postman
curl
Python requests
frontend JavaScript