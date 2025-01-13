from pydantic import BaseModel, EmailStr

class Post(BaseModel):
    title: str
    content: str
    published: bool = False

class User(BaseModel):
    email: EmailStr
    password: str