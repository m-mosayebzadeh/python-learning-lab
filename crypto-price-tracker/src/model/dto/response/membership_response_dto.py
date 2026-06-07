from pydantic import BaseModel

class MembershipResponseDTO(BaseModel):
    
    id : int
    name: str
    token_limit : int
    is_default : bool