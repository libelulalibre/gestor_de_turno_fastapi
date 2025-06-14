from pydantic import BaseModel, EmailStr, Field, validator
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    PATIENT = "patient"
    ADMIN = "admin"
    DOCTOR = "doctor"  # Rol adicional para médicos

class UserBase(BaseModel):
    email: EmailStr = Field(..., example="usuario@clinica.com")
    full_name: str = Field(..., min_length=3, example="Juan Pérez")
    dni: str = Field(..., min_length=8, max_length=20, example="12345678")

    @validator('dni')
    def validate_dni(cls, v):
        if not v.isdigit():
            raise ValueError("El DNI debe contener solo números")
        return v

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, example="secret123")
    role: UserRole = Field(default=UserRole.PATIENT)

class UserOut(UserBase):
    id: int
    is_active: bool
    role: UserRole
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "email": "usuario@clinica.com",
                "full_name": "Juan Pérez",
                "dni": "12345678",
                "is_active": True,
                "role": "patient"
            }
        }

class Token(BaseModel):
    access_token: str
    token_type: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1Ni...",
                "token_type": "bearer"
            }
        }

class TokenData(BaseModel):
    username: Optional[str] = None  # Ahora es opcional para compatibilidad
    user_id: Optional[int] = None  # Campo adicional útil para autenticación