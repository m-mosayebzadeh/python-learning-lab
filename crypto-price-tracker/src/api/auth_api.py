from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import get_session
import service.user_service as user_service
import service.auth_service as auth_service

router = APIRouter(prefix= "/auth", tags= ["Auth"])

@router.post("/login")
def login(username: str, password: str, session: Session = Depends(get_session)):

    user = user_service.get_by_username(username, session)

    if not user:
        raise ValueError("Invalid credentials")
    
    if not auth_service.verify_password(password, user.password):
        raise ValueError("Invalid credentials")
    
    token = auth_service.create_access_token(user.id)
    return {"access_token": token, "token_type": "bearer"}