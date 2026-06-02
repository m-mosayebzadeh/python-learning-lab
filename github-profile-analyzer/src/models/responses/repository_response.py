from pydantic import BaseModel

class RepositoryResponse(BaseModel):
    name : str
    star_count : int
    forks_count : int
    language : str
    created_at : str
    updated_at : str