import os
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def verify_token(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    Verify the validity of a JSON Web Token (JWT).

    Args:
        token (str): The JWT token to be verified.

    Raises:
        HTTPException: If the token is invalid or decoding fails.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.PyJWTError as e:
        error = str(e)
        raise HTTPException(status_code=401, detail=f"Invalid token: {error}")
