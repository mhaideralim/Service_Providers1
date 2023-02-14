from fastapi import FastAPI, HTTPException, Response, Depends
import app.database.db_connection
import app.models.authenticate
import app.routers.routes
from app.database import db_connection
from app.models import authenticate
from app.routers import routes

app = FastAPI()


# Login User
@app.post("/login")
def login(email: str, password: str):
    access_token = routes.authenticate_user(email, password)
    return {"access_token": access_token}


# Protected Route
@app.get("/protected")
def protected(email: str = Depends(routes.verify_token)):
    return {"message": "Welcome to the protected route, {}".format(email)}


@app.post("/register")
async def set_data(user: authenticate.Authentication, response: Response):
    if authenticate.service_provider.find_one({"email":user.email}):
         response.headers["Location"] = "/dashboard"
         raise HTTPException(status_code=409, detail="Email Already Exists!")
    else:
        db_connection.service_provider.insert_one(user.dict())
        raise HTTPException(status_code=201, detail="User Created")


# Reset Password
@app.put("/reset")
def reset_password(user: authenticate.Authentication):
    access_token = routes.authenticate_forgot_user(user.email)
    if authenticate.service_provider.update_one({"email": user.email}, {"$set": {"password": user.password}}):
        return {"access_token": access_token, "message": "Password reset successful"}
    else:
        raise HTTPException(status_code=404, detail="Data Not Found")



