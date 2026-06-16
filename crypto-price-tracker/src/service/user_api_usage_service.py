from model.entity.user import User
from sqlalchemy.orm import Session
from datetime import date
import repository.user_api_usage_repository as usage_repository
from model.entity.user_api_usage import UserApiUsage

def check_and_increament(user: User, session: Session):

    today = date.today()
    usage = usage_repository.find_by_user_and_date(user.id, today, session)

    if not usage:
        usage = UserApiUsage(user_id= user.id, date = today, call_count = 0)
        usage_repository.save(usage, session)
    
    if usage.call_count >= user.membership.token_limit:
        raise ValueError("Daily API limit reached")
    
    usage.call_count += 1
    session.commit()
    

