* **Date:** 2026-08-09
* **Previous:** `0.3.0` (2026-08-03)
* **Commits:** 30 first-parent project commits
* **Diff:** 169 files changed, +126,913 / −732 lines

## Headline

CCDP v0.2 — a major revision of the Composite Cognition Dispatch Protocol
around the Coordinator Dispatcher model — plus a complete JSON/JSON-RPC
extraction corpus, a visual guide and GitHub Pages site, and a new C++ Core
Guidelines knowledge pack with source history preserved.

## CCDP v0.2 Specification

The core protocol advanced from the initial v0.1 draft to CCDP v0.2, centered
on a tighter Coordinator Dispatcher model and a more explicit treatment of
wire examples, provenance, audit behavior, security, and version history.

The v0.2 work includes:

- Revised protocol language across the assembled specification and source
  chapters under `protocols/ccdp/src/`.
- A new `Previous Versions` chapter and a dedicated `Version History` chapter.
- Open questions split into their own chapter before references.
- Iterative provenance and audit clarifications, including escalation origin,
  achieved grade, post-receipt policy, audit placement, provenance-policy
  wording, and non-escalation outcomes.
- Security and signing consistency updates across examples and normative text.
- README updates describing the protocol work.

## JSON and JSON-RPC Extraction Corpus

This release adds a complete JSON/JSON-RPC extraction corpus for CCDP v0.2
under `protocols/ccdp/json/`.

The corpus includes:

- Canonical JSON artifacts for audit records, capability records,
  decomposition plans, error objects, message requests/responses, health
  messages, notifications, escalation, and decomposition results.
- Notes files beside the canonical artifacts to record extraction rationale.
- Section-organized examples for terminology, message format, capability
  registry, provenance grades, audit trail, flow control, error handling,
  decomposition, and security.
- Inventory documents for fields and enumerations.
- `FINDINGS.md` and `MANIFEST.md` as corpus-level review and navigation
  surfaces.

## Visual Guide and Site

The repository now has a GitHub Pages-ready site structure and a CCDP visual
guide.

The site work includes:

- `.github/workflows/pages.yml` for Pages deployment.
- Top-level site pages under `site/`.
- Protocol index pages for CCDP.
- `protocols/ccdp/visual-guide/` with a reference document and rendered HTML.

## C++ Core Guidelines Knowledge Pack

This release adds a new C++ language knowledge pack under `knowledge/cpp/`,
grounded in the ISO C++ Core Guidelines by Bjarne Stroustrup, Herb Sutter, and
contributors.

The source-preserving import is located at
`knowledge/cpp/sources/md/cpp-core-guidelines/`, added with `git subtree` from
`github.com/isocpp/CppCoreGuidelines` so upstream history and authorship remain
reachable.

The LLM-facing guide layer includes:

- `knowledge/cpp/SKILL.md` — the C++ skill entrypoint and document-selection
  guide.
- 15 topic guides under `knowledge/cpp/guides/`, including core idioms, API
  design, functions, classes/value types, resource management, error handling,
  templates/generics, concurrency, performance, expressions/statements,
  anti-patterns, project structure/tooling, standard library, C-style
  modernization, and reference/glossary material.
- `knowledge/cpp/guides/11-anti-patterns.md` as the cheap first-load safety
  net for C++ tasks.
- `knowledge/cpp/tools/split_cpp_core_guidelines.py` to regenerate the guide
  layer from the imported upstream source.
- `knowledge/cpp/extraction-metadata/cpp-core-guidelines-analysis.md` with the
  split strategy, source-section map, and rule counts.
- `make cpp` and the aggregate Makefile targets now build and install
  `cpp-guidelines.zip` alongside the existing domain skills.

## Other Changes

- Updated the CCDP assembler to support the revised chapter sequence and
  assembled-output shape.
- Updated skill packaging documentation for the new C++ domain.
- Added placeholder site pages for the broader protocol area.
- Updated repository README and ignore patterns to match the new protocol and
  site surfaces.
