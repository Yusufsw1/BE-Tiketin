from fastapi import FastAPI
from Config.db import engine, Base
from Routes import booking_routes, movie_routes
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(booking_routes.router)
app.include_router(movie_routes.router)