from sqlalchemy import Column, Integer, String, Time, Date
from src.config.database import Base

class Specialty(Base):
    __tablename__ = "specialties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)

