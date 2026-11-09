"""@brief The SQLAlchemy model of the lecture: one ``Book`` table."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from library_project import constants


class Base(DeclarativeBase):
    """@brief Declarative base of the ORM models."""


db = SQLAlchemy(model_class=Base)


class Book(db.Model):
    """@brief A book row of the library."""

    __tablename__ = constants.BOOKS_TABLE

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(
        String(constants.TITLE_MAX_LENGTH), unique=True, nullable=False
    )
    author: Mapped[str] = mapped_column(
        String(constants.AUTHOR_MAX_LENGTH), nullable=False
    )
    rating: Mapped[float] = mapped_column(Float, nullable=False)
