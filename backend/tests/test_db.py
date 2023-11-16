import pytest
from sqlalchemy import select

from src.people.model.people import People


@pytest.mark.db
def test_create_people(session):
    people = People(
        nome='John',
        rg='13245678',
        cpf='12345678912',
        data_nascimento='2000-01-01',
        data_admissao='2022-01-01',
        funcao='Cargo',
    )
    session.add(people)
    session.commit()

    person = session.scalar(select(People).where(People.rg == people.rg))

    assert person.nome == 'John'


@pytest.mark.db
def test_read_people(session, people):
    res = session.scalar(
        select(People).where(People.id_pessoa == people.id_pessoa)
    )
    assert res != None


@pytest.mark.db
def test_update_people(session, people):
    people.nome = 'Alice'
    session.add(people)
    session.commit()
    res = session.scalar(
        select(People).where(People.id_pessoa == people.id_pessoa)
    )
    assert res.nome == people.nome


@pytest.mark.db
def test_delete_people(session, people):
    session.delete(people)
    session.commit()
    res = session.scalar(
        select(People).where(People.id_pessoa == people.id_pessoa)
    )
    assert res == None

    # Tries to retrieve a person from the database using an invalid ID and checks if it returns None.


@pytest.mark.db
def test_read_people_invalid_id(session):
    res = session.scalar(select(People).where(People.id_pessoa == -1))
    assert res == None

    # Tries to delete a person from the database using an invalid ID and checks if it raises an exception.
