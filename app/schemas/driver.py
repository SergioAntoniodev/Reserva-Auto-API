from pydantic import BaseModel

class DriverCreate(BaseModel):
    nome: str
    email: str