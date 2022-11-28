import uuid

from sqlalchemy.schema import Column
from sqlalchemy.types import String, BigInteger, Integer

from app.src.utils.connection import Base


class Joke(Base):
    __tablename__ = 'joke'

    uuid = Column(
        String,
        primary_key=True,
        unique=True,
        index=True,
        default=uuid.uuid4
    )
    number = Column(Integer, index=True)
    joke = Column(String)
    created_at = Column(BigInteger)
    updated_at = Column(BigInteger)
