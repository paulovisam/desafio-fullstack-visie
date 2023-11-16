from datetime import date

from src.people.model.people import People

id_pessoa = 1
nome = 123
rg = '123456789'
cpf = '987654321'
data_nascimento = date(1990, 1, 1)
data_admissao = date(2020, 1, 1)
funcao = 'Manager'

# Act and Assert
# with pytest.raises(Exception):
People(
    id_pessoa=id_pessoa,
    nome=nome,
    rg=rg,
    cpf=cpf,
    data_nascimento=data_nascimento,
    data_admissao=data_admissao,
    funcao=funcao,
)
