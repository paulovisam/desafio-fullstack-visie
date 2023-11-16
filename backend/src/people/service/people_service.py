from typing import List, Union

from fastapi import status

from ..model.people import People
from ..repository.people_repository import PeopleRepository
from ..view.people_view import (
    ErrorDetail,
    PeopleBase,
    PeopleUpdate,
    PeopleInDBBase,
)
import logging

log = logging.getLogger(__name__)

class PeopleService:
    def __init__(self) -> None:
        self.table_people = PeopleRepository()

    async def create_people(
        self, session, data: PeopleBase
    ) -> Union[PeopleInDBBase, ErrorDetail]:
        try:
            if self.table_people.select_by(session, People.cpf, data.cpf):
                return ErrorDetail(
                    error='This CPF already registered',
                    status_code=status.HTTP_409_CONFLICT,
                )
            if self.table_people.select_by(session, People.rg, data.rg):
                return ErrorDetail(
                    error='This RG already registered',
                    status_code=status.HTTP_409_CONFLICT,
                )
            data = self.table_people.insert(
                session,
                data.nome,
                data.rg,
                data.cpf,
                data.data_nascimento,
                data.data_admissao,
                data.funcao,
            )
            return data
        except Exception as error:
            return ErrorDetail(
                error=str(error), status_code=status.HTTP_400_BAD_REQUEST
            )

    async def read_people(
        self, session, id: str, cpf: str, rg: str
    ) -> Union[PeopleInDBBase, ErrorDetail, List[PeopleInDBBase]]:
        try:
            log.info("service - read people")
            if id:
                people_data = self.table_people.select_by(
                    session, People.id_pessoa, id
                )
                if not people_data:
                    return ErrorDetail(
                        error='Person not found',
                        status_code=status.HTTP_404_NOT_FOUND,
                    )
                return people_data[0]
            elif cpf:
                people_data = self.table_people.select_by(
                    session, People.cpf, cpf
                )
                if not people_data:
                    return ErrorDetail(
                        error='Person not found',
                        status_code=status.HTTP_404_NOT_FOUND,
                    )
                return people_data[0]
            elif rg:
                people_data = self.table_people.select_by(
                    session, People.rg, rg
                )
                if not people_data:
                    return ErrorDetail(
                        error='Person not found',
                        status_code=status.HTTP_404_NOT_FOUND,
                    )
                return people_data[0]
            else:
                people_data = self.table_people.select_all(session)
                return people_data
        except Exception as error:
            return ErrorDetail(
                error=str(error), status_code=status.HTTP_400_BAD_REQUEST
            )

    async def update_people(
        self, session, data: PeopleUpdate
    ) -> Union[PeopleInDBBase, ErrorDetail]:
        try:
            result = self.table_people.update(
                session,
                data.id_pessoa,
                data.nome,
                data.rg,
                data.cpf,
                data.data_nascimento,
                data.data_admissao,
                data.funcao,
            )
            if not result:
                return ErrorDetail(
                    error='People not found',
                    status_code=status.HTTP_404_NOT_FOUND,
                )
            return result
        except Exception as error:
            return ErrorDetail(
                error=str(error), status_code=status.HTTP_400_BAD_REQUEST
            )

    async def delete_people(self, session, id: str, cpf: str, rg: str):
        try:
            if id:
                return self.table_people.delete_by(
                    session, People.id_pessoa, id
                )
            elif cpf:
                return self.table_people.delete_by(session, People.cpf, cpf)
            elif rg:
                return self.table_people.delete_by(session, People.rg, rg)
            else:
                return ErrorDetail(
                    error='expected query ID, CPF or RG parameters',
                    status_code=status.HTTP_406_NOT_ACCEPTABLE,
                )
        except Exception as error:
            return ErrorDetail(
                error=str(error), status_code=status.HTTP_400_BAD_REQUEST
            )
