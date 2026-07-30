from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 

from app.database.database import get_db
from app.models.driver import Driver
from app.schemas.driver import DriverCreate

router = APIRouter()

@router.get("/users")
def listar_usuarios():
    return {"usuarios": [] }

@router.post("/users")
def criar_driver(driver: DriverCreate, db: Session = Depends(get_db)):
    novo_driver = Driver(
        nome=driver.nome,
        email=driver.email
    )

    db.add(novo_driver)

    db.commit()

    db.refresh(novo_driver)
    
    return {"mensagem": "Driver criado com sucesso!", "dados": driver}