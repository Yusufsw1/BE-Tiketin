from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.movie_model import Seat, Booking

def get_seats_logic(db: Session, showtime_id: int):
    all_seats = db.query(Seat).all()
    booked_ids = db.query(Booking.seat_id).filter(Booking.showtime_id == showtime_id).all()
    booked_ids_list = [b[0] for b in booked_ids]

    return [
        {"id": s.id, "seat_code": s.seat_code, "is_booked": s.id in booked_ids_list}
        for s in all_seats
    ]

def create_booking(db: Session, data):
    # Cek duplikasi
    is_taken = db.query(Booking).filter(
        Booking.showtime_id == data.showtime_id, 
        Booking.seat_id == data.seat_id
    ).first()
    
    if is_taken:
        raise HTTPException(status_code=400, detail="Kursi sudah dipesan!")

    new_booking = Booking(**data.model_dump())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking