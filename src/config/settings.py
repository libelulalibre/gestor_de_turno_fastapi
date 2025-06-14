from pydantic_settings import BaseSettings, SettingsConfigDict
from urllib.parse import urlparse, quote_plus, urlunparse

class Settings(BaseSettings):
    DATABASE_URL: str  
    
    # Configuración JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @property
    def encoded_db_url(self) -> str:
        """Retorna la DATABASE_URL con la contraseña codificada si es necesario"""
        if "@" not in self.DATABASE_URL:
            return self.DATABASE_URL

        parsed = urlparse(self.DATABASE_URL)
        if parsed.password:
            encoded_password = quote_plus(parsed.password)
            netloc = f"{parsed.username}:{encoded_password}@{parsed.hostname}"
            if parsed.port:
                netloc += f":{parsed.port}"
            return urlunparse((parsed.scheme, netloc, parsed.path, '', '', ''))

        return self.DATABASE_URL

settings = Settings()

