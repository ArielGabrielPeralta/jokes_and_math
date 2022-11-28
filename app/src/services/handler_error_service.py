from fastapi.responses import JSONResponse
from app.src.schema.handler_error_schema import ResponseError, BodyResponseError
from fastapi.encoders import jsonable_encoder
import logging


def get_status_code(ex: Exception, status_code: int):
    if status_code:
        return status_code

    if hasattr(ex, 'status_code'):
        return ex.status_code

    return 400


def get_message(ex: Exception):
    if hasattr(ex, 'message'):
        return ex.message
    elif hasattr(ex, 'detail'):
        if not ex.detail:
            return str(ex)
        return str(ex.detail)
    else:
        return str(ex)


def handler_errors(ex: Exception, message: str, status_code=None):
    logging.error(f"Error found message: {message}. Exception: {ex}")

    content = ResponseError(
        message=message,
        data=BodyResponseError(
            code=ex.__class__.__name__,
            message=get_message(ex)
        )
    )

    return JSONResponse(status_code=get_status_code(ex, status_code), content=jsonable_encoder(content))
