from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    placa = Column(String, unique=True, nullable=False)
    quilometragem = Column(Integer, nullable=False)

    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=False)