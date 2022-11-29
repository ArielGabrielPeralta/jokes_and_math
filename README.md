# JOKES AND MATHS

### Requirements:

- Python 3.10
- PostgresSQL
- Docker

### How to run manual:

- <code>python -m venv ./venv</code>
- <code>.\venv\Scripts\activate</code>
- <code>pip install -r requirements.txt</code>
- <code>uvicorn main:app --host 0.0.0.0 --port 3000</code>

### How to run docker:

- <code>docker build -t joke_and_math .</code>
- <code> docker run -d --name joke_and_math --env-file=./envs/.env_docker --add-host host.internal.docker:host-gateway -p 3000:3000 joke_and_math:latest</code>