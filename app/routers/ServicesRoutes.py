from fastapi import HTTPException, FastAPI

import app.models.service
from app.database import db_connection
from app.models import service

app = FastAPI()
@app.get("/services")
async def get_provided(services: service.Service):
    if db_connection.service_data.find_one({"id": services.service_id}):
        return services
    else:
        raise HTTPException(status_code=404, detail="Required data not found")


@app.post("/set_data")
async def set_services(services: service.Service):
    if db_connection.service_data.find_one({"id": services.service_id}):
        raise HTTPException(status_code=409, detail="Data Already Exists!")
    else:
        db_connection.service_provider.insert_one(services.dict())
        raise HTTPException(status_code=201, detail="Services Stored Successfully.")