# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added CrossReference to SA-001 | pending |

---

## Executive Summary

Day 63 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" asks the participant to build a virtual bookshelf: first a Flask site that keeps books in an in-memory list, then the same site backed by an SQLite database through SQLAlchemy, with create, read, update and delete (CRUD). This project delivers that assignment as a clean, runnable, documented Python 3.13 repository with tests, a README and a three-language wiki (English, Danish, Bahasa Malaysia) that shows a screenshot and the learning gained at each lecture step.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/` (plan first, review every artifact against its QC checklist, ISO/IEC 25010:2023 characteristics on every criterion). Code follows the `coding-conventions` and `clean-architecture` skills and is documented with Doxygen comments. Tests use pytest. GUI screenshots are taken in a Docker container, never on the host desktop (`framework/process/gui-testing.md`).

## Problem Statement

A course participant who follows the lecture ends with scattered snippets, a starting zip and gists, and no single repository that is tested, documented and easy to share. Other participants comparing solutions cannot see what each lecture step changed or what it taught.

## Business Opportunity

A single repository that mirrors the lecture steps lets the participant keep a reference portfolio, lets other course participants compare solutions, and lets GitHub visitors browse a small, well-structured Flask and SQLAlchemy example.

## Objectives

- O1: Deliver the website of challenges 1 to 5 with the in-memory list `all_books` (home page, `/add` form, list, empty message).
- O2: Reproduce the SQLite and SQLAlchemy lessons (sqlite3 table and insert, SQLAlchemy model, create, read, update, delete) as runnable scripts.
- O3: Deliver the final library website with a persistent SQLite database: add, list, edit rating and delete.
- O4: Provide Python project hygiene: Python 3.13 or newer, venv, pytest, `pyproject.toml`, `constants.py`, `.gitignore`, Doxygen comments and a Doxyfile.
- O5: Provide a README (framework template) and a wiki in English, Danish and Bahasa Malaysia with a screenshot and a "what we gained" text for each lecture step.
- O6: Publish the repository with a description and topics on the git host.

## Scope

### In Scope

- Flask website with the routes `/`, `/add`, `/edit` and `/delete` and the Jinja templates of the assignment.
- Playground scripts for sqlite3 and SQLAlchemy as taught in the lessons.
- pytest tests for every step, a README, a three-language wiki, screenshots per lecture step.
- Repository description and topics.

### Out of Scope

- Authentication, deployment, styling beyond the assignment templates, a REST API.
- Any runtime dependency other than Flask and Flask-SQLAlchemy (with SQLAlchemy).
- Use cases and user stories as formal artifacts (see PP-001 Open Issues).

## Expected Benefits

### Tangible Benefits

- A tested, runnable repository for the Day 63 assignment.
- Screenshots and a wiki per lecture step in three languages.

### Intangible Benefits

- A reference the participant can reuse for later course days.
- A readable example for other course participants and repository visitors.

## Strategic Alignment

The project supports the participant's learning goal (the bootcamp) and the portfolio goal of showing structured, reviewed, documented work in a public repository.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| SC1 | All pytest tests pass on Python 3.13 | 100 % pass | `python -m pytest` exit code 0 |
| SC2 | Website works for challenges 1 to 5 and the CRUD lesson | Every challenge behaviour covered by a test | Test list in the milestone documents |
| SC3 | Data survives a server restart | Book added, app restarted, book listed | Persistence test |
| SC4 | Runtime dependencies | Only Flask and Flask-SQLAlchemy | `pyproject.toml` `dependencies` |
| SC5 | Wiki languages | en, da, ms pages for every step | Wiki page list |
| SC6 | Screenshots | One per lecture step in README and wiki | Files under `docs/images/` |
| SC7 | Repository metadata | Description and at least five topics set | Git host repository page |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Udemy download links expire, so the starting files cannot be fetched | Templates must be rebuilt from the lesson text | Rebuild templates from the described challenges; record this in the README |
| Screenshots cannot be taken without a GUI on the host | Missing evidence for steps | Headless browser in a Docker container (Docker 29 is installed) |
| Tokens in `.env` leak into the repository | Security defect | `.env` is in `.gitignore`; tokens are never printed, tested or imported |
| Danish and Bahasa Malaysia text is machine-quality | Reader confusion | Keep sentences short; the Product Owner reviews the language pages |
| Assignment function names conflict with clean layering | Hard to compare solutions | An Architecture Decision Record (ADR) keeps the assignment names at the web layer and layers the rest |

## Assumptions

- The Product Owner (S01) is also developer and reviewer; in autonomous mode the AI acts as stand-in reviewer and records it.
- The repository `063-library-project` under the organisation `Tirsvad-Udemy-100-days-of-code` on `git.tirsystem.com` is the target repository (it is the existing `origin`).
- Docker is available for headless screenshots.
- Python 3.13 is installed on the host.

## Constraints

- Python 3.13 or newer, venv, pytest, `pyproject.toml`, `constants.py` for constants.
- Folder structure `src/`, `tests/`, `docs/`.
- Doxygen comments in source and a Doxyfile.
- One pull request per milestone, from a branch.
- Tokens are read from `.env` for personal use only; `.env` is not committed, tested or imported by the project.
- Target end date 2026-11-20.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About five working sessions of the participant's time, no licence cost | Reusable reference, wiki in three languages, public portfolio item |

The assessment is qualitative on purpose: this is a learning project with no revenue, and the only cost is the participant's own time, so a money figure would add no information.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Learn, own and review the solution |
| S02 | Readable, runnable code with the assignment's names and run instructions |
| S03 | Clear description, topics and README, no heavy runtime dependencies |

## Recommendation

Proceed — the scope is small, fully specified by the lesson, and every part can be verified by tests and screenshots.

---

[SA-001]: ./stakeholder-analysis.md
