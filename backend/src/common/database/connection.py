import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

load_dotenv()


def get_session():
    engine = create_engine(os.getenv('DATABASE_URL'))
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()


class DBConnectionHandler:
    def __init__(self) -> None:
        load_dotenv()
        self.__connection_string = os.getenv('DATABASE_URL')
        self.__engine = self.__create_database_engine()
        self.session = None
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def get_session(self):
        yield self.session

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
