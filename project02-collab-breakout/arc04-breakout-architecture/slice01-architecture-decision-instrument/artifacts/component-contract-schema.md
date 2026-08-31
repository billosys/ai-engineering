# Component-Contract Schema

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice01-architecture-decision-instrument
status: proposed-done
schema-status: decision-instrument
architecture-decisions: none
```

## Input Contract

This component-contract schema is the mandatory field set later Arc04 slices
must fill for every candidate component, component family, support asset,
adapter, constraint, package/release gate, and non-component disposition. It
is grounded in the closed Arc02 conceptual model and Arc03 architecture inputs
but does not decide final architecture.

## Required Fields

Each candidate evaluation must fill these fields:

| Field | Required content |
|-------|------------------|
| `component name` | Proposed stable name, current label if different, and any compatibility alias. |
| `classification` | Candidate component, component family, support asset, adapter, constraint, package/release gate, dependency edge, non-component, or deferred question. |
| `purpose` | One-sentence purpose stated as observable behavior. |
| `owned problem` | The specific problem this component owns and why another component should not own it. |
| `boundary` | In-boundary responsibilities and out-of-boundary exclusions. |
| `reason-to-load` | Natural human or LLM trigger, direct-load value, minimum useful load, and context-cost comparison. |
| `dependency edges` | Required prerequisites, downstream users, and direction of dependency. |
| `wayfinding behavior` | How a reader reaches this component from the top-level composer, README, package, and related components. |
| `support assets and templates` | Templates, examples, checklists, or provenance files that travel with the component. |
| `adapter notes` | Role-language, source/package, repository-orientation, and tool-surface adapter requirements. |
| `source paths` | Current source path or paths that provide evidence and likely implementation input. |
| `package paths` | Proposed or candidate package path assumptions, marked non-final until accepted. |
| `package-local links` | Links that must resolve inside generated or installed packages. |
| `zip root assumptions` | Expected generated zip root and entrypoint behavior. |
| `release gates and validation commands` | Required Makefile or script checks, including `make check-package-paths` where applicable. |
| `maintenance owner` | Which component or surface owns future changes and cross-component synchronization. |
| `version history responsibility` | Which versioned file must receive updates when behavior changes. |
| `risk disposition` | Known risks, mitigations, deferrals, and required operator decisions. |
| `go / adjust / defer` | Current posture with evidence basis. |
| `operator acceptance` | Whether operator acceptance is required, obtained, or pending. |
| `Arc05 implementation-plan fields` | Source edits, README updates, `SKILL.md` entrypoints, package list changes, validation gates, migration notes, and rollback/review concerns needed later. |

## Contract Template

Later slices may copy this template into candidate-specific artifacts:

```markdown
## <Candidate Label>

- component name:
- classification:
- purpose:
- owned problem:
- boundary:
  - in:
  - out:
- reason-to-load:
- direct-load classification:
- dependency edges:
- wayfinding behavior:
- support assets and templates:
- adapter notes:
- source paths:
- package paths:
- package-local links:
- zip root assumptions:
- release gates and validation commands:
- maintenance owner:
- version history responsibility:
- risk disposition:
- go / adjust / defer:
- operator acceptance:
- Arc05 implementation-plan fields:
  - source edits:
  - README updates:
  - SKILL.md entrypoints:
  - packaging changes:
  - validation gates:
  - migration notes:
  - review concerns:
```

## Source And Package Rules

Source path and package path fields must remain distinct. A current source
file can be evidence for a component without becoming its final package path.
A package path can be proposed only as non-final until later Arc04 acceptance.

Every accepted component contract must preserve:

- source/package vocabulary;
- package-local links;
- zip root assumptions;
- README and `SKILL.md` wayfinding;
- Makefile packaging expectations;
- CCDP separation from installable skill bundles;
- `make check-package-paths` or successor package/release gate validation.

## Maintenance Rules

Each contract must name a maintenance owner. If no owner is named, the
candidate cannot be accepted because the breakout would create drift across
README, source docs, package entrypoints, support assets, templates, version
history, and release checks.

If a touched file has a Version History section, Arc05 must update it when
implementation changes behavior. If a touched component has no local version,
Arc05 must update the conceptually enclosing versioned file.

## Arc05 Implementation-Plan Fields

Arc04 does not implement source changes, but each accepted or adjusted
contract should hand Arc05 enough planning detail to write implementation
slices. Arc05 fields must include:

- exact source files likely to change;
- new or updated `SKILL.md` entrypoints;
- README and wayfinding updates;
- package list and generated zip implications;
- validation commands and gates;
- migration compatibility notes;
- unresolved risks or operator follow-up.
