from fastapi import Depends, Response
from sqlalchemy.orm import Session

from app.src.schema.joke_schema import JokeResponse, JokeParams, JokeRemoteResponse, JokeRemoteParams
from app.src.services.joke_service import JokeService
from app.src.utils.connection import get_connection

from app.src.controllers.api_router import router


@router.post("/jokes/create", response_model=JokeResponse, tags=["Jokes"])
def create_joke(response: Response, joke_params: JokeParams = Depends(), session: Session = Depends(get_connection)):
    return JokeService(session).create_joke(joke_params, response)


@router.put("/jokes/update", response_model=JokeResponse, status_code=200, tags=["Jokes"])
def update_joke(joke_params: JokeParams = Depends(), session: Session = Depends(get_connection)):
    return JokeService(session).update_joke(joke_params)


@router.delete("/jokes/delete", response_model=JokeResponse, status_code=200, tags=["Jokes"])
def delete_joke(joke_params: JokeParams = Depends(), session: Session = Depends(get_connection)):
    return JokeService(session).delete_joke(joke_params)


@router.get("/jokes", response_model=JokeResponse, status_code=200, tags=["Jokes"])
def get_db_joke(joke_params: JokeParams = Depends(), session: Session = Depends(get_connection)):
    return JokeService(session).get_db_joke(joke_params)


@router.get("/jokes/remote/{origin}", response_model=JokeRemoteResponse, status_code=200, tags=["Jokes"])
def get_remote_joke(origin: str, params: JokeRemoteParams = Depends(), session: Session = Depends(get_connection)):
    return JokeService(session).get_remote_joke(origin, params)
