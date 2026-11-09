**English** · [Dansk](Step-2-Sqlite3-Lesson-da) · [Bahasa Malaysia](Step-2-Sqlite3-Lesson-ms)

# Step 2: the sqlite3 lesson

In step 1 the books disappear when the server stops. A database keeps them. SQLite is built into Python, so the `sqlite3` module needs no installation. We connect to a file, create a cursor, run SQL commands and commit.

## How to run it

Set up the environment first, see the [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/src/branch/main/README.md).

```bash
python -m library_project.infrastructure.lessons.sqlite3_lesson create
python -m library_project.infrastructure.lessons.sqlite3_lesson insert
python -m library_project.infrastructure.lessons.sqlite3_lesson show
```

## Screenshots

![Screenshot 1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-2-1-sqlite3-create-table.png)

![Screenshot 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-2-2-sqlite3-insert.png)

## What we gained

- A database file is created the first time we connect to it.
- A cursor runs SQL: `CREATE TABLE`, `INSERT` and later `SELECT`.
- A table has typed fields; `PRIMARY KEY`, `NOT NULL` and `UNIQUE` protect the data.
- Changes are only saved after `commit()`.
- A small typo in an SQL string is only found when it runs. SQLAlchemy removes that risk.
