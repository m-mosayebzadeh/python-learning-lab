from fastapi import APIRouter, Depends
from model.dto.request.create_membership_dto import CreateMembershipDTO
from sqlalchemy.orm import Session
import service.membership_service as membership_service
from database.session import get_session

router = APIRouter()

@router.get("/membership")
def get_all_membership(session: Session = Depends(get_session)):
    return membership_service.get_all_membership(session)

@router.post("/membership/create")
def create_membership(dto : CreateMembershipDTO, session : Session = Depends(get_session)):
    return membership_service.create_membership(dto, session)

@router.put("/membership/{membership_id}/default")
def set_default_membership(membership_id:int, session : Session = Depends(get_session)):
    membership_service.set_default_membership(membership_id, session)