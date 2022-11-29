from sqlalchemy.orm import Session
from math import gcd

from app.src.schema.math_schema import MathsResponse
from app.src.utils.settings import Settings
import logging

logging.basicConfig(level=logging.INFO)

settings = Settings()


class DBSessionMixin:
    def __init__(self, session: Session):
        self.session = session


class MathDataAccess(DBSessionMixin):
    pass


class MathService(DBSessionMixin):
    def get_least_common_multiple(self, numbers):
        try:
            lcm = 1
            for i in numbers:
                lcm = lcm * i // gcd(lcm, i)
            return MathsResponse(
                message='Get least common multiple Success',
                data=lcm
            )
        except Exception as ex:
            return MathsResponse(
                message=f'{str(ex)} - Get least common multiple Fail'
            )

    def get_number_plus(self, number):
        return MathsResponse(
            message=f'Get number {number} + 1',
            data=number+1
        )
