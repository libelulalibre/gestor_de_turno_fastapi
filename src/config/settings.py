from pydantic_settings import BaseSettings, SettingsConfigDict
from urllib.parse import quote_plus

class Settings(BaseSettings):
    # Configuración de la DB (requerida)
    database_url: str
    
    # Configuración de autenticación JWT
    secret_key: str
    algorithm: str = "HS256"  # Valor por defecto
    access_token_expire_minutes: int = 30  # Valor por defecto (minutos)
    
    # Configuración avanzada de Pydantic
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"  # Ignora variables no declaradas
    )
    
    @property
    def encoded_db_url(self) -> str:
        """Codifica la URL de la BD para uso en conexiones SQLAlchemy."""
        return quote_plus(self.database_url)

# Instancia singleton de configuración
settings = Settings()