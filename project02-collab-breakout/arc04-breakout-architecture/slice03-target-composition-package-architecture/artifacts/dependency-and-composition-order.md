# Dependency And Composition Order

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice03-target-composition-package-architecture
status: proposed-done
artifact-status: proposed-composition-input
operator-acceptance: pending
```

## Input Contract

This artifact consumes the verified Slice01 architecture decision method and
component-contract schema, plus the verified Slice02 component contract
evaluation and slice03 composition inputs. It uses the target component graph
from `artifacts/target-component-architecture.md`.

The dependency order and load order below are proposed. They do not approve
final package paths, source moves, or operator acceptance.

## Dependency Order

The proposed dependency order is:

1. Package/release gates: Project01 source/package constraints, reader modes,
   release surface synchronization, CCDP separation, and component-maintenance
   fields.
2. Agent and repository adapters: role-language notes and source/package
   reader orientation.
3. `collaborative-posture-and-ethics`: posture floor and collaboration risk.
4. `engineering-methodology-and-process`: craft substrate and routing.
5. `ledger-verification-protocol`: evidence semantics.
6. `project-management`: lifecycle, planning layout, PM lifecycle, and close
   mechanics using ledgered verification.
7. Operational direct-load components: `code-audit-discipline`,
   `coverage-hardening-discipline`, `delegation-policy`, and
   `contribution-style-and-voice`.
8. Support assets: PM examples, anti-patterns, provenance/version notes,
   audit examples, `CONTRIBUTION-TICKET.md`, and protocol distribution
   guidance.

This order is not the same as user load order in every workflow. It is the
contract dependency order: gates and adapters constrain the shape first, then
posture/methodology establish the floor, then task-specific components load
only when relevant.

## Composed Collaboration-Framework Use

For composed collaboration-framework use, the load order is:

1. Load the top-level composer: `collaboration-framework` /
   `framework-entrypoint-and-routing`.
2. Read the compact safety floor:
   `collaborative-posture-and-ethics` summary plus
   `engineering-methodology-and-process` process summary.
3. Apply the route table:
   planning and close work routes to `project-management` plus
   `ledger-verification-protocol`; audit routes to `code-audit-discipline`
   and domain skills; coverage routes to `coverage-hardening-discipline` and
   domain skills; delegation decisions route to `delegation-policy`;
   upstream issue work routes to `contribution-style-and-voice`.
4. Apply central adapters:
   `agent-adapter-and-routing` for CC/CDC/Codex/Claude/operator terms and
   `repository-orientation-and-distribution` for source/package reader modes.
5. Load the selected component body and only the support assets it owns.

The top-level composer is thin but not link-only: it carries enough posture,
process, discovery, and route-table context for a broad session start, then
hands off to the selected component.

## Standalone Direct-Load Use

Each accepted direct-load component must be useful when loaded without the
composer. Standalone components include local prerequisites, central adapter
references, and package-local links.

| Direct-Load Surface | Minimum Load | Required Local Notes | Routes Out |
|---------------------|--------------|----------------------|------------|
| `collaborative-posture-and-ethics` | Posture component entrypoint and compact methodology dependency. | Agent-role note; source/package reader note. | Methodology for process; contribution for public voice. |
| `engineering-methodology-and-process` | Methodology entrypoint and route table. | Do not duplicate routed components; explain source/package modes. | PM, ledger, audit, coverage, delegation, contribution, and domain skills. |
| `ledger-verification-protocol` | Ledger entrypoint and ledger discipline guide/template. | CC/CDC verifier role note; evidence strength note. | PM lifecycle close guides and methodology. |
| `project-management` | PM family entrypoint / PM wayfinder. | Planning worktree and package reader note; ledger dependency note. | Ledger for evidence semantics; PM internal guides. |
| `code-audit-discipline` | Audit entrypoint and diagnosis-only audit guide. | Output-home note; domain skills loading note; role note. | Domain skills; contribution for ticket drafting; coverage only after audit is converted to implementation work. |
| `coverage-hardening-discipline` | Coverage entrypoint and hardening loop. | Compatibility/naming note; project-tool adapter note. | Domain skills and target project test tools. |
| `delegation-policy` | Delegation entrypoint and thinking-vs-lookup boundary. | Role-language adapter note. | Methodology or audit when broader process/review work appears. |
| `contribution-style-and-voice` | Contribution entrypoint plus `CONTRIBUTION-TICKET.md`. | Package-local template note; current-HEAD/source citation note. | Audit findings as inputs; posture for voice. |

## PM Lifecycle And Ledgered Verification

For PM lifecycle work:

1. Load `project-management` through the PM wayfinder.
2. Select project, arc, or slice scale.
3. Read canonical planning worktree and top-down planning guidance before
   opening work.
4. When closing, load `ledger-verification-protocol` before marking rows done.
5. Apply ledgered verification: evidence strength, row status, no-op/deferred
   handling, silent-drop checks, and bubble-up to the parent unit.
6. Write the proposed close report. CDC or another independent verifier later
   owns `cdc-verification.md` or equivalent verification evidence.

PM owns lifecycle and artifact layout. Ledger owns evidence semantics. This
keeps PM/ledger direction explicit and prevents duplicated closure rules.

## Audit And Coverage Sibling Use

Audit and coverage are sibling operational components:

- `code-audit-discipline` is diagnosis-only. It produces findings, severity,
  evidence, and synthesis. It can cite domain skills for correctness criteria
  and can route to contribution when an upstream ticket is the requested next
  artifact.
- `coverage-hardening-discipline` edits or directs test/code repair work to
  meet a measurable coverage target. It uses domain skills and target-project
  tooling.
- No broad quality wrapper is proposed for Arc04 acceptance. `D-08` and
  `OQ-04` should record the sibling decision or an explicit alternative.

## Delegation And Contribution Direct-Load Use

`delegation-policy` and `contribution-style-and-voice` are narrow direct-load
components:

- Delegation loads when deciding whether subagents or parallel lookup are
  appropriate. The main context retains thinking, editing, and review
  judgment.
- Contribution loads when drafting maintainer-facing issues, proposals, or
  questions. The `CONTRIBUTION-TICKET.md` support asset travels with it and
  must be package-local.

Both can be routed by methodology and composer, but neither depends on a PM
project being open.

## Reader Modes

Every accepted package contract must support these reader modes:

| Reader Mode | Composition Behavior |
|-------------|----------------------|
| Source clone | Source links may point to repository paths such as `docs/`, `templates/`, and `knowledge/`, but the text must distinguish source paths from package paths. |
| Generated zip | Links must resolve under the component zip root. The package path is non-final until Slice04 acceptance and Arc05 implementation. |
| Installed skill | The entrypoint must work when unzipped into an installed skill directory, without relying on the original source checkout. |
| CCDP-adjacent reader | CCDP references remain adjacent protocol-distribution references. They never imply that CCDP is bundled into an installable collaboration-framework skill. |

## Composition Path Summary

| Workflow | Start At | Then Load | Stop Condition |
|----------|----------|-----------|----------------|
| Broad session start | `collaboration-framework` composer | Compact posture/methodology floor, then one routed component. | The selected component owns the workflow. |
| Standalone posture or process | `collaborative-posture-and-ethics` or `engineering-methodology-and-process` | Only routed components requested by the task. | Do not expand to full composer unless the task becomes broad. |
| PM lifecycle | `project-management` PM wayfinder | `ledger-verification-protocol` for close/verify work. | Proposed-done remains pending until CDC verification. |
| Ledgered verification | `ledger-verification-protocol` | PM close guide only when lifecycle mechanics are needed. | Every row is done, deferred, or no-op with evidence. |
| Audit | `code-audit-discipline` | Relevant domain skills; contribution only for ticket output. | Diagnosis complete, no implementation edits by audit. |
| Coverage | `coverage-hardening-discipline` | Domain skills and repository test tooling. | Coverage gate or documented blocker. |
| Delegation | `delegation-policy` | Agent adapter note if role terms are ambiguous. | Delegation decision recorded. |
| Contribution | `contribution-style-and-voice` | `CONTRIBUTION-TICKET.md` support asset. | Maintainer-facing artifact complete. |
| Package reader orientation | Repository orientation adapter | Package/release gates and component-local path notes. | Reader knows source/package mode and correct package-local entrypoint. |
