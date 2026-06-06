from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

class User(Base):
    
    __tablename__ = "users"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str] = mapped_column(String(100))
    email : Mapped[str] = mapped_column(String(255))
    membership_id : Mapped[int] = mapped_column(ForeignKey("memberships.id"))
    membership : Mapped["Membership"] = relationship()