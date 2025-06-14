# Gestor de Turnos Médicos - FastAPI
Sistema de gestión de turnos médicos desarrollado con FastAPI, PostgreSQL y SQLAlchemy.
Brinda servicios de gestión de turnos medicos para centros de salud o clinicas polivalentes. Por su estructura, presenta dos roles de usuarios: administradores y pacientes.

# 📋 Requisitos Previos
- Python 3.12 
- PostgreSQL 17
- Git 

# 1. Clonar el repositorio
git clone https://github.com/libelulalibre/gestor_de_turno_fastapi.git
cd gestor_de_turno_fastapi

# 2. crear entorno virtual
python -m venv venv
.\venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
    Crear archivo .env en la raíz del proyecto con:

    DATABASE_URL=postgresql://user:password@localhost:5432/your_database_name
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    
# 5. Configurar base de datos
createdb -U postgres gestor_turnos

# 6.Ejecutar migraciones
alembic upgrade head

# 7. Ejecutar la aplicación
uvicorn main:app --reload

# 8. La aplicación estará disponible en:

API: http://127.0.0.1:8000

Documentación interactiva: http://127.0.0.1:8000/docs

# 9. Endpoints principales

Método	Endpoint	Descripción
POST	/token	Autenticación (JWT)
GET	/users/	Listar usuarios
POST	/appointments/	Crear turno médico
GET	/specialties/	Listar especialidades

# 10. Estructura del Proyecto
gestor_de_turno_fastapi/
├── src/
│   ├── config/          # Configuración y DB
│   ├── models/          # Modelos SQLAlchemy
│   ├── schemas/         # Esquemas Pydantic
│   ├── services/        # Lógica de negocio
│   └── routers/         # Endpoints API
├── alembic/             # Migraciones
├── .env                 # Variables de entorno
└── main.py              # App principal

# 11. Dependencias
Package           Version
----------------- ---------
alembic           1.16.1
annotated-types   0.7.0
anyio             4.9.0
certifi           2025.4.26
cffi              1.17.1
click             8.2.1
colorama          0.4.6
cryptography      45.0.3
dnspython         2.7.0
ecdsa             0.19.1
email_validator   2.2.0
fastapi           0.115.12
greenlet          3.2.3
h11               0.16.0
httpcore          1.0.9
httpx             0.28.1
idna              3.10
iniconfig         2.1.0
Mako              1.3.10
MarkupSafe        3.0.2
packaging         25.0
passlib           1.7.4
pip               24.2
pluggy            1.6.0
psycopg2-binary   2.9.10
pyasn1            0.6.1
pycparser         2.22
pydantic          2.11.5
pydantic_core     2.33.2
pydantic-settings 2.9.1
Pygments          2.19.1
pytest            8.4.0
python-dotenv     1.1.0
python-jose       3.5.0
python-multipart  0.0.20
rsa               4.9.1
six               1.17.0
sniffio           1.3.1
SQLAlchemy        2.0.41
starlette         0.46.2
typing_extensions 4.14.0
typing-inspection 0.4.1
uvicorn           0.34.3