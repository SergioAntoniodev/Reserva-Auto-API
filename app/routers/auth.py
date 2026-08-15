from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.driver import Driver
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.security import verificar_senha, criar_access_token

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(dados: LoginRequest, db: Session = Depends(get_db)):
    driver = db.query(Driver).filter(Driver.email == dados.email).first()

    if driver is None:
        raise HTTPException(status_code=401, detail="Email ou senha inválidos")

    senha_correta = verificar_senha(dados.senha, driver.senha_hash)

    if not senha_correta:
        raise HTTPException(status_code=401, detail="Email ou senha inválidos")

    access_token = criar_access_token(data={"sub": str(driver.id)})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }