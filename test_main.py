from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_get_products_all():
    response = client.get("/products/all")
    assert response.status_code == 200

def test_auth_error():
    response = client.post(
        "/token",
        data={
            "username": "",
            "password": ""
        }
    )
    access_token = response.json().get("access_token")
    assert access_token == None
    message = response.json().get("detail")[0].get("msg")
    assert message == "field required"

def test_auth_success():
    response = client.post(
        "/token",
        data={
            "username": "string",
            "password": "string"
        }
    )
    access_token = response.json().get("access_token")
    assert access_token

def test_post_article():
    auth = client.post(
        "/token",
        data={
            "username": "string",
            "password": "string"
        }
    )
    access_token = auth.json().get("access_token")
    assert access_token

    response = client.post(
        "/article/",
        json={
            "title": "string3",
            "content": "string3",
            "is_display": True,
            "creater_id": 1
        },
        headers={
            "Authorization": f'Bearer {access_token}'
        }
    )
    print(response.json())
    assert response.status_code == 200
    assert response.json().get("title") == "string3"