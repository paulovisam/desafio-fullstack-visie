from datetime import date

import pytest

from src.people.model.people import People


# Creating a new instance of People with valid arguments should set the attributes correctly and return the instance.
@pytest.mark.people_model
def test_create_instance_with_valid_arguments():
    # Arrange
    id_pessoa = 1
    nome = 'John Doe'
    rg = '123456789'
    cpf = '987654321'
    data_nascimento = date(1990, 1, 1)
    data_admissao = date(2020, 1, 1)
    funcao = 'Manager'

    # Act
    people = People(
        id_pessoa=id_pessoa,
        nome=nome,
        rg=rg,
        cpf=cpf,
        data_nascimento=data_nascimento,
        data_admissao=data_admissao,
        funcao=funcao,
    )

    # Assert
    assert people.id_pessoa == id_pessoa
    assert people.nome == nome
    assert people.rg == rg
    assert people.cpf == cpf
    assert people.data_nascimento == data_nascimento
    assert people.data_admissao == data_admissao
    assert people.funcao == funcao

    # Retrieving an existing instance of People from the database should return the correct object with all attributes.


@pytest.mark.people_model
def test_update_existing_instance_with_valid_arguments():
    # Arrange
    id_pessoa = 1
    nome = 'John Doe'
    rg = '123456789'
    cpf = '987654321'
    data_nascimento = date(1990, 1, 1)
    data_admissao = date(2020, 1, 1)
    funcao = 'Manager'

    # Create a new instance of People
    people = People(
        id_pessoa=id_pessoa,
        nome=nome,
        rg=rg,
        cpf=cpf,
        data_nascimento=data_nascimento,
        data_admissao=data_admissao,
        funcao=funcao,
    )

    # Act
    updated_nome = 'Jane Doe'
    updated_rg = '987654321'
    updated_cpf = '123456789'
    updated_data_nascimento = date(1995, 1, 1)
    updated_data_admissao = date(2021, 1, 1)
    updated_funcao = 'Supervisor'

    people.nome = updated_nome
    people.rg = updated_rg
    people.cpf = updated_cpf
    people.data_nascimento = updated_data_nascimento
    people.data_admissao = updated_data_admissao
    people.funcao = updated_funcao

    # Assert
    assert people.nome == updated_nome
    assert people.rg == updated_rg
    assert people.cpf == updated_cpf
    assert people.data_nascimento == updated_data_nascimento
    assert people.data_admissao == updated_data_admissao
    assert people.funcao == updated_funcao
