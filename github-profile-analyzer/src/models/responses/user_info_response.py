from pydantic import BaseModel
from datetime import datetime
class UserInfoResponse(BaseModel):
        username: str
        name: str
        bio: str
        followers: int
        following: int
        public_repos: int
        date_of_membership: datetime