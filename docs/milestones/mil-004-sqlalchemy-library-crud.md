# G4 Library with CRUD

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [e02e021] |

---

## Purpose

Decide whether the final library website with persistent storage and full CRUD works.

## Deliverable

The website of MIL-002 stored in SQLite through Flask-SQLAlchemy: add redirects to the home page, home lists all books from the database, an Edit Rating page and a Delete link, with tests including persistence across app restarts, and screenshots.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | POST `/add` stores the book in the database and redirects to `/` | Met | Not met |
| 2 | Home page lists all books from the database, each with an Edit Rating and a Delete link | Met | Not met |
| 3 | Edit Rating page for a book id shows the form; POST updates the rating and redirects to `/` | Met | Not met |
| 4 | Delete link removes the book and redirects to `/`; unknown ids return 404 | Met | Not met |
| 5 | A book added with one app instance is listed by a new instance on the same database file | Met | Not met |
| 6 | All tests pass and screenshots for each step are in `docs/images/` | Met | Not met |
| 7 | README documents this step | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] | Database lessons reproduced and reused |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O3 | [BC-001] |
| SC2, SC3, SC6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-17 — within the end date 2026-11-20 in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Persist books with Flask-SQLAlchemy | Replace the in-memory list by the `Book` model on SQLite, create the schema at start-up and keep the database path in `constants.py`. Test with a temporary database. | No | O3 |
| 2 | Add route stores book and redirects home | POST `/add` creates a `Book`, commits and redirects to the home page; duplicate titles are handled without a server error. Test the redirect and the stored row. | No | O3 |
| 3 | Home page shows all books from the database | Query all books ordered by title and render them with their rating and the Edit Rating and Delete links, or the empty message. Test with several books. | No | O3 |
| 4 | Edit rating page and update | Add `/edit?id=` with an `edit_rating.html` form; POST updates the rating of that book and redirects home. Test valid and unknown ids. | No | O3 |
| 5 | Delete route | Add `/delete?id=` that deletes the book by primary key and redirects home. Test delete and unknown id. | No | O3 |
| 6 | Persistence test across restarts | Create the app twice on one database file and check that books added by the first are listed by the second, covering SC3. | No | SC3 |
| 7 | Take step screenshots in Docker (GUI test environment: Docker container with headless browser) | Capture add, list, edit rating and delete screens with a headless browser in a Docker container, writing files to `docs/images/`. | No | O5, SC6 |
| 8 | Update README for step 3 | Describe the final website, how to run it, and add the screenshots. | No | O5 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-003]: ./mil-003-sqlite-playground.md
[e02e021]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/commit/e02e021cc1ba355061ecedf65df446c90006a8a6
