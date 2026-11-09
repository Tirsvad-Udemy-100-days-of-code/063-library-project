# G1 Project setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [e02e021] |

---

## Purpose

Decide whether the project skeleton and tooling are ready for feature work.

## Deliverable

A Python 3.13 project with `pyproject.toml`, `src/` and `tests/`, `constants.py`, `.gitignore`, a Doxyfile, a README with venv and run instructions, ADRs for the early decisions, and the repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pip install -e .[dev]` succeeds in a fresh `.venv` on Python 3.13 | Met | Not met |
| 2 | `python -m pytest` runs and passes (smoke test) | Met | Not met |
| 3 | `pyproject.toml` declares `requires-python >=3.13` and only Flask and Flask-SQLAlchemy as runtime dependencies | Met | Not met |
| 4 | `.gitignore` excludes `.venv`, `__pycache__`, `*.db` and `.env` | Met | Not met |
| 5 | `Doxyfile` exists and `constants.py` holds the shared constants | Met | Not met |
| 6 | README follows the framework template and `check-readme.sh` passes | Met | Not met |
| 7 | Repository description and topics are set on the git host | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First phase |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O4, O6 | [BC-001] |
| SC4, SC7 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-10 — within the end date 2026-11-20 in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create pyproject.toml and project layout | Add `pyproject.toml` (Python >=3.13, Flask and Flask-SQLAlchemy runtime dependencies, pytest as the `dev` extra, pytest configuration), the `src/` and `tests/` folders and `src/constants.py`, so every later step has a home and the dependencies stay minimal for S03. | No | O4 |
| 2 | Add Python .gitignore | Add the standard Python `.gitignore` plus `.env`, `*.db` and `docs/images` exceptions, so tokens, virtual environments and local databases never reach the repository. | No | O4 |
| 3 | Add Doxyfile and Doxygen comment convention | Add a `Doxyfile` that reads `src/` and document the Doxygen comment style used in source files (`@brief`, `@param`, `@return`), so S02 can generate API docs. | No | O4 |
| 4 | Write README skeleton with venv and test instructions | Create `README.md` from the framework template: how to create and use `.venv`, run `python -m pip install --upgrade pip`, install, run the app and run the tests. Screenshots are added per later milestone. | No | O4, O5 |
| 5 | Record early decisions as ADRs | ADR-0001 records that use cases and user stories are not modelled for this lesson project; ADR-0002 records the source layout that keeps the assignment names (`all_books`, `Book`, `db`, route functions) in the web layer. Review follows the ADR checklist. | No | O4 |
| 6 | Add pytest smoke test | Add a first test under `tests/` that imports `constants`, so the test run and Python 3.13 requirement are verified from the first pull request. | No | SC1 |
| 7 | Set repository description and topics | Using the token in `.env` (read in the shell only, never printed, committed or imported) set the Gitea repository description and topics through the API, so S03 sees a clear summary. | No | O6 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[e02e021]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/commit/e02e021cc1ba355061ecedf65df446c90006a8a6
