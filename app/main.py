from fastapi import FastAPI
from app.routers import users

from app.database.database import Engine, Base
from app.models.driver import Driver

app = FastAPI()

#Criar as tabelas no banco de dados
Base.metadata.create_all(bind=Engine)

app.include_router(users.router)

@app.get("/")
def home():
    return {"mensagem": "API funcionando!"}