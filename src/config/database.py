from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config.settings import settings
from urllib.parse import quote_plus
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def safe_encode_db_url(db_url: str) -> str:
    """Codifica seguramente la URL de conexión"""
    try:
        if db_url.startswith("postgresql://"):
            db_url = db_url.replace("postgresql://", "postgresql+psycopg2://")
        
        if "@" in db_url:
            protocol, rest = db_url.split("://")
            credentials, host = rest.split("@")
            if ":" in credentials:
                user, password = credentials.split(":", 1)
                password = quote_plus(password.encode('latin1').decode('utf-8', errors='ignore'))
                db_url = f"{protocol}://{user}:{password}@{host}"
        
        return db_url
    except Exception as e:
        logger.error(f"Error procesando DB URL: {e}")
        raise

# URL segura con encoding forzado
DATABASE_URL = safe_encode_db_url(settings.DATABASE_URL)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "connect_timeout": 5,
        "options": "-c client_encoding=utf8"
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
