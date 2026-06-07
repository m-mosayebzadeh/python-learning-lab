from fastapi import APIRouter, Depends
from model.dto.request.user_register_dto import UserRegisterDTO
from sqlalchemy.orm import Session
from database.session import get_session
import service.user_service as user_service

router = APIRouter()


@router.post("/user/register")
def register_user(dto : UserRegisterDTO, session : Session = Depends(get_session)):
    user_service.register_user(dto, session)