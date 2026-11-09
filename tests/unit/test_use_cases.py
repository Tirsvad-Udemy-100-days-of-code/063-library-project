"""@brief Unit tests of the use cases with the in-memory repository."""

import pytest

from library_project.application.use_cases import add_book, list_books
from library_project.domain.errors import InvalidBookError
from library_project.infrastructure.in_memory_books import InMemoryBookRepository


def test_add_book_appends_a_dictionary_to_all_books() -> None:
    repository = InMemoryBookRepository()
    add_book(repository, "Harry Potter", "J. K. Rowling", "9.3")
    assert repository.all_books == [
        {"title": "Harry Potter", "author": "J. K. Rowling", "rating": 9.3}
    ]


def test_add_book_strips_surrounding_spaces() -> None:
    repository = InMemoryBookRepository()
    book = add_book(repository, "  T ", " A  ", "1")
    assert (book.title, book.author) == ("T", "A")


def test_add_book_rejects_rating_that_is_not_a_number() -> None:
    repository = InMemoryBookRepository()
    with pytest.raises(InvalidBookError):
        add_book(repository, "T", "A", "abc")
    assert repository.all_books == []


def test_add_book_rejects_rating_out_of_range() -> None:
    repository = InMemoryBookRepository()
    with pytest.raises(InvalidBookError):
        add_book(repository, "T", "A", "11")
    assert repository.all_books == []


def test_list_books_is_empty_for_a_new_library() -> None:
    assert list_books(InMemoryBookRepository()) == []


def test_list_books_keeps_the_order_of_adding() -> None:
    repository = InMemoryBookRepository()
    add_book(repository, "B", "A", "1")
    add_book(repository, "A", "A", "2")
    assert [book.title for book in list_books(repository)] == ["B", "A"]
