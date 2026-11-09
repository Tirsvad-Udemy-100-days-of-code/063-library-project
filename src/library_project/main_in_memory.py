"""@brief Composition root for lecture step 1 (books kept in a list)."""

from library_project import constants
from library_project.infrastructure.in_memory_books import InMemoryBookRepository
from library_project.presentation.web import create_app


def main() -> None:
    """@brief Build the in-memory site and serve it."""
    app = create_app(InMemoryBookRepository())
    app.run(host=constants.HOST, port=constants.PORT)


if __name__ == "__main__":
    main()
