# Skill Kind and Topology Decision Instrument

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
slice: slice03-skill-topology-classification
artifact: skill-kind-topology-decision-instrument
artifact-status: slice classification evidence
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
created-on: 2026-09-01
source-files-edited: false
```

## Purpose and Scope

This instrument classifies repository surfaces on two separate axes:

- the kind axis: what the surface is about or what work it supports;
- the topology axis: how the surface composes knowledge, skills, packages, or
  supporting material.

The instrument is for Project04 planning. It is not final public taxonomy and
does not decide Arc02's final directory contract. It converts the external
ontology rubric into tested input against repository evidence and records where
borderline or disputed classification needs later re-entry.

## Source Inputs Used

Planning inputs:

- `project-plan.md`
- `ledger.md`
- `artifacts/external-ontology-rubric-research.md`
- `arc01-material-inventory/arc-plan.md`
- `arc01-material-inventory/ledger.md`
- `arc01-material-inventory/slice01-source-surface-inventory/cdc-verification.md`
- `arc01-material-inventory/slice01-source-surface-inventory/artifacts/current-source-surface-map.md`
- `arc01-material-inventory/slice01-source-surface-inventory/artifacts/material-role-classification.md`
- `arc01-material-inventory/slice01-source-surface-inventory/artifacts/source-validation-surface-map.md`
- `arc01-material-inventory/slice02-imported-architecture-integration/cdc-verification.md`
- `arc01-material-inventory/slice02-imported-architecture-integration/artifacts/imported-architecture-evidence-map.md`
- `arc01-material-inventory/slice02-imported-architecture-integration/artifacts/prior-proposal-register.md`
- `arc01-material-inventory/slice02-imported-architecture-integration/artifacts/project04-integration-conflicts-and-questions.md`

Source checkout inputs inspected from
`/Users/oubiwann/lab/billosys/ai-engineering`:

- `README.md`
- `SKILL.md`
- `knowledge/*/SKILL*.md`
- `knowledge/*/`
- `templates/`
- `protocols/ccdp/`
- `Makefile`
- `package-path-exceptions.tsv`

## Kind Axis Definitions

The kind axis asks what the surface is about. Classify kind before directory
placement and before topology.

| Kind | Definition | Repository adjustment |
|------|------------|-----------------------|
| domain/tooling | A bounded programming language, platform, toolchain, design discipline, linter, or professional practice area. | Current `knowledge/*` skills mostly fit here: Rust, Go, C++, JavaScript/Deno, Erlang/OTP, Cobalt, Visual Design, Tailwind CSS, Deno lint, and Biome linting. |
| framework/operational | A way to coordinate work, planning, evidence, review, quality gates, collaboration posture, testing, auditing, agent coordination, or contribution workflow. | Current top-level `SKILL.md` and planned Project02 components fit here. Some are narrow enough to be atomic despite being operational. |
| method | A reusable procedure for producing, checking, reconciling, or preserving knowledge. | Planned `concept-card-method` fits here. Some current `docs/dev/` material is method or extraction guidance but not a current packaged skill. |
| protocol/package | An interoperable protocol or separately distributed specification with its own package behavior. | CCDP fits here. It is a protocol/package surface, not an installable skill package. |
| support/template | Reusable scaffolding that supports a skill, method, framework, protocol, or contribution workflow without being a full loadable skill by itself. | `templates/GUIDE.md`, `templates/LEDGER-DISCIPLINE.md`, `templates/CONTRIBUTION-TICKET.md`, and protocol templates fit here. |
| source/provenance | Primary, copied, generated, or derived material preserved because it substantiates a knowledge substrate or historical decision. | `sources/`, `extraction-metadata/`, `concept-cards/`, `workbench/`, and some `docs/dev/` material fit here as secondary roles. |

Repository evidence adds one caution: validation and compatibility surfaces
such as `Makefile`, `package-path-exceptions.tsv`, `scripts/check-package-paths`,
`AGENTS.md`, and `CLAUDE.md` are not skill kinds. They are source/package
contract surfaces that constrain later layout decisions.

## Topology Axis Definitions

The topology axis asks how the surface is put together and what a loader or
reader receives from it.

| Topology | Definition | Repository test |
|----------|------------|-----------------|
| atomic | One bounded load reason, one primary discourse or practice community, coherent vocabulary, recognizable activities, constraints, and failure modes. It may point to adjacent guidance, but its main contract stands alone. | Rust is the candidate atomic anchor: current source has one `knowledge/rust/SKILL.md`, one package, and a domain-local guide payload for Rust work. |
| composite | A composed whole whose identity depends on selecting, sequencing, routing, governing, or reconciling multiple independently meaningful components or loadable units. | `collaboration-framework` is the accepted composite anchor because Project02 preserves it as the daily-driver composer over specialist components. |
| bridge/integration layer | A connector between domains, tasks, package surfaces, or governance layers. It may not own a complete domain or method; its value is translation, routing, or interoperability. | CCDP is a protocol bridge; `engineering-methods` and `agent-coordination` have bridge pressure because they connect process, gates, roles, and other skills. |
| application/task bundle | A local arrangement of domain plus task knowledge for one workflow, product need, or operational recipe. It can be useful without being a general domain or framework. | The five-agent concept-card workflow is a task recipe, not the whole `concept-card-method` topology. Some future examples may fit this topology. |

Do not collapse topology into size. Atomic can be broad. Composite can be lean.
Bridge/integration can be small but load-bearing. An application/task bundle
can be narrow and still require multiple inputs.

## Evidence Questions

Kind-axis evidence questions:

1. What work does the user load or read this surface to perform?
2. Does it name a domain, toolchain, method, protocol, workflow, template, or
   provenance source?
3. Does the surface own correctness norms for a field, or does it own process
   and coordination norms?
4. Does it include a `SKILL.md` or `SKILL*.md` entrypoint, or is it support
   material consumed by another entrypoint?
5. Is its package behavior installable skill behavior, separate protocol
   package behavior, or source-only provenance?
6. What source paths, README routes, Makefile targets, or package exceptions
   corroborate the kind?

Topology-axis evidence questions:

1. Can the load reason be stated without naming several other loadable units as
   required parts?
2. Does the surface own one coherent vocabulary and failure model, or does its
   value depend on choosing and sequencing other components?
3. Does it have one entrypoint and one package, multiple entrypoints in one
   source root, or a selected-file package assembled from several roots?
4. Is a route table, component map, orchestration contract, or package bridge
   necessary to explain it?
5. Would removing composition behavior merely simplify the surface, or destroy
   its identity?
6. Are external protocol, memory, validation, or runtime concerns internal
   topics, adjacent routes, or required independent components?

## Classification Rules

Classification rule 1: record current versus planned status before kind or
topology. A planned Project02 or Project03 surface is not live source.

Classification rule 2: classify the kind axis from load reason and problem
ownership, not from current folder name.

Classification rule 3: classify the topology axis from composition behavior,
not from kind. Do not collapse "domain/tooling" into "atomic" or
"framework/operational" into "composite."

Classification rule 4: allow secondary roles in caveats. A surface can be
domain/tooling with provenance subdirectories, framework/operational with
method guides, or protocol/package with support templates.

Classification rule 5: prefer package and entrypoint evidence for current
packaged surfaces. `Makefile`, `ALL_SKILL_FILES`, `INSTALL_ZIPS`, and
`pack_skill` show what is currently packaged.

Classification rule 6: planned surfaces use accepted planning artifacts as
evidence, not source checkout claims.

Classification rule 7: protocol/package and support/template surfaces should
not be called skills unless they have accepted skill entrypoints and package
behavior.

Classification rule 8: borderline cases remain actionable. Record what
evidence would change the classification and route final public language to
Arc05 after Arc02 settles the directory contract.

## Borderline and Re-Entry Conditions

Re-entry condition: a current atomic classification should reopen if a future
entrypoint becomes a router over multiple independently loadable components.

Re-entry condition: a composite classification should reopen if a future source
layout removes the route table or component map and leaves one coherent,
self-contained load reason.

Re-entry condition: a bridge/integration classification should reopen if the
surface becomes a full domain or method owner rather than a connector.

Re-entry condition: an application/task bundle classification should reopen if
the local task recipe becomes a reusable method skill with its own vocabulary,
failure model, and package behavior.

Re-entry condition: any classification should reopen if `Makefile`,
`ALL_SKILL_FILES`, `INSTALL_ZIPS`, generated zip roots, README route language,
or package-path validation changes the load/package contract.

Re-entry condition: any disputed classification should reopen when Arc02
chooses a target source root that contradicts this slice's package or source
assumptions.

Evidence would change a classification when it changes load reason, entrypoint
shape, package behavior, component ownership, or whether composition is
identity-defining.

## External Rubric Status

The external ontology rubric is tested input, not accepted taxonomy. It is
useful because it forces Project04 to ask about discourse boundary,
activities, relations, constraints, interdisciplinary integration, bodies of
knowledge, and method/practice separation before looking at folders. It
becomes Project04 vocabulary only where repository evidence supports it and
where Arc05 later accepts public language.
