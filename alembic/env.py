import os
import sys
import io
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from src.config.database import Base
from src.config.settings import settings

# Configuración de encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Path configuration
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

config = context.config

# Configuración de logging con manejo de encoding
if config.config_file_name is not None:
    try:
        with open(config.config_file_name, 'r', encoding='utf-8') as f:
            fileConfig(f)
    except UnicodeDecodeError:
        with open(config.config_file_name, 'r', encoding='latin-1') as f:
            fileConfig(f)

target_metadata = Base.metadata

def run_migrations_online():
    # Usa settings.database_url (en minúsculas) y evita la codificación manual innecesaria
    connectable = engine_from_config(
        {"sqlalchemy.url": settings.database_url},  # ¡Corregido aquí!
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            render_as_batch=True,
        )
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()