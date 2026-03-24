from sqlalchemy import Column, Float, ForeignKey, Integer, String, Date, BigInteger, DateTime, Boolean, Enum, DECIMAL, SmallInteger
from app.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

class UsuarioModel(Base):
    __tablename__ = "usuario"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False) 
    cpf = Column(String(11), unique=True, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    idade = Column(Integer, nullable=False)
    senha = Column(String(64), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    nome_usuario = Column(String(255), unique=True, nullable=False)


    passageiro = relationship("PassageiroModel", back_populates="usuario", uselist=False)
    motorista = relationship("MotoristaModel", back_populates="usuario", uselist=False)

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

class PassageiroModel(Base):
    __tablename__ = "passageiro"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_usuario = Column(BigInteger, ForeignKey("usuario.id"), unique=True, nullable=False)
    media_avaliacao = Column(Float, nullable=True)

    usuario = relationship("UsuarioModel", back_populates="passageiro")
    corridas = relationship("CorridaModel", back_populates="passageiro")

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

class MotoristaModel(Base):
    __tablename__ = "motorista"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_usuario = Column(BigInteger, ForeignKey("usuario.id"), unique=True, nullable=False)
    media_avaliacao = Column(Float, nullable=True)
    cnh = Column(String(9), unique=True, nullable=False)

    usuario = relationship("UsuarioModel", back_populates="motorista")
    motorista_veiculo = relationship("MotoristaVeiculoModel", back_populates="motorista")
    corridas = relationship("CorridaModel", back_populates="motorista")

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

class MotoristaVeiculoModel(Base):
    __tablename__ = "motorista_veiculo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_motorista = Column(BigInteger, ForeignKey("motorista.id"), nullable=False)
    id_veiculo = Column(Integer, ForeignKey("veiculo.id"), nullable=False)
    datahora_inicio = Column(DateTime, default=datetime.now, nullable=False)
    datahora_fim = Column(DateTime, nullable=True)
    
    motorista = relationship("MotoristaModel", back_populates="motorista_veiculo")
    veiculo = relationship("VeiculoModel", back_populates="motorista_veiculo")

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

class VeiculoModel(Base):
    __tablename__ = "veiculo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    placa = Column(String(7), nullable=False, unique=True)
    id_modelo_veiculo = Column(Integer, ForeignKey("modelo_veiculo.id"), nullable=False)
    tem_seguro = Column(Boolean, nullable=False, default=False)
    id_classe = Column(Integer, ForeignKey("classe.id"), nullable=False)

    
    modelo_veiculo = relationship("ModeloVeiculoModel", back_populates="veiculo")
    classe = relationship("ClasseModel", back_populates="veiculo")
    motorista_veiculo = relationship("MotoristaVeiculoModel", back_populates="veiculo")

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

class PropriedadeEnum(enum.Enum):
    alugado = "Alugado"
    proprio = "Próprio"

class ModeloVeiculoModel(Base):
    __tablename__ = "modelo_veiculo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_modelo = Column(String(50), nullable=False)
    cor = Column(String(20), nullable=False)
    fabricante = Column(String(30), nullable=False)
    ano = Column(Integer, nullable=False)
    capacidade = Column(Integer, nullable=False)
    propriedade = Column(Enum(PropriedadeEnum), nullable=False)
    id_combustivel = Column(Integer, ForeignKey("combustivel.id"), nullable=False)

    combustivel = relationship("CombustivelModel", back_populates="modelo_veiculo")
    veiculo = relationship("VeiculoModel", back_populates="modelo_veiculo")

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

class CombustivelModel(Base):
    __tablename__ = "combustivel"

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(45), nullable=False)
    fator_carbono = Column(Float, nullable=True)

    
    modelo_veiculo = relationship("ModeloVeiculoModel", back_populates="combustivel")

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

class ClasseModel(Base):
    __tablename__ = "classe"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_classe = Column(String(50), nullable=False)
    fator_preco = Column(Float, nullable=False)

    
    veiculo = relationship("VeiculoModel", back_populates="classe")
    servicos = relationship("ServicoModel", back_populates="classe")

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

class ServicoModel(Base):
    __tablename__ = "servico"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_servico = Column(String(100), nullable=False)
    id_classe = Column(Integer, ForeignKey("classe.id"), nullable=False)

    classe = relationship("ClasseModel", back_populates="servicos")
    corridas = relationship("CorridaModel", back_populates="servico")
    
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

class StatusCorridaEnum(enum.Enum):
    pendente = "Pendente"
    em_andamento = "Em andamento"
    concluida = "Concluída"
    cancelada = "Cancelada"


class CorridaModel(Base):
    __tablename__ = "corrida"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_passageiro = Column(BigInteger, ForeignKey("passageiro.id"), nullable=False)
    id_motorista = Column(BigInteger, ForeignKey("motorista.id"), nullable=False)
    id_servico = Column(Integer, ForeignKey("servico.id"), nullable=False)
    id_avaliacao = Column(BigInteger, ForeignKey("avaliacao.id"), unique=True, nullable=True)
    datahora_inicio = Column(DateTime, default=datetime.now, nullable=False)
    datahora_fim = Column(DateTime, nullable=True)
    local_partida = Column(String(50), nullable=False)
    local_destino = Column(String(50), nullable=False)
    valor_estimado = Column(DECIMAL(10, 2), nullable=False)
    status = Column(Enum(StatusCorridaEnum), default=StatusCorridaEnum.pendente, nullable=False)

    passageiro = relationship("PassageiroModel", back_populates="corridas")
    motorista = relationship("MotoristaModel", back_populates="corridas")
    servico = relationship("ServicoModel", back_populates="corridas")
    avaliacao = relationship("AvaliacaoModel", back_populates="corrida")
    pagamentos = relationship("PagamentoModel", back_populates="corrida")

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

class AvaliacaoModel(Base):
    __tablename__ = "avaliacao"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nota_passageiro = Column(Integer, nullable=True)
    nota_motorista = Column(Integer, nullable=True)
    datahora_limite = Column(DateTime, nullable=False, default=datetime.now)

    corrida = relationship("CorridaModel", back_populates="avaliacao", uselist=False)

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

class PagamentoModel(Base):
    __tablename__ = "pagamento"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_corrida = Column(BigInteger, ForeignKey("corrida.id"), nullable=False)
    valor = Column(DECIMAL(10, 2), nullable=False)
    id_metodo_pagamento = Column(SmallInteger, ForeignKey("metodo_pagamento.id"), nullable=False)
    datahora_transacao = Column(DateTime, default=datetime.now, nullable=False)

    corrida = relationship("CorridaModel", back_populates="pagamentos")
    metodo_pagamento = relationship("MetodoPagamentoModel", back_populates="pagamentos")
    
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

class MetodoPagamentoModel(Base):
    __tablename__ = "metodo_pagamento"

    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    descricao = Column(String(45), nullable=False)
    nome_financeira = Column(String(45), nullable=False)

    pagamentos = relationship("PagamentoModel", back_populates="metodo_pagamento")