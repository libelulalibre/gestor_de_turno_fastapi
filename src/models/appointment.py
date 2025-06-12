from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.config.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    patient_id = Column(Integer, ForeignKey("users.id"))
    specialty_id = Column(Integer, ForeignKey("specialties.id"))
