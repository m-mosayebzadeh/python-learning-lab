import requests
from model.enum.crypto_currency import CryptoCurrency
from model.enum.fiat_currency import FiatCurrency

GECKO_TOKEN = "CG-LxLjHqoaJPJwXMCtcR164khA"
GECKO_BASE_URL = "https://api.coingecko.com/api/v3/simple/"
PRICE_URL = GECKO_BASE_URL + "price"


def get_price(fiat: FiatCurrency, crypto: CryptoCurrency):

    params = {
        "vs_currencies": fiat.value,
        "ids" : crypto.value,
        "x_cg_demo_api_key" : GECKO_TOKEN
    }

    response = requests.get(PRICE_URL, params=params)

    response.raise_for_status()

    return response.json()
