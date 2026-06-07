import repository.user_repository as user_repository
from model.dto.request.user_register_dto import UserRegisterDTO
from sqlalchemy.orm import Session
from model.entity.user import User


def register_user(dto : UserRegisterDTO, session : Session):
    
    user = user_repository.find_user_by_username_or_email(dto.username, dto.email, session)
    
    if user:
        raise ValueError("User already exist")
    
    user = User(
        username = dto.username,
        email= dto.email,
        password= dto.password,
        #find and set base membership
    )
    
    session.add(user)
    session.commit()
    
    return user
    