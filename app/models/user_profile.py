import pymongo
from pydantic import BaseModel
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["service_provider"]
profile_data = db["orders_data"]

class UserProfile(BaseModel):
    username: str
    email: str
    phone: int
    password: str
    img: str