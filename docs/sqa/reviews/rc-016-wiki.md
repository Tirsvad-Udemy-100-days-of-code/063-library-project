# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [MIL-005], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-005]
- Checklist used: [QC-WIKI-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none (the stand-in reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | docs/wiki/_Sidebar.md exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Sidebar starts with the bold title, then one list of the English pages with Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | Every English page (6) is in the list and every link target exists. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | N-A | The wiki has no related wikis, so there is no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | The Languages section is last, one line per language written in that language, linking to Home, Home-da and Home-ms. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is written by hand, not generated. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Each page also has the language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English plus Danish and Bahasa Malaysia exist; the PO language is English. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Six pages in each of three languages: the page sets are identical (18 pages plus the sidebar). |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Every page starts with the language line with the current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | da pages end in -da.md and ms pages in -ms.md; English has no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Commands, file names and code identifiers stay in English in every language. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | Pages and links can be checked on the host only after the merge publishes the wiki. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | Optional: no layout rule change. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | docs/wiki is flat; languages are told apart by file name. |

## Overall Verdict

Go-with-conditions — all Mandatory criteria pass except criterion 14, which is Pending until the wiki is published. Autonomous mode: the reviewer is a stand-in for S01, so this review is not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| After the merge publishes the wiki, open every page and link on the host and record the result | S01 | 2026-11-20 |

---

[MIL-005]: ../../milestones/mil-005-wiki-and-readme.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
