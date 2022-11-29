FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install pytest pytest-cov && rm -rf /root/.cache
RUN pip install requests

COPY ./app /code/app
COPY ./envs/* /envs/

RUN mkdir -p /code/jokes_and_math/

RUN pytest -v

CMD ["uvicorn", "app.src.main:app", "--host", "0.0.0.0", "--port", "3000"]
