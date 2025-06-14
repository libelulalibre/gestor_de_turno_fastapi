from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    date: datetime
    notes: str | None = None

class Appointment(AppointmentCreate):
    id: int
    created_at: datetime
    updated_at: datetime