from pydantic_settings import BaseSettings
import urllib.parse

class Settings(BaseSettings):
    # Campos obligatorios (deben estar en .env o ser proporcionados)
    database_url: str  # ¡Nuevo campo añadido!
    secret_key: str
    algorithm: str = "HS256"  # Valor por defecto
    access_token_expire_minutes: int = 30  # Valor por defecto

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"  # Para soportar caracteres especiales

    @property
    def encoded_db_url(self) -> str:
        """Codifica la URL de la base de datos para uso en conexiones."""
        return urllib.parse.quote_plus(self.database_url)  # ¡Usa self.database_url!

# Instancia única de configuración
settings = Settings()