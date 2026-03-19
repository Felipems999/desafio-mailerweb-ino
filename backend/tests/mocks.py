import pytest
from fastapi.testclient import TestClient
from datetime import datetime, timezone

from fastapi import FastAPI
from app.routes import user_router, room_router, booking_router
from app.db import get_db
from app.services import get_current_user

app = FastAPI()
app.include_router(user_router)
app.include_router(room_router)
app.include_router(booking_router)


def override_get_db():
    yield None


def override_get_current_user():
    class MockUser:
        id = 1
        username = "testuser"
        email = "test@example.com"

    return MockUser()


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)


def get_utc_now():
    return datetime.now(timezone.utc)
