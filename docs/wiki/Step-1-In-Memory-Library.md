**English** · [Dansk](Step-1-In-Memory-Library-da) · [Bahasa Malaysia](Step-1-In-Memory-Library-ms)

# Step 1: books in an in-memory list

The first website keeps every book in the list `all_books`. Each book is a dictionary with a title, an author and a rating. The home page shows the books, or the text "Library is empty.", and a link to the page where a book is added.

## How to run it

Set up the environment first, see the [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/src/branch/main/README.md).

```bash
python -m library_project.main_in_memory
```

## Screenshots

![Screenshot 1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-1-1-home.png)

![Screenshot 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-1-2-add-form.png)

![Screenshot 3](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-1-3-add-book.png)

![Screenshot 4](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-1-4-book-list.png)

![Screenshot 5](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-1-5-empty-library.png)

## What we gained

- A Flask route is a Python function with a decorator, and the function name can be used to build links.
- A Jinja template can loop over a list and choose with `if`/`else`, so the empty library has its own message.
- A form sends data with `POST`, and Flask reads it with `request.form`.
- Data kept in a variable is lost when the program stops. That is why we need a database.
