# Arc03 Functional Model

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice04-functional-synthesis
status: proposed-done
model-status: analytical, non-final, not accepted architecture
architecture-decisions: none
```

## Input Contract

This functional model consumes verified Arc03 evidence from Slice01, Slice02,
and Slice03:

- Slice01 CDC verification, the `scenario matrix`, the
  `functional-analysis method`, the usage-surface inventory, and the Arc03
  input register.
- Slice02 CDC verification, the `current-workflow` evaluation, the
  `load-path friction` register, the `functional-deficiency` register, and the
  `source/package role-language` notes.
- Slice03 CDC verification, the `minimum-load` matrix, the
  `dependency-adapter` findings, standalone and composition evaluations, and
  Arc03 functional decision inputs.

It also consumes the closed Arc02 `conceptual model`, boundary and naming
findings, operator decision register, and closing report as candidate-boundary
evidence. Arc02 evidence is not accepted architecture; this artifact does not
decide final component boundaries, source moves, package paths, or operator
acceptance.

## Model Summary

The current collaboration framework is functionally a rich composer: it gives
human and LLM users a durable posture and process floor, then routes them into
project management, ledger discipline, code audit, coverage hardening,
delegation, and contribution workflows. That shape works for broad session
start and ambiguous work, but it is over-rich for narrow work such as "close a
slice" or "draft an upstream issue." The breakout direction supported by
Arc03 is not a set of arbitrary file moves. It is a load model:

- Keep a thin top-level composer for discovery, human orientation, skill
  loading, and combination workflow routing.
- Promote strongly evidenced narrow workflows to direct-load surfaces.
- Preserve dependency order where a standalone surface would otherwise become
  over-thin.
- Carry source/package and role-language adapter behavior into every accepted
  component contract.

The model remains non-final and architecture deferred to Arc04.

## Functional Surfaces

| Surface | Current behavior | Functional finding | Arc04 implication |
|---------|------------------|--------------------|-------------------|
| Direct source reading | A reader starts in README, `SKILL.md`, docs, templates, and planning files in a source-clone. | Source-clone reading is viable but depends on distributed source/package guidance and repo-local context. | Arc04 should preserve a source-clone adapter or README/SKILL route for each accepted component. |
| Packaged skill reading | A reader loads the generated skill zip or an installed unzipped skill. | Packaged skill reading needs package-local links, coherent zip root behavior, and a small entrypoint. | Every component contract should name package-local entrypoint files, support assets, and release surface checks. |
| Skill loading | An LLM loads `/collaboration-framework` or a future narrower component. | Skill loading works best when the minimum useful load is small, dependencies are explicit, and adapter notes are local enough to avoid role-language confusion. | Direct-load components need concise `SKILL.md` surfaces plus dependency links. |
| Human orientation | A human reader needs the purpose, package shape, and maintenance expectations. | Human orientation currently lives mostly in README plus top-level `SKILL.md`; after breakout it must not be available only in the monolith. | Arc04 needs a repository-orientation adapter and per-component source/package cues. |
| Session start | The current composer provides posture, methodology, and routing at session start. | This is a valid broad entrypoint, but context cost is high for narrow tasks. | Thin composer with compact posture/process floor is favored over retaining the rich monolith. |
| Planning | Project planning uses PM wayfinder, scale model, canonical planning worktree, top-down planning, and ledger discipline. | Project management behaves as a component family with internal guides; splitting every guide as a top-level component is not functionally proven. | Arc04 should treat PM as a family first and decide package granularity explicitly. |
| Execution | Execution uses methodology, project plans, slice prompts, repository instructions, and domain skills. | Execution benefits from the composer, but most task-specific execution should direct-load a domain or operational component. | Component dependency edges must distinguish method, PM lifecycle, and domain skill loading. |
| Review | Review uses code-audit, ledger evidence language, domain skills, and sometimes coverage guidance. | Review is not the same workflow as coverage hardening; audit is diagnosis-only while coverage can edit tests/code. | Audit and coverage should remain sibling operational candidates unless Arc04 deliberately creates a quality family. |
| Audit | Code audit has a strong direct load moment, but audit output-location rules need repair after the `workbench/` to slice `artifacts/` convention. | The audit surface is strong but needs adapter and output-location correction before implementation. | Arc04 should classify audit as go / adjust, not plain go. |
| Coverage | Coverage hardening has a real workflow but current title/examples are Claude/Cargo-shaped. | Coverage is plausible to strong as a component, but naming and examples are underfit for the general framework. | Arc04 should adjust naming or add a surface-neutral adapter. |
| Delegation | Delegation policy has a narrow, low-cost, strongly evidenced direct load path. | It works as a standalone operational rule set and should retain Codex/Claude role-language clarity. | Arc04 can treat delegation as strong direct load with minimal adapter notes. |
| Contribution | Contribution guidance plus ticket template has a strong direct load path. | The template is a support asset, not a separate component. Style without the template is less actionable; the template without style risks overclaiming. | Arc04 should package contribution guidance with `CONTRIBUTION-TICKET.md` as a support asset. |
| Combination workflow | PM plus ledger, posture plus methodology, audit plus domain skills, contribution plus template, and coverage plus repo tooling are real composed flows. | Composition reduces over-thin risk when dependency order is explicit; hidden dependencies recreate current routing friction. | Arc04 should encode dependency edge ownership and component contract fields. |

## Direct-Load Classifications

Strong direct load:

- `ledger-verification-protocol`, because row closure, evidence strength,
  deferral/no-op discipline, and silent-drop prevention are coherent even
  outside the full PM lifecycle.
- `delegation-policy`, because the narrow rule set has low context cost and a
  clear trigger.
- `contribution-style-and-voice` when shipped with the
  `contribution-ticket-template` support asset.
- `code-audit-discipline`, with the adjustment that artifact homes and
  role-language adapter notes must match the current planning convention.

Plausible direct load:

- `coverage-hardening-discipline`, because the workflow is real but naming,
  examples, and language-neutral routing need adjustment.
- `collaborative-posture-and-ethics`, because posture is a strong dependency
  and session-start floor, but Arc04 still needs to decide whether it is a
  standalone component or a required summary inside the composer.
- `engineering-methodology-and-process`, because it owns the craft substrate
  but should route rather than duplicate PM, ledger, audit, coverage,
  delegation, and contribution mechanics.
- `project-management` as a family, because PM has real direct-load demand but
  not every current PM guide is proven as a separately loadable component.

Weak direct load or non-component on current evidence:

- `verification-methodology`, better modeled as shared ontology and dependency
  edge across methodology, ledger, PM close, audit, and coverage.
- `path-contract-constraints`, better modeled as source/package constraint and
  package/release gate rather than a user-facing component.
- `planning-confirmation-protocol`, PM examples, and PM provenance, better
  treated as PM support assets unless future evidence proves direct use.
- Ontology critique and component-maintenance discipline, both important but
  not yet proven as direct-load workflows in Arc03.

## Dependency And Adapter Model

The functional model depends on explicit dependency edge direction:

- Posture precedes methodology.
- Methodology routes to PM, ledger, audit, coverage, delegation, and
  contribution without absorbing their full mechanics.
- PM close mechanics use ledger verification semantics; PM owns lifecycle and
  bubble-up behavior while ledger owns evidence language and row closure.
- Audit uses domain skills and evidence discipline while preserving
  diagnosis-only scope.
- Coverage uses repository tooling and domain test idioms.
- Contribution style owns the ticket template as a support asset.
- Source/package behavior, package-local links, zip root behavior, release
  surface documentation, CCDP separation, and `make check-package-paths` apply
  as package/release gate constraints across all accepted components.

Role-language handling is an adapter requirement. A central agent adapter plus
short local component notes is functionally stronger than central-only routing
or fully repeated instructions, because standalone components must be readable
by CC, CDC, Codex, Claude, and human operators without forcing the whole
composer to load.

## Arc04 Use

Arc04 can use this model as a functional input, not as final architecture. The
model says which workflows have real usage surfaces, which are dependency
edges, which are support assets, which are adapters, which are constraints,
and where go / adjust / defer posture is justified. Operator acceptance remains
required before any implementation planning or source/package change.
