"""@brief The storage ports the use cases depend on."""

from typing import Protocol

from library_project.domain.book import Book


class BookRepository(Protocol):
    """@brief Storage that can add books and list them."""

    def add(self, book: Book) -> None:
        """@brief Store a new book.

        @param book The book to store.
        @throws DuplicateTitleError When the title is already stored.
        """
        ...

    def list_all(self) -> list[Book]:
        """@brief Return every stored book in a stable order."""
        ...


class EditableBookRepository(BookRepository, Protocol):
    """@brief Storage that can also change and remove stored books."""

    def get(self, book_id: int) -> Book:
        """@brief Return one stored book.

        @param book_id The identity of the book.
        @throws BookNotFoundError When no book has this identity.
        """
        ...

    def update_rating(self, book_id: int, rating: float) -> Book:
        """@brief Change the rating of one book.

        @param book_id The identity of the book.
        @param rating The new rating.
        @return The changed book.
        @throws BookNotFoundError When no book has this identity.
        """
        ...

    def delete(self, book_id: int) -> None:
        """@brief Remove one book.

        @param book_id The identity of the book.
        @throws BookNotFoundError When no book has this identity.
        """
        ...
