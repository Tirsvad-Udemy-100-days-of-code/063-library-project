# G5 Wiki and README

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether the project is documented for S02 and S03 in three languages and ready to publish.

## Deliverable

A wiki in English, Danish and Bahasa Malaysia explaining each lecture step with its screenshot and what was gained, the final README with all screenshots, and the checks of the framework passing.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Wiki has a home page and a page per lecture step in `en`, `da` and `ms` | Met | Not met |
| 2 | Every step page embeds its screenshot and has a "What we gained" section | Met | Not met |
| 3 | README lists the steps with screenshots and links to the wiki | Met | Not met |
| 4 | `check-readme.sh` and `check-languages.sh` pass | Met | Not met |
| 5 | Wiki is published to the git host wiki | Met | Not met |
| 6 | Final run of `python -m pytest` passes | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-004] | All lecture steps and screenshots exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O5, O6 | [BC-001] |
| SC5, SC6, SC7 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-20 — within the end date 2026-11-20 in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the English wiki | Following `framework/process/wiki.md`, write Home plus one page per lecture step (in-memory site, sqlite3, SQLAlchemy, CRUD website) with its screenshot and a "What we gained" section. | No | O5 |
| 2 | Write the Danish wiki | Translate the English wiki into Danish (`da`) with the same structure and screenshots, in short sentences. | No | O5 |
| 3 | Write the Bahasa Malaysia wiki | Translate the English wiki into Bahasa Malaysia (`ms`) with the same structure and screenshots, in short sentences. | No | O5 |
| 4 | Finalize README with all screenshots | Make the README list each lecture step with its screenshot, link to the three wiki languages and keep the run and test instructions current. | No | O5 |
| 5 | Run framework checks | Run `check-readme.sh`, `check-languages.sh`, `check-plan.sh`, `python -m pytest` and fix what fails. | No | SC1 |
| 6 | Publish the wiki to the git host | Push the wiki pages to the repository wiki using the token in `.env` (read in the shell only), then confirm the pages are visible. | No | SC5 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-004]: ./mil-004-sqlalchemy-library-crud.md
