import repository.user_repository as user_repository
from model.dto.request.user_register_dto import UserRegisterDTO
from sqlalchemy.orm import Session
from model.entity.user import User
import service.membership_service as membership_service
from model.dto.response.user_response_dto import UserResponseDTO
import service.auth_service as auth_service
from model.entity.membership import Membership
from model.dto.response.user_profile_response_dto import UserProfileResponse
from model.entity.user_api_usage import UserApiUsage
import service.user_api_usage_service as user_api_usage_service
from datetime import date
from fastapi import HTTPException, status

def get_user_profile(session: Session, user: User) -> UserProfileResponse:
    
    membership = user.membership

    usage = user_api_usage_service.find_by_user_and_date(user.id, date.today(), session)
    call_count = usage.call_count if usage else 0

    return UserProfileResponse(
        username= user.username,
        email= user.email,
        membership_name= membership.name,
        token_limit= membership.token_limit,
        remaining_tokens= max(0, membership.token_limit - call_count)
    )


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
    
def get_by_id(user_id: int, session: Session) -> User:
    return session.get(User, user_id)