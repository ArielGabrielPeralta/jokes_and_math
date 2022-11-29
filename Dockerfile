FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install pytest

COPY ./app /code/app
COPY ./envs/* /envs/
COPY test_main.py /code/

RUN mkdir -p /code/jokes_and_math/

CMD ["uvicorn", "app.src.main:app", "--host", "0.0.0.0", "--port", "3000", "--reload"]
