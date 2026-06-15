from fastapi import APIRouter
import service.crypto_service as crypto_service
from model.enum.crypto_currency import CryptoCurrency
from model.enum.fiat_currency import FiatCurrency

router = APIRouter()

@router.get("/crypto/price")
def get_price(fiat : FiatCurrency, crypto: CryptoCurrency):
    return crypto_service.get_price(fiat, crypto)