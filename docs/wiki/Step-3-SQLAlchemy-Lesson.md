**English** · [Dansk](Step-3-SQLAlchemy-Lesson-da) · [Bahasa Malaysia](Step-3-SQLAlchemy-Lesson-ms)

# Step 3: the SQLAlchemy lesson

SQL text is easy to get wrong, and a typo only shows up when the code runs. SQLAlchemy is an ORM: a table is a Python class, a row is an object and a column is an attribute. The same table `books` is now described by the class `Book`.

## How to run it

Set up the environment first, see the [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/src/branch/main/README.md).

```bash
python -m library_project.infrastructure.lessons.sqlalchemy_lesson create
python -m library_project.infrastructure.lessons.sqlalchemy_lesson read
```

## Screenshots

![Screenshot 1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-3-1-sqlalchemy-create.png)

![Screenshot 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-3-2-sqlalchemy-read.png)

![Screenshot 3](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-3-3-sqlalchemy-update.png)

![Screenshot 4](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-3-4-sqlalchemy-delete.png)

## What we gained

- `db.create_all()` creates the tables from the model, inside the Flask app context.
- Create: `db.session.add()` and `commit()`. Read: `db.select()` with `scalars()` for many rows and `scalar()` for one.
- Update: change the attribute of a loaded object and commit.
- Delete: `db.session.delete()` and commit. A missing id is handled as an error, not as a crash.
