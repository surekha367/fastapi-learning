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


"""
    Path parameter, Query parameter, Request body
    Path parameter → identifies something in the URL
    Query parameter → provides filtering/options in the URL
    Request body → sends structured data inside the HTTP request itself
    Why do we need a request body?
    Imagine we want to create a new product.
    The product has:name,price, category, description, quantity
    We could technically put everything into the URL:
    /products?name=Dell&price=55000&category=laptop&quantity=5
    But that's not a good design for a large amount of structured data.
    Instead, we normally send:
    POST /products
    with a body such as:
    {
        "name":"Dell",
        "price":55000,
        "category":"laptop",
        "quantity":5
    }

    An HTTP request can contain several parts.
    ex: POST /products HTTP/1.1
        HOST example.com
        Content-Type: application/json

        {
            "name":"Dell",
            "price":55000
        }

        POST /products HTTP/1.1
        this tells server -> method = POST, path = /products

        Headers -> Content-Type: application/json  this tells server The body contains JSON data.

        Body ->  {"name": "Dell Laptop",
                  "price": 55000
                 }
        JSON is a data format commonly used for APIs.This represents an object containing key-value pairs.JSON is not Python. but it looks like python dictionary.

        How does FastAPI receive this JSON?
        This is where Pydantic becomes important.we create models 
"""

from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    category:str
#this model describes how a product should look like.it says a product must have values like name,price and category and these values should have these types.
"""
    FastAPI uses Pydantic extensively for data validation and serialization.
"""

@app.post("/products")
def create_products(product:Product): #this tells fastapi Read the request body and validate it according to the Product model.
    return {"name":product.name, 
            "price":product.price,
            "category":product.category}
#product is a pydantic model instance.

# path,query parameter and request body
class productUpdate(BaseModel):
    price:float
    category:str

@app.patch("/product/{product_id}")
def update_product(product_id:int,
                   notify:bool = False,
                   product:productUpdate = None):
    return {"product id":product_id, "notification of products":notify, "price":product.price,"category":product.category}

#Response Model ->is about What our API returns to the client.
class ProductResponse(BaseModel):
    id:int
    category:str
    price:float

@app.get("/prod/{product_id}",response_model=ProductResponse)
def get_prods(product_id:int):
    return {"id":product_id,
            "category":"Laptop",
            "price":45000.245,
            "reviews_rating":4.2}