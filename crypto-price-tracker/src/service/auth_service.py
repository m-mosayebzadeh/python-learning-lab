from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt
import config
from model.dto.jwt_token_model import JWTTokenModel

password_context = CryptContext(schemes=["bcrypt"])

def hash_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(plain_password: str, hashed_password) -> bool:
    return password_context.verify(plain_password, hashed_password)

def create_access_token(user_id: int) -> JWTTokenModel:

    expire = datetime.now(timezone.utc) + timedelta(minutes=config.JWT_EXPIRE_MINUTES)
    payload = {"sub": str(user_id), "exp": expire}
    token = jwt.encode(payload, config.SECRET_KEY, config.JWT_ALGORITHM)
    
    return JWTTokenModel(
        access_token=token,
        token_type=config.JWT_TOKEN_TYPE,
        expires_in=(config.JWT_EXPIRE_MINUTES * 60)
    )

def decode_token(token: str) -> int:

    payload = jwt.decode(token, config.SECRET_KEY, config.JWT_ALGORITHM)
    return int(payload["sub"])
