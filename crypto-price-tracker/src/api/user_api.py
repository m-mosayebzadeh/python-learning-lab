from fastapi import APIRouter, Depends
from model.dto.request.user_register_dto import UserRegisterDTO
from sqlalchemy.orm import Session
from database.session import get_session
import service.user_service as user_service
from model.dto.response.user_response_dto import UserResponseDTO

router = APIRouter(prefix= "/user", tags= ["User"])

@router.get("/get-all", response_model= list[UserResponseDTO])
def get_all(session: Session = Depends(get_session)):
    return user_service.get_all(session)


@router.post("/register", response_model= UserResponseDTO)
def register_user(dto : UserRegisterDTO, session : Session = Depends(get_session)):
    return user_service.register_user(dto, session)