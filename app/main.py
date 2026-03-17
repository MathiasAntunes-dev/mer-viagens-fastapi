from fastapi import FastAPI
from app.database import Base, engine
from app.route.viagem import usuario
from app.route.viagem import passageiro

# Criar todas as entidades no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuario)
app.include_router(passageiro)

@app.get("/")
async def health_check():
    return {"status": "API Online"}