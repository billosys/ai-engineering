---
status: proposed-done
closed-on: 2026-08-31
closed-by: Codex CC
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
---

# Slice 03 Closing Report: Guide, Template, and Example Architecture

## Capability

Slice03 defined the v4.0 concept-card method skill's guide, template, and
example architecture. It decided guide surfaces by method concern, separated
user-authored template surfaces from trace/result-record surfaces, and
identified release-critical examples for the first v4.0 release.

Status: proposed-done pending independent CDC verification.

## Artifact List

- `artifacts/v40-guide-architecture.md`
- `artifacts/v40-template-architecture.md`
- `artifacts/v40-example-architecture.md`
- Updated `ledger.md`
- This `closing-report.md`

## Ledger Row Walk

| Row | Final status | Evidence |
|-----|--------------|----------|
| F-1 | done | Attested by CC: `test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && test -d artifacts` exited 0. |
| F-2 | done | Attested by CC: `test -f artifacts/v40-guide-architecture.md && test -f artifacts/v40-template-architecture.md && test -f artifacts/v40-example-architecture.md` exited 0. |
| F-3 | done | Attested by CC: `rg -n "guide architecture|SKILL.md|thin entrypoint|route|extraction|re-extraction|evidence lifecycle|graph|CQ|competency question|reconciliation|validation|verification|memory admission" artifacts/v40-guide-architecture.md` found the required guide concerns and thin-entrypoint routing terms. |
| F-4 | done | Attested by CC: `rg -n "template architecture|user-authored|trace record|result record|concept card|claim|source support|competency question|CQ|extraction run|validation result|verification result|reconciliation result|memory admission" artifacts/v40-template-architecture.md` found the required template surface and construct terms. |
| F-5 | done | Attested by CC: `rg -n "example architecture|minimal card|claim-backed|CQ coverage|relationship|edge|extraction-run|reconciliation|memory-admission|five-agent|parallel-worker" artifacts/v40-example-architecture.md` found the required release-critical example terms. |
| F-6 | done | Attested by CC: `rg -n "positive load|negative load|reason to load|problem ownership|dependency direction|adjacent guidance|five-agent|default recipe|not an invariant|parallel-worker provenance|operator workflow" artifacts/v40-guide-architecture.md artifacts/v40-template-architecture.md artifacts/v40-example-architecture.md` found Slice02 load, ownership, dependency, and five-agent default-recipe terms. |
| F-7 | done | Attested by CC: `rg -n "concept card|claim|source support|source span|evidence grade|extraction confidence|verification state|validation result|reconciliation state|memory admission|distinct|not one confidence" artifacts/v40-guide-architecture.md artifacts/v40-template-architecture.md artifacts/v40-example-architecture.md` found Arc03 distinction terms. |
| F-8 | done | Attested by CC: `rg -n "Slice04|Slice05|Arc05|validation determinism|package behavior|README|Makefile|source edit|schema syntax|enum spelling|generated zips|release mechanics|implementation planning" artifacts/v40-guide-architecture.md artifacts/v40-template-architecture.md artifacts/v40-example-architecture.md` found later-owner routing terms. |
| F-9 | done | Attested by CC: `rg -n "Out of scope|validation candidate selection|package inclusion|README integration|Makefile|validator-code|generated zips|released skill|source checkout edits|schema syntax|enum spelling|graph database|memory runtime|CCDP service|live extraction" slice-plan.md artifacts/v40-guide-architecture.md artifacts/v40-template-architecture.md artifacts/v40-example-architecture.md` found required scope-fence terms. |
| F-10 | done | Attested by CC: `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` exited 0, confirming the source checkout remained clean. |
| F-11 | done | Attested by CC: `LC_ALL=C grep -RIn '[^ -~]' slice-plan.md ledger.md cc-prompt.md artifacts || true; grep -RIn '[[:blank:]]$' slice-plan.md ledger.md cc-prompt.md artifacts || true` printed no matches; stricter `rg` checks for non-ASCII and trailing whitespace also printed no matches. |

Rows: 11. Done: 11. Deferred: 0. No-op: 0.

## Verification Summary

CC ran F-1 through F-11 from the Slice03 directory and also ran
`git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff
--check`. All checks passed. The source checkout remained clean.

## Boundary Check

This slice did not choose validation candidate selection, package inclusion,
README integration, Makefile changes, validator-code, deterministic validation
scripts, generated zips, released skill bundles, graph database design, memory
runtime design, CCDP service design, live extraction behavior, exact schema
syntax, exact enum spelling, source checkout edits, or source implementation.

## Bubble-up to Arc04

Slice03 delivered the Arc04 piece assigned in `arc-plan.md`: it defined the
guide set, template set, example set, and user-authored surfaces needed for
the first v4.0 skill while preserving Arc03 construct distinctions and the
Slice02 load contract.

What this slice revealed:

- The first-release guide architecture should be concern-based: load/routing,
  extraction, re-extraction/preservation, evidence lifecycle, graph/CQ,
  reconciliation, validation/verification, and memory admission.
- The template architecture needs three surface classes: user-authored, trace
  record, and result record. This distinction should be preserved by Slice05
  synthesis and later Arc05 implementation planning.
- The first-release example set should include minimal card, claim-backed
  card, CQ coverage, relationship/edge, extraction-run trace, reconciliation,
  memory-admission, and five-agent default-recipe examples.
- No Arc04 re-sequencing is required. Slice04 can now decide validation
  determinism, package behavior, README integration, discoverability, and
  maintenance ownership against these surfaces.

Silent-drop diff:

- Scope-as-specified required guide architecture, template architecture,
  example architecture, updated ledger, and closing report.
- Scope-as-delivered includes `artifacts/v40-guide-architecture.md`,
  `artifacts/v40-template-architecture.md`,
  `artifacts/v40-example-architecture.md`, updated `ledger.md`, and this
  `closing-report.md`.
- Silent drops: none identified.

Arc-plan change required: no sequencing or scope change. Slice04 should
consume the concern-based guide set, surface-class template model, and
release-critical example set when deciding validation, package, README, and
maintenance architecture.

## Closure

Status: proposed-done pending independent CDC verification.

Rows: 11. Done: 11. Deferred: 0. No-op: 0.
