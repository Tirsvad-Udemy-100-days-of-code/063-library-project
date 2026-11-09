# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Tracks backward and forward links between artifact instances so that the Business Case's traceability success criteria are measurable. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | it | - | [SA-001], [PP-001] | [RC-001], [RC-009] |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | Project Plan | en | it | [BC-001], [SA-001] | MIL-001 to MIL-005 | [RC-003] |
| [MIL-001] | Milestone / Gateway | en | it | [BC-001], [PP-001] | tasks (issues) | [RC-004] |
| [MIL-002] | Milestone / Gateway | en | it | [BC-001], [PP-001] | tasks (issues) | [RC-005] |
| [MIL-003] | Milestone / Gateway | en | it | [BC-001], [PP-001] | tasks (issues) | [RC-006] |
| [MIL-004] | Milestone / Gateway | en | it | [BC-001], [PP-001] | tasks (issues) | [RC-007] |
| [MIL-005] | Milestone / Gateway | en | it | [BC-001], [PP-001] | tasks (issues) | [RC-008] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | - | - | - | Gap |
| CN-002 | - | - | - | Gap |
| CN-003 | - | - | - | Gap |
| CN-004 | - | - | - | Gap |
| CN-005 | - | - | - | Gap |
| CN-006 | - | - | - | Gap |
| CN-007 | - | - | - | Gap |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | none | - | Closed | - |

## Coverage Notes

No view artifacts exist yet, so every concern is a Gap until the milestones deliver code, tests and the wiki. `-` in Last Reviewed means no `RC-*` exists yet.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[MIL-002]: ../milestones/mil-002-in-memory-library.md
[MIL-003]: ../milestones/mil-003-sqlite-playground.md
[MIL-004]: ../milestones/mil-004-sqlalchemy-library-crud.md
[MIL-005]: ../milestones/mil-005-wiki-and-readme.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001-project-setup.md
[RC-005]: ./reviews/rc-005-mil-002-in-memory-library.md
[RC-006]: ./reviews/rc-006-mil-003-sqlite-playground.md
[RC-007]: ./reviews/rc-007-mil-004-sqlalchemy-library-crud.md
[RC-008]: ./reviews/rc-008-mil-005-wiki-and-readme.md
[RC-009]: ./reviews/rc-009-business-case-delta.md
