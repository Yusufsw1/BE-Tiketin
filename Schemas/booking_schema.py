from pydantic import BaseModel, Field

class BookingCreate(BaseModel):
    showtime_id: int = Field(..., gt=0, description="ID Jadwal harus lebih dari 0")
    seat_id: int = Field(..., gt=0)
    user_name: str = Field(..., min_length=3, max_length=50)