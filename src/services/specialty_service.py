from sqlalchemy.orm import Session
from src.models.specialty import Specialty
from src.schemas.specialty_schemas import SpecialtyCreate  # Importación añadida
from typing import List

def get_specialties(db: Session, skip: int = 0, limit: int = 100) -> List[Specialty]:
    """Obtiene lista de especialidades médicas"""
    return db.query(Specialty).offset(skip).limit(limit).all()

def create_specialty(db: Session, specialty: SpecialtyCreate) -> Specialty:
    """Crea una nueva especialidad médica"""
    db_specialty = Specialty(**specialty.model_dump())
    db.add(db_specialty)
    db.commit()
    db.refresh(db_specialty)
    return db_specialty