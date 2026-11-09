"""@brief The book entity and the rules a book must satisfy."""

from dataclasses import dataclass

from library_project import constants
from library_project.domain.errors import InvalidBookError


def parse_rating(text: str) -> float:
    """@brief Convert the rating typed in a form into a number.

    @param text The text of the rating field, for example "9.3".
    @return The rating as a float.
    @throws InvalidBookError When the text is not a number.
    """
    try:
        return float(text.strip().replace(",", "."))
    except ValueError as error:
        raise InvalidBookError(f"Rating must be a number, not {text!r}.") from error


@dataclass(frozen=True, slots=True)
class Book:
    """@brief A book with a title, an author and a rating.

    @param title The title of the book, 1 to 250 characters.
    @param author The author of the book, 1 to 250 characters.
    @param rating The rating from 0 to 10.
    @param book_id The identity in storage, or None while the book is new.
    """

    title: str
    author: str
    rating: float
    book_id: int | None = None

    def __post_init__(self) -> None:
        """@brief Reject a book that breaks the rules of the library."""
        validate_title(self.title)
        validate_author(self.author)
        validate_rating(self.rating)


def validate_title(title: str) -> None:
    """@brief Check the title rule.

    @param title The title to check.
    @throws InvalidBookError When the title is empty or too long.
    """
    if not title.strip() or len(title) > constants.TITLE_MAX_LENGTH:
        raise InvalidBookError(
            f"Title must have 1 to {constants.TITLE_MAX_LENGTH} characters."
        )


def validate_author(author: str) -> None:
    """@brief Check the author rule.

    @param author The author to check.
    @throws InvalidBookError When the author is empty or too long.
    """
    if not author.strip() or len(author) > constants.AUTHOR_MAX_LENGTH:
        raise InvalidBookError(
            f"Author must have 1 to {constants.AUTHOR_MAX_LENGTH} characters."
        )


def validate_rating(rating: float) -> None:
    """@brief Check the rating rule.

    @param rating The rating to check.
    @throws InvalidBookError When the rating is outside the allowed range.
    """
    if not constants.RATING_MIN <= rating <= constants.RATING_MAX:
        raise InvalidBookError(
            f"Rating must be from {constants.RATING_MIN:g} to {constants.RATING_MAX:g}."
        )
