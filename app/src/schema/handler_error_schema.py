from pydantic import BaseModel
from typing import Optional


class BodyResponseError(BaseModel):
    code: Optional[str]
    message: Optional[str]


class ResponseError(BaseModel):
    message: str
    data: BodyResponseError
