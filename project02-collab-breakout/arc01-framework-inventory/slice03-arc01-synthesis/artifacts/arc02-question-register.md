# Arc 02 Question Register

```yaml
project: project02-collab-breakout
arc: arc01-framework-inventory
slice: slice03-arc01-synthesis
status: proposed-done
purpose: operator discussion and Arc 02 conceptual analysis input
architecture-decisions: none
```

## Basis

Slice 01 is verified-closed with `Rows: 7` and `Done: 7`. Slice 02 is
verified-closed with `Rows: 8` and `Done: 8`. The questions below are for
Operator and Arc 02 decision work. They are non-final and do not select the
accepted architecture.

## Conceptual Boundary Questions

### Q-01: Posture and methodology boundary

Owner: Operator and Arc 02.

Decision needed: Decide whether `collaborative-posture-and-ethics` is a
standalone component, a required dependency of
`engineering-methodology-and-process`, or both.

Why it matters: Splitting posture away from methodology can reduce load cost,
but methodology without the peer-frame basis may degrade into procedural
checklists.

Source evidence: Slice02 PSF-02; PSM-08; Slice01 inventory entries for
`docs/AI-CONSTITUTION-SUPPLEMENT.md` and
`docs/AI-ENGINEERING-METHODOLOGY.md`.

### Q-02: Methodology internal structure

Owner: Arc 02.

Decision needed: Decide whether substrate, 9-point SDLC, verification,
anti-degradation, audit, coverage, and delegation are one methodology
component or separate components connected by dependency edges.

Why it matters: The current monolith gives a coherent story, but it may hide
improper merge candidates and preserve monolithic load cost.

Source evidence: Slice02 PSM-01, PSM-03, PSM-05, PSM-12, and PSM-16.

### Q-03: Ledger versus project-management ownership

Owner: Arc 02 with Operator review.

Decision needed: Decide whether ledger owns evidence semantics while project
management owns lifecycle routing, and whether either component can be loaded
standalone.

Why it matters: Ledger and PM close deliberately overlap today. Without an
explicit owner and dependency edge, the overlap can become duplication and
drift.

Source evidence: Slice02 PSF-01; PSM-06; PSM-10; Slice01 inventory entries for
`templates/LEDGER-DISCIPLINE.md`, `docs/pm/04-closing-slices.md`, and
`docs/pm/05-closing-arcs.md`.

### Q-04: Project-management component granularity

Owner: Arc 02.

Decision needed: Decide whether the PM corpus is one component with internal
support assets, a family of components, or a thin wayfinder plus separately
loadable mechanics.

Why it matters: The PM split files have distinct load moments, but examples,
provenance, anti-patterns, and confirmation may be support assets rather than
primary components.

Source evidence: Slice01 source-to-concept map rows for all `docs/pm/*.md`;
Slice02 PSF-09; mechanism matrix rows for the PM labels.

### Q-05: Abstraction and ontology critique

Owner: Arc 02 and Operator.

Decision needed: Decide whether conceptual analysis needs a reusable
abstraction-boundary or ontology-critique discipline beyond the general
methodology.

Why it matters: Generalization and abstraction failure are named strongly, but
the current mechanisms are mostly review gates and human presence rather than a
focused decision protocol.

Source evidence: Slice02 PSM-05 and PSF-03.

## Functional And Package Constraint Questions

### Q-06: Top-level composer contract

Owner: Operator and Arc 02.

Decision needed: Decide what the top-level `collaboration-framework` entrypoint
must promise after breakout: composition routing only, posture summary,
mandatory safety floor, or a richer default bundle.

Why it matters: Existing users enter through `SKILL.md`; lowering load cost
cannot break the main runtime adapter.

Source evidence: Slice01 `SKILL.md` inventory entry; Slice02 PSM-02 and
PSM-16; Project02 project-plan definition of done.

### Q-07: Project01 package path contract

Owner: Operator and Arc 02.

Decision needed: Decide which Project01 source/package promises are hard
compatibility gates for every component package.

Why it matters: Component boundaries that break package-local links, zip roots,
source/package wording, or release-surface validation would regress the
accepted Project01 contract.

Source evidence: Slice01 `artifacts/project01-path-contract-notes.md`;
Slice02 PSM-10, PSM-11, and PSF-06.

### Q-08: Audit output placement

Owner: Arc 02.

Decision needed: Decide whether code audit owns `workbench/<DATE>-audit-*` for
standalone audits while ledgered slices inherit the slice-local `artifacts/`
home.

Why it matters: A code-audit component can reintroduce orphaned durable
planning evidence unless its output convention is scoped against PM rules.

Source evidence: Slice02 PSF-05; PSM-10; Slice01 project01 path-contract
notes.

### Q-09: Component contract fields

Owner: Arc 02 with Operator acceptance.

Decision needed: Decide whether every future component contract must name
scope, out-of-scope, load moment, dependencies, package behavior, source paths,
verification gates, and maintenance owner.

Why it matters: Monolithic load cost is a missing solution until components
have explicit contracts that are checkable by later implementation slices.

Source evidence: Slice02 PSM-16 and PSF-10; Project02 definition of done.

## Naming And Mislabel Risk Questions

### Q-10: Coverage guide name and generality

Owner: Arc 02 and Operator.

Decision needed: Decide whether `docs/CLAUDE-CODE-COVERAGE.md` should feed a
renamed, surface-neutral `coverage-hardening-discipline` component, or remain a
legacy Claude Code guide with adapted Codex notes.

Why it matters: A surface-specific filename and Rust/cargo-heavy examples may
mislead users about a discipline intended to generalize across repositories.

Source evidence: Slice02 PSF-04 and PSM-12.

### Q-11: Agent adapter ownership

Owner: Arc 02.

Decision needed: Decide whether Claude/Codex/CDC/CC translation belongs in one
adapter component, in the top-level `SKILL.md`, or repeated as local notes
inside each guide.

Why it matters: Repeating surface-adapter language creates drift, but hiding it
inside one entrypoint can make standalone components less usable.

Source evidence: Slice01 source-to-concept map `agent-adapter-and-routing`;
Slice02 PSM-09 and matrix row for `agent-adapter-and-routing`.

### Q-12: Component naming threshold

Owner: Operator and Arc 02.

Decision needed: Decide what makes a label a component rather than a problem
class, support asset, adapter, constraint, or package/release gate.

Why it matters: Arc 01 intentionally produced non-final labels. Arc 02 needs a
selection rule before it can avoid tidy but false component boundaries.

Source evidence: Slice02 PSF-10; mechanism coverage matrix; this slice's
`candidate-component-inputs.md`.

## Maintenance Implication Questions

### Q-13: Contribution guide and template packaging

Owner: Arc 02.

Decision needed: Decide whether contribution style and contribution ticket
template are one component with a support asset, two subcomponents under one
package, or two independently loadable components.

Why it matters: Style without template may be too abstract; template without
style may produce formulaic or overclaimed tickets.

Source evidence: Slice02 PSF-07 and PSM-14; Slice01 inventory entries for
`docs/CONTRIBUTION-STYLE.md` and `templates/CONTRIBUTION-TICKET.md`.

### Q-14: Post-breakout maintenance owner

Owner: Operator and Arc 02.

Decision needed: Decide how version history, examples, support assets, and
cross-file synchronization will be owned once the framework has multiple
components.

Why it matters: Project02 will increase the number of maintained surfaces.
Without an explicit maintenance contract, routing tables, package guidance, PM
rules, ledger rules, and README instructions can drift.

Source evidence: Slice02 PSM-15 and PSF-09; Slice01 inventory entries for
`docs/pm/08-maintenance.md`, `docs/pm/version-history.md`, README, and
`SKILL.md`.

### Q-15: Cross-component release gate

Owner: Operator and Arc 02.

Decision needed: Decide whether package/release gate checks are centralized in
the top-level framework, repeated per component, or both centralized and
component-specific.

Why it matters: Project01 made the release surface explicit. Project02 should
not let component extraction make package validation optional or ambiguous.

Source evidence: Slice01 `artifacts/project01-path-contract-notes.md`;
Slice02 PSM-11 and PSF-06; `candidate-component-inputs.md` package/release
gate section.

## Arc 02 Starting Criteria

Arc 02 can begin conceptual analysis once CDC verifies this Slice 03 close and
the Operator accepts that these questions are the right discussion set. The
question register is an input to Arc 02, not final architecture and not an
accepted component model.
