"""@brief The Flask delivery mechanism: routes that call the use cases."""

from typing import cast

from flask import Flask, abort, redirect, render_template, request
from werkzeug.wrappers import Response

from library_project import constants
from library_project.application import use_cases
from library_project.application.ports import (
    BookRepository,
    EditableBookRepository,
)
from library_project.domain.errors import (
    BookNotFoundError,
    DuplicateTitleError,
    InvalidBookError,
)

BAD_REQUEST = 400
NOT_FOUND = 404

ADD_TEMPLATE = "add.html"
EDIT_TEMPLATE = "edit_rating.html"
INDEX_TEMPLATE = "index.html"


def create_app(repository: BookRepository, *, editable: bool = False) -> Flask:
    """@brief Build the website around a repository.

    @param repository Where the books are stored.
    @param editable True to also offer the edit and delete routes.
    @return The configured Flask application.
    """
    app = Flask(__name__, template_folder="templates")

    @app.context_processor
    def inject_constants() -> dict[str, object]:
        return {"c": constants, "editable": editable}

    @app.errorhandler(BookNotFoundError)
    def book_not_found(_error: BookNotFoundError) -> tuple[str, int]:
        return "Book not found.", NOT_FOUND

    _register_adding(app, repository)
    if editable:
        # The caller promises an editable repository when it asks for editing.
        _register_editing(app, cast(EditableBookRepository, repository))
    return app


def _register_adding(app: Flask, repository: BookRepository) -> None:
    """@brief Add the home and add routes."""

    @app.get(constants.ROUTE_HOME)
    def home() -> str:
        return render_template(INDEX_TEMPLATE, books=use_cases.list_books(repository))

    @app.route(constants.ROUTE_ADD, methods=["GET", "POST"])
    def add() -> str | Response | tuple[str, int]:
        if request.method == "GET":
            return render_template(ADD_TEMPLATE)
        try:
            use_cases.add_book(
                repository,
                request.form.get("title", ""),
                request.form.get("author", ""),
                request.form.get("rating", ""),
            )
        except (InvalidBookError, DuplicateTitleError) as error:
            return render_template(ADD_TEMPLATE, error=str(error)), BAD_REQUEST
        return redirect(constants.ROUTE_HOME)


def _book_id_from_query() -> int:
    """@brief Read the book id from the query string, or answer 404."""
    book_id = request.args.get("id", type=int)
    if book_id is None:
        abort(NOT_FOUND)
    return book_id


def _register_editing(app: Flask, repository: EditableBookRepository) -> None:
    """@brief Add the edit and delete routes."""

    @app.route(constants.ROUTE_EDIT, methods=["GET", "POST"])
    def edit() -> str | Response | tuple[str, int]:
        book_id = _book_id_from_query()
        book = use_cases.get_book(repository, book_id)
        if request.method == "GET":
            return render_template(EDIT_TEMPLATE, book=book)
        try:
            use_cases.change_rating(repository, book_id, request.form.get("rating", ""))
        except InvalidBookError as error:
            return (
                render_template(EDIT_TEMPLATE, book=book, error=str(error)),
                BAD_REQUEST,
            )
        return redirect(constants.ROUTE_HOME)

    @app.get(constants.ROUTE_DELETE)
    def delete() -> Response:
        use_cases.remove_book(repository, _book_id_from_query())
        return redirect(constants.ROUTE_HOME)
