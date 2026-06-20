from sqlalchemy.orm import Session
import repository.membership_repository as membership_repository
from model.dto.response.membership_response_dto import MembershipResponseDTO
from model.dto.request.create_membership_dto import CreateMembershipDTO
from model.entity.membership import Membership
from model.entity.user import User
from fastapi import HTTPException, status


def get_all_membership(session: Session) -> list[MembershipResponseDTO]:
    
    memberships = membership_repository.get_all_membership(session)

    return [
        MembershipResponseDTO(
            id = membership.id,
            name= membership.name,
            token_limit= membership.token_limit,
            is_default= membership.is_default
        )
            for membership in memberships
        ]

def create_membership(dto : CreateMembershipDTO, session : Session):
    
    is_exist = membership_repository.find_by_name(dto.name, session)
    
    if is_exist:
        raise ValueError("Membership already exist")
    
    membership = Membership(
        name = dto.name,
        token_limit = dto.token_limit,
        is_default = False
    )
    
    session.add(membership)
    session.commit()
    
    return membership

def set_default_membership(membership_id:int, session : Session):
    
    new_membership = session.get(Membership, membership_id)
    
    if not new_membership:
        raise ValueError("Membership is not valid")
    
    old_default_membership = membership_repository.find_default_membership(session)
    
    if old_default_membership:
        old_default_membership.is_default = False
    
    new_membership.is_default = True
    session.commit()

def find_default_membership(session:Session) -> Membership:
    return membership_repository.find_default_membership(session)

def update_membership(membership_id: int, session: Session, user: User):
        
    if user.membership_id == membership_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You already have this membership"
        )  
    
    new_membership = session.get(Membership, membership_id)

    if not new_membership:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Membership not found"
    )

    old_membership = session.get(Membership, user.membership_id)

    user.membership_id = membership_id
    session.commit()

    is_upgrade = new_membership.token_limit > old_membership.token_limit
    return {"message": f"Membership successfully {'upgraded' if is_upgrade else 'downgraded'} to {new_membership.name}"}
