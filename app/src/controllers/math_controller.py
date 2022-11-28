from fastapi import Depends, Request
from sqlalchemy.orm import Session
from app.src.utils.connection import get_connection

from app.src.controllers.api_router import router


@router.get("/math/least-common-multiple", status_code=200, tags=["Maths"])
def get_least_common_multiple(request: Request, session: Session = Depends(get_connection)):
    return True


@router.get("/math/number-plus", status_code=200, tags=["Maths"])
def get_number_plus(request: Request, session: Session = Depends(get_connection)):
    return True
