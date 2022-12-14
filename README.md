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

### If you wish use MongoDB or other noSQL database: 
```
import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.jokes

joke_collection = database.get_collection("joke_collection")
```

### Poject:

- <http://localhost:3000/>

#### Jokes:
![img.png](img.png)

#### Math:
![img_1.png](img_1.png)