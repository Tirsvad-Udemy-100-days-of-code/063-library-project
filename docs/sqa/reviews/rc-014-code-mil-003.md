# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-003]
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none (the stand-in reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | ruff N rules pass; modules, functions and constants use PEP 8 casing. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (create_table, read_book_by_title, update_title_by_primary_key). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | ruff check and ruff format are clean. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function and test is annotated, including -> None (ruff ANN). |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | BookNotFoundError is raised for missing ids and titles; no bare except. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | Pass | sqlite3 connections use contextlib.closing; the SQLAlchemy session runs inside app.app_context(). |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Public modules and functions have Doxygen docstrings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | CLI output uses sys.stdout.write; no print and no secrets are written. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists; deviation recorded in ADR-0001 and ADR-0002. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 63 tests (27 new) with tmp_path databases, independent of order and network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | N-A | Optional: mypy is not installed. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | No new dependency; Flask-SQLAlchemy was already declared. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Lesson data and SQL limits come from constants.py (LESSON_* and BOOKS_TABLE), defined once; the model is reused later by the website. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | infrastructure imports domain and constants only; no import cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Each function has one reason to change; the Book model carries no lesson logic. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Lessons live in infrastructure/lessons; tests in tests/integration. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Names are lowercase English with letters, digits, _ and . |

## Overall Verdict

Go — the Mandatory criteria pass for the sqlite3 and SQLAlchemy lesson code. Autonomous mode: the reviewer is a stand-in for S01, so this review is not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None; S01 may challenge this stand-in review in the end-of-run summary | S01 | 2026-11-20 |

---

[MIL-003]: ../../milestones/mil-003-sqlite-playground.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
