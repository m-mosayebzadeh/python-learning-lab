from pydantic import BaseModel
from datetime import datetime

class RepositoryResponse(BaseModel):
    name : str
    star_count : int
    forks_count : int
    language : str | None = None
    created_at : datetime
    updated_at : datetime | None = None