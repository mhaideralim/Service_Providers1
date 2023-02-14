from fastapi import HTTPException, FastAPI

import app.models.service
from app.database import db_connection
from app.models import user_profile


app = FastAPI()
@app.get("/orders")
async def view_provided(users: user_profile.UserProfile):
    if db_connection.profile_data.find_one({"id": users.user_id}):
        return users
    else:
        raise HTTPException(status_code=404, detail="Required data not found")


@app.post("/set_data")
async def set_services(users: user_profile.UserProfile):
    if db_connection.profile_data.find_one({"id": users.user_id}):
        raise HTTPException(status_code=409, detail="Data Already Exists!")
    else:
        db_connection.profile_data.insert_one(users.dict())
        raise HTTPException(status_code=201, detail="Services Stored Successfully.")