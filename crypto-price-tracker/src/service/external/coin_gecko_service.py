import requests
from model.enum.crypto_currency import CryptoCurrency
from model.enum.fiat_currency import FiatCurrency
import config
from exception.app_exception import NotFoundException
from model.dto.response.crypto_price_response_dto import CryptoPriceResponse

PRICE_URL = config.GECKO_BASE_URL + "price"

def get_price(fiat: FiatCurrency, crypto: CryptoCurrency) -> CryptoPriceResponse:

    params = {
        "vs_currencies": fiat.value,
        "ids" : crypto.value,
        "x_cg_demo_api_key" : config.GECKO_TOKEN
    }

    response = requests.get(PRICE_URL, params=params)

    response.raise_for_status()

    res = response.json()
    crypto_detail = res.get(crypto.value, None)

    if not crypto_detail:
        raise NotFoundException(f"Cryptocurrency '{crypto.value}' not found")
    
    return CryptoPriceResponse(
        crypto=crypto.value,
        fiat=fiat.value,
        price=crypto_detail.get(fiat.value)
    )
