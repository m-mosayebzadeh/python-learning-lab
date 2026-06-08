from sqlalchemy.orm import Session
import repository.membership_repository as membership_repository
from model.dto.response.membership_response_dto import MembershipResponseDTO
from model.dto.request.create_membership_dto import CreateMembershipDTO
from model.entity.membership import Membership

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
        
    