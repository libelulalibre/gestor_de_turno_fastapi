from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config.settings import settings
from urllib.parse import quote_plus
import logging
from typing import Generator

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def ensure_proper_encoding(db_url: str) -> str:
    """Asegura que la URL de la DB tenga encoding correcto"""
    try:
        if "@" in db_url:
            protocol_part, rest = db_url.split("://")
            auth_part, host_part = rest.split("@")
            
            if ":" in auth_part:
                username, password = auth_part.split(":", 1)
                password = quote_plus(password.encode('utf-8').decode('utf-8'))
                auth_part = f"{username}:{password}"
            
            return f"{protocol_part}://{auth_part}@{host_part}"
        return db_url
    except Exception as e:
        logger.error(f"Error procesando DB URL: {e}")
        raise ValueError("URL de base de datos inválida") from e

# Asegurar que la URL use psycopg2
DB_URL = ensure_proper_encoding(settings.DATABASE_URL)
if not DB_URL.startswith("postgresql+psycopg2://"):
    DB_URL = DB_URL.replace("postgresql://", "postgresql+psycopg2://")

logger.info(f"DB URL utilizada: {DB_URL[:50]}...")  # Log parcial

engine = create_engine(
    DB_URL,
    pool_size=20,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False,
    connect_args={
        "connect_timeout": 5,
        "keepalives": 1,
        "keepalives_idle": 30,
        "keepalives_interval": 10,
        "application_name": "gestor_turnos",
        "options": "-c client_encoding=utf8"  # Configura encoding aquí
    },
    pool_timeout=30
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False
)

Base = declarative_base()

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Error en sesión de DB: {e}")
        db.rollback()
        raise
    finally:
        db.close()