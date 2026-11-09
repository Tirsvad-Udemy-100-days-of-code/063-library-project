"""@brief Errors raised by the library rules."""


class InvalidBookError(ValueError):
    """@brief The data of a book breaks a rule of the library."""


class BookNotFoundError(LookupError):
    """@brief No book has the requested identity."""


class DuplicateTitleError(ValueError):
    """@brief A book with the same title is already in the library."""
