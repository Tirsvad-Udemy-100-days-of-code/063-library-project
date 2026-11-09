# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [e02e021] |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the stand-in reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Start 2026-11-09, end 2026-11-20, constraint 'target end date 2026-11-20' from BC-001 Constraints. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | G1 to G5 listed once with document, decision date, owner S01. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates equal the Target Date of each MIL (11-10, 11-12, 11-14, 11-17, 11-20) and lie inside the window. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage table maps every in-scope item to a gateway. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Chain G1 to G5, acyclic, matches the schedule order. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Dependencies section: a No-Go moves later windows; S01 decides the end date. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Owners are S01; Planning Assumptions explain that S01 holds all roles and no GOV document is kept (ADR-0001). |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Assumptions list their sources; no baseline change yet. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan risks have mitigation and one traces to BC risk 1. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open issues are current and do not contradict the plan. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Main deliverable column matches each MIL Deliverable. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Stories column says 'none (technical tasks, ADR-0001)'. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt bars equal the table windows; chain equals the dependency view. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Column header says 'not yet synced'. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | One plan file; Version History has one row. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has `Language | en` and `Domain | it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register follows the registry row for this type (checked by the stand-in reviewer). |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No domain dictionary (`DICT`) exists; standard IT terms are used consistently. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists beside the file. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version; no language change. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The stand-in reviewer reads English and knows the IT domain (autonomous, not independent). |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out on first use or are framework IDs. |

## Overall Verdict

Go — all Mandatory criteria pass. Autonomous mode: the reviewer is a stand-in for S01, so this review is not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None; S01 may challenge this stand-in review in the end-of-run summary | S01 | 2026-11-20 |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[e02e021]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/commit/e02e021cc1ba355061ecedf65df446c90006a8a6
