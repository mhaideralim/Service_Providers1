# Authenticate User and Generate JWT Token
import jwt
from fastapi import Header, HTTPException, FastAPI, Response
from fastapi.params import Depends


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

app = FastAPI()
@app.post("/login")
def login(email: str, password: str):
    access_token = authenticate_user(email, password)
    return {"access_token": access_token}


# Protected Route
@app.get("/protected")
def protected(email: str = Depends(verify_token)):
    return {"message": "Welcome to the protected route, {}".format(email)}


@app.post("/register")
async def set_data(user: authenticate.Authentication, response: Response):
    if authenticate.service_provider.find_one({"email": user.email}):
        response.headers["Location"] = "/dashboard"
        raise HTTPException(status_code=409, detail="Email Already Exists!")
    else:
        db_connection.service_provider.insert_one(user.dict())
        raise HTTPException(status_code=201, detail="User Created")

    # Reset Password


@app.put("/reset")
def reset_password(user: authenticate.Authentication):
    access_token = authenticate_forgot_user(user.email)
    if authenticate.service_provider.update_one({"email": user.email}, {"$set": {"password": user.password}}):
        return {"access_token": access_token, "message": "Password reset successful"}
    else:
        raise HTTPException(status_code=404, detail="Data Not Found")


