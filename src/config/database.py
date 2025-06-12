from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config.settings import settings

# Usa settings.encoded_db_url si hay caracteres especiales en la contraseña,
# o settings.database_url si no los hay.
engine = create_engine(
    settings.encoded_db_url,  # ¡Corregido! Usa la URL codificada.
    pool_pre_ping=True,      # Maneja reconexiones automáticamente
    echo=True                # Muestra SQL en consola (útil para desarrollo)
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """Generador de sesiones para FastAPI."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()