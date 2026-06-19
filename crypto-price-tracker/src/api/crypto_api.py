from fastapi import APIRouter, Depends
import service.crypto_service as crypto_service
from model.enum.crypto_currency import CryptoCurrency
from model.enum.fiat_currency import FiatCurrency
from service.security_service import get_current_user
from model.entity.user import User
from sqlalchemy.orm import Session
from database.session import get_session

router = APIRouter(prefix="/crypto", tags=["Crypto"])

@router.get("/price")
def get_price(fiat : FiatCurrency, crypto: CryptoCurrency, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    return crypto_service.get_price(fiat, crypto, user, session)