from fastapi import HTTPException, FastAPI

import app.models.service
from app.database import db_connection
from app.models import order


app = FastAPI()
@app.get("/orders")
async def view_provided(orders: order.Order):
    if db_connection.service_data.find_one({"id": orders.order_id}):
        return orders
    else:
        raise HTTPException(status_code=404, detail="Required data not found")


@app.post("/set_data")
async def set_services(orders: order.Order):
    if db_connection.service_data.find_one({"id": orders.order_id}):
        raise HTTPException(status_code=409, detail="Data Already Exists!")
    else:
        db_connection.service_provider.insert_one(orders.dict())
        raise HTTPException(status_code=201, detail="Services Stored Successfully.")