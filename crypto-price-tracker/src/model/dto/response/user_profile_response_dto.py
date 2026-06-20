from pydantic import BaseModel

class UserProfileResponse(BaseModel):
    username: str
    email: str
    membership_name: str
    token_limit : int
    remaining_tokens: int