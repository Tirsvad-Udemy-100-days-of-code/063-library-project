"""@brief The raw sqlite3 lesson: create the books table and insert a row.

Run with ``python -m library_project.infrastructure.lessons.sqlite3_lesson create``.
"""

import argparse
import sqlite3
import sys
from collections.abc import Sequence
from contextlib import closing
from pathlib import Path

from library_project import constants

type BookRow = tuple[int, str, str, float]

COMMAND_CREATE = "create"
COMMAND_INSERT = "insert"
COMMAND_SHOW = "show"

CREATE_TABLE_SQL = (
    f"CREATE TABLE IF NOT EXISTS {constants.BOOKS_TABLE} ("
    "id INTEGER PRIMARY KEY, "
    f"title varchar({constants.TITLE_MAX_LENGTH}) NOT NULL UNIQUE, "
    f"author varchar({constants.AUTHOR_MAX_LENGTH}) NOT NULL, "
    "rating FLOAT NOT NULL)"
)
INSERT_BOOK_SQL = (
    f"INSERT OR IGNORE INTO {constants.BOOKS_TABLE} "
    "(id, title, author, rating) VALUES (?, ?, ?, ?)"
)
SELECT_BOOKS_SQL = (
    f"SELECT id, title, author, rating FROM {constants.BOOKS_TABLE} ORDER BY id"
)


def create_table(database: str | Path = constants.SQLITE_LESSON_DATABASE) -> None:
    """@brief Create the books table when it does not exist yet."""
    with closing(sqlite3.connect(database)) as connection:
        cursor = connection.cursor()
        # constant SQL built from project constants, no user input
        # nosemgrep: opengrep.rules.python.sqlalchemy.security.sqlalchemy-execute-raw-query  # noqa: E501
        cursor.execute(CREATE_TABLE_SQL)
        connection.commit()


def insert_harry_potter(
    database: str | Path = constants.SQLITE_LESSON_DATABASE,
) -> None:
    """@brief Insert the lesson book; a second run leaves the table unchanged."""
    with closing(sqlite3.connect(database)) as connection:
        cursor = connection.cursor()
        # constant SQL with bound parameters, no user input
        # nosemgrep: opengrep.rules.python.sqlalchemy.security.sqlalchemy-execute-raw-query  # noqa: E501
        cursor.execute(
            INSERT_BOOK_SQL,
            (
                constants.LESSON_BOOK_ID,
                constants.LESSON_BOOK_TITLE,
                constants.LESSON_BOOK_AUTHOR,
                constants.LESSON_BOOK_RATING,
            ),
        )
        connection.commit()


def read_rows(database: str | Path = constants.SQLITE_LESSON_DATABASE) -> list[BookRow]:
    """@brief Return every row of the books table ordered by id."""
    with closing(sqlite3.connect(database)) as connection:
        cursor = connection.cursor()
        # constant SQL built from project constants, no user input
        # nosemgrep: opengrep.rules.python.sqlalchemy.security.sqlalchemy-execute-raw-query  # noqa: E501
        cursor.execute(SELECT_BOOKS_SQL)
        return [(row[0], row[1], row[2], row[3]) for row in cursor.fetchall()]


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Day 63 sqlite3 lesson")
    parser.add_argument(
        "--database",
        default=constants.SQLITE_LESSON_DATABASE,
        help="path of the SQLite database file",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser(COMMAND_CREATE, help="create the books table")
    commands.add_parser(COMMAND_INSERT, help="insert Harry Potter")
    commands.add_parser(COMMAND_SHOW, help="print all rows")
    return parser


def _show(database: str) -> None:
    for row in read_rows(database):
        sys.stdout.write(f"{row}\n")


def main(argv: Sequence[str] | None = None) -> int:
    """@brief Run the lesson sub-command named in ``argv``."""
    arguments = _build_parser().parse_args(argv)
    database: str = arguments.database
    if arguments.command == COMMAND_CREATE:
        create_table(database)
    elif arguments.command == COMMAND_INSERT:
        insert_harry_potter(database)
    else:
        _show(database)
    return 0


if __name__ == "__main__":
    sys.exit(main())
