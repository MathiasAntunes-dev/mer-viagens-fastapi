from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.viagem import UsuarioModel, PassageiroModel, MotoristaModel, MotoristaVeiculoModel, VeiculoModel, ModeloVeiculoModel, CombustivelModel, ClasseModel, ServicoModel, CorridaModel, AvaliacaoModel, PagamentoModel, MetodoPagamentoModel
from app.schema.viagem import UsuarioSchema, UsuarioUpdateSchema, PassageiroSchema, PassageiroUpdateSchema, MotoristaSchema, MotoristaUpdateSchema, MotoristaVeiculoUpdateSchema, MotoristaVeiculoSchema, VeiculoSchema, VeiculoUpdateSchema, ModeloVeiculoSchema, ModeloVeiculoUpdateSchema, CombustivelSchema, CombustivelUpdateSchema, ClasseSchema, ClasseUpdateSchema, ServicoSchema, ServicoUpdateSchema, CorridaSchema, CorridaUpdateSchema, AvaliacaoSchema, AvaliacaoUpdateSchema, PagamentoSchema, PagamentoUpdateSchema, MetodoPagamentoSchema, MetodoPagamentoUpdateSchema


usuario = APIRouter(tags = ["Usuários"])
passageiro = APIRouter(tags = ["Passageiros"])
motorista = APIRouter(tags = ["Motoristas"])
motorista_veiculo = APIRouter(tags = ["Motorista-Veículo"])
veiculo = APIRouter(tags = ["Veículos"])
modelo_veiculo = APIRouter(tags = ["Modelo-Veículo"])
combustivel = APIRouter(tags = ["Combustíveis"])
classe = APIRouter(tags = ["Classes"])
servico = APIRouter(tags = ["Serviços"])
corrida = APIRouter(tags = ["Corridas"])
avaliacao = APIRouter(tags = ["Avaliações"])
pagamento = APIRouter(tags = ["Pagamentos"])
metodo_pagamento = APIRouter(tags = ["Metodo-Pagamento"])


@usuario.post("/usuario/post")
async def criar_usuario(dados: UsuarioSchema, db: Session = Depends(get_db)):
    novo_usuario = UsuarioModel(**dados.model_dump())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return {"mensagem": "Usuário criado com sucesso", "Usuário": novo_usuario}


@usuario.get("/usuario/get")
async def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioModel).all()


@usuario.put("/usuario/{id}/update")
async def atualizar_usuario(id: int, dados: UsuarioUpdateSchema, db: Session = Depends(get_db)):
    usuarioUpdate = db.query(UsuarioModel).filter(UsuarioModel.id == id).first()

    if not usuarioUpdate:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Usuário não encontrado.")
    
    for campo, valor in dados.model_dump().items():
        setattr(usuarioUpdate, campo, valor)

    db.add(usuarioUpdate)
    db.commit()
    db.refresh(usuarioUpdate) 

    return {"mensagem": "Usuário atualizado com sucesso.", "Usuário": usuarioUpdate}


@usuario.delete("/usuario/{id}/delete")
async def deletar_usuario(id: int, db: Session = Depends(get_db)):
    usuarioDelete = db.query(UsuarioModel).filter(UsuarioModel.id == id).first()

    if not usuarioDelete:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Usuário não encontrado.")

    db.delete(usuarioDelete)
    db.commit()
    return {"mensagem": "Usuário deletado com sucesso."}


# --------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------


@passageiro.post("/passageiro/post")
async def criar_passageiro(dados: PassageiroSchema, db: Session = Depends(get_db)):
    usuario_existente = db.query(UsuarioModel).filter(UsuarioModel.id == dados.id_usuario).first()
    
    if not usuario_existente:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Usuário com ID {dados.id_usuario} não encontrado."
        )
    
    passageiro_duplicado = db.query(PassageiroModel).filter(PassageiroModel.id_usuario == dados.id_usuario).first()
    if passageiro_duplicado:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail = "Este usuário já possui um perfil de passageiro ativo."
        )

    novo_passageiro = PassageiroModel(**dados.model_dump())
    db.add(novo_passageiro)
    db.commit()
    db.refresh(novo_passageiro)
    return novo_passageiro


@passageiro.get("/passageiro/get")
async def listar_passageiros(db: Session = Depends(get_db)):
    return db.query(PassageiroModel).all()


@passageiro.put("/passageiro/{id}/update")
async def atualizar_passageiro(id: int, dados: PassageiroUpdateSchema, db: Session = Depends(get_db)):
    passageiroUpdate = db.query(PassageiroModel).filter(PassageiroModel.id == id).first()

    if not passageiroUpdate:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Passageiro não encontrado.")
    
    for campo, valor in dados.model_dump().items():
        setattr(passageiroUpdate, campo, valor)

    db.add(passageiroUpdate)
    db.commit()
    db.refresh(passageiroUpdate) 

    return {"mensagem": "Passageiro atualizado com sucesso", "Passageiro": passageiroUpdate}


@passageiro.delete("/passageiro/{id}/delete")
async def deletar_passageiro(id: int, db: Session = Depends(get_db)):
    passageiroDelete = db.query(PassageiroModel).filter(PassageiroModel.id == id).first()

    if not passageiroDelete:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Passageiro não encontrado.")
    
    db.delete(passageiroDelete)
    db.commit()
    return {"message": "Passageiro deletado com sucesso."}


# --------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------


@motorista.post("/motorista/post")
async def criar_motorista(dados: MotoristaSchema, db: Session = Depends(get_db)):
    usuario_existente = db.query(UsuarioModel).filter(UsuarioModel.id == dados.id_usuario).first()
    
    if not usuario_existente:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Usuário com ID {dados.id_usuario} não encontrado."
        )
    
    motorista_duplicado = db.query(MotoristaModel).filter(MotoristaModel.id_usuario == dados.id_usuario).first()
    if motorista_duplicado:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail = "Este usuário já possui um perfil de motorista ativo."
        )

    novo_motorista = MotoristaModel(**dados.model_dump())
    db.add(novo_motorista)
    db.commit()
    db.refresh(novo_motorista)
    return novo_motorista


@motorista.get("/motorista/get")
async def listar_motoristas(db: Session = Depends(get_db)):
    return db.query(MotoristaModel).all()


@motorista.put("/motorista/{id}/update")
async def atualizar_motorista(id: int, dados: MotoristaUpdateSchema, db: Session = Depends(get_db)):
    motoristaUpdate = db.query(MotoristaModel).filter(MotoristaModel.id == id).first()

    if not motoristaUpdate:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Motorista não encontrado.")
    
    for campo, valor in dados.model_dump().items():
        setattr(motoristaUpdate, campo, valor)

    db.add(motoristaUpdate)
    db.commit()
    db.refresh(motoristaUpdate) 

    return {"mensagem": "Motorista atualizado com sucesso.", "Motorista": motoristaUpdate}


@motorista.delete("/motorista/{id}/delete")
async def deletar_motorista(id: int, db: Session = Depends(get_db)):
    motoristaDelete = db.query(MotoristaModel).filter(MotoristaModel.id == id).first()

    if not motoristaDelete:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Motorista não encontrado.")

    db.delete(motoristaDelete)
    db.commit()
    return {"mensagem": "Motorista removido com sucesso."}


# --------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------


@motorista_veiculo.post("/motorista_veiculo/post")
async def criar_motorista_veiculo(dados: MotoristaVeiculoSchema, db: Session = Depends(get_db)):
    
    motorista_existente = db.query(MotoristaModel).filter(MotoristaModel.id == dados.id_motorista).first()
    if not motorista_existente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Motorista com ID {dados.id_motorista} não encontrado."
        )

    veiculo_existente = db.query(VeiculoModel).filter(VeiculoModel.id == dados.id_veiculo).first()
    if not veiculo_existente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Veículo com ID {dados.id_veiculo} não encontrado."
        )

    nova_relacao = MotoristaVeiculoModel(**dados.model_dump())
    db.add(nova_relacao)
    db.commit()
    db.refresh(nova_relacao)

    return {"mensagem": "Relação motorista-veículo criada com sucesso.", "dados": nova_relacao}


@motorista_veiculo.get("/motorista_veiculo/get")
async def listar_motorista_veiculo(db: Session = Depends(get_db)):
    return db.query(MotoristaVeiculoModel).all()


@motorista_veiculo.put("/motorista_veiculo/{id}/update")
async def atualizar_motorista_veiculo(id: int, dados: MotoristaVeiculoUpdateSchema, db: Session = Depends(get_db)):
    
    relacao = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id == id).first()

    if not relacao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Relação motorista-veículo não encontrada."
        )

    for campo, valor in dados.model_dump().items():
        setattr(relacao, campo, valor)

    db.add(relacao)
    db.commit()
    db.refresh(relacao)

    return {"mensagem": "Relação atualizada com sucesso.", "dados": relacao}


@motorista_veiculo.delete("/motorista_veiculo/{id}/delete")
async def deletar_motorista_veiculo(id: int, db: Session = Depends(get_db)):
    
    relacao = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id == id).first()

    if not relacao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Relação motorista-veículo não encontrada."
        )

    db.delete(relacao)
    db.commit()

    return {"mensagem": "Relação removida com sucesso"}


# --------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------


@veiculo.post("/veiculo/post")
async def criar_veiculo(dados: VeiculoSchema, db: Session = Depends(get_db)):

    modelo_existente = db.query(ModeloVeiculoModel).filter(
        ModeloVeiculoModel.id == dados.id_modelo_veiculo
    ).first()

    if not modelo_existente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Modelo com ID {dados.id_modelo_veiculo} não encontrado."
        )

    classe_existente = db.query(ClasseModel).filter(
        ClasseModel.id == dados.id_classe
    ).first()

    if not classe_existente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Classe com ID {dados.id_classe} não encontrada."
        )

    veiculo_duplicado = db.query(VeiculoModel).filter(
        VeiculoModel.placa == dados.placa
    ).first()

    if veiculo_duplicado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe um veículo com essa placa."
        )

    novo_veiculo = VeiculoModel(**dados.model_dump())

    db.add(novo_veiculo)
    db.commit()
    db.refresh(novo_veiculo)

    return {"mensagem": "Veículo criado com sucesso", "veiculo": novo_veiculo}


@veiculo.get("/veiculo/get")
async def listar_veiculos(db: Session = Depends(get_db)):
    return db.query(VeiculoModel).all()


@veiculo.put("/veiculo/{id}/update")
async def atualizar_veiculo(id: int, dados: VeiculoUpdateSchema, db: Session = Depends(get_db)):

    veiculo = db.query(VeiculoModel).filter(VeiculoModel.id == id).first()

    if not veiculo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Veículo não encontrado."
        )

    for campo, valor in dados.model_dump().items():
        setattr(veiculo, campo, valor)

    db.add(veiculo)
    db.commit()
    db.refresh(veiculo)

    return {"mensagem": "Veículo atualizado com sucesso", "veiculo": veiculo}


@veiculo.delete("/veiculo/{id}/delete")
async def deletar_veiculo(id: int, db: Session = Depends(get_db)):

    veiculo = db.query(VeiculoModel).filter(VeiculoModel.id == id).first()

    if not veiculo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Veículo não encontrado."
        )

    db.delete(veiculo)
    db.commit()

    return {"mensagem": "Veículo removido com sucesso"}


# --------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------


@modelo_veiculo.post("/modelo_veiculo/post")
async def criar_modelo_veiculo(dados: ModeloVeiculoSchema, db: Session = Depends(get_db)):

    combustivel_existente = db.query(CombustivelModel).filter(
        CombustivelModel.id == dados.id_combustivel
    ).first()

    if not combustivel_existente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Combustível com ID {dados.id_combustivel} não encontrado."
        )

    novo_modelo = ModeloVeiculoModel(**dados.model_dump())

    db.add(novo_modelo)
    db.commit()
    db.refresh(novo_modelo)

    return {"mensagem": "Modelo de veículo criado com sucesso", "modelo": novo_modelo}


@modelo_veiculo.get("/modelo_veiculo/get")
async def listar_modelos_veiculo(db: Session = Depends(get_db)):
    return db.query(ModeloVeiculoModel).all()


@modelo_veiculo.put("/modelo_veiculo/{id}/update")
async def atualizar_modelo_veiculo(id: int, dados: ModeloVeiculoUpdateSchema, db: Session = Depends(get_db)):

    modelo = db.query(ModeloVeiculoModel).filter(ModeloVeiculoModel.id == id).first()

    if not modelo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Modelo de veículo não encontrado."
        )

    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(modelo, campo, valor)

    db.add(modelo)
    db.commit()
    db.refresh(modelo)

    return {"mensagem": "Modelo atualizado com sucesso", "modelo": modelo}


@modelo_veiculo.delete("/modelo_veiculo/{id}/delete")
async def deletar_modelo_veiculo(id: int, db: Session = Depends(get_db)):

    modelo = db.query(ModeloVeiculoModel).filter(ModeloVeiculoModel.id == id).first()

    if not modelo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Modelo de veículo não encontrado."
        )

    db.delete(modelo)
    db.commit()

    return {"mensagem": "Modelo removido com sucesso"}


# --------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------


@combustivel.post("/combustivel/post")
async def criar_combustivel(dados: CombustivelSchema, db: Session = Depends(get_db)):

    novo_combustivel = CombustivelModel(**dados.model_dump())

    db.add(novo_combustivel)
    db.commit()
    db.refresh(novo_combustivel)

    return {"mensagem": "Combustível criado com sucesso", "combustivel": novo_combustivel}


@combustivel.get("/combustivel/get")
async def listar_combustiveis(db: Session = Depends(get_db)):
    return db.query(CombustivelModel).all()


@combustivel.put("/combustivel/{id}/update")
async def atualizar_combustivel(id: int, dados: CombustivelUpdateSchema, db: Session = Depends(get_db)):

    combustivel = db.query(CombustivelModel).filter(CombustivelModel.id == id).first()

    if not combustivel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Combustível não encontrado."
        )

    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(combustivel, campo, valor)

    db.add(combustivel)
    db.commit()
    db.refresh(combustivel)

    return {"mensagem": "Combustível atualizado com sucesso", "combustivel": combustivel}


@combustivel.delete("/combustivel/{id}/delete")
async def deletar_combustivel(id: int, db: Session = Depends(get_db)):

    combustivel = db.query(CombustivelModel).filter(CombustivelModel.id == id).first()

    if not combustivel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Combustível não encontrado."
        )

    db.delete(combustivel)
    db.commit()

    return {"mensagem": "Combustível removido com sucesso"}


# --------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------


@classe.post("/classe/post")
async def criar_classe(dados: ClasseSchema, db: Session = Depends(get_db)):

    nova_classe = ClasseModel(**dados.model_dump())

    db.add(nova_classe)
    db.commit()
    db.refresh(nova_classe)

    return {"mensagem": "Classe criada com sucesso", "classe": nova_classe}


@classe.get("/classe/get")
async def listar_classes(db: Session = Depends(get_db)):
    return db.query(ClasseModel).all()


@classe.put("/classe/{id}/update")
async def atualizar_classe(id: int, dados: ClasseUpdateSchema, db: Session = Depends(get_db)):

    classe = db.query(ClasseModel).filter(ClasseModel.id == id).first()

    if not classe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Classe não encontrada."
        )

    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(classe, campo, valor)

    db.add(classe)
    db.commit()
    db.refresh(classe)

    return {"mensagem": "Classe atualizada com sucesso", "classe": classe}


@classe.delete("/classe/{id}/delete")
async def deletar_classe(id: int, db: Session = Depends(get_db)):

    classe = db.query(ClasseModel).filter(ClasseModel.id == id).first()

    if not classe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Classe não encontrada."
        )

    db.delete(classe)
    db.commit()

    return {"mensagem": "Classe removida com sucesso"}


# --------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------


@servico.post("/servico/post")
async def criar_servico(dados: ServicoSchema, db: Session = Depends(get_db)):
    classe = db.query(ClasseModel).filter(ClasseModel.id == dados.id_classe).first()

    if not classe:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Classe não encontrada."
        )

    novo_servico = ServicoModel(**dados.model_dump())

    db.add(novo_servico)
    db.commit()
    db.refresh(novo_servico)

    return {"mensagem": "Serviço criado com sucesso", "Serviço": novo_servico}


@servico.get("/servico/get")
async def listar_servicos(db: Session = Depends(get_db)):
    return db.query(ServicoModel).all()


@servico.put("/servico/{id}/update")
async def atualizar_servico(id: int, dados: ServicoUpdateSchema, db: Session = Depends(get_db)):
    servicoUpdate = db.query(ServicoModel).filter(ServicoModel.id == id).first()

    if not servicoUpdate:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Serviço não encontrado."
        )

    for campo, valor in dados.model_dump().items():
        setattr(servicoUpdate, campo, valor)

    db.commit()
    db.refresh(servicoUpdate)

    return servicoUpdate


@servico.delete("/servico/{id}/delete")
async def deletar_servico(id: int, db: Session = Depends(get_db)):
    servicoDelete = db.query(ServicoModel).filter(ServicoModel.id == id).first()

    if not servicoDelete:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Serviço não encontrado."
        )
    
    db.delete(servicoDelete)
    db.commit()

    return {"mensagem": "Serviço deletado com sucesso."}


# --------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------


@corrida.post("/corrida/post")
async def criar_corrida(dados: CorridaSchema, db: Session = Depends(get_db)):
    
    passageiro = db.query(PassageiroModel).filter(PassageiroModel.id == dados.id_passageiro).first()
    motorista = db.query(MotoristaModel).filter(MotoristaModel.id == dados.id_motorista).first()
    servico = db.query(ServicoModel).filter(ServicoModel.id == dados.id_servico).first()

    if not passageiro:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Passageiro não encontrado.")
    
    if not motorista:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Motorista não encontrado.")
    
    if not servico:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Serviço não encontrado.")

    nova_corrida = CorridaModel(**dados.model_dump())

    db.add(nova_corrida)
    db.commit()
    db.refresh(nova_corrida)

    return nova_corrida


@corrida.get("/corrida/get")
async def listar_corridas(db: Session = Depends(get_db)):
    return db.query(CorridaModel).all()


@corrida.get("/corrida/{id}/update")
async def buscar_corrida(id: int, db: Session = Depends(get_db)):
    corrida = db.query(CorridaModel).filter(CorridaModel.id == id).first()

    if not corrida:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Corrida não encontrada.")

    return corrida


@corrida.put("/corrida/{id}/update")
async def atualizar_corrida(id: int, dados: CorridaUpdateSchema, db: Session = Depends(get_db)):
    corrida = db.query(CorridaModel).filter(CorridaModel.id == id).first()

    if not corrida:
        raise HTTPException(status_code=404, detail="Corrida não encontrada")

    for campo, valor in dados.model_dump().items():
        setattr(corrida, campo, valor)

    db.commit()
    db.refresh(corrida)

    return corrida


@corrida.delete("/corrida/{id}/delete")
async def deletar_corrida(id: int, db: Session = Depends(get_db)):
    corrida = db.query(CorridaModel).filter(CorridaModel.id == id).first()

    if not corrida:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Corrida não encontrada.")

    db.delete(corrida)
    db.commit()

    return {"mensagem": "Corrida deletada com sucesso."}


# --------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------


@avaliacao.post("/avaiacao/post")
async def criar_avaliacao(dados: AvaliacaoSchema, db: Session = Depends(get_db)):
    nova_avaliacao = AvaliacaoModel(**dados.model_dump())
    db.add(nova_avaliacao)
    db.commit()
    db.refresh(nova_avaliacao)

    return nova_avaliacao


@avaliacao.get("/avaliacao/get")
async def listar_avaliacoes(db: Session = Depends(get_db)):
    return db.query(AvaliacaoModel).all()


@avaliacao.put("/avaliacao/{id}/update")
async def atualizar_avaliacao(id: int, dados: AvaliacaoUpdateSchema, db: Session = Depends(get_db)):
    avaliacao_db = db.query(AvaliacaoModel).filter(AvaliacaoModel.id == id).first()

    if not avaliacao_db:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Avaliação não encontrada.")

    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(avaliacao_db, campo, valor)

    db.commit()
    db.refresh(avaliacao_db)

    return avaliacao_db


@avaliacao.delete("/avaliacao/{id}/delete")
async def deletar_avaliacao(id: int, db: Session = Depends(get_db)):
    avaliacao_db = db.query(AvaliacaoModel).filter(AvaliacaoModel.id == id).first()

    if not avaliacao_db:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")

    db.delete(avaliacao_db)
    db.commit()

    return {"mensagem": "Avaliação deletada com sucesso"}


# --------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------


@pagamento.post("/pagamento/post")
async def criar_pagamento(dados: PagamentoSchema, db: Session = Depends(get_db)):

    corrida = db.query(CorridaModel).filter(CorridaModel.id == dados.id_corrida).first()
    
    if not corrida:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Corrida não encontrada."
        )

    pagamento_existente = db.query(PagamentoModel)\
        .filter(PagamentoModel.id_corrida == dados.id_corrida)\
        .first()

    if pagamento_existente:
        raise HTTPException(
            status_code=400,
            detail="Essa corrida já possui pagamento"
        )

    novo_pagamento = PagamentoModel(**dados.model_dump())
    db.add(novo_pagamento)
    db.commit()
    db.refresh(novo_pagamento)

    return novo_pagamento


@pagamento.get("/pagamento/get")
async def listar_pagamentos(db: Session = Depends(get_db)):
    return db.query(PagamentoModel).all()


@pagamento.put("/pagamento/{id}/update")
async def atualizar_pagamento(id: int, dados: PagamentoUpdateSchema, db: Session = Depends(get_db)):
    pagamento = db.query(PagamentoModel).filter(PagamentoModel.id == id).first()

    if not pagamento:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Pagamento não encontrado."
        )

    for campo, valor in dados.model_dump().items():
        setattr(pagamento, campo, valor)

    db.commit()
    db.refresh(pagamento)

    return pagamento


@pagamento.delete("/pagamento/{id}/delete")
async def deletar_pagamento(id: int, db: Session = Depends(get_db)):
    pagamento = db.query(PagamentoModel).filter(PagamentoModel.id == id).first()

    if not pagamento:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Pagamento não encontrado."
        )

    db.delete(pagamento)
    db.commit()

    return {"mensagem": "Pagamento deletado com sucesso."}


# --------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------


@metodo_pagamento.post("/metodo_pagamento/post")
async def criar_metodo_pagamento(dados: MetodoPagamentoSchema, db: Session = Depends(get_db)):

    novo_metodo = MetodoPagamentoModel(**dados.model_dump())
    db.add(novo_metodo)
    db.commit()
    db.refresh(novo_metodo)

    return novo_metodo


@metodo_pagamento.get("/metodos_pagamento/get")
async def listar_metodos(db: Session = Depends(get_db)):
    return db.query(MetodoPagamentoModel).all()


@metodo_pagamento.put("/metodo_pagamento/{id}/update")
async def atualizar_metodo(id: int, dados: MetodoPagamentoUpdateSchema, db: Session = Depends(get_db)):
    metodo = db.query(MetodoPagamentoModel).filter(MetodoPagamentoModel.id == id).first()

    if not metodo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Método de pagamento não encontrado.")

    for campo, valor in dados.model_dump().items():
        setattr(metodo, campo, valor)

    db.commit()
    db.refresh(metodo)

    return metodo


@metodo_pagamento.delete("/metodo_pagamento/{id}/delete")
async def deletar_metodo(id: int, db: Session = Depends(get_db)):
    metodo = db.query(MetodoPagamentoModel).filter(MetodoPagamentoModel.id == id).first()

    if not metodo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Método de pagamento não encontrado.")

    db.delete(metodo)
    db.commit()

    return {"mensagem": "Método de pagamento deletado com sucesso."}