from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from ..schemas import BookingCreate, BookingResponse
from ..services import booking_services
from ..services import get_current_user

booking_router = APIRouter(prefix="/bookings", tags=["Bookings"])


@booking_router.post("/", response_model=BookingResponse)
def post_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return booking_services.create_booking(db, booking, current_user.id)


@booking_router.patch("/{booking_id}/cancel")
def cancel_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return booking_services.cancel_booking(db, booking_id, current_user.id)
