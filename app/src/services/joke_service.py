import requests
from sqlalchemy.orm import Session

from app.src.schema.joke_schema import JokeParams, JokeResponse, JokeRemoteResponse
from app.src.services.handler_error_service import handler_errors
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
        try:
            joke = None

            if origin.lower() == "chuck":

                joke = self.chuck_joke()

            elif origin.lower() == "dad":

                joke = self.dad_joke()

            else:
                raise Exception(f'API {origin} not Found')

            return JokeRemoteResponse(
                status_code=200,
                message=f"Get Joke Success",
                joke=joke
            )

        except Exception as ex:
            return JokeRemoteResponse(
                status_code=400,
                message=f"'{str(ex)}' - 'Error to get joke from API'"
            )

    def dad_joke(self):
        url = settings.DAD_API
        request = requests.get(url=url, headers={"Accept": "text/plain"})

        if request.status_code != 200:
            raise Exception(f'Error to get Joke from {url}')

        joke = request.text

        return joke

    def chuck_joke(self):
        url = settings.CHUCK_API
        request = requests.get(url=url)

        if request.status_code != 200:
            raise Exception(f'Error to get Joke from {url}')

        joke = request.json().get('value')

        return joke
