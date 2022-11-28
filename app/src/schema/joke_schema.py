from pydantic import BaseModel
from typing import Optional
import uuid


class JokeParams(BaseModel):
    joke: Optional[str]
    number: Optional[int]


class JokeBase(BaseModel):
    joke: str
    number: Optional[int]


class Joke(JokeBase):
    uuid: uuid.UUID
    created_at: int
    updated_at: int


class JokeCreate(JokeBase):
    created_at: Optional[int]


class JokeUpdated(JokeBase):
    updated_at: Optional[int]


class JokeResponse(BaseModel):
    status_code: int = 200
    message: str
    data: Optional[Joke]
