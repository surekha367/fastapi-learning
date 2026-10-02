from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ProductCreate(BaseModel):
    name: str
    price: float

class productResponse(BaseModel):
    id: int
    name: str
    price: float

@app.post("/products",response_model=productResponse)
def create_product(product: ProductCreate):
    return {"id":111,"name":product.name,"price":product.price}


"""
    1. HTTP request arrives
       ↓
    2. Route matching
        ↓
    3. FastAPI sees POST /products
        ↓
    4. Request body is read
        ↓
    5. Pydantic validates ProductCreate
        ↓
    6. create_product(product) executes
        ↓
    7. Function returns Python dictionary
        ↓
    8. Response model is applied
        ↓
    9. FastAPI creates HTTP response
        ↓
    10. Client receives JSON
"""

# HTTP Exception
@app.get("/products/{product_id}")
def get_products(product_id: int):
    if product_id == 923:   #if we use db then we dont need to hardcode the id value
        raise HTTPException(status_code=404,detail="product not found")

    return product_id

# raise is used to stop processing this request and send an HTTP error response

# in-memory product api

products = {
    1:{
        "id": 1,
        "name": "AC",
        "price": 35000
    },
    2:{
        "id":2,
        "name": "mobile",
        "price": 56000
    }
}

@app.get("/product/{product_id}")
def get_product(product_id: int):
    if product_id not in products:
        raise HTTPException(status_code=404,detail="products not found")

    return products[product_id]

class UserCreate(BaseModel):
    name: str
    age: int

users = {}
user_id = 1
@app.post("/users")
def create_user(user: UserCreate):
    global user_id

    users[user_id] = {
        "user_id":user_id,
        "name":user.name,
        "age":user.age
    }
    user_id += 1

    return users[user_id-1]
