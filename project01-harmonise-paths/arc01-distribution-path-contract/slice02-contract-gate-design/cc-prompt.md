# CC Prompt: Slice 02 Contract Gate Design

You are working in the ai-engineering repository.

Implementation checkout:

`/Users/oubiwann/lab/billosys/ai-engineering`

Planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

## Objective

Complete Slice 02:

`project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design`

This is a design slice, not an implementation slice. Produce the gate design
that Slice 03 can implement.

## Required Inputs

Read these files before writing the report:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/2026.08.29-package-path-audit.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/closing-report.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/slice-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`

## Deliverables

Create:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md`

Then update:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/ledger.md`

Then create:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/closing-report.md`

## Report Requirements

The design report must specify:

- the validation surface: generated zips, staging directories, or both;
- the chosen Make target and checker script entry point names;
- whether the implementation should be pure Make/Bash, a Make-facing shell
  wrapper around a structured parser, or a small checked-in parser script;
- classification behavior for bundled-reference, source-clone-reference,
  repo-only/provenance, example-project path, external URL, and parser false
  positive;
- hard-fail, warning, pass, and explicit-exception behavior;
- the exception or allowlist schema and proposed repository path;
- Markdown-aware parsing requirements, including fenced code, inline links,
  reference definitions, code spans, anchors, placeholders, and external URLs;
- source edit versus staging-time transform guidance;
- package layout change boundaries;
- CCDP/protocol deferral or reservation language;
- Slice 03 implementation scope and non-goals.

Carry forward these Slice 01 CDC constraints:

- the final gate must not be a raw regex hard gate;
- future reports must not claim that filtered CSV output contains classes that
  the scanner intentionally suppresses.

## Boundaries

Do not implement the checker in this slice.

Do not modify the Makefile, package source Markdown, mature language guides,
CCDP package targets, or zip layout in this slice.

Do not put generated planning/audit artifacts under implementation checkout
`workbench/`; slice-local planning artifacts belong in this slice directory.

## Verification

After writing the report and close set, run from the planning worktree:

```sh
git diff --check
rg -n "Slice 01|parser false positive|filtered CSV|external URL|145" project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md
rg -n "check-package-paths|Makefile|script|generated zip|staging" project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md
rg -n "bundled-reference|source-clone-reference|repo-only/provenance|example-project path|external URL|parser false positive|hard fail|warning|exception" project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md
rg -n "Markdown-aware|fenced code|inline link|reference definition|code span|anchor|raw regex" project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md
rg -n "allowlist|exception schema|classification|reason|path" project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md
rg -n "source edit|staging-time transform|package layout|repo-only|provenance" project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md
rg -n "Slice 03|implementation scope|non-goals|out of scope|CCDP|mature" project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md
test -f project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/closing-report.md
```

Close by walking ledger rows F-1 through F-8 and adding Bubble-up to Arc 01.
