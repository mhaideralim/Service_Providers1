# Authenticate User and Generate JWT Token
import jwt
from fastapi import Header, HTTPException
import app.core.security
import app.database.db_connection
from app.core import security
from app.database import db_connection
from app.models import authenticate


def authenticate_user(email: str, password: str):
    user = db_connection.service_provider.find_one({"email": email, "password": password})
    if user:
        access_token = jwt.encode({"sub": email}, security.JWT_SECRET, algorithm=security.JWT_ALGORITHM)
        return access_token
    else:
        raise HTTPException(status_code=400, detail="Incorrect username or password")


# Verify JWT Token
def verify_token(x_token: str = Header(None)):
    try:
        decoded_token = jwt.decode(x_token, app.JWT_SECRET, algorithms=[app.JWT_ALGORITHM])
        email = decoded_token["sub"]
        return email
    except jwt.PyJWTError:
        raise HTTPException(status_code=400, detail="Invalid token")


def authenticate_forgot_user(email: str):
    user = db_connection.service_provider.find_one({"email": email})
    if user:
        access_token = jwt.encode({"sub": email}, app.JWT_SECRET, algorithm=app.JWT_ALGORITHM)
        return access_token
    else:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
