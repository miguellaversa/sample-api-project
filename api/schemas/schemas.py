from pydantic import BaseModel
from typing import Optional, List, Union


# --------------------------------------------------


class Address(BaseModel):
    address_1: str
    address_2: Optional[str]
    city: str
    state: str
    zip: str
    country: str


# --------------------------------------------------


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    addresses: Optional[List[Address]] = []


# --------------------------------------------------


class Login(BaseModel):
    username: str 
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None