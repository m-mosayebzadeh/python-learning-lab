import service.external.coin_gecko_service as gecko_service
from model.enum.crypto_currency import CryptoCurrency
from model.enum.fiat_currency import FiatCurrency
from model.entity.user import User
import service.user_api_usage_service as user_api_usage_service
from sqlalchemy.orm import Session

def get_price(fiat : FiatCurrency, crypto: CryptoCurrency, user: User, session: Session):
    user_api_usage_service.check_and_increament(user, session)
    price_response = gecko_service.get_price(fiat, crypto)
    return price_response