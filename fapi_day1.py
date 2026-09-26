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