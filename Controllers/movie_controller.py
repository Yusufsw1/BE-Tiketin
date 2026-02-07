from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.movie_model import Movie

def get_all_movies(db: Session):
    movies = db.query(Movie).all()
    # Opsional: Jika database benar-benar kosong, kamu bisa kasih info
    return movies

def get_movie_by_id(db: Session, movie_id: int):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    
    # VALIDASI: Jika film tidak ditemukan
    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Film dengan ID {movie_id} tidak ditemukan. Mungkin sudah tidak tayang."
        )
    
    return movie