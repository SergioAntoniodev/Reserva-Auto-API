from fastapi import FastAPI
from app.routers import users, auth
from app.database.database import Engine, Base
from app.models.driver import Driver
from app.models.Vehicle import Vehicle

app = FastAPI()

#Criar as tabelas no banco de dados
Base.metadata.create_all(bind=Engine)

app.include_router(users.router)
app.include_router(auth.router)
@app.get("/")
def home():
    return {"mensagem": "API funcionando!"}

#uvicorn app.main:app