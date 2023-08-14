from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from database import get_db

from schemas import schemas
from controllers import auth

from typing import List


# --------------------------------------------------


router = APIRouter()

@router.post('/login', status_code = status.HTTP_200_OK)
def login(user: schemas.Login, db: Session = Depends(get_db)):
    auth_token = auth.auth_user(user, db)
    return auth_token