**English** · [Dansk](Project-Structure-da) · [Bahasa Malaysia](Project-Structure-ms)

# Project structure and tests

The source is split in four layers inside `src/library_project/`:

| Layer | What it holds |
| --- | --- |
| `domain` | The `Book` and its rules (title, author, rating). It imports no framework. |
| `application` | The use cases (add, list, change rating, delete) and the storage port they need. |
| `infrastructure` | The in-memory list `all_books`, the SQLAlchemy `Book` model and repository, and the lesson scripts. |
| `presentation` | The Flask routes `home`, `add`, `edit`, `delete` and the Jinja templates. |

`constants.py` holds every shared constant. `main_in_memory.py` and `main.py` build the two websites. The tests are in `tests/` and are run with `python -m pytest`. The screenshots on these pages are made by `scripts/screenshots/capture_screenshot.sh`, which runs a headless browser in a Docker container, so no window opens on your desktop.

## What we gained

- Business rules do not depend on Flask or on the database, so they are tested without them.
- The assignment's names (`all_books`, `Book`, `db`, `home`, `add`, `edit`, `delete`) are kept where they belong.
- Screenshots can be made again at any time, in the same way, in a container.
