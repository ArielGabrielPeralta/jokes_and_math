import os

from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    # Database
    db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')

    APP_PATH: str = os.getenv('APP_PATH')

    # APIs
    CHUCK_API: str = os.getenv('CHUCK_API')
    DAD_API: str = os.getenv('DAD_API')
