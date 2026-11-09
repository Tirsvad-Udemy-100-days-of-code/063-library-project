"""@brief The SQLAlchemy lesson: model, create table and CRUD operations.

Run with ``python -m library_project.infrastructure.lessons.sqlalchemy_lesson create``.
The data functions must be called inside ``app.app_context()``.
"""

import argparse
import sys
from collections.abc import Callable, Sequence

from flask import Flask

from library_project import constants
from library_project.domain.errors import BookNotFoundError
from library_project.infrastructure.sqlalchemy_models import Book, db

COMMAND_CREATE = "create"
COMMAND_READ = "read"
COMMAND_UPDATE = "update"
COMMAND_DELETE = "delete"
COMMAND_SHOW = "show"


def create_lesson_app(
    database_uri: str = constants.SQLALCHEMY_LESSON_DATABASE_URI,
) -> Flask:
    """@brief Build a Flask app bound to the database at ``database_uri``."""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    db.init_app(app)
    return app


def create_schema() -> None:
    """@brief Create the tables of all models that do not exist yet."""
    db.create_all()


def create_book(
    title: str, author: str, rating: float, book_id: int | None = None
) -> Book:
    """@brief Insert a book; the database picks the id when ``book_id`` is None."""
    book = Book(id=book_id, title=title, author=author, rating=rating)
    db.session.add(book)
    db.session.commit()
    return book


def read_all_books() -> list[Book]:
    """@brief Return every book ordered by title."""
    return list(db.session.execute(db.select(Book).order_by(Book.title)).scalars())


def read_book_by_title(title: str) -> Book | None:
    """@brief Return the book with ``title`` or None."""
    return db.session.execute(db.select(Book).where(Book.title == title)).scalar()


def _get_book_or_raise(book_id: int) -> Book:
    book = db.session.get(Book, book_id)
    if book is None:
        raise BookNotFoundError(f"No book with id {book_id}")
    return book


def update_title_by_query(old_title: str, new_title: str) -> None:
    """@brief Rename the book found by its title."""
    book = read_book_by_title(old_title)
    if book is None:
        raise BookNotFoundError(f"No book with title {old_title!r}")
    book.title = new_title
    db.session.commit()


def update_title_by_primary_key(book_id: int, new_title: str) -> None:
    """@brief Rename the book found by its primary key."""
    book = _get_book_or_raise(book_id)
    book.title = new_title
    db.session.commit()


def delete_by_primary_key(book_id: int) -> None:
    """@brief Delete the book found by its primary key."""
    book = _get_book_or_raise(book_id)
    db.session.delete(book)
    db.session.commit()


def _write_book(book: Book) -> None:
    sys.stdout.write(f"{book.id}, {book.title}, {book.author}, {book.rating}\n")


def _run_create() -> None:
    create_schema()
    if db.session.get(Book, constants.LESSON_BOOK_ID) is None:
        create_book(
            constants.LESSON_BOOK_TITLE,
            constants.LESSON_BOOK_AUTHOR,
            constants.LESSON_BOOK_RATING,
            constants.LESSON_BOOK_ID,
        )


def _run_show() -> None:
    for book in read_all_books():
        _write_book(book)


def _run_read() -> None:
    _run_show()
    found = read_book_by_title(constants.LESSON_BOOK_TITLE)
    if found is not None:
        sys.stdout.write("Found by title: ")
        _write_book(found)


def _run_update() -> None:
    update_title_by_query(
        constants.LESSON_BOOK_TITLE, constants.LESSON_RENAMED_BY_QUERY_TITLE
    )
    update_title_by_primary_key(
        constants.LESSON_BOOK_ID, constants.LESSON_RENAMED_BY_KEY_TITLE
    )
    _run_show()


def _run_delete() -> None:
    delete_by_primary_key(constants.LESSON_BOOK_ID)
    sys.stdout.write(f"Books left: {len(read_all_books())}\n")


COMMANDS: dict[str, Callable[[], None]] = {
    COMMAND_CREATE: _run_create,
    COMMAND_READ: _run_read,
    COMMAND_UPDATE: _run_update,
    COMMAND_DELETE: _run_delete,
    COMMAND_SHOW: _run_show,
}


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Day 63 SQLAlchemy lesson")
    parser.add_argument(
        "--database-uri",
        default=constants.SQLALCHEMY_LESSON_DATABASE_URI,
        help="SQLAlchemy URI of the database",
    )
    parser.add_argument("command", choices=list(COMMANDS))
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """@brief Run the lesson sub-command named in ``argv``."""
    arguments = _build_parser().parse_args(argv)
    app = create_lesson_app(arguments.database_uri)
    with app.app_context():
        COMMANDS[arguments.command]()
    return 0


if __name__ == "__main__":
    sys.exit(main())
