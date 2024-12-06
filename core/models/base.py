from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    # это значит табличка в базе данных не создастся. так как модель абстрактная
    __abstract__ = True

    @declared_attr.directive
    # формируем имя таблицы в базе данных путем бобавления в конец модели буквы "s"
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)
