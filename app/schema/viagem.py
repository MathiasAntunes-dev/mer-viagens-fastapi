from pydantic import BaseModel
from typing import Optional
from datetime import date

class UsuarioSchema(BaseModel):
    nome: str
    cpf: str
    data_nascimento: date
    idade: Optional[int] = None
    senha: str
    email: str
    usuario: str

    class Config:
        from_attributes = True

class PassageiroSchema(BaseModel):
    id_usuario: int
    media_avaliacao: int

    class Config:
        from_attributes = True

