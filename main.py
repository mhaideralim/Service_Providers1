from fastapi import FastAPI, HTTPException, Response, Depends

from app.routers import OrderRoutes, AuthenticationRoutes, ServicesRoutes, ProfileRouters
import uvicorn
import app.routers

app = FastAPI()
app.include_router(OrderRoutes.router)
app.include_router(AuthenticationRoutes.router)
app.include_router(ServicesRoutes.router)
app.include_router(ProfileRouters.router)


# Login User
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)







































