from sqlalchemy import Column, Float, ForeignKey, Integer, String, Date, BigInteger, DateTime, Boolean, Enum
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

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

class MotoristaModel(Base):
    __tablename__ = "motorista"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_usuario = Column(BigInteger, ForeignKey("usuario.id"), unique=True, nullable=False)
    media_avaliacao = Column(Float, nullable=True)
    cnh = Column(String(9), unique=True, nullable=False)

    usuario = relationship("UsuarioModel", back_populates="motorista")

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

class MotoristaVeiculoModel(Base):
    __tablename__ = "motorista_veiculo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_motorista = Column(Integer, ForeignKey("motorista.id"), nullable=False)
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

    
    id_modelo_veiculo = relationship("ModeloVeiculoModel", back_populates="veiculo")
    classe = relationship("ClasseModel", back_populates="veiculo")

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

class PropriedadeEnum(enum.Enum):
    alugado = "alugado"
    proprio = "proprio"

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

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------