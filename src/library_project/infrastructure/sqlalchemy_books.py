"""@brief Lecture step 4: books stored in SQLite through Flask-SQLAlchemy."""

from flask import Flask
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from library_project.domain.book import Book as DomainBook
from library_project.domain.errors import BookNotFoundError, DuplicateTitleError
from library_project.infrastructure.sqlalchemy_models import Book as BookRow
from library_project.infrastructure.sqlalchemy_models import db


def _to_domain(row: BookRow) -> DomainBook:
    """@brief Map a table row to the domain book."""
    return DomainBook(row.title, row.author, row.rating, row.id)


class SqlAlchemyBookRepository:
    """@brief Keeps the books in the `books` table.

    Every method needs a Flask application context, which a request provides.
    """

    def add(self, book: DomainBook) -> None:
        """@brief Insert the book.

        @param book The book to store.
        @throws DuplicateTitleError When the title is already stored.
        """
        db.session.add(
            BookRow(title=book.title, author=book.author, rating=book.rating)
        )
        try:
            db.session.commit()
        except IntegrityError as error:
            db.session.rollback()
            raise DuplicateTitleError(
                f"A book titled {book.title!r} is already in the library."
            ) from error

    def list_all(self) -> list[DomainBook]:
        """@brief Return every book ordered by title."""
        rows = db.session.execute(select(BookRow).order_by(BookRow.title)).scalars()
        return [_to_domain(row) for row in rows]

    def get(self, book_id: int) -> DomainBook:
        """@brief Return one book.

        @param book_id The primary key of the book.
        @throws BookNotFoundError When no row has this key.
        """
        return _to_domain(self._row(book_id))

    def update_rating(self, book_id: int, rating: float) -> DomainBook:
        """@brief Change the rating of one book.

        @param book_id The primary key of the book.
        @param rating The new rating.
        @return The changed book.
        @throws BookNotFoundError When no row has this key.
        """
        row = self._row(book_id)
        row.rating = rating
        db.session.commit()
        return _to_domain(row)

    def delete(self, book_id: int) -> None:
        """@brief Remove one book.

        @param book_id The primary key of the book.
        @throws BookNotFoundError When no row has this key.
        """
        db.session.delete(self._row(book_id))
        db.session.commit()

    @staticmethod
    def _row(book_id: int) -> BookRow:
        row = db.session.get(BookRow, book_id)
        if row is None:
            raise BookNotFoundError(f"No book has the id {book_id}.")
        return row


def configure_database(app: Flask, database_uri: str) -> None:
    """@brief Connect the application to a database and create the schema.

    @param app The Flask application.
    @param database_uri The SQLAlchemy URI, for example "sqlite:///books.db".
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    db.init_app(app)
    with app.app_context():
        db.create_all()
