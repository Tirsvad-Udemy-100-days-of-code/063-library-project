"""@brief Unit tests of the book rules."""

import pytest

from library_project import constants
from library_project.domain.book import Book, parse_rating
from library_project.domain.errors import InvalidBookError


def test_book_is_created_with_valid_data() -> None:
    book = Book("Harry Potter", "J. K. Rowling", 9.3)
    assert (book.title, book.author, book.rating, book.book_id) == (
        "Harry Potter",
        "J. K. Rowling",
        9.3,
        None,
    )


@pytest.mark.parametrize("rating", [constants.RATING_MIN, constants.RATING_MAX])
def test_book_accepts_rating_at_the_limits(rating: float) -> None:
    assert Book("T", "A", rating).rating == rating


@pytest.mark.parametrize(
    "rating", [constants.RATING_MIN - 0.1, constants.RATING_MAX + 0.1]
)
def test_book_rejects_rating_outside_the_limits(rating: float) -> None:
    with pytest.raises(InvalidBookError):
        Book("T", "A", rating)


@pytest.mark.parametrize("title", ["", "   "])
def test_book_rejects_blank_title(title: str) -> None:
    with pytest.raises(InvalidBookError):
        Book(title, "A", 5)


def test_book_rejects_title_longer_than_the_limit() -> None:
    with pytest.raises(InvalidBookError):
        Book("x" * (constants.TITLE_MAX_LENGTH + 1), "A", 5)


def test_book_accepts_title_at_the_limit() -> None:
    assert Book("x" * constants.TITLE_MAX_LENGTH, "A", 5).title


def test_book_rejects_blank_author() -> None:
    with pytest.raises(InvalidBookError):
        Book("T", " ", 5)


def test_book_rejects_author_longer_than_the_limit() -> None:
    with pytest.raises(InvalidBookError):
        Book("T", "x" * (constants.AUTHOR_MAX_LENGTH + 1), 5)


def test_parse_rating_reads_a_decimal_point() -> None:
    assert parse_rating("9.3") == 9.3


def test_parse_rating_reads_a_decimal_comma() -> None:
    assert parse_rating(" 9,3 ") == 9.3


def test_parse_rating_rejects_text_that_is_not_a_number() -> None:
    with pytest.raises(InvalidBookError):
        parse_rating("abc")
