"""@brief The library website on SQLite, through the composition root."""

from pathlib import Path

import pytest
from flask.testing import FlaskClient

from library_project.main import create_library_app

BOOK_FORM = {"title": "Harry Potter", "author": "J. K. Rowling", "rating": "9.3"}
DUNE_FORM = {"title": "Dune", "author": "Frank Herbert", "rating": "8"}


@pytest.fixture
def database_uri(tmp_path: Path) -> str:
    return f"sqlite:///{tmp_path / 'library.db'}"


@pytest.fixture
def client(database_uri: str) -> FlaskClient:
    return create_library_app(database_uri).test_client()


def test_post_add_redirects_to_home(client: FlaskClient) -> None:
    response = client.post("/add", data=BOOK_FORM)
    assert (response.status_code, response.headers["Location"]) == (302, "/")


def test_post_add_stores_the_book(client: FlaskClient) -> None:
    client.post("/add", data=BOOK_FORM)
    assert "Harry Potter - J. K. Rowling - 9.3/10" in client.get("/").get_data(
        as_text=True
    )


def test_home_lists_books_from_the_database_by_title(client: FlaskClient) -> None:
    client.post("/add", data=BOOK_FORM)
    client.post("/add", data=DUNE_FORM)
    html = client.get("/").get_data(as_text=True)
    assert html.index("Dune") < html.index("Harry Potter")


def test_home_has_edit_rating_and_delete_links(client: FlaskClient) -> None:
    client.post("/add", data=BOOK_FORM)
    html = client.get("/").get_data(as_text=True)
    assert '<a href="/edit?id=1">Edit Rating</a>' in html
    assert '<a href="/delete?id=1">Delete</a>' in html


def test_home_shows_empty_message_for_an_empty_database(client: FlaskClient) -> None:
    assert "<p>Library is empty.</p>" in client.get("/").get_data(as_text=True)


def test_get_edit_shows_the_form(client: FlaskClient) -> None:
    client.post("/add", data=BOOK_FORM)
    response = client.get("/edit?id=1")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "Harry Potter" in html
    assert 'name="rating"' in html


def test_post_edit_updates_the_rating_and_redirects(client: FlaskClient) -> None:
    client.post("/add", data=BOOK_FORM)
    response = client.post("/edit?id=1", data={"rating": "4.5"})
    assert (response.status_code, response.headers["Location"]) == (302, "/")
    assert "4.5/10" in client.get("/").get_data(as_text=True)


def test_post_edit_with_invalid_rating_gives_400(client: FlaskClient) -> None:
    client.post("/add", data=BOOK_FORM)
    response = client.post("/edit?id=1", data={"rating": "abc"})
    assert response.status_code == 400
    assert "9.3/10" in client.get("/").get_data(as_text=True)


def test_get_delete_removes_the_book_and_redirects(client: FlaskClient) -> None:
    client.post("/add", data=BOOK_FORM)
    response = client.get("/delete?id=1")
    assert (response.status_code, response.headers["Location"]) == (302, "/")
    assert "Library is empty." in client.get("/").get_data(as_text=True)


def test_get_edit_with_unknown_id_gives_404(client: FlaskClient) -> None:
    assert client.get("/edit?id=42").status_code == 404


def test_post_edit_with_unknown_id_gives_404(client: FlaskClient) -> None:
    assert client.post("/edit?id=42", data={"rating": "5"}).status_code == 404


def test_delete_with_unknown_id_gives_404(client: FlaskClient) -> None:
    assert client.get("/delete?id=42").status_code == 404


def test_post_add_with_duplicate_title_gives_400_and_a_message(
    client: FlaskClient,
) -> None:
    client.post("/add", data=BOOK_FORM)
    response = client.post("/add", data=BOOK_FORM)
    assert response.status_code == 400
    assert "already in the library" in response.get_data(as_text=True)


def test_book_added_by_one_app_is_listed_by_a_new_app(database_uri: str) -> None:
    create_library_app(database_uri).test_client().post("/add", data=BOOK_FORM)
    second = create_library_app(database_uri).test_client()
    assert "Harry Potter" in second.get("/").get_data(as_text=True)
