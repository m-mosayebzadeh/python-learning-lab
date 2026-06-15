from pydantic import BaseModel

class UserResponseDTO(BaseModel):
    username : str
    email : str
    membership : str