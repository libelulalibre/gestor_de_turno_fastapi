from datetime import datetime, timedelta
from jose import jwt
from sqlalchemy.orm import Session
from src.config.settings import settings
from passlib.context import CryptContext
from src.models.user import User
from typing import Optional
import logging
import binascii

logger = logging.getLogger(__name__)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- Funciones de seguridad ---
def safe_decode(value: str) -> str:
    """Maneja strings con encoding problemático"""
    try:
        return value.encode('utf-8').decode('utf-8')
    except UnicodeError:
        try:
            return value.encode('latin1').decode('utf-8')
        except Exception:
            logger.error("Error grave de codificación en los datos")
            raise ValueError("Credenciales con formato inválido")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Versión robusta de verificación de contraseña"""
    try:
        plain_password = safe_decode(plain_password)
        if not hashed_password.startswith("$2b$"):
            logger.error("Formato de hash inválido")
            return False
        return pwd_context.verify(plain_password, hashed_password)
    except (ValueError, binascii.Error, UnicodeError) as e:
        logger.warning(f"Error verificando contraseña: {e}")
        return False

def get_password_hash(password: str) -> str:
    """Genera hash seguro de la contraseña"""
    password = safe_decode(password)
    return pwd_context.hash(password)

# --- Funciones de autenticación ---
def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    """Autenticación con manejo completo de errores"""
    try:
        username = safe_decode(username)
        password = safe_decode(password)

        user = db.query(User).filter(
            (User.email == username) | (User.dni == username)
        ).first()

        if not user or not verify_password(password, user.hashed_password):
            return None

        if not user.is_active:
            raise ValueError("Usuario inactivo")

        return user

    except Exception as e:
        logger.error(f"Error en autenticación: {e}", exc_info=True)
        return None

# --- Funciones de Token JWT ---
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Crea un token JWT seguro"""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    ))
    to_encode.update({"exp": expire})
    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

def create_user_token(user: User) -> dict:
    """Genera el payload estándar para tokens de usuario"""
    return {
        "sub": str(user.id),
        "email": user.email,
        "full_name": user.full_name,
        "role": user.role.value,
        "dni": user.dni
    }