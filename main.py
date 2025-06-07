from fastapi import FastAPI

# Crea la instancia de FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}