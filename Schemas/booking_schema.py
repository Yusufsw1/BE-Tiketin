from pydantic import BaseModel

class BookingCreate(BaseModel):
    showtime_id: int
    seat_id: int
    user_name: str