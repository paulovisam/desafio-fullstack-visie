from sqlalchemy import Column, Date, Integer, String

from ...common.database.base import Base


class People(Base):
    __tablename__ = 'pessoas'
    id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    rg = Column(String(100), nullable=False)
    cpf = Column(String(100), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    data_admissao = Column(Date, nullable=False)
    funcao = Column(String(100), nullable=True)

    def __repr__(self) -> str:
        return f'(id_pessoa={self.id_pessoa}, nome={self.nome}, rg={self.rg}, cpf={self.cpf}, data_nascimento={self.data_nascimento}, data_admissao={self.data_admissao}, funcao={self.funcao})'
