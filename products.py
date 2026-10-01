from fastapi import FastAPI
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