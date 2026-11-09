"""@brief Lecture step 1: books kept in a plain Python list."""

from library_project.domain.book import Book


class InMemoryBookRepository:
    """@brief Keeps the books in the list `all_books`, as the lecture does.

    Every book is a dictionary with the keys "title", "author" and "rating".
    The data is lost when the program stops, which is the point of the lesson.
    """

    def __init__(self) -> None:
        """@brief Start with an empty library."""
        self.all_books: list[dict[str, str | float]] = []

    def add(self, book: Book) -> None:
        """@brief Append the book as a dictionary to `all_books`.

        @param book The book to store.
        """
        self.all_books.append(
            {"title": book.title, "author": book.author, "rating": book.rating}
        )

    def list_all(self) -> list[Book]:
        """@brief Return the books in the order they were added."""
        return [
            Book(str(entry["title"]), str(entry["author"]), float(entry["rating"]))
            for entry in self.all_books
        ]
