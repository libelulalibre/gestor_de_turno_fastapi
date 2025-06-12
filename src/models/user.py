from enum import Enum
from sqlalchemy import Column, Integer, String, Boolean, Enum as SQLEnum
from src.config.database import Base

class UserRole(str, Enum):
    PATIENT = "patient"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    dni = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    role = Column(SQLEnum(UserRole), default=UserRole.PATIENT)

# src/models/user.py


