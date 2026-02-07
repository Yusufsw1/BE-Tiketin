from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.movie_model import Seat, Booking

def get_seats(db: Session, showtime_id: int):
    all_seats = db.query(Seat).all()
    booked_ids = db.query(Booking.seat_id).filter(Booking.showtime_id == showtime_id).all()
    booked_ids_list = [b[0] for b in booked_ids]

    return [
        {"id": s.id, "seat_code": s.seat_code, "is_booked": s.id in booked_ids_list}
        for s in all_seats
    ]

def create_booking(db: Session, data):
    # 1. Validasi: Apakah kursi benar-benar ada di database?
    seat_exists = db.query(Seat).filter(Seat.id == data.seat_id).first()
    if not seat_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Kursi dengan ID {data.seat_id} tidak ditemukan."
        )

    # 2. Validasi: Apakah kursi sudah dipesan untuk jadwal ini? (Race Condition Check)
    already_booked = db.query(Booking).filter(
        Booking.showtime_id == data.showtime_id, 
        Booking.seat_id == data.seat_id
    ).first()

    if already_booked:
        # Kirim 409 Conflict karena data sudah ada
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail="Waduh! Kursi ini baru saja dipesan oleh orang lain. Silakan pilih kursi lain."
        )

    try:
        # 3. Proses Simpan
        new_booking = Booking(
            showtime_id=data.showtime_id,
            seat_id=data.seat_id,
            user_name=data.user_name
        )
        db.add(new_booking)
        db.commit()
        db.refresh(new_booking)
        
        return {
            "status": "success",
            "message": "Booking berhasil dikonfirmasi!",
            "data": {
                "booking_id": new_booking.id,
                "seat": seat_exists.seat_code,
                "user": new_booking.user_name
            }
        }
    except Exception as e:
        db.rollback() # Batalkan transaksi jika ada error database
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Terjadi kesalahan pada server. Silakan coba lagi nanti."
        )