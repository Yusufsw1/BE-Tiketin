from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.db import get_db
from schemas.booking_schema import BookingCreate
from Controllers import booking_controller

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.get("/status/{showtime_id}")
def get_status(showtime_id: int, db: Session = Depends(get_db)):
    return booking_controller.get_seats_logic(db, showtime_id)

@router.post("/reserve")
def reserve(data: BookingCreate, db: Session = Depends(get_db)):
    return booking_controller.create_booking(db, data)