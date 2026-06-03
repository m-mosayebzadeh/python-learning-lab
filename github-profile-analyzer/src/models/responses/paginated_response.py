from pydantic import BaseModel

class PaginatedResponse(BaseModel):
    items: list
    page :int
    page_size : int