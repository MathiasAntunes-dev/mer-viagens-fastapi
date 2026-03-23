from fastapi import FastAPI
from app.database import Base, engine
from app.route.viagem import usuario, passageiro, motorista, motorista_veiculo, veiculo, modelo_veiculo, combustivel, classe

# Criar todas as entidades no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuario, tags = ["Usuários"])
app.include_router(passageiro, tags = ["Passageiros"])
app.include_router(motorista, tags = ["Motoristas"])
app.include_router(motorista_veiculo, tags = ["Motorista-Veículo"])
app.include_router(veiculo, tags = ["Veículos"])
app.include_router(modelo_veiculo, tags = ["Modelo_Veículo"])
app.include_router(combustivel, tags = ["Combustíveis"])
app.include_router(classe, tags = ["Classes"])

@app.get("/")
async def health_check():
    return {"status": "API Online"}