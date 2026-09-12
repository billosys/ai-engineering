---
project: project08-concept-card-metadata
status: active
depends-on: [project05-concept-card-skill]
blocks: []
related: [project03-concept-card-method, CompCogNeuro/book, ai-music-theory]
version: "1.1"
---

# Concept Card Metadata

Deliver concept cards that retain the early method's useful teaching bodies and
directly queryable concept relationships, generalize across source types, and
preserve the current evidence and lifecycle distinctions. Implement and exercise
the resulting skills against real sources until repeated extraction meets the
operator's quality bar. Metadata is the initial focus; card bodies and extraction
guidance are explicitly in scope throughout the project.

Project05 is formally closed in its recorded history. Subsequent use exposed
gaps that its package and bounded UAT evidence did not settle. This project owns
those gaps and their resolution. It does not inherit a presumption that the
current profile, its field names, or its body structure are sufficient.

## Basis And Design Status

The operator accepted this project name, the five-arc starting hypothesis, and
room for a potentially long Arc04 on 2026-09-12. The source checkout was clean at
`e763c661`; concept-cards reports `metadata.version: "4.8.1"`. The teaching-profile
changes are already in that baseline, not an uncommitted prototype. Historical
workbench reports retain their original 1.8.x labels; do not rewrite provenance
or infer an exact instruction match from a relabeled version alone.

The initial design hypothesis is recorded in
[the planning brief](./arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/planning-brief.md).
It combines directly usable discovery/graph metadata with scoped evidence and
lifecycle records. Exact fields, nesting, authorities and migration rules remain
research/design decisions. Arc02 will supply the accepted architecture artifact.

## Required Outcomes

- A complete historical/current metadata inventory and capability crosswalk,
  including values, types, meaning, query behavior and migration consequences.
  The operator's named fields are examples, not an exhaustive requirement list.
- A researched, readable metadata profile covering books, research papers,
  white papers, blog posts, and wiki/encyclopedia articles, with source identity
  distinct from format, edition/snapshot, location and extraction provenance.
- Directly machine-readable typed relationships and competency-question data
  that support useful traversal without parsing narrative prose. Preserve
  identity, direction, support, uncertainty and revision applicability.
- Flexible discovery/classification without imposing category/subcategory/tier
  on every domain, while preserving historical classification information.
- Explicit semantics for lifecycle summaries and evidence/result references,
  including unknown, unassessed, missing, conflicting and stale data. No false
  implication that a whole card inherits one claim's evidence or admission.
- Implemented concept-cards guidance, templates, examples, reference material,
  and the document-extraction handoff changes the evidence shows are needed.
  Preserve sibling support directories and single-purpose guides.
- Real, repeated CC extraction of body and metadata; comparison against the
  historical Complete Musician/Erlang cards and the same CompCogNeuro subset;
  source-type diversity checks; and evidence-driven refinements as needed.
- Full-book CompCogNeuro extraction after subset quality acceptance, with
  coverage and dependency reconciliation. The conditional gate is not a quiet
  deferral: failure returns to refinement; success opens the full-book slices.
- Fresh package/version/install checks and independent composition review,
  plus explicit operator acceptance of output quality before project closure.

## Arc Roadmap: Starting Hypothesis

| Arc | Capability | Depends On | Current State |
| --- | --- | --- | --- |
| `arc01-metadata-research-and-requirements` | Historical/current inventory, primary-source standards research, capability and no-loss requirements | Baseline and operator brief | Active; Slice01 Iteration 01 required after CDC review |
| `arc02-metadata-architecture` | Usable profile, field authorities, compatibility/migration and validation design | Arc01 | Hypothesis; detailed plan when near |
| `arc03-skill-and-template-updates` | Implemented profile and extraction handoffs with representative examples and focused checks | Arc02 | Hypothesis; detailed plan when near |
| `arc04-real-extraction-and-refinement` | Repeated real-source extraction, body/metadata refinements, cross-source trials and conditional full-book delivery | Initial Arc03 profile; feeds back into design and implementation | Intentionally expandable; no fixed slice count |
| `arc05-package-gates-and-closure` | Fresh packaging/install evidence, migration and UAT reconciliation, independent project acceptance | Arc04 quality and coverage evidence | Closure cannot outrun UAT |

These arcs can split, grow or be resequenced when findings justify it. Arc04 can
change skills and revisit Arc02 decisions through newly scoped slices; Arc03's
completion does not freeze implementation. Record additions and superseded
assumptions in plan histories and ledgers. A coherent new capability may warrant
an additional arc rather than overloading Arc04.

## Arc04 Operating Contract

Plan each next slice using the findings from the previous run. A normal sequence
is protocol/baseline capture, CC extraction, independent comparison and operator
review, targeted source refinement, then extraction in a fresh CC session. Keep
execution units bounded while allowing arbitrarily many such slices.

Require at least three new, separately identified CC extraction runs during
Arc04, including at least two fresh sessions on the final candidate profile and
the same bounded CompCogNeuro input. This is a minimum for observing consistency,
not an automatic stop count. Historical workbench outputs are comparison inputs
and do not satisfy the new-run requirement. A material change after a successful
run requires fresh evidence against the changed profile.

Pin source snapshots, skill files and hashes, prompts, actual loaded routes,
model/settings where available, tools, task scope, and output locations. Keep
prior answers and review conclusions out of fresh extraction contexts; give
them to the comparison context afterward. Record unavoidable contamination or
configuration differences. Count all attempts, including failed runs, and retain
their raw outputs before any manual correction. Label edited outputs separately.

Before generation, define anchored qualitative criteria for definitions,
construction/recognition, concrete examples, common errors, relationship richness,
source fidelity, metadata completeness, graph use, and usability. Section counts,
YAML parsing, verbosity and package gates are supporting observations, not quality
verdicts. Match the original subset for controlled comparisons; use historical
music/Erlang cards as quality references with cross-domain limitations recorded.

Inspect metadata and prose together. Exercise prerequisite traversal, extension,
contrast and related-concept queries from structured fields with a disposable
local harness. Verify edge direction, missing endpoints, cycles and uncertain
relations against expected results; a production graph server is unnecessary
for this acceptance evidence. Include the operator's fugue prerequisite question
as a motivating query and source-grounded analogues for the trial corpus.

Use representative bounded samples spanning all five source types named above;
choose actual accessible/licensed sources and controls before their runs. Separate
type from format, and test locator/identity behavior for the preparation formats
the profile claims to support. Do not force every source to contain a chapter,
page number, procedure, or other inapplicable feature.

Once repeated subset runs satisfy the agreed criteria and the operator accepts
their body and metadata quality, open full-book slices. Account for every chapter,
appendix and dependency with explicit disposition, stable concept identities,
duplicate/boundary reconciliation, cross-chapter edges and review coverage.
Sampling cannot be relabeled full-book extraction. Full-book findings can reopen
refinement and require affected subset/full-book reruns. An unavailable input or
capacity limit is an unresolved condition with a re-entry plan, not proof of done.

## Scope And Version Boundaries

The expected concept-cards delivery range is 4.9.x, continuing the released 4.x
line from 4.8.1. Recheck the live authority on each implementation slice. Design
compatibility and explicit migration within that intent; do not conceal a breaking
change to fit a version number. Escalate a genuine conflict with the version
intent as a recorded design decision. Other skills own their own versions.

Focused parsers, validation fixtures, migration demonstrations and local graph
query checks are in scope when required to prove the profile. Decide the form
of any shipped schema/validator in Arc02; do not inherit Project05's exclusion
as an obstacle to this project's requirements. A general ontology-engineering
skill remains a future possibility, not a prerequisite to completing this work.

Production graph DB, MCP/RAG service deployment and automatic memory admission
remain downstream. Preserve the data and query capability needed for them.
Publishing releases, installing into managed user directories and changing
unrelated skills require their own applicable scope. Install smoke uses an
explicit temporary `INSTALL_DIR`.

## Closure And Plan Changes

The sibling [ledger](./ledger.md) governs acceptance. Formal closure requires
independent composition evidence and the operator's explicit quality decision.
Do not discharge a substantive gap as a no-op merely because current guidance
mentions the topic: compare generated behavior and explain the observed result.
Record each finding, affected requirements, source fix or justified disposition,
and rerun evidence. Add slices before advancing past unresolved failures.

No fixed timeline, slice count or green package report overrides these outcomes.
Reducing a required capability or moving unfinished quality work to a future
project requires an explicit operator decision recorded in the plan.

## Version History

- 1.1 (2026-09-12): Slice01 CDC review requires a Fennel helper replacement,
  complete field dispositions, corrected counts, reproducible commands and
  refreshed source availability. Operator language preference and commit hold
  are recorded in AGENTS.md. Was: Slice01 ready for its initial CC run.

- 1.0 (2026-09-12): Operator-authorized Project08 opening. Adopts five provisional
  arcs, the 4.8.1 baseline and 4.9.x intent, broad metadata preservation, body
  refinement, uncapped Arc04 slices, separate CC runs and conditional full-book
  extraction. Addresses quality gaps surfaced after Project05 closure.
