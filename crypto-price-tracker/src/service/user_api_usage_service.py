from model.entity.user import User
from sqlalchemy.orm import Session
from datetime import date
import repository.user_api_usage_repository as usage_repository
from model.entity.user_api_usage import UserApiUsage
from fastapi import HTTPException, status

def check_and_increament(user: User, session: Session):

    today = date.today()
    usage = find_by_user_and_date(user.id, today, session)

    if not usage:
        usage = UserApiUsage(user_id= user.id, date = today, call_count = 0)
        usage_repository.save(usage, session)
    
    if usage.call_count >= user.membership.token_limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Daily API limit reached"
        )
    
    usage.call_count += 1
    session.commit()
    
def find_by_user_and_date(user_id: int, date: date, session: Session) -> UserApiUsage:
    return usage_repository.find_by_user_and_date(user_id, date, session)
