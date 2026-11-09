# Architecture Decision Record

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0002 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The assignment is a single `main.py` with the list `all_books`, a `Book` model, a `db` object and the route functions of the lecture; S02 compares solutions by those names ([SA-001], CN-004). The Python checklist and the `clean-architecture` skill ask for the layers `domain`, `application`, `infrastructure` and `presentation`, with imports pointing inward. The same site exists in two forms: first with the in-memory list, then with SQLite. Options: (a) one flat `main.py` per step, as in the lecture; (b) layered source where the storage is replaced behind a port, and the assignment names stay where they belong (`all_books` in the in-memory repository, `Book` in the SQLAlchemy model, route functions `home`, `add`, `edit`, `delete` in the presentation layer); (c) layered source with renamed, idiomatic names only.

## Decision

Use option (b): layered packages under `src/library_project/`, a `BookRepository` port in the application layer, an in-memory repository holding `all_books` and a SQLAlchemy repository with the `Book` model in the infrastructure layer, and a Flask application factory with the lecture's route function names in the presentation layer. Constants live in `constants.py`.

## Consequences

**Positive:**

- The step 1 and step 4 sites share templates, routes and tests, and only the repository changes.
- The assignment's names are still found by S02 and the business rules import no framework.

**Negative:**

- More files than the lecture's single `main.py`, which may confuse a beginner; the README and wiki explain the map.
- No Design Class Diagram exists for the classes, because ADR-0001 skips the modelling artifacts; this ADR is the recorded deviation.

## Affected Artifacts

- [BC-001] — objective O4 (project hygiene) and the constraint on the folder structure.
- [SA-001] — concern CN-004 (assignment names) and the conflict between flat names and layers.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
