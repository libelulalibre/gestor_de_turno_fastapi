from pydantic import BaseModel, EmailStr
from enum import Enum

class UserRole(str, Enum):
    patient = "patient"
    admin = "admin"

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    dni: str

class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.patient

class UserOut(UserBase):
    id: int
    is_active: bool
    role: UserRole

    class Config:
        from_attributes = True