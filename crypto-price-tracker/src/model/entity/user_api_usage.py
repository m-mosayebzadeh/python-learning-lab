from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Date
from datetime import date

class UserApiUsage(Base):

    __tablename__ = "user_api_usages"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    date: Mapped[date] = mapped_column(Date)
    call_count: Mapped[int] = mapped_column(default=0)
