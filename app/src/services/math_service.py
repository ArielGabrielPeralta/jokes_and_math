from sqlalchemy.orm import Session

from app.src.utils.settings import Settings
import logging

logging.basicConfig(level=logging.INFO)

settings = Settings()


class DBSessionMixin:
    def __init__(self, session: Session):
        self.session = session


class MathDataAccess(DBSessionMixin):
    pass


class MathService(MathDataAccess):
    pass
