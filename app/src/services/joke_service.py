import time

import requests
from sqlalchemy.orm import Session

from app.src.models import Joke as JokeModel
from app.src.schema.joke_schema import JokeParams, JokeResponse, JokeRemoteResponse, JokeRemoteParams, JokeCreate, Joke, \
    JokeUpdate
from app.src.utils.settings import Settings
import logging

logging.basicConfig(level=logging.INFO)

settings = Settings()


class DBSessionMixin:
    def __init__(self, session: Session):
        self.session = session


class JokeDataAccess(DBSessionMixin):
    def create_item(self, joke_create: JokeCreate) -> JokeModel:
        item = JokeModel(**joke_create.dict())
        self.session.add(item)
        self.session.commit()
        return item

    def get_item_by_number(self, number) -> JokeModel:
        item = self.session.query(JokeModel).filter(JokeModel.number == number).first()
        return item

    def update_item_by_number(self, joke_update: JokeUpdate) -> JokeModel:
        item = self.session.query(JokeModel).filter(JokeModel.number == joke_update.number)
        item.update(joke_update.dict())
        self.session.commit()
        return item.first()


class JokeService(JokeDataAccess):
    def create_joke(self, joke_params: JokeParams):
        try:

            joke = self.get_item_by_number(joke_params.number)

            status_code = 200
            message = 'This joke has been created'

            if not joke:

                now = int(time.time())
                joke_create = JokeCreate(**joke_params.dict(), created_at=now, updated_at=now)
                joke = self.create_item(joke_create)

                status_code = 201
                message = 'Create Success'

            return JokeResponse(
                status_code=status_code,
                message=message,
                data=joke.__dict__
            )

        except Exception as ex:
            return JokeResponse(
                message=f'{str(ex)} - Error to create Joke'
            )

    def update_joke(self, joke_params: JokeParams):
        try:
            joke = self.get_item_by_number(joke_params.number)

            if not joke:
                raise Exception("This Joke doesn't exist")

            joke = self.update_item_by_number(JokeUpdate(**joke_params.dict(), updated_at=int(time.time())))

            return JokeResponse(
                status_code=200,
                message='Update Joke Success',
                data=joke.__dict__
            )

        except Exception as ex:
            return JokeResponse(
                message=f'{str(ex)} - Error to update Joke'
            )

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
