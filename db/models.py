from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Cabin(Base):
    __tablename__ = "cabins"
    id = Column(Integer, primary_key=True)
    number = Column(Integer, unique=True, nullable=False)
    reservations = relationship("Reservation", back_populates="cabin")


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    cabin_id = Column(Integer, ForeignKey("cabins.id"))
    user_name = Column(String)
    user_email = Column(String)
    user_phone = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    cabin = relationship("Cabin", back_populates="reservations")
