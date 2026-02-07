from sqlalchemy import Column, Integer, String, ForeignKey
from config.db import Base

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)

class Seat(Base):
    __tablename__ = "seats"
    id = Column(Integer, primary_key=True, index=True)
    seat_code = Column(String)

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    showtime_id = Column(Integer) # Bisa dikembangkan pakai ForeignKey ke tabel Showtimes
    seat_id = Column(Integer, ForeignKey("seats.id"))
    user_name = Column(String)