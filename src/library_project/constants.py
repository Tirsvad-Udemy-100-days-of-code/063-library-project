"""@brief Constants shared by every layer of the library project.

Every literal that is used in more than one place lives here, so each piece of
knowledge is defined once.
"""

# Website
APP_TITLE = "My Library"
HOST = "127.0.0.1"
PORT = 5000

ROUTE_HOME = "/"
ROUTE_ADD = "/add"
ROUTE_EDIT = "/edit"
ROUTE_DELETE = "/delete"

LINK_ADD_BOOK = "Add New Book"
BUTTON_ADD_BOOK = "Add Book"
BUTTON_CHANGE_RATING = "Change Rating"
LINK_EDIT_RATING = "Edit Rating"
LINK_DELETE = "Delete"
EMPTY_LIBRARY_MESSAGE = "Library is empty."

# Book rules (the lecture table: title and author varchar(250), rating FLOAT)
TITLE_MAX_LENGTH = 250
AUTHOR_MAX_LENGTH = 250
RATING_MIN = 0.0
RATING_MAX = 10.0

# Databases
SQLITE_LESSON_DATABASE = "books-collection.db"
SQLALCHEMY_LESSON_DATABASE_URI = "sqlite:///new-books-collection.db"
LIBRARY_DATABASE_URI = "sqlite:///books-collection.db"
BOOKS_TABLE = "books"

# Lesson sample data (the Harry Potter row used by both database lessons)
LESSON_BOOK_ID = 1
LESSON_BOOK_TITLE = "Harry Potter"
LESSON_BOOK_AUTHOR = "J. K. Rowling"
LESSON_BOOK_RATING = 9.3
LESSON_RENAMED_BY_QUERY_TITLE = "Harry Potter and the Chamber of Secrets"
LESSON_RENAMED_BY_KEY_TITLE = "Harry Potter and the Goblet of Fire"
