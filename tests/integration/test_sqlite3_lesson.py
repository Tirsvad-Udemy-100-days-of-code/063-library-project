import sqlite3
from pathlib import Path

import pytest

from library_project import constants
from library_project.infrastructure.lessons import sqlite3_lesson


@pytest.fixture
def database(tmp_path: Path) -> Path:
    return tmp_path / "lesson.db"


def _column_info(database: Path) -> dict[str, tuple[str, int]]:
    with sqlite3.connect(database) as connection:
        rows = connection.execute(
            f"PRAGMA table_info({constants.BOOKS_TABLE})"
        ).fetchall()
    connection.close()
    return {row[1]: (row[2].lower(), row[3]) for row in rows}


def test_create_table_defines_the_lesson_columns(database: Path) -> None:
    sqlite3_lesson.create_table(database)

    assert _column_info(database) == {
        "id": ("integer", 0),
        "title": (f"varchar({constants.TITLE_MAX_LENGTH})", 1),
        "author": (f"varchar({constants.AUTHOR_MAX_LENGTH})", 1),
        "rating": ("float", 1),
    }


def test_create_table_is_rerunnable(database: Path) -> None:
    sqlite3_lesson.create_table(database)
    sqlite3_lesson.create_table(database)

    assert "id" in _column_info(database)


def test_duplicate_title_raises_integrity_error(database: Path) -> None:
    sqlite3_lesson.create_table(database)
    insert = (
        f"INSERT INTO {constants.BOOKS_TABLE} (title, author, rating) VALUES (?, ?, ?)"
    )
    with sqlite3.connect(database) as connection:
        connection.execute(insert, ("Same", "A", 1.0))
        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(insert, ("Same", "B", 2.0))
    connection.close()


def test_missing_author_raises_integrity_error(database: Path) -> None:
    sqlite3_lesson.create_table(database)
    with sqlite3.connect(database) as connection:
        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(
                f"INSERT INTO {constants.BOOKS_TABLE} (title, rating) VALUES (?, ?)",
                ("No author", 1.0),
            )
    connection.close()


def test_insert_harry_potter_stores_the_lesson_row(database: Path) -> None:
    sqlite3_lesson.create_table(database)

    sqlite3_lesson.insert_harry_potter(database)

    assert sqlite3_lesson.read_rows(database) == [
        (1, "Harry Potter", "J. K. Rowling", 9.3)
    ]


def test_insert_harry_potter_is_rerunnable(database: Path) -> None:
    sqlite3_lesson.create_table(database)

    sqlite3_lesson.insert_harry_potter(database)
    sqlite3_lesson.insert_harry_potter(database)

    assert len(sqlite3_lesson.read_rows(database)) == 1


def test_read_rows_returns_empty_list_for_empty_table(database: Path) -> None:
    sqlite3_lesson.create_table(database)

    assert sqlite3_lesson.read_rows(database) == []


def test_main_create_then_insert_then_show_prints_the_row(
    database: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    db_arguments = ["--database", str(database)]

    assert sqlite3_lesson.main([*db_arguments, "create"]) == 0
    assert sqlite3_lesson.main([*db_arguments, "insert"]) == 0
    assert sqlite3_lesson.main([*db_arguments, "show"]) == 0

    assert capsys.readouterr().out == "(1, 'Harry Potter', 'J. K. Rowling', 9.3)\n"


def test_main_rejects_unknown_command(database: Path) -> None:
    with pytest.raises(SystemExit):
        sqlite3_lesson.main(["--database", str(database), "drop"])
