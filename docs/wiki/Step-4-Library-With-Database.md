**English** · [Dansk](Step-4-Library-With-Database-da) · [Bahasa Malaysia](Step-4-Library-With-Database-ms)

# Step 4: the library website with a database

Now the website of step 1 stores its books in SQLite. The home page lists every book from the database with an **Edit Rating** link and a **Delete** link. Add, edit and delete all end with a redirect to the home page.

## How to run it

Set up the environment first, see the [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/src/branch/main/README.md).

```bash
python -m library_project.main
```

## Screenshots

![Screenshot 1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-4-1-add-book.png)

![Screenshot 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-4-2-library-list.png)

![Screenshot 3](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-4-3-edit-rating.png)

![Screenshot 4](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-4-4-rating-changed.png)

![Screenshot 5](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-4-5-book-deleted.png)

## What we gained

- The website talks to a repository, so the in-memory list and the database can be swapped without changing the routes.
- The id of a book travels in the address (`/edit?id=3`, `/delete?id=3`).
- After a change we redirect to the home page, so a refresh does not repeat the change.
- A duplicate title is a normal error shown to the reader, and an unknown id gives 404.
- A test starts a second app on the same database file and shows that the books survive a restart.
