from fastapi import HTTPException, FastAPI, APIRouter
from app.database import db_connection
from app.models import service
from app.models.service import service_data

router = APIRouter()
@router.get("/get_services_data")
async def get_provided_services(services: service.Service):
    if  service_data.find_one({"id": services.service_id}):
        return services
    else:
        raise HTTPException(status_code=404, detail="Required data not found")


@router.post("/set_services_data")
async def set_services_data(services: service.Service):
    if  service_data.find_one({"id": services.service_id}):
        raise HTTPException(status_code=409, detail="Data Already Exists!")
    else:
        db_connection.service_provider.insert_one(services.dict())
        raise HTTPException(status_code=201, detail="Services Stored Successfully.")


