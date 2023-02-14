from fastapi import HTTPException, FastAPI, APIRouter

import app.models.service
from app.database import db_connection
from app.models import order
from app.models.order import order_data

router = APIRouter()



async def completed_order_data(order_status: str):
    for status in order_data:
        if order_status == "Completed":
            return status
        else:
            raise HTTPException(status_code=404, detail="No Completed Order yet!")

async def running_order_data(order_status: str):
    for status in order_data:
        if order_status == "Running":
            return status
        else:
            raise HTTPException(status_code=404, detail="No Completed Order yet!")

async def archived_order_data(order_status: str):
    for status in order_data:
        if order_status == "Archived":
            return status
        else:
            raise HTTPException(status_code=404, detail="No Completed Order yet!")

@router.get("/orders")
async def get_order_data(orders: order.Order):
    if order_data.find_one({"id": orders.order_id}):
        return orders
    else:
        raise HTTPException(status_code=404, detail="Required data not found")


@router.post("/set_data")
async def set_order_data(orders: order.Order):
    if order_data.find_one({"id": orders.order_id}):
        raise HTTPException(status_code=409, detail="Data Already Exists!")
    else:
        db_connection.service_provider.insert_one(orders.dict())
        raise HTTPException(status_code=201, detail="Services Stored Successfully.")


@router.delete("/delete_data")
async def set_order_data(orders: order.Order):
    if order_data.find_one({"id": orders.order_id}):
        raise HTTPException(status_code=201, detail="Data Deleted Successfully!")
    else:
        raise HTTPException(status_code=404, detail="Data Not Found.")





