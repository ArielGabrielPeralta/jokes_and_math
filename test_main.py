from fastapi.testclient import TestClient

from app.src.main import app

client = TestClient(app)


# Test Jokes
def test_create_joke():
    params = {
        "joke": "Where are average things manufactured? The satisfactory.",
        "number": 1
    }
    response = client.post("/jokes/create", params=params)
    assert response.status_code == 201
    response = response.json()
    response = response.get("data")
    assert response.get("number") == 1
    assert response.get("joke") == "Where are average things manufactured? The satisfactory."


def test_update_joke():
    params = {
        "joke": "How do you drown a hipster? Throw him in the mainstream.",
        "number": 1
    }
    response = client.put("/jokes/update", params=params)
    assert response.status_code == 200
    response = response.json()
    response = response.get("data")
    assert response.get("number") == 1
    assert response.get("joke") == "How do you drown a hipster? Throw him in the mainstream."


def test_get_joke():
    params = {
        "joke": "How do you drown a hipster? Throw him in the mainstream.",
        "number": 1
    }
    response = client.get("/jokes", params=params)
    assert response.status_code == 200
    response = response.json()
    response = response.get("data")
    assert response.get("number") == 1
    assert response.get("joke") == "How do you drown a hipster? Throw him in the mainstream."
