from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas.appointment_schemas import AppointmentCreate, Appointment
from src.services.appointment_service import create_appointment, get_appointments
from src.config.database import get_db

router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)

@router.post("/", response_model=Appointment)
async def create_new_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    return create_appointment(db=db, appointment=appointment)

@router.get("/", response_model=list[Appointment])
async def read_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_appointments(db=db, skip=skip, limit=limit)