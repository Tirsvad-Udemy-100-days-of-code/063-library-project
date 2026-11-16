# G6 Framework baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001], [PP-001], [MIL-005] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; accepted with the Go verdict of the review record (autonomous, not independent) | [351a3e9] |

---

## Purpose

This gate decides whether the project has the baseline of the framework: the adopted framework release, the README in the framework template with an appendix that lists only the documents of the repository, project URL metadata, the editor settings of the baseline, the environment template of the framework, a screenshot tool that passes the shared checks and runs as an unprivileged user, an updated traceability matrix, a passing test suite, an updated plan and reviewed documents, merged to the default branch with a green build. The wiki in English, Danish and Bahasa Malaysia already has a sidebar in the framework's shape and the language line on the first line of each page; this gate checks it again against the current checklist and does not change a page. The work is delivered on the branch `mil-006-framework-baseline` and one pull request. It changes no behaviour of the program.

## Deliverable

A merged pull request that holds: the updated Business Case, Project Plan, Artifact Registry and Traceability Matrix, this milestone and the review records of the changed documents and of the wiki; the README without the private framework files in its appendix; `pyproject.toml` with the project URLs; `.editorconfig` and `.env.example` of the framework baseline; the formatted screenshot script and the image of the screenshot tool with an unprivileged user; and the framework release adopted by the project. The program (`src/`), the tests (`tests/`), the screenshots (`docs/images/`) and the wiki pages do not change.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | BC-001, PP-001 and MIL-006 each have an `Accepted` Version History row and a review record, and the wiki has a review record | Verdict `Go` | Any missing or `No-Go` |
| 2 | `python -m pytest` runs (the tests need no network) and `git diff origin/main --stat -- src tests docs/images docs/wiki` lists no file | Exit code 0 and an empty diff | Any failure or any change |
| 3 | `docs/wiki/` has `_Sidebar.md` and the six English pages (Home, Step-1-In-Memory-Library, Step-2-Sqlite3-Lesson, Step-3-SQLAlchemy-Lesson, Step-4-Library-With-Database and Project-Structure) in en, da and ms (18 pages), directly in the folder, each page starting with the language line, and the sidebar has the title, one list of the English pages and the Languages section last; the published wiki is the same as the folder | 18 pages, the sidebar and the same content on the host | A page or language missing, a subfolder, a sidebar of another shape or a difference on the host |
| 4 | `framework/scripts/check-readme.sh`, `framework/scripts/check-languages.sh` and `framework/scripts/check-editorconfig.sh` run, and `shfmt -d scripts/screenshots/*.sh` prints no difference | Exit code 0 and no difference | Any finding |
| 5 | `pyproject.toml` sets the licence as an SPDX expression with `license-files`, requires a setuptools release that reads it and sets the project URLs for the repository, the documentation and the issue tracker | All set | Any missing |
| 6 | `.env.example` is tracked and holds empty placeholders for the framework tokens only (the program reads no environment variable); `.env` is not tracked | Present, no real value | Missing, a real value present or `.env` tracked |
| 7 | `docs/sqa/traceability-matrix.md` lists every document of the project, MIL-006 and the wiki included, with its upstream and downstream links and its last review | One row per document | A document missing |
| 8 | The image of the screenshot tool (`scripts/screenshots/Dockerfile.screenshots`) sets an unprivileged `USER`, builds, and the tool takes screenshots into a scratch output folder | Image builds, screenshots are written, `USER` is not root | Build fails, no screenshot or the user is root |
| 9 | All CI checks of the pull request | Green | Red or pending |
| 10 | The pull request carries one `Closes #N` line per task of this milestone | Every issue is closed after the merge | An issue stays open |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-005] accepted | Documents and baselines the finished program, its tests, its README and its wiki |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 to O6, SC1 to SC7 | Criterion 2 (the behaviour is unchanged and its tests pass) |
| O7 | Criteria 1, 3, 4, 5, 6, 7, 8 and 10 (documents, wiki, README, metadata, environment template, traceability matrix, screenshot tool and issues) |
| SC8 | Criteria 1, 2, 3, 4 and 9 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-11-23: one week after the start, as the Business Case constraint for this milestone requires.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Adopt the framework release | Move the `framework/` submodule to the newest release, track `.gitmodules` (lowercase repository URL), install the skills and hooks, add the framework baseline `.editorconfig` and bring `.env.example` to the framework's template, so the project follows the same rules as the other projects of the portfolio. | No | BC-001 objective O7 |
| 2 | Update and review the planning documents | Add this milestone to the Business Case, Project Plan, Artifact Registry and Traceability Matrix, set the domain of the changed documents and of the registry to education, name the PlantUML server in the Artifact Registry, add the missing link definition to RC-009 and review each changed document against its QC checklist, so the plan-first gate is met. | No | BC-001 objective O7 |
| 3 | Check the wiki against the current checklist | Compare the pages and the sidebar with the wiki checklist of the adopted framework release, read the published wiki back from the host and add a review record for the wiki. No page changes. | No | BC-001 objectives O5 and O7 |
| 4 | Bring the README to the framework template | Keep the text of the README, describe the framework files in the overview, name the licence expression and give the appendix only the documents that are in the repository, so the README is complete and checkable. | No | BC-001 objectives O4 and O7 |
| 5 | Complete the package metadata | Add the repository, documentation and issue tracker URLs to `pyproject.toml` and require a setuptools release that reads the licence expression, which is already set. | No | BC-001 objective O7 |
| 6 | Make the screenshot tool pass the shared checks | Format `scripts/screenshots/capture_screenshot.sh` with the indentation of the baseline `.editorconfig` and let the image of the tool run as an unprivileged user, with no change to what the tool does. | No | BC-001 objective O7 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-005]: ./mil-005-wiki-and-readme.md
[351a3e9]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/commit/351a3e9cd72ecaafcfc8ccd09c480433fae0c21a
