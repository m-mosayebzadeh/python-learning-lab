from pydantic import BaseModel

class CryptoPriceResponse(BaseModel):
    crypto: str
    fiat: str
    price: float