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


#CRUD Operations
# Create (POST)
class UserCreate(BaseModel):
    name: str
    age: int

class UserResponse(BaseModel):
    user_id: int
    name: str
    age: int

users = {}
user_id = 1

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    global user_id
    current_user_id = user_id
    users[current_user_id] = {
        "user_id":user_id,
        "name":user.name,
        "age":user.age
    }
    user_id += 1

    return users[current_user_id]

# Read all users(GET)
@app.get("/users")
def get_users():
    return users

@app.get("/users", response_model=list[UserResponse])
def get_all_users():
    return list(users.values())

#Read one user (GET)
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="user not found")
    
    return users[user_id]

#Update PUT & PATCH

"""
    There are two important HTTP methods for updates:
    PUT → replace the resource
    PATCH → partially modify the resource
"""

class UpdateUser(BaseModel):
    name: str
    age: int

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UpdateUser):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="user not found")

    users[user_id] = {
        "user_id":user_id,
        "name": user.name,
        "age": user.age
    }
    return users[user_id]

@app.patch("/users")
def update_all_users():
    for user in users.values():
        print(user)
        print(users.values())
        user["age"] = 14
    return users

class UpdateUserField(BaseModel):
    name: str| None = None
    age: int| None = None

@app.patch("/users/{user_id}", response_model=UserResponse)
def update_user_field(user_id: int, user: UpdateUserField):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="user id not found")
    update_user = user.model_dump(exclude_unset=True)
    users[user_id].update(update_user)

    return users[user_id]