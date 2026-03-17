
from sqlalchemy import Column, ForeignKey, Integer, String, Date, BigInteger
from app.database import Base
from sqlalchemy.orm import relationship


class UsuarioModel(Base):
    __tablename__ = "usuario"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False) 
    cpf = Column(String(11), unique=True, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    idade = Column(Integer)
    senha = Column(String(64), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    usuario = Column(String(50), unique=True, nullable=False)


    passageiro = relationship("PassageiroModel", back_populates="usuario", uselist=False)

# -------------------------------------------------------------------------------------------------

class PassageiroModel(Base):
    __tablename__ = "passageiro"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_usuario = Column(BigInteger, ForeignKey("usuario.id", ondelete="CASCADE"), unique=True, nullable=False)
    media_avaliacao = Column(Integer)

    usuario = relationship("UsuarioModel", back_populates="passageiro")


# class MotoristaModel(Base):
#     __tablename__ = "motorista"

#     id = Column(BigInteger, primary_key=True, autoincrement=True)
#     media_avaliacao = Column