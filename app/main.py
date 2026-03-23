from fastapi import FastAPI
from app.database import Base, engine
from app.route.viagem import usuario, passageiro, motorista, motorista_veiculo, veiculo, modelo_veiculo, combustivel, classe, servico, corrida, avaliacao, pagamento, metodo_pagamento

# Criar todas as entidades no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuario, tags = ["Usuários"])
app.include_router(passageiro, tags = ["Passageiros"])
app.include_router(motorista, tags = ["Motoristas"])
app.include_router(motorista_veiculo, tags = ["Motorista-Veículo"])
app.include_router(veiculo, tags = ["Veículos"])
app.include_router(modelo_veiculo, tags = ["Modelo-Veículo"])
app.include_router(combustivel, tags = ["Combustíveis"])
app.include_router(classe, tags = ["Classes"])
app.include_router(servico, tags = ["Serviços"])
app.include_router(corrida, tags = ["Corridas"])
app.include_router(avaliacao, tags = ["Avaliações"])
app.include_router(pagamento, tags = ["Pagamentos"])
app.include_router(metodo_pagamento, tags = ["Metodo-Pagamento"])

@app.get("/")
async def health_check():
    return {"status": "API Online"}