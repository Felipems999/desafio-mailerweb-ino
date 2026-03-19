import pytest
from unittest.mock import patch


@patch("app.routes.user_routes.get_user")
@patch("app.routes.user_routes.verify_password")
@patch("app.routes.user_routes.create_access_token")
def test_login_user_success(mock_create_token, mock_verify, mock_get_user, client):
    mock_get_user.return_value.username = "testuser"
    mock_get_user.return_value.email = "test@example.com"
    mock_get_user.return_value.hashed_password = "hashed"
    mock_verify.return_value = True
    mock_create_token.return_value = "fake-jwt-token"

    response = client.post(
        "/users/login",
        data={"username": "testuser", "password": "password123"},
    )

    assert response.status_code == 200
    assert response.json()["access_token"] == "fake-jwt-token"


@patch("app.routes.user_routes.get_user")
def test_register_user_already_exists(mock_get_user, client):
    mock_get_user.return_value = True

    payload = {
        "email": "test@example.com",
        "username": "testuser",
        "name": "Test",
        "surname": "User",
        "password": "password123",
    }
    response = client.post("/users/register", json=payload)

    assert response.status_code == 400
    assert response.json()["detail"] == "Username ou e-mail já cadastrados!"
