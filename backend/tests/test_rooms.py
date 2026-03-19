import pytest
from unittest.mock import patch


@patch("app.routes.room_routes.room_services.create_room")
def test_create_room_success(mock_create_room, client):
    mock_create_room.return_value = {
        "id": 1,
        "name": "Sala A",
        "key": "123",
        "capacity": 10,
    }

    response = client.post(
        "/rooms/", json={"name": "Sala A", "key": "123", "capacity": 10}
    )

    assert response.status_code == 201
    assert response.json()["id"] == 1


def test_create_room_invalid_capacity(client):
    response = client.post("/rooms/", json={"name": "Sala B", "capacity": 0})

    assert response.status_code == 422
