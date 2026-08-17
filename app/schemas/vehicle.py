from pydantic import BaseModel

class VehicleCreate(BaseModel):
    marca: str
    modelo: str
    ano: int
    placa: str
    quilometragem: int

class VehicleUpdate(BaseModel):
    marca: str
    modelo: str
    ano: int
    placa: str
    quilometragem: int
    
class VehicleResponse(BaseModel):
    id: int
    marca: str
    modelo: str
    ano: int
    placa: str
    quilometragem: int
    driver_id: int

class Config:
    from_attributes = True