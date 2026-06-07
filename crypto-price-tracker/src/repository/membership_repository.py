from sqlalchemy.orm import Session
from model.entity.membership import Membership

def get_all_membership(session: Session) -> list[Membership]:
    return session.query(Membership).all()

def find_by_name(name: str, session: Session):
    return session.query(Membership).filter(Membership.name == name).first()

def find_default_membership(session:Session) -> Membership:
    return session.query(Membership).filter(Membership.is_default == True).first()