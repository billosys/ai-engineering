# Project05 Naming And Scope Register

```yaml
project: project05-concept-card-skill
arc: arc01-readiness-and-scope-lock
slice: slice01-current-layout-reconciliation
artifact: project05-naming-and-scope-register
status: cc-produced
date: 2026-09-06
```

## Purpose

This register records the accepted Project05 names and scope boundaries so
later implementation arcs do not revive superseded names or collapse adjacent
skills into one root.

## Accepted Live Skill Names

| Accepted name | Replaces | Source root | Package zip | Scope summary |
| --- | --- | --- | --- | --- |
| `document-extraction` | `source-preparation` | `knowledge/document-extraction/` | `document-extraction.zip` | Standalone upstream skill for extracting usable Markdown, structure, media references, locators, manifests, reports, caveats, and readiness decisions from PDF, EPUB, HTML, converted Markdown, indexing, reading, source review, and downstream method workflows. |
| `concept-cards` | `concept-card-method` | `knowledge/concept-cards/` | `concept-cards.zip` | Standalone method skill for provenance-bearing concept cards: cards, claims, source support, source spans/locators, relationship edges, competency questions, extraction runs, validation, verification, reconciliation, preservation decisions, evidence lifecycle, and memory admission. |
| `ontology-engineering` | none | reserved | reserved | Likely future composite skill. Reserve for ontology lifecycle, NeON-style methods, competency questions, alignment, graph/knowledge modeling, and routing among adjacent method skills. |

## `document-extraction` Ownership

`document-extraction` owns:

- raw input preservation expectations for PDF, EPUB, HTML, and converted
  Markdown workflows;
- converter-output inspection before edits;
- Markdown preparation for downstream use;
- media path normalization;
- PDF `metadata.json` and TOC/page mapping when available;
- EPUB heading, navigation, anchor, and media mapping;
- HTML source capture and locator preservation;
- source structure maps and split-file decisions;
- locator model guidance for pages, anchors, headings, line numbers, and URI
  fragments;
- manifests, validation reports, readiness reports, and caveat records;
- final readiness classification for concept-card extraction, full-text
  indexing, standalone reading, and source review.

`document-extraction` does not own:

- concept-card schema or card semantics;
- relationship/CQ semantics;
- memory admission;
- ontology lifecycle methodology;
- generic runtime conversion services or a mature CLI unless explicitly scoped
  later.

## `concept-cards` Ownership

`concept-cards` owns:

- concept card representation and record shape;
- claims and source support;
- source spans and source locator use after upstream source extraction;
- evidence grade, extraction confidence, verification state, validation
  result, reconciliation state, preservation decision, and memory admission as
  distinct fields or records;
- relationship edges and competency questions;
- extraction and re-extraction workflows from prepared source snapshots;
- validation and verification review boundaries;
- reconciliation and preservation rules;
- memory-admission guidance and caveats.

`concept-cards` does not own:

- PDF/EPUB/HTML conversion and cleanup;
- raw source preservation mechanics except as upstream provenance
  requirements;
- ontology database or ontology-engineering lifecycle work;
- GraphRAG, graph database, memory runtime, CCDP service, or live extraction
  runtime implementation.

## Routing Between The Two Required Skills

When a task begins with raw or converter-produced source, route first to
`document-extraction`:

- PDF plus Marker output;
- EPUB plus pandoc output;
- HTML source capture or cleanup;
- converted Markdown requiring structure mapping, media repair, locators,
  splitting, or readiness reports.

When a task begins with prepared source evidence and asks for concept-card
method work, route to `concept-cards`:

- extract cards, claims, relationships, or competency questions;
- re-extract or reconcile cards;
- validate source support;
- decide preservation or memory admission;
- audit evidence lifecycle or field semantics.

`concept-cards` should consume `document-extraction` manifests, structure
maps, locators, and caveat reports as upstream provenance.

## Reserved `ontology-engineering` Boundary

Project05 may mention future routing to `ontology-engineering`, but must not
implement or absorb that skill unless the operator expands Project05.

Reserved future scope includes:

- ontology lifecycle and competency-question methodology beyond concept-card
  support;
- NeON-style ontology-engineering process;
- ontology alignment and critique as a larger composite activity;
- graph/knowledge modeling that coordinates concept-card, source, and domain
  skills.

Current Project05 implication:

- `concept-cards` can include relationship and competency-question semantics
  needed for cards.
- It should not claim to be the general ontology-engineering skill.

## Nondeferrable Scope

The following remain nondeferrable in Project05 unless the operator records an
explicit override:

- create the live `document-extraction` skill;
- create the live `concept-cards` skill;
- make both detailed enough for assistant-direct and human-assisted use;
- wire both into Makefile targets, generated zips, install behavior,
  docs/skill-library discoverability, and validation gates;
- preserve and modernize the PDF and EPUB preparation logic inside
  `document-extraction`;
- preserve and modernize v4.0 concept-card semantics inside `concept-cards`.

Allowed deferrals remain adjacent runtime or infrastructure systems, not the
two required skills themselves.
