---
arc: arc01-portable-contract
status: active
depends-on: [project09-design-audit evidence intake]
---

# Arc01 — Portable Contract

## Capability and authority

Establish an executable contract for a portable design skill and full review of
its existing knowledge corpus. Separate reusable method from adopting-project
identity, specify removal of C&B coupling, pin the review population, establish
source needs, and prepare the evidence method consumed by Arc02. This arc produces
design and investigation artifacts; it does not perform the complete semantic
review or rewrite the skill under an evidence-only assignment.

The Operator opened Arc01/Slice01 on 2026-10-09 after approving all-233-card
semantic review, Git-only C&B retention, bug-correction treatment without a
compatibility bridge, and `sources/md/`. The [project plan](../project-plan.md)
governs. Initial source: `dffa504e851b03b8e4746f1941068e4cc850b612` on `main`.
Project09 audit artifacts are consumed at planning commit
`795ac75b`; this is evidence intake, not acceptance of their conclusions.

## Slice roadmap

| Slice | Capability | Dependency and state |
|---|---|---|
| slice01-scope-and-portability-contract | Pin all cards/live files/local sources; identify source gaps; produce the concrete portable contract and change map | Open; initial CC assignment issued to Operator |
| slice02-source-and-review-readiness | Resolve acquisition/preparation needs and establish the claim-level review procedure, locators and complete coverage accounting | Planned after accepted Slice01; source availability controls readiness; no prompt issued |
| slice03-contract-composition-and-handoff | Compose the portable contract and review method, settle proposed wording/configuration, and prepare bounded Arc02 execution groups with traceable coverage | Planned after accepted Slice02; no prompt issued |

Only Slice01 is detailed. Slice02 must follow actual source findings: record
missing inputs and obtain necessary evidence without pretending local Markdown
alone proves fidelity. Any needed source acquisition/conversion edits require
their own explicit slice allowlist. Slice03 must not silently archive unreviewed
cards or use a representative sample as the full-corpus acceptance gate.

## Scope and composition criteria

- One pinned baseline manifest and card/source index account for all 233 existing
  cards, all six guides, entrypoint/history, and local source holdings. Splits,
  merges and removals in later work remain traceable to the original population.
- The portable contract preserves compositional ethos, separates binding user
  decisions from proposed teaching formulations, and defines input/profile
  behavior without a new C&B preset or an unexplained universal aesthetic.
- The review method covers source fidelity, correctness, scope/attribution,
  consistency, and relationship/question coverage for every card and substantive
  claim, with revision-specific source witnesses and correction history.
- Source gaps have named resolution work and affected populations. They may be
  faithfully reported by Slice01, but required unresolved source/review gaps
  cannot be waved through the arc's readiness gate for dependent semantic work.
- Arc02 receives accepted contract/method revisions and a complete allocation of
  the corpus, including repeated guide claims and all relevant DES findings.

The [arc ledger](ledger.md) records the composition gate. Project09 acceptance
remains a separate project release dependency; this arc does not close Project09.

## Roles, evidence and current handoff

Default Two-Contributor Workflow. CDC: Sofie in the planning chat; CC: the separate
implementing context to which the Operator relays the prompt. No CRC or Expedited
Mode is selected. This opening does not start another chat or execute CC's work.
Slice evidence belongs in its `artifacts/`; shared audit evidence stays in Project09.
Slice acceptance uses `cdc-verification.md`, written only after independent review.
Arc closure needs its own composition demonstration and attributed independent
gate. Do not pre-create close or verification records.

Current assignment:
`slice01-scope-and-portability-contract/cc-prompt.md` (initial, issued 2026-10-09).
CDC owns structural decisions and later slice preparation. Escalate changes to
scope, source baseline, evidence requirements or adopted design; local formatting
and ephemeral query mechanics are CC discretion within the assignment.

## Version History

- 1.0 (2026-10-09): Opened Arc01 with three bounded slices; issued the first
  evidence/contract assignment under the settled Operator scope decisions.
