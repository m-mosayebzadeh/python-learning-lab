from pydantic import BaseModel

class LanguageUsageResponse(BaseModel):
    
    language: str
    usage: float