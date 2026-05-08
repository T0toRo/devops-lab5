from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_get_existed_user():
    response = client.get("/users/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Ivan",
        "age": 25,
    }


def test_get_non_existed_user():
    response = client.get("/users/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_get_users_list():
    response = client.get("/users/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 2


def test_create_user():
    response = client.post(
        "/users/",
        json={
            "name": "Petr",
            "age": 30,
        },
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Petr"
    assert response.json()["age"] == 30
    assert "id" in response.json()


def test_create_user_with_invalid_age():
    response = client.post(
        "/users/",
        json={
            "name": "Bad user",
            "age": -1,
        },
    )

    assert response.status_code == 422
