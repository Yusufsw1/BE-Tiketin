from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Config.db import get_db
from Controllers import movie_controller

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.get("/")
def get_movies(db: Session = Depends(get_db)):
    return movie_controller.get_all_movies(db)

@router.get("/{movie_id}")
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    return movie_controller.get_movie_by_id(db, movie_id)