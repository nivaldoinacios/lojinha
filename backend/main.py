from fastapi import FastAPI
import database
import crud

app = FastAPI()
client = database.Engine()


@app.get("/")
async def root():
    return client.info()


# User
# Criar usuario
@app.post("/api/v1/users")
async def register_user(cpf):
    return crud.create_user(cpf)


# Buscar usuario especifico
@app.get("/api/v1/users/{user_id}")
async def fetch_user(user_id):
    return crud.get_user(user_id)


# Listar todos os usuarios
@app.get("/api/v1/users")
async def fetch_all_users():
    return crud.get_all_users()


# Product
# Buscar produto especifico
@app.get("/api/v1/products/{product_id}")
async def fetch_product(product_id: int):
    return crud.get_product(product_id)


# Listar todos os produtos
@app.get("/api/v1/products")
async def fetch_products():
    return crud.get_products()
