from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime

class UsuarioSchema(BaseModel):
    nome: str
    cpf: str
    data_nascimento: str
    idade: int
    senha: str
    email: str
    nome_usuario: str

    class Config:
        from_attributes = True


class UsuarioUpdateSchema(BaseModel):
    nome: Optional[str] = None
    cpf: Optional[str] = None
    data_nascimento: Optional[str] = None
    idade: Optional[int] = None
    senha: Optional[str] = None
    email: Optional[str] = None
    nome_usuario: Optional[str] = None

    class Config:
        from_attributes = True

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

class PassageiroSchema(BaseModel):
    id_usuario: int
    media_avaliacao: float

    class Config:
        from_attributes = True


class PassageiroUpdateSchema(BaseModel):
    media_avaliacao: Optional[float] = None

    class Config:
        from_attributes = True

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

class MotoristaSchema(BaseModel):
    id_usuario: int
    media_avaliacao: float
    cnh: str

    class Config:
        from_attributes = True


class MotoristaUpdateSchema(BaseModel):
    media_avaliacao: Optional[float] = None
    cnh: Optional[str] = None

    class Config:
        from_attributes = True

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

class MotoristaVeiculoSchema(BaseModel):
    id_motorista: int
    id_veiculo: int
    datahora_inicio: datetime
    datahora_fim: datetime
    

    class Config:
        from_attributes = True

class MotoristaVeiculoUpdateSchema(BaseModel):
    datahora_inicio: Optional[datetime] = None
    datahora_fim: Optional[datetime] = None

    class Config:
        from_attributes = True

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


class VeiculoSchema(BaseModel):
    placa: str
    id_modelo_veiculo: int
    tem_seguro: bool
    id_classe: int

    class Config:
        from_attributes = True
        

class VeiculoUpdateSchema(BaseModel):
    placa: Optional[str] = None
    tem_seguro: Optional[bool] = None


    class Config:
        from_attributes = True

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

class PropriedadeEnum(str, Enum):
    alugado = "Alugado"
    proprio = "Próprio"

class ModeloVeiculoSchema(BaseModel):
    nome_modelo: str
    cor: str
    fabricante: str
    ano: int
    capacidade: int
    propriedade: PropriedadeEnum
    id_combustivel: int

    class Config:
        from_attributes = True

class ModeloVeiculoUpdateSchema(BaseModel):
    nome_modelo: Optional[str] = None
    cor: Optional[str] = None
    fabricante: Optional[str] = None
    ano: Optional[int] = None
    capacidade: Optional[int] = None
    propriedade: Optional[PropriedadeEnum] = None
    
    class Config:
        from_attributes = True

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

class CombustivelSchema(BaseModel):
    descricao: str
    fator_carbono: float

    class Config:
        from_attributes = True
        

class CombustivelUpdateSchema(BaseModel):
    descricao: Optional[str] = None
    fator_carbono: Optional[float] = None


    class Config:
        from_attributes = True

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

class ClasseSchema(BaseModel):
    nome_classe: str
    fator_preco: float

    class Config:
        from_attributes = True
        

class ClasseUpdateSchema(BaseModel):
    nome_classe: Optional[str] = None
    fator_preco: Optional[float] = None


    class Config:
        from_attributes = True

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

class ServicoSchema(BaseModel):
    nome_servico: str
    id_classe: int

    class Config:
        from_attributes = True


class ServicoUpdateSchema(BaseModel):
    nome_class: Optional[str] = None
    id_classe: Optional[int] = None

    class Config:
        from_attributes = None

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

class StatusCorridaEnum(str, Enum):
    pendente = "Pendente"
    em_andamento = "Em andamento"
    concluida = "Concluída"
    cancelada = "Cancelada"

class CorridaSchema(BaseModel):
    id_passageiro: int
    id_motorista: int
    id_servico: int
    id_avaliacao: int
    local_partida: str
    local_destino: str
    valor_estimado: float
    status: StatusCorridaEnum

    class Config:
        from_attributes = True


class CorridaUpdateSchema(BaseModel):
    datahora_inicio: Optional[datetime] = None
    datahora_fim: Optional[datetime] = None
    local_partida: Optional[str] = None
    local_destino: Optional[str] = None
    valor_estimado: Optional[float] = None
    status: Optional[StatusCorridaEnum] = None

    class Config:
        from_attributes = True
        
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

class AvaliacaoSchema(BaseModel):
    nota_passageiro: Optional[int] = Field(None, ge=1, le=5)
    nota_motorista: Optional[int] = Field(None, ge=1, le=5)

    class Config:
        from_attributes = True


class AvaliacaoUpdateSchema(BaseModel):
    nota_passageiro: Optional[int] = Field(None, ge=1, le=5)
    nota_motorista: Optional[int] = Field(None, ge=1, le=5)
    datahora_limite: Optional[datetime] = None

    class Config:
        from_attributes = True
        
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

class PagamentoSchema(BaseModel):
    id_corrida: int
    valor: float
    id_metodo_pagamento: int

    class Config:
        from_attributes = True


class PagamentoUpdateSchema(BaseModel):
    valor: Optional[float] = None

    class Config:
        from_attributes = True

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

class MetodoPagamentoSchema(BaseModel):
    descricao: str
    nome_financeira: str

    class Config:
        from_attributes = True
        

class MetodoPagamentoUpdateSchema(BaseModel):
    descricao: Optional[str] = None
    nome_financeira: Optional[str] = None

    class Config:
        from_attributes = True