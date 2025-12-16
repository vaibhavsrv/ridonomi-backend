from fastapi import FastAPI
from app.routes import auth, rides, booking
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ridonomi Backend")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(rides.router, prefix="/rides", tags=["Rides"])
app.include_router(booking.router, prefix="/booking", tags=["Booking"])

@app.get("/")
def root():
    return {"message": "Ridonomi backend is running"}
