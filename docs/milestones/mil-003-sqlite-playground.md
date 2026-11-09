# G3 SQLite playground

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [e02e021] |

---

## Purpose

Decide whether the SQLite and SQLAlchemy lessons are reproduced correctly as runnable scripts.

## Deliverable

Playground scripts under `src/playground/`: sqlite3 table and insert (`books-collection.db`), SQLAlchemy model and create (`new-books-collection.db`), and the CRUD operations create, read all, read by query, update by query and by primary key, delete by primary key, with tests and screenshots.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | sqlite3 script creates table `books` (id, title unique, author, rating) and inserts Harry Potter | Met | Not met |
| 2 | SQLAlchemy script defines `Book` with the same limits and creates the table in `new-books-collection.db` | Met | Not met |
| 3 | Create, read all, read by query, update by query, update by primary key and delete by primary key each have a passing test | Met | Not met |
| 4 | Playground databases are created in a temporary folder by tests and are ignored by git | Met | Not met |
| 5 | Screenshots for each lesson step are in `docs/images/` | Met | Not met |
| 6 | README documents this step | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | Previous lecture step delivered |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O2 | [BC-001] |
| SC1, SC6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-14 — within the end date 2026-11-20 in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | sqlite3 lesson: connect, cursor, create table, insert | Reproduce steps 1 to 12 with the `sqlite3` module and `books-collection.db`, making the script re-runnable (create table only if it does not exist). Test with a temporary database. | No | O2 |
| 2 | SQLAlchemy lesson: model and create table | Define `Base`, `db`, `Book` with `Mapped` and `mapped_column`, create `new-books-collection.db` in the app context and insert Harry Potter (id 1, rating 9.3). Test with a temporary database. | No | O2 |
| 3 | CRUD with SQLAlchemy: read operations | Implement read all ordered by title and read a single record by title, as in the lesson. Test both. | No | O2 |
| 4 | CRUD with SQLAlchemy: create, update and delete operations | Implement create, update by query, update by primary key and delete by primary key (including `get_or_404` use in the app). Test each. | No | O2 |
| 5 | Capture screenshots of each lesson step (GUI test environment: Docker container with headless browser) | Render the script output and the resulting table contents in a headless browser inside a Docker container and save one screenshot per lesson step. | No | O5, SC6 |
| 6 | Update README for step 2 | Describe the playground scripts, how to run them and add the screenshots. | No | O5 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-002]: ./mil-002-in-memory-library.md
[e02e021]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/commit/e02e021cc1ba355061ecedf65df446c90006a8a6
