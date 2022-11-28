from sqlalchemy.orm import Session

from app.src.schema.joke_schema import JokeParams
from app.src.utils.settings import Settings
import logging

logging.basicConfig(level=logging.INFO)

settings = Settings()


class DBSessionMixin:
    def __init__(self, session: Session):
        self.session = session


class JokeDataAccess(DBSessionMixin):
    pass


class JokeService(JokeDataAccess):
    def create_joke(self, joke_params: JokeParams):
        pass

    def update_joke(self, joke_params: JokeParams):
        pass

    def delete_joke(self, joke_params: JokeParams):
        pass

    def get_db_joke(self, joke_params: JokeParams):
        pass

    def get_remote_joke(self, origin: str):
        pass
