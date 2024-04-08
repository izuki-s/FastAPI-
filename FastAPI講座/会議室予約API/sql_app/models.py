from sqlalchemy import Column,ForeignKey,Integer,String,DateTime
from .database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer,primary_key=True, index=True,comment="ユーザーID")
    user_name = Column(String, unique=True, index = True,comment="ユーザー名")

class Room(Base):
    __tablename__ = "rooms"
    room_id = Column(Integer,primary_key=True, index=True,comment="会議室ID")
    room_name = Column(String, unique=True, index = True,comment="会議室名")
    capacity = Column(Integer,comment="定員")

class Booking(Base):
    __tablename__ = "bookings"
    booking_id = Column(Integer,primary_key=True, index=True,comment="予約ID")
    user_id = Column(Integer,ForeignKey("users.user_id",onupdate="SET NULL"),nullable=False,comment="ユーザーID")
    room_id = Column(Integer,ForeignKey("rooms.room_id",onupdate="SET NULL"),nullable=False,comment="会議室ID")
    reserved_num = Column(Integer,comment="予約人数")
    start_datetime = Column(DateTime,nullable=False,comment="開始時刻")
    end_datetime = Column(DateTime,nullable=False,comment="終了時刻")
    