from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.Vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate, VehicleUpdate, VehicleResponse

from app.models.driver import Driver
from app.services.security import get_current_driver 


router = APIRouter(
    prefix="/vehicles",
    tags=["vehicles"]
)

@router.post("/", response_model=VehicleResponse)
def create_vehicle(
    vehicle: VehicleCreate,
    db: Session = Depends(get_db),
    current_driver: Driver = Depends(get_current_driver)
):
    new_vehicle = Vehicle(
        marca=vehicle.marca,
        modelo=vehicle.modelo,
        ano=vehicle.ano,
        placa=vehicle.placa,
        quilometragem=vehicle.quilometragem,
        driver_id=current_driver.id #API pega o motorista pelo token
    )

    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)

    return new_vehicle

@router.get("/", response_model=list[VehicleResponse])
def listar_veiculos(
    db: Session = Depends(get_db),
    current_driver: Driver = Depends(get_current_driver)
):
    vehicles = db.query(Vehicle).filter(
        Vehicle.driver_id == current_driver.id
    ).all()

    return vehicles

@router.put("/{vehicle_id}", response_model=VehicleResponse)
def atualizar_veiculo(
    vehicle_id: int,
    vehicle_update: VehicleUpdate,
    db: Session = Depends(get_db),
    current_driver: Driver = Depends(get_current_driver)
):
    vehicle = db.query(Vehicle).filter(
        Vehicle.id == vehicle_id,
        Vehicle.driver_id == current_driver.id
    ).first()

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Veículo não encontrado"
        )

    vehicle.marca = vehicle_update.marca
    vehicle.modelo = vehicle_update.modelo
    vehicle.ano = vehicle_update.ano
    vehicle.placa = vehicle_update.placa
    vehicle.quilometragem = vehicle_update.quilometragem

    db.commit()
    db.refresh(vehicle)

    return vehicle

@router.delete("/{vehicle_id}")
def deletar_veiculo(
    vehicle_id: int,
    db: Session = Depends(get_db),
    current_driver: Driver = Depends(get_current_driver)
):
    vehicle = db.query(Vehicle).filter(
        Vehicle.id == vehicle_id,
        Vehicle.driver_id == current_driver.id
    ).first()

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Veículo não encontrado"
        )

    db.delete(vehicle)
    db.commit()

    return {"mensagem": "Veículo deletado com sucesso!"}