from fastapi import HTTPException, FastAPI, APIRouter

import app.models.service
from app.database import db_connection
from app.models import user_profile
from app.models.user_profile import profile_data

router = APIRouter()
@router.get("/get_profile_data")
async def view_user_data(users: user_profile.UserProfile):
    if  profile_data.find_one({"id": users.user_id}):
        return users
    else:
        raise HTTPException(status_code=404, detail="Required data not found")


@router.post("/set_profile_data")
async def set_user_data(users: user_profile.UserProfile):
    if profile_data.find_one({"id": users.user_id}):
        raise HTTPException(status_code=409, detail="Data Already Exists!")
    else:
        profile_data.insert_one(users.dict())
        raise HTTPException(status_code=201, detail="Services Stored Successfully.")