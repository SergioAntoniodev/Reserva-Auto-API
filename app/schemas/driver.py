from pydantic import BaseModel, ConfigDict

class DriverCreate(BaseModel):
    nome: str
    email: str
    senha: str

class DriverUpdate(BaseModel):
    nome: str
    email: str
    senha: str

class DriverResponse(BaseModel):
    id: int
    nome: str
    email: str

    model_config = ConfigDict(from_attributes=True)