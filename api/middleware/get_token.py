from schemas import schemas

from jose import JWTError, jwt
from datetime import datetime, timedelta


# --------------------------------------------------


SECRET_KEY = "67d5b3918b802164464535c85d1783743f55147d89e36d31597a9a33530e8238"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120


def create_access_token(data: dict):
    """Create an access token.

    Args:
        data: The data to be encoded in the token.

    Returns:
        The encoded token.
    """

    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_token(token: str, credentials_exception):
    """Verify an access token.

    Args:
        token: The token to be verified.
        credentials_exception: The exception to be raised if the token is invalid.

    Returns:
        The decoded token data.

    Raises:
        credentials_exception: If the token is invalid.
    """

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username = username)

        return True

    except JWTError:
        raise credentials_exception