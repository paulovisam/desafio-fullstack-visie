# Desafio Fullstack - Visie

Este é um projeto de exemplo de um CRUD de pessoas desenvolvido em Python com o micro framework FastAPI. O sistema segue a arquitetura MVCR (Model, View, Controller, Repository) e permite a criação, edição, exclusão e visualização de pessoas. [Documentação](http://144.22.220.135:8000/redoc)

![Interface CRUD](https://i.imgur.com/tsCu8U0.png)

## Endpoints da API

`/people` Endpoint para criar, editar, listar e excluir uma pessoa.

A estrutura do projeto segue a arquitetura MVCR:

**Model**: Classes que representam os dados do aplicativo e são mapeadas para o banco de dados.

**View (DTO)**: Padrões de entrada e saída da API 

**Controller**: Controladores que lidam com as requisições da API e as interações com o banco de dados.

**Repository**: Interfaces que definem as operações de banco de dados (CRUD) para as entidades.

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=Desafio%20Fullstack%20-%20Visie&uri=https%3A%2F%2Fraw.githubusercontent.com%2Fpaulovisam%2Fdesafio-fullstack-visie%2Fmain%2Fbackend%2FInsomnia.json)
## Requisitos
Certifique-se de que você tenha as seguintes ferramentas instaladas:

- Python
- NodeJS
## Instalação
**Observação**: *Para facilitar o uso, a aplicação angular já está configurada para usar um servidor backend já em execução iniciado pelo GitHub Actions. Basta executar o comando `ng serve` dentro da pasta frontend.*

Clone o repositório para a sua máquina:

```git clone https://github.com/paulovisam/desafio-fullstack-visie```

Instale as dependências para o backend:

```
cd backend
pip install -r requirements.txt
```
Instale as dependências para o frontend:
```
cd frontend
npm install
```
## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`DATABASE_URL=mysql+mysqlconnector://user:password@host:port/db_name`
`DATABASE_PYTEST_URL=mysql+mysqlconnector://user:password@host:port/db_pytest`

Você pode usar um banco de dados embutido para testes locais ou configurar um banco de dados de produção, como MySQL.


# 
## Iniciando o backend

```
cd backend
python3 main.py
```
O servidor backend será iniciado e estará acessível em http://localhost:8000. Você pode alterar a porta no arquivo de main.py, se necessário.

## Iniciando o frontend
```
cd frontend
ng s
```
Acesse a aplicação em http://localhost:4200
## Rodando os testes

Para rodar os testes, rode o seguinte comando

```bash
  cd backend
  pytest -v
```
