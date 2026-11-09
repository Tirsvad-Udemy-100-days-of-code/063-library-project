"""@brief The SQLAlchemy repository against a real SQLite file."""

from collections.abc import Iterator
from pathlib import Path

import pytest
from flask import Flask

from library_project.domain.book import Book
from library_project.domain.errors import BookNotFoundError, DuplicateTitleError
from library_project.infrastructure.sqlalchemy_books import (
    SqlAlchemyBookRepository,
    configure_database,
)
from library_project.infrastructure.sqlalchemy_models import db

HARRY = Book("Harry Potter", "J. K. Rowling", 9.3)
DUNE = Book("Dune", "Frank Herbert", 8.0)
MISSING_ID = 999


@pytest.fixture
def repository(tmp_path: Path) -> Iterator[SqlAlchemyBookRepository]:
    app = Flask(__name__)
    configure_database(app, f"sqlite:///{tmp_path / 'books.db'}")
    with app.app_context():
        yield SqlAlchemyBookRepository()
        db.session.remove()
        db.engine.dispose()


def test_add_stores_the_book_and_assigns_an_id(
    repository: SqlAlchemyBookRepository,
) -> None:
    repository.add(HARRY)
    assert repository.list_all() == [Book("Harry Potter", "J. K. Rowling", 9.3, 1)]


def test_add_raises_on_duplicate_title(repository: SqlAlchemyBookRepository) -> None:
    repository.add(HARRY)
    with pytest.raises(DuplicateTitleError):
        repository.add(HARRY)


def test_add_after_duplicate_still_works(
    repository: SqlAlchemyBookRepository,
) -> None:
    repository.add(HARRY)
    with pytest.raises(DuplicateTitleError):
        repository.add(HARRY)
    repository.add(DUNE)
    assert len(repository.list_all()) == 2


def test_list_all_is_ordered_by_title_with_ids(
    repository: SqlAlchemyBookRepository,
) -> None:
    repository.add(HARRY)
    repository.add(DUNE)
    assert [(b.title, b.book_id) for b in repository.list_all()] == [
        ("Dune", 2),
        ("Harry Potter", 1),
    ]


def test_list_all_is_empty_for_a_new_database(
    repository: SqlAlchemyBookRepository,
) -> None:
    assert repository.list_all() == []


def test_get_returns_the_book_with_its_id(
    repository: SqlAlchemyBookRepository,
) -> None:
    repository.add(HARRY)
    assert repository.get(1) == Book("Harry Potter", "J. K. Rowling", 9.3, 1)


def test_update_rating_changes_the_stored_rating(
    repository: SqlAlchemyBookRepository,
) -> None:
    repository.add(HARRY)
    changed = repository.update_rating(1, 5.0)
    assert changed.rating == 5.0
    assert repository.get(1).rating == 5.0


def test_delete_removes_the_book(repository: SqlAlchemyBookRepository) -> None:
    repository.add(HARRY)
    repository.delete(1)
    assert repository.list_all() == []


def test_get_raises_for_a_missing_id(repository: SqlAlchemyBookRepository) -> None:
    with pytest.raises(BookNotFoundError):
        repository.get(MISSING_ID)


def test_update_rating_raises_for_a_missing_id(
    repository: SqlAlchemyBookRepository,
) -> None:
    with pytest.raises(BookNotFoundError):
        repository.update_rating(MISSING_ID, 5.0)


def test_delete_raises_for_a_missing_id(
    repository: SqlAlchemyBookRepository,
) -> None:
    with pytest.raises(BookNotFoundError):
        repository.delete(MISSING_ID)
