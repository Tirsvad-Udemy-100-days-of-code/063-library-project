"""@brief Challenges 1 to 5 against the Flask site with the in-memory list."""

import pytest
from flask.testing import FlaskClient

from library_project import constants
from library_project.infrastructure.in_memory_books import InMemoryBookRepository
from library_project.presentation.web import create_app

BOOK_FORM = {"title": "Harry Potter", "author": "J. K. Rowling", "rating": "9.3"}


@pytest.fixture
def repository() -> InMemoryBookRepository:
    return InMemoryBookRepository()


@pytest.fixture
def client(repository: InMemoryBookRepository) -> FlaskClient:
    return create_app(repository).test_client()


def test_home_has_the_heading_my_library(client: FlaskClient) -> None:
    assert "<h1>My Library</h1>" in client.get("/").get_data(as_text=True)


def test_home_links_to_the_add_page(client: FlaskClient) -> None:
    html = client.get("/").get_data(as_text=True)
    assert '<a href="/add">Add New Book</a>' in html


def test_add_page_has_the_form_fields(client: FlaskClient) -> None:
    html = client.get("/add").get_data(as_text=True)
    assert 'method="POST"' in html
    for name in ("title", "author", "rating"):
        assert f'name="{name}"' in html


def test_add_page_has_the_add_book_button(client: FlaskClient) -> None:
    assert "Add Book</button>" in client.get("/add").get_data(as_text=True)


def test_add_page_rating_field_is_a_number_with_any_step(
    client: FlaskClient,
) -> None:
    html = client.get("/add").get_data(as_text=True)
    assert 'type="number" step="any" name="rating"' in html


def test_post_add_appends_a_dictionary_to_all_books(
    client: FlaskClient, repository: InMemoryBookRepository
) -> None:
    client.post("/add", data=BOOK_FORM)
    assert repository.all_books == [
        {"title": "Harry Potter", "author": "J. K. Rowling", "rating": 9.3}
    ]


def test_post_add_redirects_to_home(client: FlaskClient) -> None:
    response = client.post("/add", data=BOOK_FORM)
    assert (response.status_code, response.headers["Location"]) == (302, "/")


def test_home_lists_each_book_as_li_inside_ul(client: FlaskClient) -> None:
    client.post("/add", data=BOOK_FORM)
    client.post("/add", data={**BOOK_FORM, "title": "Dune", "rating": "8"})
    html = client.get("/").get_data(as_text=True)
    assert "<ul>" in html
    assert "<li>Harry Potter - J. K. Rowling - 9.3/10</li>" in html
    assert "<li>Dune - J. K. Rowling - 8.0/10</li>" in html


def test_home_shows_empty_message_when_no_books(
    client: FlaskClient, repository: InMemoryBookRepository
) -> None:
    assert repository.all_books == []
    html = client.get("/").get_data(as_text=True)
    assert "<p>Library is empty.</p>" in html
    assert "<ul>" not in html


def test_post_add_with_invalid_rating_gives_400(
    client: FlaskClient, repository: InMemoryBookRepository
) -> None:
    response = client.post("/add", data={**BOOK_FORM, "rating": "abc"})
    assert response.status_code == 400
    assert "Rating must be a number" in response.get_data(as_text=True)
    assert repository.all_books == []


def test_post_add_with_rating_out_of_range_gives_400(client: FlaskClient) -> None:
    response = client.post("/add", data={**BOOK_FORM, "rating": "11"})
    assert response.status_code == 400


@pytest.mark.parametrize("route", [constants.ROUTE_EDIT, constants.ROUTE_DELETE])
def test_edit_and_delete_routes_are_404_when_not_editable(
    client: FlaskClient, route: str
) -> None:
    assert client.get(f"{route}?id=1").status_code == 404
