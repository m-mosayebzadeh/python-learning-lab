from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.session import get_session
import service.user_service as user_service
import service.auth_service as auth_service
from model.dto.jwt_token_model import JWTTokenModel

router = APIRouter(prefix= "/auth", tags= ["Auth"])

@router.post(
    path= "/login",
    response_model= JWTTokenModel
)
def login(username: str, password: str, session: Session = Depends(get_session)):

    user = user_service.get_by_username(username, session)

    if not user:
        return HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Invalid credentials"
        )
    
    if not auth_service.verify_password(password, user.password):
        return HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Invalid credentials"
        )
    
    return auth_service.create_access_token(user.id)