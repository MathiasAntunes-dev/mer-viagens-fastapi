from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.viagem import UsuarioModel
from app.schema.viagem import UsuarioSchema
from app.model.viagem import PassageiroModel
from app.schema.viagem import PassageiroSchema

usuario = APIRouter()
passageiro = APIRouter()

@usuario.post("/usuario/create", tags=["Usuário"])
async def criar_usuario(dados: UsuarioSchema, db: Session = Depends(get_db)):
    novo_usuario = UsuarioModel(**dados.model_dump())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

@usuario.get("/usuarios/get", tags=["Usuário"])
async def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioModel).all()


@usuario.put("/usuarios/{id}/update", tags=["Usuário"])
async def atualizar_usuario(id: int, dados: UsuarioSchema, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id == id).first()

    if not usuario:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Usuário com ID {id} não encontrado.")

    for campo, valor in dados.model_dump().items():
        setattr(usuario, campo, valor)

    db.commit()
    db.refresh(usuario)

    return usuario


@usuario.delete("/usuarios/{id}/delete", tags=["Usuário"])
async def deletar_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id == id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")

    db.delete(usuario)
    db.commit()

    return {"mensagem": "Usuário deletado com sucesso."}

# --------------------------------------------------------------------------------------------------

@passageiro.post("/passageiro", tags=["Passageiro"])
async def criar_passageiro(dados: PassageiroSchema, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id == dados.id_usuario).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não existe.")

    novo_passageiro = PassageiroModel(**dados.model_dump())
    
    db.add(novo_passageiro)
    db.commit()
    db.refresh(novo_passageiro)

    return novo_passageiro

@passageiro.get("/passageiros", tags=["Passageiro"])
async def listar_passageiros(db: Session = Depends(get_db)):
    passageiros = db.query(PassageiroModel)\
        .join(UsuarioModel, PassageiroModel.id_usuario == UsuarioModel.id)\
        .all()

    return passageiros


@passageiro.put("/passageiro/{id}/update", tags=["Passageiro"])
async def atualizar_passageiro(id: int, dados: PassageiroSchema, db: Session = Depends(get_db)):
    passageiro = db.query(PassageiroModel).filter(PassageiroModel.id == id).first()

    if not passageiro:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Passageiro com ID {id} não encontrado.")

    for campo, valor in dados.model_dump().items():
        setattr(passageiro, campo, valor)

    db.commit()
    db.refresh(passageiro)

    return passageiro


@passageiro.delete("/passageiro/{id}/delete", tags=["Passageiro"])
async def deletar_passageiro(id: int, db: Session = Depends(get_db)):
    passageiro = db.query(PassageiroModel).filter(PassageiroModel.id == id).first()

    if not passageiro:
        raise HTTPException(status_code=404, detail="Passageiro não encontrado.")

    db.delete(passageiro)
    db.commit()

    return {"mensagem": "Passageiro deletado com sucesso."}