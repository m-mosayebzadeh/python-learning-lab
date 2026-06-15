import service.external.coin_gecko_service as gecko_service
from model.enum.crypto_currency import CryptoCurrency
from model.enum.fiat_currency import FiatCurrency

def get_price(fiat : FiatCurrency, crypto: CryptoCurrency):
    return gecko_service.get_price(fiat, crypto)