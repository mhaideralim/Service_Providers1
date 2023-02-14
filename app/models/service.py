from pydantic import BaseModel
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["service_provider"]
service_data = db["services_info"]
class Service(BaseModel):
    service_id: str
    service_name: str
    service_rating: str
    service_rate: str
    service_category: str
    service_desc: str
    service_provider: str
    service_review: str
