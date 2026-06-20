import service.external.coin_gecko_service as gecko_service
from model.enum.crypto_currency import CryptoCurrency
from model.enum.fiat_currency import FiatCurrency
from model.entity.user import User
import service.user_api_usage_service as user_api_usage_service
from sqlalchemy.orm import Session
from model.dto.response.crypto_price_response_dto import CryptoPriceResponse

def get_price(fiat : FiatCurrency, crypto: CryptoCurrency, user: User, session: Session) -> CryptoPriceResponse:
    user_api_usage_service.check_and_increament(user, session)
    return gecko_service.get_price(fiat, crypto)