import requests
from sqlalchemy.orm import Session

from app.src.schema.joke_schema import JokeParams, JokeResponse, JokeRemoteResponse, JokeRemoteParams
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

    def get_remote_joke(self, origin: str, params: JokeRemoteParams):
        try:
            joke = None

            if origin.lower() == "chuck":

                joke = self.chuck_joke(params)

            elif origin.lower() == "dad":

                joke = self.dad_joke(params)

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

    def dad_joke(self, remote_params: JokeRemoteParams):

        url = settings.DAD_API
        params = None
        if remote_params.pokemon:
            url += '/search'
            params = {"term": remote_params.pokemon,
                      "limit": 1}

        request = requests.get(url=url, headers={"Accept": "application/json"}, params=params)

        if request.status_code != 200:
            raise Exception(f'Error to get Joke from {url}')

        request = request.json()

        joke = request.get("joke")
        if not joke:
            joke = request.get("results")[0].get("joke") if request.get("results") else None

        return joke

    def chuck_joke(self, remote_params: JokeRemoteParams):

        url = settings.CHUCK_API
        params = None

        if remote_params.pokemon:
            url += '/search'
            params = {"query": remote_params.pokemon}
        else:
            url += '/random'
        request = requests.get(url=url, params=params)

        if request.status_code != 200:
            raise Exception(f'Error to get Joke from {url}')

        request = request.json()

        joke = request.get('value')
        if not joke:
            joke = request.get("result")[0].get('value') if request.get("result") else None

        return joke
