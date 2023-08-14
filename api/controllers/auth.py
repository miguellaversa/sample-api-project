from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from middleware import get_token, hashing
from models import models


def auth_user(user: models.APIUser, db: Session):
    """Authenticate a user and return an access token.

    Args:
        user: The user to authenticate.
        db: The database session.

    Returns:
        The access token and token type.

    Raises:
        HTTPException: If the username or password is invalid.
    """

    if not user.username or not user.password:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="username and password are required"
        )

    user_in_db = db.query(models.APIUser).filter(models.APIUser.username == user.username).first()

    if not user_in_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Username {user.username} doesn't exist. Unable to login"
        )

    if not hashing.Hash.verify_password(user.password, user_in_db.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid password")

    access_token = get_token.create_access_token(data={"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}