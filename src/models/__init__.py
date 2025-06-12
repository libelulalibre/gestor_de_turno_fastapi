# src/models/__init__.py
from src.config.database import Base
from .user import User
from .specialty import Specialty
from .appointment import Appointment

__all__ = ["Base", "User", "Specialty", "Appointment"]
