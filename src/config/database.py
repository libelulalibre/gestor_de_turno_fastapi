from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config.settings import settings

SQLALCHEMY_DATABASE_URL = settings.encoded_db_url

print(">> Tipo de settings.DATABASE_URL:", type(settings.DATABASE_URL))
print(">> Valor de settings.DATABASE_URL:", settings.DATABASE_URL)
print(">> Valor de settings.encoded_db_url:", settings.encoded_db_url)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=20,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False,  # Cambiar a True solo en desarrollo
    connect_args={
        "connect_timeout": 5,
        "keepalives": 1,
        "keepalives_idle": 30,
        "keepalives_interval": 10,
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False  # Mejor para APIs
)

Base = declarative_base()

def get_db():
    """Generador de sesiones con manejo seguro de recursos"""
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
