# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

This analysis names the people the project serves and what each needs, using a power/interest grid. It feeds the Business Case [BC-001] and the Project Plan.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A correct, reviewed solution that shows what each lecture step taught |
| S02 | Udemy course participants | Fellow students | Udemy | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and run instructions |
| S03 | GitHub viewers | Repository visitors | Public | LOW | MEDIUM | Keep Informed | A clear description, topics and README, and no runtime dependencies beyond what is needed |

## Power/Interest Classification Rationale

- **Manage Closely:** S01 decides scope, reviews and accepts every artifact.
- **Keep Informed:** S02 and S03 cannot change the project but use its output; they are served by the README and the wiki.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The site does what challenges 1 to 5 and the CRUD lesson require | Functionality |
| CN-002 | S01 | Books survive a restart | Reliability |
| CN-003 | S01 | Every lecture step has a screenshot and a "what we gained" text in en, da and ms | Supportability |
| CN-004 | S02 | Code is easy to read and uses the assignment's names (`all_books`, `Book`, `db`) | Usability |
| CN-005 | S02 | Clear steps to create `.venv`, install and run the app and tests | Supportability |
| CN-006 | S03 | Repository description, topics and README are clear | Usability |
| CN-007 | S03 | Few runtime dependencies | Implementation constraint |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Chat with S01 | Per request | Plan acceptance, end-of-run summary | All |
| CR-002 | README | Per milestone | Run and test instructions, screenshots | MIL-002 to MIL-005 |
| CR-003 | Wiki (en, da, ms) | Per milestone | Step explanations | MIL-005 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants the assignment's flat names; clean architecture wants layers | S02, S01 | Keep the assignment names in the web layer; layer the rest (ADR) |
| S03 wants no dependencies; the lesson needs Flask and SQLAlchemy | S03, S01 | Only Flask and Flask-SQLAlchemy at runtime; test tools as optional extras |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-002 | O1, O2, O3 in [BC-001] |
| S01 | CN-003 | O5 in [BC-001] |
| S02 | CN-004, CN-005 | O4, O5 in [BC-001] |
| S03 | CN-006, CN-007 | O4, O6 in [BC-001] |

## Sign-Off

Pending review. In autonomous mode the AI signs as stand-in for S01.

---

[BC-001]: ./business-case.md
