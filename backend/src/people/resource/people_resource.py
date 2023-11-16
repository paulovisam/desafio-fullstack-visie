import json
from typing import List, Optional, Union

from fastapi import APIRouter, Body, Depends, HTTPException, status
from pydantic import ValidationError
from sqlalchemy.orm import Session

from src.common.database.connection import get_session

from ..repository.people_repository import PeopleRepository
from ..service.people_service import PeopleService
from ..view.people_view import (
    ErrorDetail,
    PeopleBase,
    PeopleUpdate,
    PeopleInDBBase,
)

router = APIRouter(prefix='/people')
table_people = PeopleRepository()
service = PeopleService()


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    tags=['People'],
)
async def people_create(
    data: PeopleBase = Body(),
    session: Session = Depends(get_session),
) -> PeopleInDBBase:
    """
    ## Criação de Pessoa
    - **Endpoint:** `/api/v1/people`
    - **Método:** `POST`
    - **Descrição:** Cria uma nova pessoa com os dados fornecidos.
    """
    try:
        result = await service.create_people(session, data)
        if isinstance(result, ErrorDetail):
            raise HTTPException(
                status_code=result.status_code, detail=result.error
            )
        return result
    except HTTPException as error:
        raise error
    except Exception as error:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )


@router.get(
    '',
    status_code=status.HTTP_200_OK,
    tags=['People'],
)
async def people_read(
    id: Optional[str] = None,
    cpf: Optional[str] = None,
    rg: Optional[str] = None,
    session: Session = Depends(get_session),
) -> Union[PeopleInDBBase, List[PeopleInDBBase]]:
    """
    ## Leitura de Pessoa
    - **Endpoint:** `/api/v1/people`
    - **Método:** `GET`
    - **Descrição:** Retorna informações sobre uma pessoa específica com base no ID, CPF ou RG fornecido. Se nenhum parâmetro for fornecido, retorna a lista completa de pessoas.
    """
    try:
        result = await service.read_people(session, id, cpf, rg)
        if isinstance(result, ErrorDetail):
            raise HTTPException(
                status_code=result.status_code, detail=result.error
            )
        return result
    except HTTPException as error:
        raise error
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=error
        )


@router.put('', status_code=status.HTTP_202_ACCEPTED, tags=['People'])
async def people_update(
    data: PeopleUpdate = Body(),
    session: Session = Depends(get_session),
):
    """
    ## Atualização de Pessoa
    - **Endpoint:** `/api/v1/people`
    - **Método:** `PUT`
    - **Descrição:** Atualiza as informações de uma pessoa existente com base no ID fornecido.
    """
    try:
        result = await service.update_people(session, data)
        if isinstance(result, ErrorDetail):
            raise HTTPException(
                status_code=result.status_code, detail=result.error
            )
        return result
    except json.decoder.JSONDecodeError as error:
        raise HTTPException(
            status.HTTP_406_NOT_ACCEPTABLE,
            'Object is not JSON serializable - ' + str(error),
        )


@router.delete('', status_code=status.HTTP_204_NO_CONTENT, tags=['People'])
async def people_delete(
    id: Optional[str] = None,
    cpf: Optional[str] = None,
    rg: Optional[str] = None,
    session: Session = Depends(get_session),
):
    """
    ## Exclusão de Pessoa
    - **Endpoint:** `/api/v1/people`
    - **Método:** `PUT`
    - **Descrição:** Remove uma pessoa com base no ID, CPF ou RG fornecido.
    """
    try:
        result = await service.delete_people(session, id, cpf, rg)
        if isinstance(result, ErrorDetail):
            raise HTTPException(
                status_code=result.status_code, detail=result.error
            )
        return result
    except HTTPException as error:
        raise error
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=error
        )
