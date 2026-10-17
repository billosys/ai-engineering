# Slice01 — Fennel guidelines

Status: closed. Completed the direct Operator request under the recorded single-contributor transition; initial `cc-prompt.md` remains preserved.

## Goal and boundaries

Deliver the source-preserving import and complete packaged Fennel authoring skill.
In scope: six requested pages plus API, Lua primer, rationale, Clojure migration,
security and changelog; root LICENSE; source provenance; skill and guides; Makefile,
README and skill-library documentation. Retain source bytes, attribution and history.
Do not import compiler implementation, website assets or unrelated documents.
Do not edit `knowledge/lfe/`, install the new skill into profiles, or push.

## Design

The website README and Makefile resolve its pages to the Fennel submodule.
Pin website 253e9463c2d6a306feecb37237beee303f9714c1 and language
9af5e47fa7ddea806544d15507412ddc51bd046d (release 1.6.1).
Filter a disposable full clone to the selected root paths, prefix them with
`knowledge/fennel/sources/md/`, and merge without squash. Keep a commit map,
retained path manifest, full reproducible commands and verification evidence.
Compare selected path history before filtering, current blobs and rewritten trees;
verify messages, author identities and timestamps. History rewriting necessarily
changes hashes and removes commit signatures; it does not preserve cryptographic
signatures as valid on new commits.

Use Rust's wayfinding/pattern structure, not its Rust-specific topics or defaults.
Teach Lua runtime semantics explicitly: tables are mutable, colon strings are
strings, nil/false truth, multiple returns, lexical bindings, matching, modules,
expected errors, macros, embedding and runtime target compatibility. Give source
sections per rule, bounded strength claims, examples and review checks. Preserve
the style guide's CC BY-NC-SA 3.0 attribution; derived skill prose is distributed
under that license rather than silently claiming the repository MIT license.

The installed fnlfmt 0.3.2, Fennel 1.6.1 and Lua 5.5 are available. No formatter
installation is necessary. Test complete positive examples and selected deliberately
incorrect examples with discriminating assertions/compile failures. Host versions
other than the tested Lua runtime remain explicitly untested.

## Verification and exit

Ledger S01–S07 defines implementation checks. Run `make check-skills` and
`make check-package-paths` (includes source and freshly built package version
checks). Inspect the whole owned skill tree for version duplication and histories.
Check extracted package routing and source-link policy. Return a closing report
with row-by-row attributed evidence. The required fresh-context audit and corrections are complete; see closing-report.md and artifacts/final-audit.md.
Artifacts: `artifacts/` for execution checks/logs. Source provenance is a delivered
part of `knowledge/fennel/sources/`, not a planning artifact override.

## Readiness and applied guidance

Inspected Rust SKILL.md selection/rule conventions, a core chapter's pattern shape,
Makefile pack_skill and gates, docs/skill-library.md, upstream README/Makefile and
submodule pointer. Consequential choices are resolved in Design and cc-prompt.
Skill-creator progressive disclosure supports a concise wayfinder and task guides;
the repository version contract requires metadata.version and one sibling history.
Source inspection, history proof, runtime examples and package checks exercise
different promises; none substitutes for independent semantic review.

## Assignment history

- 2026-10-17 — `cc-prompt.md`; initial request, no predecessor; active in this
  context under the Operator's direct instruction, no independent handoff claimed.

## Source-lineage clarification — 2026-10-17

`git log --follow` shows `api.md` originated in `README.md`. Retain README
as the language overview and API-history ancestor, within the Operator-authorized
useful supplemental docs. All other selected paths have no predecessor rename.

## Workflow transition — 2026-10-17

Operator selected single-contributor mode and authorized autonomous completion,
checking subagents and a fully prompted fresh final audit. The primary context
owns all implementation and findings dispositions; no CDC acceptance or further
Operator approval is required. Initial cc-prompt.md remains preserved historical
authority except for its superseded multi-contributor gate. Final audit evidence
lives in artifacts/final-audit.md, with subsequent corrections and verification
recorded in closing-report.md. This explicit instruction authorizes audit judgment
by a subagent despite the normal agent-coordination lookup-only boundary.

## Completion — 2026-10-17

All seven ledger rows are done. Initial assignment completed, with the recorded
workflow transition. All three fresh-audit findings were corrected and independently
rechecked. Final source commit: `c9d98a3ec3d0a24c30a18431d7aeaa13f6451872`. No remaining assignment or gate.
