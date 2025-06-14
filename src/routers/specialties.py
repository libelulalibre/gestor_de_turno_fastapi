from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.specialty_schemas import SpecialtyCreate, SpecialtyOut
from src.services.specialty_service import get_specialties, create_specialty
from src.config.database import get_db

router = APIRouter(
    prefix="/specialties",
    tags=["Specialties"]
)

@router.get("/", response_model=list[SpecialtyOut])
async def read_specialties(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_specialties(db, skip=skip, limit=limit)

@router.post("/", response_model=SpecialtyOut)
async def create_new_specialty(specialty: SpecialtyCreate, db: Session = Depends(get_db)):
    return create_specialty(db, specialty)