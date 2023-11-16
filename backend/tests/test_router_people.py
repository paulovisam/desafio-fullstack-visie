import json

import pytest

from src.people.model.people import People
from src.people.view.people_view import PeopleBase


@pytest.mark.people
def test_create_people_with_valid_data(client):
    res = client.post(
        '/api/v1/people',
        json={
            'nome': 'John',
            'rg': '13.245.678-9',
            'cpf': '123.456.789-41',
            'data_nascimento': '2000-01-01',
            'data_admissao': '2022-01-01',
            'funcao': 'Cargo',
        },
    )
    assert res.status_code == 201
    assert PeopleBase.model_validate_json(json.dumps(res.json()))


@pytest.mark.people
def test_create_people_with_invalid_data(client):
    res = client.post(
        '/api/v1/people',
        json="""{
            'nome': 'John'
            'rg': '13.245.678-9',
            'cpf': '123.456.789-41',
            'data_nascimento': '2000-01-01',
            'data_admissao': '2022-01-01',
            'funcao': 'Cargo',
        }""",
    )
    assert res.status_code == 422


@pytest.mark.people
def test_create_people_already_registered_cpf(client, people):
    res = client.post(
        '/api/v1/people',
        json={
            'nome': 'John',
            'rg': '13.245.678-9',
            'cpf': '123.456.789-41',
            'data_nascimento': '2000-01-01',
            'data_admissao': '2022-01-01',
            'funcao': 'Cargo',
        },
    )
    assert res.status_code == 409
    assert res.json()['detail'] == 'This CPF already registered'


@pytest.mark.people
def test_create_people_already_registered_rg(client, people):
    res = client.post(
        '/api/v1/people',
        json={
            'nome': 'John',
            'rg': '13.245.678-9',
            'cpf': '111.222.333-44',
            'data_nascimento': '2000-01-01',
            'data_admissao': '2022-01-01',
            'funcao': 'Cargo',
        },
    )
    assert res.status_code == 409
    assert res.json()['detail'] == 'This RG already registered'


@pytest.mark.people
def test_create_people_without_optional_data(client):
    res = client.post(
        '/api/v1/people',
        json={
            'nome': 'John',
            'rg': '13.245.678-9',
            'cpf': '123.456.789-41',
            'data_nascimento': '2000-01-01',
            'data_admissao': '2022-01-01',
        },
    )
    assert res.status_code == 201
    assert PeopleBase.model_validate_json(json.dumps(res.json()))


@pytest.mark.people
def test_create_people_with_missing_fields(client):
    res = client.post(
        '/api/v1/people',
        json={
            'nome': 'John',
            'cpf': '123.456.789-41',
            'data_nascimento': '2000-01-01',
            'data_admissao': '2022-01-01',
        },
    )
    assert res.status_code == 422
    assert 'detail' in res.json()

    # Test if a people with invalid data types in the fields cannot be created.


@pytest.mark.people
def test_create_people_with_invalid_data_types(client):
    res = client.post(
        '/api/v1/people',
        json={
            'nome': 123,
            'rg': '13.245.678-9',
            'cpf': '123.456.789-41',
            'data_nascimento': '2000-01-01',
            'data_admissao': '2022-01-01',
            'funcao': 'Cargo',
        },
    )
    assert res.status_code == 422
    assert 'detail' in res.json()


@pytest.mark.people
def test_read_people_all(client, people):
    res = client.get(
        '/api/v1/people',
    )
    assert res.status_code == 200


@pytest.mark.people
def test_read_people_by_id(client, people):
    res = client.get(
        '/api/v1/people',
        params={'id': people.id_pessoa},
    )
    assert res.status_code == 200
    assert PeopleBase.model_validate_json(json.dumps(res.json()))


@pytest.mark.people
def test_read_people_by_cpf(client, people):
    res = client.get(
        '/api/v1/people',
        params={'cpf': people.cpf},
    )
    assert res.status_code == 200
    assert PeopleBase.model_validate_json(json.dumps(res.json()))


@pytest.mark.people
def test_read_people_by_rg(client, people):
    res = client.get(
        '/api/v1/people',
        params={'rg': people.rg},
    )
    assert res.status_code == 200
    assert PeopleBase.model_validate_json(json.dumps(res.json()))


@pytest.mark.people
def test_update_people(client, people):
    res = client.put(
        '/api/v1/people',
        json={
            'id_pessoa': people.id_pessoa,
            'nome': 'Name Updated',
            'rg': '13.245.678-9',
            'cpf': '123.456.789-41',
            'data_nascimento': '2000-01-01',
            'data_admissao': '2022-01-01',
            'funcao': 'Cargo',
        },
    )
    assert res.status_code == 202
    assert PeopleBase.model_validate_json(json.dumps(res.json()))


@pytest.mark.people
def test_update_people_partial_data(client, people):
    res = client.put(
        '/api/v1/people',
        json={
            'id_pessoa': people.id_pessoa,
            'nome': 'Name Updated',
        },
    )
    assert res.status_code == 202
    assert PeopleBase.model_validate_json(json.dumps(res.json()))

    # Can update a person's information with invalid data types


@pytest.mark.people
def test_update_people_with_invalid_data_types(client, people):
    res = client.put(
        '/api/v1/people',
        json={
            'id_pessoa': people.id_pessoa,
            'nome': 123,
            'rg': '13.245.678-9',
            'cpf': '123.456.789-41',
            'data_nascimento': '2000-01-01',
            'data_admissao': '2022-01-01',
            'funcao': 'Cargo',
        },
    )
    assert res.status_code == 422
    assert 'detail' in res.json()

    # Can update a person's information with missing id_pessoa field


@pytest.mark.people
def test_update_people_missing_id_pessoa(client, people):
    res = client.put(
        '/api/v1/people',
        json={
            'nome': 'Name Updated',
            'rg': '13.245.678-9',
            'cpf': '123.456.789-41',
            'data_nascimento': '2000-01-01',
            'data_admissao': '2022-01-01',
            'funcao': 'Cargo',
        },
    )
    assert res.status_code == 422
    assert 'detail' in res.json()

    # Can update a person's information with invalid id_pessoa field


@pytest.mark.people
def test_update_people_invalid_id_pessoa(client, people):
    res = client.put(
        '/api/v1/people',
        json={
            'id_pessoa': 'invalid_id',
            'nome': 'Name Updated',
            'rg': '13.245.678-9',
            'cpf': '123.456.789-41',
            'data_nascimento': '2000-01-01',
            'data_admissao': '2022-01-01',
            'funcao': 'Cargo',
        },
    )
    assert res.status_code == 422
    assert 'detail' in res.json()


@pytest.mark.people
def test_delete_people_with_id(client, session, people):
    id = people.id_pessoa
    res = client.delete(
        '/api/v1/people',
        params={'id': id},
    )
    result = session.query(People).filter_by(id_pessoa=id).first()
    assert res.status_code == 204
    assert result == None


@pytest.mark.people
def test_delete_people_with_cpf(client, session, people):
    cpf = people.cpf
    res = client.delete(
        '/api/v1/people',
        params={'cpf': cpf},
    )
    result = session.query(People).filter_by(cpf=cpf).first()
    assert res.status_code == 204
    assert result == None


@pytest.mark.people
def test_delete_people_with_rg(client, session, people):
    rg = people.rg
    res = client.delete(
        '/api/v1/people',
        params={'rg': rg},
    )
    result = session.query(People).filter_by(rg=rg).first()
    assert res.status_code == 204
    assert result == None


@pytest.mark.people
def test_delete_people_without_param(client):
    res = client.delete('/api/v1/people')
    assert res.status_code == 406
    assert res.json()['detail'] == 'expected query ID, CPF or RG parameters'
