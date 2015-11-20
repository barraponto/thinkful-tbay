from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, Float, String, DateTime
from sqlalchemy.orm import relationship

from database import Base, engine


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)

    # One-to-many relationship between User and Item
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    owner = relationship('User', backref="items")


class Bid(Base):
    __tablename__ = "bids"
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)

    # One-to-many relationship between Item and Bid
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    item = relationship('Item', backref="bid")

    # One-to-many relationship between User and Bid
    bidder_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    bidder = relationship('User', backref="bids")

Base.metadata.create_all(engine)
