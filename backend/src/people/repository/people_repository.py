from typing import Optional

from sqlalchemy import Date
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from ..model.people import People


class PeopleRepository:
    def select_all(self, session: Session) -> None:
        try:
            data = session.query(People).all()
            return data
        except NoResultFound:
            return None
        except Exception as error:
            session.rollback()
            raise error

    def select_by(self, session, field, value: any):
        try:
            return session.query(People).filter(field == value).all()
        except NoResultFound:
            return None
        except Exception as error:
            session.rollback()
            raise error

    def insert(
        self,
        session: Session,
        nome: str,
        rg: str,
        cpf: str,
        data_nascimento: Date,
        data_admissao: Date,
        funcao: str,
    ) -> People:
        try:
            data_insert = People(
                nome=nome,
                rg=rg,
                cpf=cpf,
                data_nascimento=data_nascimento,
                data_admissao=data_admissao,
                funcao=funcao,
            )
            session.add(data_insert)
            session.commit()
            return (
                session.query(People)
                .filter_by(id_pessoa=data_insert.id_pessoa)
                .one()
            )
        except NoResultFound:
            return None
        except Exception as error:
            session.rollback()
            raise error

    def update(
        self,
        session: Session,
        where_id: str,
        nome: Optional[str] = None,
        rg: Optional[str] = None,
        cpf: Optional[str] = None,
        data_nascimento: Optional[Date] = None,
        data_admissao: Optional[Date] = None,
        funcao: Optional[str] = None,
    ) -> None:
        try:
            people = (
                session.query(People)
                .filter(People.id_pessoa == where_id)
                .first()
            )
            if not people:
                return None
            nome = nome if nome is not None else people.nome
            rg = rg if rg is not None else people.rg
            cpf = cpf if cpf is not None else people.cpf
            data_nascimento = (
                data_nascimento
                if data_nascimento is not None
                else people.data_nascimento
            )
            data_admissao = (
                data_admissao
                if data_admissao is not None
                else people.data_admissao
            )
            funcao = funcao if funcao is not None else people.funcao

            session.query(People).filter(People.id_pessoa == where_id).update(
                {
                    'nome': nome,
                    'rg': rg,
                    'cpf': cpf,
                    'data_nascimento': data_nascimento,
                    'data_admissao': data_admissao,
                    'funcao': funcao,
                }
            )
            session.commit()
            return (
                session.query(People)
                .filter(People.id_pessoa == people.id_pessoa)
                .first()
            )
        except NoResultFound:
            return None
        except Exception as error:
            session.rollback()
            raise error

    def delete_by(self, session: Session, field, value: str) -> None:
        try:
            session.query(People).filter(field == value).delete()
            session.commit()
        except NoResultFound:
            return None
        except Exception as error:
            session.rollback()
            raise error
