from sqlalchemy.orm import Mapped

from .base import Base


# создали новую модель
class Product(Base):

    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
