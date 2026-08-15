import os
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.driver import Driver

password_hash = PasswordHash.recommended()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

security = HTTPBearer() #função para verificar o token

def criar_hash_senha(senha: str):
    return password_hash.hash(senha)


def verificar_senha(senha: str, senha_hash: str):
    return password_hash.verify(senha, senha_hash)

def criar_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta 

    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def verificar_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido ou expirado"
        )


def get_current_driver(
    payload: dict = Depends(verificar_token),
    db: Session = Depends(get_db)
):
    driver_id = payload.get("sub")

    if driver_id is None:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )

    driver = db.query(Driver).filter(
        Driver.id == int(driver_id)
    ).first()

    if driver is None:
        raise HTTPException(
            status_code=401,
            detail="Motorista não encontrado"
        )

    return driver