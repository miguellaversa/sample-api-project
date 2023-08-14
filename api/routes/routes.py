from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from enum import Enum

from sqlalchemy.orm import Session
from database import get_db

from middleware import oauth

from schemas import schemas
from controllers import controllers
from models import models



class Tags(Enum):
    users = "Users"
    address = "Address"


router = APIRouter()


# --------------------------------------------------


# User routes
@router.get("/users", tags=[Tags.users])
async def get_users(db: Session=Depends(get_db), current_user: schemas.Token = Depends(oauth.get_current_user)):
    users = db.query(models.User).all()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(users), media_type='application/json')


@router.get("/user/{id}", tags=[Tags.users])
async def get_user(id: str, db: Session=Depends(get_db), current_user: schemas.Token = Depends(oauth.get_current_user)):
    user = controllers.get_user(id, db)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(user), media_type='application/json')


@router.get("/users/{country}", tags=[Tags.users])
async def get_users_by_country(country: str, db: Session=Depends(get_db), current_user: schemas.Token = Depends(oauth.get_current_user)):
    users = db.query(models.User).join(models.Address, models.User.id == models.Address.user_id).filter(models.Address.country == country)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(users), media_type='application/json')


@router.post("/user", tags=[Tags.users])
async def add_user(user: schemas.User, db: Session=Depends(get_db), current_user: schemas.Token = Depends(oauth.get_current_user)):
    controllers.add_user(user, db)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=user.dict(), media_type='application/json')


@router.put("/user/{id}", tags=[Tags.users])
async def update_user(id: str, user: schemas.User, db: Session=Depends(get_db), current_user: schemas.Token = Depends(oauth.get_current_user)):
    controllers.update_user(id, user, db)
    return JSONResponse(status_code=status.HTTP_200_OK, content=user.dict(), media_type='application/json')


@router.delete("/user/{id}", tags=[Tags.users])
async def delete_user(id: str, db: Session=Depends(get_db), current_user: schemas.Token = Depends(oauth.get_current_user)):
    controllers.delete_user(id, db)
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=f'User ID {id} deleted')


# --------------------------------------------------


# Address routes
@router.get("/addresses", tags=[Tags.address])
async def get_addresses(db: Session=Depends(get_db), current_user: schemas.Token = Depends(oauth.get_current_user)):
    addresses = db.query(models.Address).all()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(addresses), media_type='application/json')


@router.get("/address/{user_id}", tags=[Tags.address])
async def get_address(user_id: str, db: Session=Depends(get_db), current_user: schemas.Token = Depends(oauth.get_current_user)):
    address = controllers.get_address(user_id, db)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(address), media_type='application/json')


@router.post("/address", tags=[Tags.address])
async def add_address(address: schemas.Address, db: Session=Depends(get_db), current_user: schemas.Token = Depends(oauth.get_current_user)):
    controllers.add_address(address, db)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=address.dict(), media_type='application/json')


@router.put("/address/{id}", tags=[Tags.address])
async def update_address(id: int, address: schemas.Address, db: Session=Depends(get_db), current_user: schemas.Token = Depends(oauth.get_current_user)):
    controllers.update_address(id, address, db)
    return JSONResponse(status_code=status.HTTP_200_OK, content=address.dict(), media_type='application/json')


@router.delete("/address/{id}", tags=[Tags.address])
async def delete_address(id: int, db: Session=Depends(get_db), current_user: schemas.Token = Depends(oauth.get_current_user)):
    controllers.delete_address(id, db)
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=f'Address ID {id} deleted')