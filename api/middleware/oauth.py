from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from middleware import get_token


# --------------------------------------------------


oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    """Get the current user from the token.

    Args:
        token: The token to be decoded.

    Returns:
        The decoded token data.

    Raises:
        HTTPException: If the token is invalid.
    """

    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers = {"WWW-Authenticate": "Bearer"},
    )

    return get_token.verify_token(token, credentials_exception)