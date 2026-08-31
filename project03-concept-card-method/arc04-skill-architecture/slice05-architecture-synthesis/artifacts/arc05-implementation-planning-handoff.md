# Arc05 Implementation Planning Handoff

```yaml
project: project03-concept-card-method
from-arc: arc04-skill-architecture
from-slice: slice05-architecture-synthesis
to-arc: arc05-implementation-plan
status: proposed-done
mode: implementation planning handoff
```

## Purpose

This handoff gives Arc05 bounded implementation-planning input from the final
Arc04 v4.0 concept-card method skill architecture. It is not source
implementation and does not authorize source edit work by itself.

## Arc04 Decisions Arc05 Must Preserve

- SKILL.md remains a thin entrypoint: reason to load, positive load, negative
  load, problem ownership, dependency direction, and route to guides.
- The skill owns concept-card method representation and routes project
  management, generic source reading, domain correctness, source edits, and
  implementation planning to adjacent guidance.
- Guide files must preserve the concern split: load/routing, extraction,
  re-extraction and preservation, evidence lifecycle, graph/CQ,
  reconciliation, validation/verification, and memory admission.
- Template files must preserve user-authored, trace record, and result record
  surface classes.
- Example files must include the release-critical examples unless Arc05 records
  an explicit deferral: minimal card, claim-backed card, CQ coverage,
  relationship/edge, extraction-run trace, reconciliation, memory-admission,
  and five-agent default recipe.
- The five-agent workflow is a default recipe, not an invariant; extraction
  runs must record actual agent scope and parallel-worker provenance.
- Validation candidates are split into deterministic structural checks,
  semantic audit, human/operator review, and deferred runtime checks.
- Package behavior treats guides, templates, and release-critical examples as
  packaged surfaces; generated artifacts, executable validator, generated zip,
  package release, and release mechanics require Arc05 decisions.
- README and library text must preserve the promise boundary and must not
  imply runtime GraphRAG, graph database, ontology database, memory runtime,
  CCDP service, live extraction, executable validator, generated zip, package
  release, or source implementation behavior before implementation planning
  accepts that work.

## Implementation Planning Work Categories

| Category | Arc05 planning output needed |
|----------|------------------------------|
| source layout | Decide exact source layout for SKILL.md, guides, templates, examples, validation documentation, schemas, package metadata, and generated skill inputs. |
| source edit sequencing | Break source edit work into slices with explicit verification and no unstated package/release claims. |
| guide files | Decide filenames, guide boundaries, cross-links, and whether any guide is split or merged without violating the concern model. |
| template files | Decide template files, exact schema syntax, field names, examples, and rendered Markdown conventions. |
| example files | Decide exact example files, fixture source, release-critical coverage, optional example deferrals, and example verification. |
| schema | Decide schema syntax for cards, claims, source spans, source support, edges, CQs, extraction runs, validation result, verification result, reconciliation result, preservation decision, and memory admission records. |
| enum | Decide exact enum spelling for evidence grade, extraction confidence, verification state, reconciliation state, CQ status, validation result, and memory admission. |
| validator-code | Decide validator-code scope, language, entrypoint, failure messages, path handling, deterministic structural checks, and non-goals. |
| Makefile | Decide Makefile targets for skill validation, package path checks, generated zips, release gates, and CI integration. |
| package list | Decide package list edits and how the concept-card method skill enters the packaged skill/library distribution. |
| README | Decide README edits that explain the skill, supported package behavior, verification commands, and promise boundary. |
| library text | Decide skill library indexing, tags, description, reason to load, and discoverability text. |
| generated zips | Decide whether generated zips are produced, where, by which command, and how they are verified. |
| tests | Decide tests for schemas, templates, examples, validator-code, package paths, generated zips, README/library discoverability, and release gates. |
| release gates | Decide release mechanics, package release criteria, CI gates, and evidence required before claiming release readiness. |
| package updates | Decide package updates and how package behavior is checked against generated artifacts. |
| version history | Decide source version history updates for every changed source document, including enclosing versioned files where needed. |

## Unresolved Implementation Questions

Arc05 should answer these before source edits begin:

- What exact file layout should the skill use under the source checkout?
- Which guide files, template files, and example files are first-release
  required?
- Which source support locator and source span identity scheme is implemented?
- Which exact schema syntax and enum spelling become authoritative?
- Which deterministic structural validation candidates become validator-code?
- Does validator-code exist in the first implementation arc, or only
  documented validation candidates?
- Which Makefile and package list changes are required for package updates?
- What README and library text is sufficient for discoverability without
  runtime overclaims?
- Which generated zips are produced, and which tests or package-path checks
  verify them?
- What release gates must pass before package release or release readiness is
  claimed?
- Which source version history entries are required for each changed source
  file?

## Arc04 Close Rows

Arc05 should treat Arc04 arc-ledger rows A-6, A-7, and A-8 as formal arc-close
composition inputs, not as work for CC to close inside Slice05:

- A-6: composition verification for load contract, problem ownership,
  dependency direction, package behavior, and maintenance ownership.
- A-7: composition verification that concept card, claim, source support,
  evidence grade, verification, validation result, reconciliation, competency
  question, extraction run, memory admission, guide, template, and example
  surfaces preserve distinct constructs.
- A-8: composition verification that source edit, validator code,
  validator-code, README, Makefile, package, generated zip, implementation
  planning, and implementation-planning work are routed to Arc05.

Arc05 planning should begin only after formal arc close accepts those rows.

## Package/Discoverability Promise Boundary

The handoff preserves the package/discoverability promise boundary. Arc04 does
not promise runtime GraphRAG, graph database, ontology database, memory
runtime, CCDP service, live extraction, executable validator, generated zip,
package release, generated zips, release gates, package updates, source
checkout edits, or source implementation. Arc05 may plan some of those items
only after explicitly accepting them as implementation-planning work.

## Out of Scope

Out of scope for this handoff: source SKILL.md edits, source checkout edits,
source edit execution, validator-code implementation, deterministic validation
scripts, runtime services, GraphRAG, graph database, memory runtime, CCDP
service, live extraction, generated zips, package release, source
implementation, and the Arc04 arc-level closing-report.
