from sqlalchemy.orm import Session
from Config.db import SessionLocal, engine
from Models.movie_model import Base, Movie, Seat

# Fungsi untuk seeding
def seed_data():
    db = SessionLocal()
    try:
        # 1. Tambahkan Film Contoh
        print("Menanam data film...")
        movie1 = Movie(title="Avengers: Endgame")
        movie2 = Movie(title="Spiderman: No Way Home")
        db.add_all([movie1, movie2])
        
        # 2. Tambahkan Kursi Otomatis (A1-A10, B1-B10, C1-C10)
        print("Menanam data kursi...")
        rows = ['A', 'B', 'C', 'D']
        seats_to_add = []
        for row in rows:
            for i in range(1, 11): # Angka 1 sampai 10
                seat_code = f"{row}{i}"
                new_seat = Seat(seat_code=seat_code)
                seats_to_add.append(new_seat)
        
        db.add_all(seats_to_add)
        
        # Simpan ke Database
        db.commit()
        print("Seeding selesai! Database siap digunakan.")
        
    except Exception as e:
        print(f"Waduh, ada error pas seeding: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()