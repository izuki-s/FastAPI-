from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from . import crud,models,schemas
from .database import SessionLocal,engine
from typing import List

#metadataに記載されているテーブルを作成、接続先はengine
models.Base.metadata.create_all(bind = engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.get("/")
# async def imdex():
#     return {"message":"Success"}

#Read
@app.get("/users",response_model=List[schemas.User]) #schemaのUserクラスのデータをListで返す
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip = skip, limit = limit)
    return users

@app.get("/rooms",response_model=List[schemas.Room]) #schemaのroomクラスのデータをListで返す
async def read_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms = crud.get_rooms(db, skip = skip, limit = limit)
    return rooms

@app.get("/bookings",response_model=List[schemas.Booking]) #schemaのbookingクラスのデータをListで返す
async def read_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = crud.get_bookings(db, skip = skip, limit = limit)
    return bookings

#Create
@app.post("/users",response_model=schemas.User)
async def create_user(user: schemas.UserCreate,db: Session = Depends(get_db)):
    return crud.create_user(db=db,user=user)

@app.post("/rooms",response_model=schemas.Room)
async def create_room(room: schemas.RoomCreate,db: Session = Depends(get_db)):
    return crud.create_room(db=db,room=room)

@app.post("/bookings",response_model=schemas.Booking)
async def create_booking(booking: schemas.BookingCreate,db: Session = Depends(get_db)):
    return crud.create_booking(db=db,booking=booking)