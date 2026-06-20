from fastapi import APIRouter, Depends
from model.dto.request.create_membership_dto import CreateMembershipDTO
from sqlalchemy.orm import Session
import service.membership_service as membership_service
from database.session import get_session
from service.security_service import get_current_user
from model.entity.user import User

router = APIRouter(prefix= "/membership", tags=["Memberships"])

@router.get("")
def get_all_membership(session: Session = Depends(get_session)):
    return membership_service.get_all_membership(session)

@router.post("/create")
def create_membership(dto : CreateMembershipDTO, session : Session = Depends(get_session)):
    return membership_service.create_membership(dto, session)

@router.put("/{membership_id}/default")
def set_default_membership(membership_id:int, session : Session = Depends(get_session)):
    membership_service.set_default_membership(membership_id, session)

@router.put("/update/{membership_id}")
def update_membership(membership_id: int, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    membership_service.update_membership(membership_id, session, user)