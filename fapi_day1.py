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

#dynamic path parameters
@app.get("/products/{product_id}")
def get_product(product_id : int):
    return {"product id is": product_id}

@app.get("/products")
def get_products():
    return {"products": ["laptop","phone",23,67]}

@app.delete("/orders/{order_id}")
def delete_order(order_id:int):
    return {"order id is":order_id}

# Query parameters
"""
    query parameters, which are used for things like filtering, searching, sorting, and pagination
"""
# /products/25   ("path parameter -> 25 is part of path.it identifies a particular resource.")
# /products?category=laptop    ->  ("query parameter")
# everything after '?' is query string.   category=laptop   is a query parameter.

@app.get("/items")
def get_items(category:str | None = None):
    return {"category": category}

"""
    category : str | None = None
    category -> parameter 
    str | None -> it can be string or none
    = None  -> if user doesn't provide category then it will be null

    when we request only GET /items the category will be null
    else when we request GET /items?category=laptop then category will have laptop as a value.
"""

#multiple query parameters
@app.get("/order")
def get_order(category:str|None = None, 
              price:float|None = None,
              brand:str|None = None):
    return {"category":category,"price":price,"brand":brand}

"""
    GET /products?category=laptop&brand=dell
    ? and &  ->  The first query parameter starts after "?"  and then remaining query parameters are separated with "&"
    = → separates name and value
"""


#Query parameter type validation
"""
    FastAPI can validate query parameters based on Python type annotations.
    suppose price type is float i gave string value. /order?price=abc  fastapi cannot convert str to float so it return a validation error 422 unprocessable entity ( 127.0.0.1:64715 - "GET /order?category=laptop&brand=HP&price=abc HTTP/1.1" 422 Unprocessable Entity)
"""

#Required vs Optional parameters
# Required parameters
@app.get("/order")
def get_orders(category:str):
    return {"category":category}
# there is no default value so category need to be required value. if not provide then it will give validation error.

#optional parameters
@app.get("/order")
def get_item(category:str | None = None):
    return {"category":category}

"""
    if we didn't provide any value then it will consider as None it wont provide any validation error.we can provide default value as well like category:str = "laptop"
"""

# Pagination related query parameters  GET /products?page=2&limit=50 it means page no is 2 and limit per page is 50