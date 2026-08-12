from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from typing import List
from app.database.database import get_db
from app.models.driver import Driver
from app.schemas.driver import DriverCreate, DriverResponse, DriverUpdate
from app.services.security import criar_hash_senha

router = APIRouter()

@router.get("/users", response_model=List[DriverResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    drivers = db.query(Driver).all()
    return drivers

@router.get("/users/{id}", response_model=DriverResponse)
def buscar_usuario(id: int, db: Session = Depends(get_db)):
    driver = db.query(Driver).filter(Driver.id == id).first()
    if driver is None:
        raise HTTPException(
            status_code=404, 
            detail="Motorista não encontrado"
        )
    return driver

@router.put("/users/{driver_id}", response_model=DriverResponse)
def atualizar_usuario(
    driver_id: int,
    driver_update: DriverUpdate,
    db: Session = Depends(get_db)
): 
    driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if driver is None:
        raise HTTPException(
            status_code=404,
            detail="Motorista não encontrado"
        )
    for key, value in driver_update.dict().items():
        setattr(driver, key, value)

        db.commit()
        db.refresh(driver)

    return driver

@router.delete("/users/{driver_id}")
def deletar_usuario(driver_id: int,
                    db: Session = Depends(get_db)):
    driver = db.query(Driver).filter(Driver.id == driver_id).first()

    if driver is None:
        raise HTTPException(
            status_code=404,
            detail="Motorista não encontrado"
        )
    db.delete(driver)
    db.commit()
    return {"mensagem": "Driver deletado com sucesso!"}

@router.post("/users", response_model=DriverResponse)
def criar_driver(driver: DriverCreate, db: Session = Depends(get_db)):
    novo_driver = Driver(
        nome=driver.nome,
        email=driver.email,
        senha_hash=criar_hash_senha(driver.senha)    )

    db.add(novo_driver)

    db.commit()

    db.refresh(novo_driver)
    
    return novo_driver