import pymongo
from pydantic import BaseModel
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["service_provider"]
order_data = db["orders_data"]
class Order(BaseModel):
    order_id: int
    order_name: str
    delivery_add: str
    datetime: str
    order_type: str
    order_status: str
    payment_method: str
    price: str | None = None
    tax: str | None = None
    total: str | None = None
