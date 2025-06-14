from sqlalchemy.orm import Session
from src.models.appointment import Appointment
from src.schemas.appointment_schemas import AppointmentCreate

def create_appointment(db: Session, appointment: AppointmentCreate):
    db_appointment = Appointment(**appointment.model_dump())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def get_appointments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Appointment).offset(skip).limit(limit).all()