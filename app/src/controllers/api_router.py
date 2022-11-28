from fastapi import APIRouter
from app.src.schema.handler_error_schema import ResponseError
from app.src.utils.settings import Settings

settings = Settings()

responses = {
    400: {"model": ResponseError},
    401: {"model": ResponseError},
    422: {}
}

router = APIRouter(responses={**responses})
