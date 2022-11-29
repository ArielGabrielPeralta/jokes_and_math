from typing import Union

from fastapi import Depends, Query
from sqlalchemy.orm import Session

from app.src.schema.math_schema import MathsResponse
from app.src.services.math_service import MathService
from app.src.utils.connection import get_connection

from app.src.controllers.api_router import router


@router.get("/math/least-common-multiple", response_model=MathsResponse, status_code=200, tags=["Maths"])
def get_least_common_multiple(numbers: Union[list[int], None] = Query(default=None), session: Session = Depends(get_connection)):
    return MathService(session).get_least_common_multiple(numbers)


@router.get("/math/number-plus", response_model=MathsResponse, status_code=200, tags=["Maths"])
def get_number_plus(number: int, session: Session = Depends(get_connection)):
    return MathService(session).get_number_plus(number)
