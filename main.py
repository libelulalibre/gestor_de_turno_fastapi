import logging
from fastapi import FastAPI

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    logger.info("Iniciando aplicación...")

# Importar routers
from src.routers import auth, users, specialties, appointments
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(specialties.router)
app.include_router(appointments.router)