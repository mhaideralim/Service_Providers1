class UserProfile(BaseModel):
    username: str
    email: str
    phone: int
    password: str
    img: str