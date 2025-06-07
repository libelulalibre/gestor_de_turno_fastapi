gestor_turno_fastapi/
├── venv/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── src/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   └── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── appointment.py
│   │   ├── specialty.py
│   │   └── schedule.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user_schemas.py
│   │   ├── appointment_schemas.py
│   │   └── specialty_schemas.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   ├── appointments.py
│   │   ├── specialties.py
│   │   └── auth.py
│   └── services/
│       ├── __init__.py
├── tests/
│   ├── __init__.py