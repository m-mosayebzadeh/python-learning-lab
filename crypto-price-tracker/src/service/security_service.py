from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from database.session import get_session
from jose import jwt, JWTError
import service.auth_service as auth_service
import service.user_service as user_service
from model.entity.user import User

# OAuth2PasswordBearer is used for full OAuth2 "Password Flow" authentication.
# This flow is typically used in larger systems where a real OAuth2 authorization server is involved
# and may require additional concepts such as client_id, client_secret, scopes, and external identity providers.
# In this project, authentication is based on a simple JWT Bearer token mechanism, so this OAuth2 flow
# is not fully utilized and is kept only for compatibility with FastAPI's security utilities.

# oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")
# def get_current_user(token: str = Depends(oauth2), session: Session = Depends(get_session)) -> User:


http_bearer = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(http_bearer), session: Session = Depends(get_session)) -> User:

    try:
        token = credentials.credentials
        user_id = auth_service.decode_token(token)

        if not user_id:
            raise HTTPException(
                status_code= status.HTTP_401_UNAUTHORIZED,
                detail= "Invalid token"
            )
         
        user = user_service.get_by_id(user_id, session)

        if not user:
            raise HTTPException(
                status_code= status.HTTP_401_UNAUTHORIZED,
                detail= "Invalid token"
            )
        
        return user

    except JWTError:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Invalid token" 
        )