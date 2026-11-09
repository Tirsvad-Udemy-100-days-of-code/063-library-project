# Architecture Decision Record

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [982abab] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The framework models what users do as use cases and user stories, then derives tasks from them (`project-planning`, "The hierarchy"). This project is a course assignment with four small lecture steps (an in-memory site, two SQLite lessons, a CRUD site). The Product Owner is also the only developer and reviewer, and the behaviour is already specified step by step in the lesson text. Options: (a) write a use case, system sequence diagram and domain model for each step; (b) treat the lecture challenges as plain tasks, each with a test, and skip use cases and user stories; (c) write one user-story document for the whole site. Forces: a deadline of 2026-11-20 in [BC-001], a very small scope, and a wish to keep the documents proportional to the work.

## Decision

Use cases, user stories and a separate governance document are not created for this project. Each lecture challenge is a plain task in a milestone, with a pytest test as its acceptance check, and S01 holds the owner, reviewer and approver roles.

## Consequences

**Positive:**

- Documents stay proportional to a one-person learning project.
- Every task still has a checkable result (a test and a screenshot).

**Negative:**

- No use case or domain model artifacts exist to trace code to; the Traceability Matrix lists concerns as gaps in views.
- If the project grows (more users or features), use cases must be added and this ADR deprecated.

## Affected Artifacts

- [BC-001] — scope states that use cases are out of scope.
- [PP-001] — the Stories column says "none (technical tasks, ADR-0001)".

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[982abab]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/commit/982abab59b0f2bfbc32ffbf96ae1eb41651bbb64
