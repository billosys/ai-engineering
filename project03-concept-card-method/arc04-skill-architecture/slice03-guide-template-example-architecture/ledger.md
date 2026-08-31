# Slice 03: Guide, Template, and Example Architecture

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice03 open set exists with slice plan, ledger, prompt, and artifact home | `test -f slice-plan.md && test -f ledger.md && test -f cc-prompt.md && test -d artifacts` | correctness-grade | slice-plan | open | | |
| F-2 | Required artifacts are produced under the slice-local artifact home | `test -f artifacts/v40-guide-architecture.md && test -f artifacts/v40-template-architecture.md && test -f artifacts/v40-example-architecture.md` | correctness-grade | slice-plan | open | | |
| F-3 | Guide architecture assigns required method concerns to guide surfaces and preserves thin SKILL.md routing | `rg -n "guide architecture|SKILL.md|thin entrypoint|route|extraction|re-extraction|evidence lifecycle|graph|CQ|competency question|reconciliation|validation|verification|memory admission" artifacts/v40-guide-architecture.md` | serious | slice-plan | open | | |
| F-4 | Template architecture distinguishes user-authored surfaces from trace/result-record surfaces | `rg -n "template architecture|user-authored|trace record|result record|concept card|claim|source support|competency question|CQ|extraction run|validation result|verification result|reconciliation result|memory admission" artifacts/v40-template-architecture.md` | serious | slice-plan | open | | |
| F-5 | Example architecture covers release-critical example classes | `rg -n "example architecture|minimal card|claim-backed|CQ coverage|relationship|edge|extraction-run|reconciliation|memory-admission|five-agent|parallel-worker" artifacts/v40-example-architecture.md` | serious | slice-plan | open | | |
| F-6 | Artifacts preserve the Slice02 load contract, problem ownership, dependency direction, and five-agent default-recipe decision | `rg -n "positive load|negative load|reason to load|problem ownership|dependency direction|adjacent guidance|five-agent|default recipe|not an invariant|parallel-worker provenance|operator workflow" artifacts/v40-guide-architecture.md artifacts/v40-template-architecture.md artifacts/v40-example-architecture.md` | correctness-grade | slice-plan | open | | |
| F-7 | Artifacts preserve Arc03 conceptual distinctions instead of flattening lifecycle and evidence concepts | `rg -n "concept card|claim|source support|source span|evidence grade|extraction confidence|verification state|validation result|reconciliation state|memory admission|distinct|not one confidence" artifacts/v40-guide-architecture.md artifacts/v40-template-architecture.md artifacts/v40-example-architecture.md` | correctness-grade | slice-plan | open | | |
| F-8 | Unresolved validation, package, README, Makefile, source-edit, schema, enum, and release questions are routed to later owners | `rg -n "Slice04|Slice05|Arc05|validation determinism|package behavior|README|Makefile|source edit|schema syntax|enum spelling|generated zips|release mechanics|implementation planning" artifacts/v40-guide-architecture.md artifacts/v40-template-architecture.md artifacts/v40-example-architecture.md` | serious | slice-plan | open | | |
| F-9 | Slice scope fences keep validation/package decisions, implementation mechanics, runtime services, and source edits out of scope | `rg -n "Out of scope|validation candidate selection|package inclusion|README integration|Makefile|validator-code|generated zips|released skill|source checkout edits|schema syntax|enum spelling|graph database|memory runtime|CCDP service|live extraction" slice-plan.md artifacts/v40-guide-architecture.md artifacts/v40-template-architecture.md artifacts/v40-example-architecture.md` | serious | slice-plan | open | | |
| F-10 | Source checkout remains clean | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | serious | operator constraint | open | | |
| F-11 | New and modified Slice03 Markdown is ASCII-clean and has no trailing whitespace | `LC_ALL=C grep -RIn '[^ -~]' slice-plan.md ledger.md cc-prompt.md artifacts || true; grep -RIn '[[:blank:]]$' slice-plan.md ledger.md cc-prompt.md artifacts || true` | polish | repo hygiene | open | | Verify commands should print no matches. |

## What Worked

_(At slice close. Patterns that made the slice close cleanly.)_

## Closure

Slice remains open.
