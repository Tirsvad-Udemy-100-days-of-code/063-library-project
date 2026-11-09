"""@brief The things a reader can do with the library."""

from library_project.application.ports import BookRepository, EditableBookRepository
from library_project.domain.book import Book, parse_rating, validate_rating


def add_book(
    repository: BookRepository, title: str, author: str, rating_text: str
) -> Book:
    """@brief Add a new book to the library.

    @param repository Where the book is stored.
    @param title The title typed by the reader.
    @param author The author typed by the reader.
    @param rating_text The rating typed by the reader, as text.
    @return The book that was added.
    @throws InvalidBookError When the data breaks a rule of the library.
    """
    book = Book(title.strip(), author.strip(), parse_rating(rating_text))
    repository.add(book)
    return book


def list_books(repository: BookRepository) -> list[Book]:
    """@brief Return every book of the library.

    @param repository Where the books are stored.
    @return The books in the order the storage lists them.
    """
    return repository.list_all()


def get_book(repository: EditableBookRepository, book_id: int) -> Book:
    """@brief Return one book.

    @param repository Where the books are stored.
    @param book_id The identity of the book.
    @throws BookNotFoundError When no book has this identity.
    """
    return repository.get(book_id)


def change_rating(
    repository: EditableBookRepository, book_id: int, rating_text: str
) -> Book:
    """@brief Give a book a new rating.

    @param repository Where the books are stored.
    @param book_id The identity of the book.
    @param rating_text The new rating, as text.
    @return The changed book.
    @throws InvalidBookError When the rating is not allowed.
    @throws BookNotFoundError When no book has this identity.
    """
    rating = parse_rating(rating_text)
    validate_rating(rating)
    return repository.update_rating(book_id, rating)


def remove_book(repository: EditableBookRepository, book_id: int) -> None:
    """@brief Delete a book from the library.

    @param repository Where the books are stored.
    @param book_id The identity of the book.
    @throws BookNotFoundError When no book has this identity.
    """
    repository.delete(book_id)
