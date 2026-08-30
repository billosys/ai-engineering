# Usage Surface Inventory

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice01-usage-surface-instrument
status: proposed-done
architecture-decisions: none
inventory-status: analytical, non-final, not accepted architecture
```

## Evidence Basis

This inventory consumes Arc02 as a closed/composed input, especially the
conceptual model, boundary and naming findings, operator decision register, and
close-readiness artifact. It converts Arc02 concepts into usage surfaces for
later functional evaluation.

The current source checkout was used for factual grounding: README build and
install guidance, `SKILL.md` routing, project-management and ledger guides,
audit, coverage, delegation, contribution, and CCDP package contrast. No
source files were edited.

Project01 and `project01-harmonise-paths` remain source/package, package-local,
zip, release surface, component contract, package/release gate, and
`make check-package-paths` functional test surfaces.

## Inventory Rows

| Surface ID | Usage surface | Actor | Entrypoint or load path | Trigger | Expected success | Likely friction or deficiency |
|------------|---------------|-------|-------------------------|---------|------------------|-------------------------------|
| US-01 | direct source-clone reading | Human source reader or maintainer | `README.md`, then source docs and templates | User clones the repo to understand or change the framework | Reader can distinguish source docs, generated skill packages, CCDP package, planning worktree, and release gates. | Source/package wording or package-local link rules may be hard to keep visible across split components. |
| US-02 | packaged skill reading | Human or LLM reading an unzipped skill package | package root `SKILL.md` and package-local docs | User downloads or installs `collaboration-framework.zip` | Package reader can follow local links without source-only paths. | Component split can break local links or hide support assets. |
| US-03 | LLM skill loading | Active LLM context | `/collaboration-framework` or installed skill entrypoint | Substantial session starts and needs the framework | Model loads the minimum useful load set and routes to deeper guides only when needed. | Monolithic inline content may impose high context cost; split components may hide prerequisites. |
| US-04 | human orientation | Operator or collaborator | `README.md` "How to use it" and "Under the hood" | Human wants to know what the framework is for | Human can pick source, package, or skill invocation path. | README may need to list components after breakout without becoming a second composer. |
| US-05 | session start | Operator and active LLM | top-level composer plus posture/methodology floor | New sustained session begins | Session gets peer frame, process floor, and routing without loading every operational guide. | Top-level composer may be too rich or too thin. |
| US-06 | planning | CC, CDC, or operator | project-management wayfinder and PM guides | Opening a project, arc, or slice | Actor loads scales, layout, top-down planning, ledger, and artifact-home rules in order. | PM granularity may create routing friction if every guide is separate. |
| US-07 | execution | CC implementation seat | slice `cc-prompt.md`, `slice-plan.md`, `ledger.md`, source checkout | Operator starts a slice | CC can execute against the ledger without editing planning/source in the wrong place. | Role-language clarity and source/package mode matter. |
| US-08 | review | CDC or fresh verifier | closing report, ledger, diff, artifacts | A slice reports proposed-done | Reviewer can reproduce ledger rows and distinguish attested from reproduced evidence. | Verification vocabulary overlaps methodology, ledger, PM close, and audit. |
| US-09 | slice close | CC and CDC | slice `ledger.md`, `closing-report.md`, `cdc-verification.md` | Slice work is complete | Close includes row walk, artifact inventory, silent-drop diff, and bubble-up to arc. | Ledger versus PM ownership must stay explicit. |
| US-10 | arc close | CDC, operator, or fresh gate reviewer | arc `ledger.md`, arc `closing-report.md`, child close reports | Last slice in an arc closes | Parent composition is reproduced at arc scale; remediation slice used if needed. | Inherited-composition failure if children are trusted without arc-scale proof. |
| US-11 | audit | User commissioning audit and active LLM | `docs/CODE-AUDIT.md`, domain skills, output `workbench/` | Whole-repo quality audit requested | Audit covers every relevant language and produces evidence-backed findings and modernization synthesis. | Standalone audit output location can conflict with slice-local `artifacts/` unless scoped. |
| US-12 | coverage | CC or test-focused LLM | `docs/CLAUDE-CODE-COVERAGE.md` adapted to repo tooling | Coverage threshold work requested | Actor drives coverage with root-cause tests and quality gates. | Current guide name and examples are Claude/Cargo-shaped; generality must be tested. |
| US-13 | delegation | Active LLM and operator | `docs/SUBAGENT-DELEGATION-POLICY.md` | Multi-step work may use subagents | Actor keeps thinking work in main context and parallelizes lookup only. | Standalone component needs enough context to enforce the rule without full methodology. |
| US-14 | contribution | User drafting upstream OSS issue | `docs/CONTRIBUTION-STYLE.md` plus `templates/CONTRIBUTION-TICKET.md` | Bug, feature, doc fix, or question needs filing | Ticket is specific, calibrated, respectful, and shaped by the right template. | Template alone is weak; style without template may be too abstract. |
| US-15 | standalone use | Human or LLM loads one candidate component | candidate component entrypoint after breakout | User needs posture, ledger, PM, audit, coverage, delegation, or contribution alone | Minimum useful load set works without the top-level composer. | Hidden dependencies, role-language gaps, or missing support assets. |
| US-16 | composed use and combinations | Human or LLM loads multiple components | top-level composer or explicit component set | Task needs multiple disciplines together | Components load in coherent dependency order and avoid duplicate context cost. | Component overlaps may duplicate evidence rules, adapter notes, or package constraints. |

## Source/Package Modes

- source clone: direct checkout at `/Users/oubiwann/lab/billosys/ai-engineering`.
- planning worktree: `.worktrees/planning` with project, arc, slice, ledger,
  close, CDC verification, and slice-local `artifacts/`.
- generated skill zip: package-local root and links for installable skills.
- unzipped installed skill: Codex/agent local skill tree.
- CCDP package: separate protocol package, not an installable skill component.

## Functional Questions For Later Slices

- Which usage surfaces work today in the current monolith with acceptable
  context cost?
- Which surfaces require the top-level composer, and which can be standalone?
- Which component combinations are common enough to deserve composed routing?
- Which support assets must travel with component owners?
- Which Project01 package/release gate checks should be tested as user-visible
  source/package behavior, not only implementation validation?
- Which role-language clarity issues appear when a component is loaded without
  the top-level composer?

This inventory is analytical and non-final. It does not decide architecture;
architecture deferred to Arc04 after Arc03 functional analysis and operator
acceptance.
