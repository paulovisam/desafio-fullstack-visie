# ...
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from main import app
from settings import Settings
from src.common.database.base import Base
from src.common.database.connection import get_session
from src.people.model.people import People

# ...


settings = Settings()


def pytest_configure(config):
    config.addinivalue_line('markers', 'db: mark test as database')
    config.addinivalue_line('markers', 'people: mark test as people')
    config.addinivalue_line(
        'markers', 'people_model: mark test as model people'
    )


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def session():
    engine = create_engine(settings.DATABASE_PYTEST_URL)
    Session = sessionmaker(bind=engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)


@pytest.fixture
def people(session):
    people = People(
        nome='John',
        rg='13.245.678-9',
        cpf='123.456.789-41',
        data_nascimento='2000-01-01',
        data_admissao='2022-01-01',
        funcao='Cargo',
    )
    session.add(people)
    session.commit()
    session.refresh(people)
    return people
