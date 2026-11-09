"""@brief Composition root for lecture step 4 (books in SQLite, full CRUD)."""

from flask import Flask

from library_project import constants
from library_project.infrastructure.sqlalchemy_books import (
    SqlAlchemyBookRepository,
    configure_database,
)
from library_project.presentation.web import create_app


def create_library_app(database_uri: str = constants.LIBRARY_DATABASE_URI) -> Flask:
    """@brief Build the library website on a SQLite database.

    @param database_uri The SQLAlchemy URI of the database.
    @return The configured Flask application.
    """
    app = create_app(SqlAlchemyBookRepository(), editable=True)
    configure_database(app, database_uri)
    return app


def main() -> None:
    """@brief Build the site and serve it."""
    create_library_app().run(host=constants.HOST, port=constants.PORT)


if __name__ == "__main__":
    main()
