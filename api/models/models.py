from sqlalchemy import Column, Integer, String, Boolean, DateTime 
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

from database import Base


# --------------------------------------------------


class User(Base):
    """Model to create a new user"""
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    addresses = relationship("Address", backref="users")


# --------------------------------------------------


class Address(Base):
    """Model to create a new address"""
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))
    address_1 = Column(String)
    address_2 = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)
    country = Column(String)


# --------------------------------------------------


class APIUser(Base):
    """Model for API users"""
    __tablename__ = 'api_users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String )