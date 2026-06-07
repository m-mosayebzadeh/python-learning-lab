from pydantic import BaseModel, Field

class CreateMembershipDTO(BaseModel):
    
    name: str = Field(min_length=3, max_length=20)
    token_limit : int