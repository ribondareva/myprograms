from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


# создали новую модель
class User(Base):

    username: Mapped[str] = mapped_column(String(32), unique=True)
