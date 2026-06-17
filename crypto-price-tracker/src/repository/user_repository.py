from sqlalchemy.orm import Session
from model.entity.user import User

def find_all_user(session:Session) -> list[User]:
    return session.query(User).all()

def find_user_by_username_or_email(username: str, email : str, session : Session):
    
    return session.query(User).filter(
        (User.username == username) | (User.email == email)
        ).first()   

def find_by_username(username: str, session: Session) -> User:

    return session.query(User).filter(
        User.username == username
    ).first()
    