from pydantic import BaseModel, EmailStr, Field

class UserRegisterDTO(BaseModel):
    username : str = Field(min_length=3, max_length=100)
    password : str = Field(min_length=6)
    email : EmailStr