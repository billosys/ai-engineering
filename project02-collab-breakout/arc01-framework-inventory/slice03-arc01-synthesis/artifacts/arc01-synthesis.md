# Arc 01 Synthesis

```yaml
project: project02-collab-breakout
arc: arc01-framework-inventory
slice: slice03-arc01-synthesis
status: proposed-done
architecture-decisions: none
candidate-labels: non-final, not accepted architecture
evidence-basis:
  - ../slice01-source-inventory/cdc-verification.md
  - ../slice02-problem-solution-map/cdc-verification.md
```

## Evidence Basis

Slice 01 is verified-closed. CDC recorded `Rows: 7`, `Done: 7`,
`Deferred: 0`, and `No-op: 0` in
`../slice01-source-inventory/cdc-verification.md`.

Slice 02 is verified-closed. CDC recorded `Rows: 8`, `Done: 8`,
`Deferred: 0`, and `No-op: 0` in
`../slice02-problem-solution-map/cdc-verification.md`.

This synthesis consumes those verified artifacts:

- `../slice01-source-inventory/artifacts/framework-source-inventory.md`
- `../slice01-source-inventory/artifacts/source-to-concept-map.md`
- `../slice01-source-inventory/artifacts/project01-path-contract-notes.md`
- `../slice02-problem-solution-map/artifacts/problem-solution-map.md`
- `../slice02-problem-solution-map/artifacts/mechanism-coverage-matrix.md`
- `../slice02-problem-solution-map/artifacts/problem-solution-findings.md`

Current source files were not edited. Source files were only used through the
citations preserved in the verified Slice 01 and Slice 02 artifacts.

## Arc 01 established

Arc 01 established a source-backed evidence base for the collaboration
framework breakout:

- The current source corpus is known: `README.md`, `SKILL.md`,
  `docs/AI-CONSTITUTION-SUPPLEMENT.md`,
  `docs/AI-ENGINEERING-METHODOLOGY.md`,
  `docs/PROJECT-MANAGEMENT.md`, every current `docs/pm/*.md` file,
  `templates/LEDGER-DISCIPLINE.md`, `docs/CODE-AUDIT.md`,
  `docs/CLAUDE-CODE-COVERAGE.md`, `docs/SUBAGENT-DELEGATION-POLICY.md`,
  `docs/CONTRIBUTION-STYLE.md`, and `templates/CONTRIBUTION-TICKET.md`.
- The current framework has 26 non-final candidate labels from Slice 01 and
  Slice 02. Those labels are evidence handles, not final component boundaries.
- Slice 02 mapped 16 historical or functional problem classes to current
  mechanisms, source evidence, fit assessments, and follow-up questions.
- Slice 02 produced 10 critical findings covering overlap, duplication,
  underfit, overfit, mislabel candidates, improper merge candidates, improper
  split candidates, and missing solution areas.
- Project01 path/package constraints are accepted as cross-cutting gates for
  later work, not a component: preserve the source/package vocabulary,
  package-local Markdown links, zip-root behavior, `make check-package-paths`,
  generated skill package expectations, CCDP as a separate protocol package,
  and the standard planning artifact home.

## Undecided

Arc 01 did not decide final architecture. The following remain Undecided and
must be handled by Arc 02 conceptual analysis and operator discussion:

- Which labels are candidate components, which are support assets, and which
  are only problem classes or release constraints.
- Whether posture and methodology remain together, split into separately
  loadable pieces, or form a dependency relation.
- Whether ledger verification is its own component, a subcomponent of project
  management, or both a standalone component and a dependency of PM close.
- Whether project-management material should remain one component with
  internal support assets, or split into scale model, worktree layout, open
  planning, close/bubble-up, confirmation, anti-patterns, maintenance, examples,
  and provenance pieces.
- Whether code-audit and coverage hardening are sibling code-quality
  components or one broader quality-floor component with specialized guides.
- Whether contribution style and ticket template are one component with a
  support asset or two independently loadable components.
- Whether agent-adapter wording belongs in the top-level framework entrypoint,
  in every operational guide, or in one surface-neutral adapter.
- Which package promises from Project01 are hard compatibility gates for every
  future component package.

These are not final, not decided, and not accepted architecture.

## Inputs for Arc 02

Arc 02 should evaluate candidate boundaries using at least five axes:

- Reason to load: a component should have a distinct moment when a human or LLM
  needs it without needing the rest of the monolith.
- Problem ownership: a component should own a real problem class rather than a
  convenient file boundary.
- Dependency direction: overlapping mechanisms should say which component owns
  the base rule and which component specializes or routes to it.
- Package behavior: a component must have a package-local path story that can
  pass Project01's source/package gate.
- Maintenance ownership: version history, examples, templates, and provenance
  should travel with the component that owns the rule they support.

Candidate areas that deserve Arc 02 analysis:

- `collaborative-posture-and-ethics`
- `engineering-methodology-and-process`
- `project-management-*` as a possible component family
- `ledger-verification-protocol`
- `code-audit-discipline`
- `coverage-hardening-discipline`
- `delegation-policy`
- `contribution-style-and-voice` with `contribution-ticket-template`
- `framework-entrypoint-and-routing` as the likely top-level composer or
  adapter rather than a domain component

## Risks carried forward

- Mislabel risk: `CLAUDE-CODE-COVERAGE.md` appears broader than its name and
  examples imply; `agent-adapter-and-routing` may be buried in `SKILL.md`
  rather than owned explicitly.
- Improper merge risk: posture, methodology, substrate, verification, audit,
  and coverage may be merged because the monolith narrates them together, not
  because a user always needs them together.
- Improper split risk: contribution style and ticket template, PM examples and
  PM provenance, and PM close guidance and ledger evidence semantics may lose
  correctness if separated without explicit dependency edges.
- Overlap and duplication risk: ledger, PM close, methodology, and code audit
  all name silent drops, spec-softening, partial adoption, and evidence
  discipline. Arc 02 must decide deliberate reinforcement versus duplication
  likely to drift.
- Underfit risk: generalization and abstraction failure are named clearly but
  do not yet have a focused ontology or abstraction-decision protocol.
- Missing solution risk: monolithic load cost remains unresolved until Project02
  accepts component contracts and package behavior.
- Package/release risk: splitting source files without a component-level
  release surface could break package-local links, zip roots, reader guidance,
  or `make check-package-paths`.

## Readiness Verdict

Ready to close after independent CDC verification. Based on CC-attested
evidence, Arc 01 has produced the inventory, problem map, candidate
classification inputs, constraint list, and operator questions needed for Arc
02 conceptual analysis.

No remediation slice is required before Arc 02 can begin, provided CDC
reproduces the Slice 03 ledger and agrees that this synthesis did not select
final architecture.

Arc 01 still needs the normal arc-close step after Slice 03 CDC verification:
the arc ledger has to close, the slices must be checked for composition, and
the arc-to-project bubble-up must be written at arc scale.
