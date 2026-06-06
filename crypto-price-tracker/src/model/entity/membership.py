from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

class Membership(Base):
    
    __tablename__ = "memberships"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    token_limit : Mapped[int]
