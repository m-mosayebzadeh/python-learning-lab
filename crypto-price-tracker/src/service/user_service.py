import repository.user_repository as user_repository
from model.dto.request.user_register_dto import UserRegisterDTO
from sqlalchemy.orm import Session
from model.entity.user import User
import service.membership_service as membership_service
from model.dto.response.user_response_dto import UserResponseDTO
import service.auth_service as auth_service

def get_all(session : Session) -> list[UserResponseDTO]:
    user_list = user_repository.find_all_user(session)
    return [
        UserResponseDTO(
            username= user.username,
            email= user.email,
            membership= user.membership.name
        ) for user in user_list
    ]

def get_by_username(username: str, session: Session) -> User:
    return user_repository.find_by_username(username, session)

def register_user(dto : UserRegisterDTO, session : Session) -> UserResponseDTO:
    
    user = user_repository.find_user_by_username_or_email(dto.username, dto.email, session)
    
    if user:
        raise ValueError("User already exist")
    
    membership = membership_service.find_default_membership(session)    

    if not membership:
        raise ValueError(
            "No default membership configured"
    )

    user = User(
        username = dto.username,
        email= dto.email,
        password= auth_service.hash_password(dto.password),
        membership = membership
    )
    
    session.add(user)
    session.commit()

    return UserResponseDTO(
        username= user.username,
        email= user.email,
        membership= membership.name
    )
    