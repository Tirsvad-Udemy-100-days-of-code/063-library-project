# G2 In-memory library

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [e02e021] |

---

## Purpose

Decide whether the first lecture step (website with an in-memory list, challenges 1 to 5) works and is documented.

## Deliverable

A Flask app in `src/` with `index.html` and `add.html` templates where books live in the list `all_books`, pytest tests for challenges 1 to 5, and one screenshot per challenge in the README.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | GET `/` returns an `<h1>` "My Library" and a link "Add New Book" to `/add` | Met | Not met |
| 2 | GET `/add` shows a form with title, author and rating fields and an "Add Book" button | Met | Not met |
| 3 | POST `/add` appends `{title, author, rating}` to `all_books` | Met | Not met |
| 4 | Home page lists every book as `<li>` inside `<ul>` | Met | Not met |
| 5 | Home page shows `<p>Library is empty.</p>` when `all_books` is empty | Met | Not met |
| 6 | All tests pass and screenshots for challenges 1 to 5 are in `docs/images/` | Met | Not met |
| 7 | README documents this step | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Project skeleton and tooling |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 | [BC-001] |
| SC1, SC2, SC6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-12 — within the end date 2026-11-20 in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Challenge 1: home page heading and add link | Create the Flask app and `index.html` with `<h1>My Library</h1>` and an `<a>` to `/add`. Test with the Flask test client. | No | O1 |
| 2 | Challenge 2: /add form | Create `add.html` with the title, author and rating form and the "Add Book" button. Test that GET `/add` returns the form. | No | O1 |
| 3 | Challenge 3: store submitted book in all_books | POST `/add` appends a dictionary with title, author and rating to the list `all_books`. Test the data structure. | No | O1 |
| 4 | Challenge 4: list books as ul and li | Render each book of `all_books` as an `<li>` in a `<ul>` on the home page with Jinja. Test the markup. | No | O1 |
| 5 | Challenge 5: empty library message | Show `<p>Library is empty.</p>` when `all_books` is `[]`; the Add New Book link goes to `/add`. Test both branches. | No | O1 |
| 6 | Take step screenshots in Docker (GUI test environment: Docker container with headless browser) | Run the app and a headless browser in a Docker container and write one screenshot per challenge to `docs/images/`, so no host desktop is used (`framework/process/gui-testing.md`). | No | O5, SC6 |
| 7 | Update README for step 1 | Add the step description, run command and screenshots to the README. | No | O5 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-001]: ./mil-001-project-setup.md
[e02e021]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/commit/e02e021cc1ba355061ecedf65df446c90006a8a6
