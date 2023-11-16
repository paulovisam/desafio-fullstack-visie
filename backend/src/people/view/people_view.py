from datetime import date
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict

config = ConfigDict(from_attributes=True)


class PeopleBase(BaseModel):
    nome: str
    rg: str
    cpf: str
    data_nascimento: date
    data_admissao: date
    funcao: Optional[str] = None


class PeopleInDBBase(PeopleBase):
    id_pessoa: int


class PeopleUpdate(PeopleInDBBase):
    nome: Optional[str] = None
    rg: Optional[str] = None
    cpf: Optional[str] = None
    data_nascimento: Optional[date] = None
    data_admissao: Optional[date] = None
    funcao: Optional[str] = None


class ErrorDetail(BaseModel):
    error: Union[str, dict]
    status_code: int
    data: Any = None
