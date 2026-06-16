from model.entity.user_api_usage import UserApiUsage
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

def save(usage: UserApiUsage, session: Session) -> UserApiUsage:

    session.add(usage)
    session.commit()
    session.refresh(usage)
    return usage

def find_by_user_and_date(user_id: int, date: date, session: Session) -> Optional[UserApiUsage]:

    return session.query(UserApiUsage).filter(
        UserApiUsage.user_id == user_id,
        UserApiUsage.date == date
    ).first()