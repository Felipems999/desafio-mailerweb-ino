from datetime import datetime, timedelta

import pytest
from unittest.mock import patch

from .mocks import get_utc_now


@patch("app.services.booking_services.create_booking")
def test_post_booking_success(mock_create_booking, client):
    start_time = get_utc_now()
    end_time = start_time + timedelta(hours=2)

    mock_create_booking.return_value = {
        "id": 1,
        "title": "Reunião Sync",
        "room_id": 1,
        "start_at": start_time,
        "end_at": end_time,
        "participants": ["user1@test.com"],
        "status": "ACTIVE",
        "user_id": 1,
    }

    payload = {
        "title": "Reunião Sync",
        "room_id": 1,
        "start_at": start_time.isoformat(),
        "end_at": end_time.isoformat(),
        "participants": ["user1@test.com"],
    }

    response = client.post("/bookings/", json=payload)

    assert response.status_code == 200
    assert response.json()["status"] == "ACTIVE"


def test_post_booking_missing_timezone(client):
    naive_start = datetime.now()
    naive_end = naive_start + timedelta(hours=1)

    payload = {
        "title": "Reunião",
        "room_id": 1,
        "start_at": naive_start.isoformat(),
        "end_at": naive_end.isoformat(),
        "participants": [],
    }

    response = client.post("/bookings/", json=payload)

    assert response.status_code == 422
    assert "As datas devem conter Timezone" in str(response.json())


def test_post_booking_duration_too_short(client):
    start_time = get_utc_now()
    end_time = start_time + timedelta(minutes=10)

    payload = {
        "title": "Rapidinha",
        "room_id": 1,
        "start_at": start_time.isoformat(),
        "end_at": end_time.isoformat(),
        "participants": [],
    }

    response = client.post("/bookings/", json=payload)

    assert response.status_code == 422
    assert "A duração mínima é de 15 minutos" in str(response.json())
