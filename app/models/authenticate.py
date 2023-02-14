from pydantic import BaseModel


class Authentication(BaseModel):
    username: str
    email: str
    phone: int
    password: str