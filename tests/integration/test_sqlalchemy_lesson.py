from collections.abc import Iterator
from pathlib import Path

import pytest
from flask import Flask
from sqlalchemy import inspect

from library_project import constants
from library_project.domain.errors import BookNotFoundError
from library_project.infrastructure.lessons import sqlalchemy_lesson as lesson
from library_project.infrastructure.sqlalchemy_models import db

RENAMED_BY_QUERY = constants.LESSON_RENAMED_BY_QUERY_TITLE
RENAMED_BY_KEY = constants.LESSON_RENAMED_BY_KEY_TITLE


def _uri(tmp_path: Path) -> str:
    return f"sqlite:///{tmp_path / 'lesson.db'}"


@pytest.fixture
def app(tmp_path: Path) -> Flask:
    return lesson.create_lesson_app(_uri(tmp_path))


@pytest.fixture
def schema(app: Flask) -> Iterator[None]:
    with app.app_context():
        lesson.create_schema()
        yield
        db.session.remove()


def _add_harry_potter() -> None:
    lesson.create_book(
        constants.LESSON_BOOK_TITLE,
        constants.LESSON_BOOK_AUTHOR,
        constants.LESSON_BOOK_RATING,
        constants.LESSON_BOOK_ID,
    )


@pytest.mark.usefixtures("schema")
def test_create_schema_defines_the_book_columns() -> None:
    columns = {
        column["name"]: column for column in inspect(db.engine).get_columns("books")
    }

    assert list(columns) == ["id", "title", "author", "rating"]
    assert columns["id"]["primary_key"] == 1
    assert [columns[name]["nullable"] for name in ("title", "author", "rating")] == [
        False,
        False,
        False,
    ]
    assert columns["title"]["type"].length == constants.TITLE_MAX_LENGTH
    assert columns["author"]["type"].length == constants.AUTHOR_MAX_LENGTH


@pytest.mark.usefixtures("schema")
def test_create_book_with_id_keeps_the_id() -> None:
    book = lesson.create_book("Dune", "Frank Herbert", 9.0, book_id=7)

    assert book.id == 7


@pytest.mark.usefixtures("schema")
def test_create_book_without_id_assigns_one() -> None:
    book = lesson.create_book("Dune", "Frank Herbert", 9.0)

    assert book.id == 1


@pytest.mark.usefixtures("schema")
def test_read_all_books_orders_by_title() -> None:
    lesson.create_book("Zebra", "A", 1.0)
    lesson.create_book("Apple", "B", 2.0)

    assert [book.title for book in lesson.read_all_books()] == ["Apple", "Zebra"]


@pytest.mark.usefixtures("schema")
def test_read_all_books_returns_empty_list_for_empty_table() -> None:
    assert lesson.read_all_books() == []


@pytest.mark.usefixtures("schema")
def test_read_book_by_title_returns_the_book_when_found() -> None:
    _add_harry_potter()

    book = lesson.read_book_by_title(constants.LESSON_BOOK_TITLE)

    assert book is not None
    assert book.author == constants.LESSON_BOOK_AUTHOR


@pytest.mark.usefixtures("schema")
def test_read_book_by_title_returns_none_when_missing() -> None:
    assert lesson.read_book_by_title("Missing") is None


@pytest.mark.usefixtures("schema")
def test_update_title_by_query_renames_the_book() -> None:
    _add_harry_potter()

    lesson.update_title_by_query(constants.LESSON_BOOK_TITLE, RENAMED_BY_QUERY)

    assert [book.title for book in lesson.read_all_books()] == [RENAMED_BY_QUERY]


@pytest.mark.usefixtures("schema")
def test_update_title_by_query_raises_when_title_missing() -> None:
    with pytest.raises(BookNotFoundError):
        lesson.update_title_by_query("Missing", "Other")


@pytest.mark.usefixtures("schema")
def test_update_title_by_primary_key_renames_the_book() -> None:
    _add_harry_potter()

    lesson.update_title_by_primary_key(constants.LESSON_BOOK_ID, RENAMED_BY_KEY)

    assert [book.title for book in lesson.read_all_books()] == [RENAMED_BY_KEY]


@pytest.mark.usefixtures("schema")
def test_update_title_by_primary_key_raises_when_id_missing() -> None:
    with pytest.raises(BookNotFoundError):
        lesson.update_title_by_primary_key(99, "Other")


@pytest.mark.usefixtures("schema")
def test_delete_by_primary_key_removes_the_book() -> None:
    _add_harry_potter()

    lesson.delete_by_primary_key(constants.LESSON_BOOK_ID)

    assert lesson.read_all_books() == []


@pytest.mark.usefixtures("schema")
def test_delete_by_primary_key_raises_when_id_missing() -> None:
    with pytest.raises(BookNotFoundError):
        lesson.delete_by_primary_key(99)


def _run(tmp_path: Path, command: str) -> int:
    return lesson.main(["--database-uri", _uri(tmp_path), command])


def test_main_create_inserts_harry_potter_once(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    assert _run(tmp_path, "create") == 0
    assert _run(tmp_path, "create") == 0
    _run(tmp_path, "show")

    assert capsys.readouterr().out == "1, Harry Potter, J. K. Rowling, 9.3\n"


def test_main_read_prints_all_books_and_the_one_found_by_title(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    _run(tmp_path, "create")

    _run(tmp_path, "read")

    assert capsys.readouterr().out == (
        "1, Harry Potter, J. K. Rowling, 9.3\n"
        "Found by title: 1, Harry Potter, J. K. Rowling, 9.3\n"
    )


def test_main_update_renames_by_query_then_by_primary_key(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    _run(tmp_path, "create")

    _run(tmp_path, "update")

    assert capsys.readouterr().out == f"1, {RENAMED_BY_KEY}, J. K. Rowling, 9.3\n"


def test_main_delete_prints_remaining_count(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    _run(tmp_path, "create")

    _run(tmp_path, "delete")

    assert capsys.readouterr().out == "Books left: 0\n"


def test_main_show_prints_nothing_for_empty_table(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    _run(tmp_path, "create")
    _run(tmp_path, "delete")
    capsys.readouterr()

    _run(tmp_path, "show")

    assert capsys.readouterr().out == ""
