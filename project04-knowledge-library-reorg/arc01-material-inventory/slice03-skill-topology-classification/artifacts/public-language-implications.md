# Public Language Implications

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
slice: slice03-skill-topology-classification
artifact: public-language-implications
artifact-status: slice classification evidence
created-on: 2026-09-01
source-files-edited: false
```

## Purpose

This artifact records vocabulary guidance for later README, docs, and skill
wayfinding work. It does not write final public language. Arc05 owns final
public wording after Arc02 decides the directory contract and later arcs land
source/package changes.

## Vocabulary to Use

Use these terms when repository evidence supports them:

| Term | Use |
|------|-----|
| skill kind | The "what is it about?" axis: domain/tooling, framework/operational, method, protocol/package, support/template, or source/provenance. |
| topology | The "how is it composed?" axis: atomic, composite, bridge/integration layer, or application/task bundle. |
| domain/tooling skill | A loadable skill for a language, toolchain, linter, design discipline, or platform. |
| framework/operational skill | A loadable skill for planning, verification, testing, auditing, coordination, contribution, or collaboration posture. |
| method skill | A loadable skill for a reusable knowledge-work method, such as planned `concept-card-method`. |
| atomic skill | A skill with one bounded load reason and a coherent vocabulary, activities, constraints, and failure model. |
| composite skill | A skill whose identity is composing, routing, sequencing, or governing multiple loadable components. |
| bridge/integration layer | A surface whose value is interoperability, translation, routing, or connecting package/workflow boundaries. |
| application/task bundle | A local task arrangement or recipe that combines domain and task concerns for one workflow. |
| protocol package | A separately distributed protocol surface such as CCDP, with package rules distinct from installable skill zips. |
| support template | A reusable skeleton or payload owned by a skill, method, framework component, or protocol package. |
| current source surface | A surface that exists in `/Users/oubiwann/lab/billosys/ai-engineering` now. |
| planned surface | A Project02 or Project03 planning surface that is accepted or proposed but not yet implemented in source. |

## Vocabulary to Avoid

Avoid language that collapses kind and topology or overclaims source state:

| Avoid | Reason |
|-------|--------|
| "Atomic means domain skill." | Domain/tooling skills are often atomic, but the topology must be proved from load reason and package/entrypoint behavior. |
| "Composite means framework skill." | Some framework/operational components, such as `project-management` or `code-auditing`, may be atomic operational methods. |
| "Method skills are composite." | `concept-card-method` is a borderline method skill; current evidence supports provisional atomic method classification with composite pressure. |
| "All knowledge lives in docs." | Project04 direction is that `docs/` explains the library while `knowledge/` holds substrate and skill source material where appropriate. |
| "All framework material is documentation." | Slice01 showed current `docs/` contains framework/operational source and method material. |
| "`concept-card-method` is available." | It is planned Project03 work, not yet implemented and not live source. |
| "CCDP is a skill." | CCDP is currently a separate protocol/package surface, not an installable skill package. |
| "`collaboration-framework` is deprecated." | Project02 explicitly preserves it as the daily-driver composer and accepted composite anchor. |
| "Package root always equals source root." | Current package roots follow frontmatter names and selected package behavior; `knowledge/biome/` already has two package roots. |

## How to Talk About Surface Types

Atomic skills:

- Say an atomic skill has one bounded load reason and can satisfy its primary
  user need without acting as a router over other independently loadable
  components.
- Use Rust as the candidate atomic example, with the caveat that broad does not
  mean composite.

Composite skills:

- Say a composite skill earns the label when composition is its identity:
  selecting, sequencing, routing, or governing multiple components.
- Use `collaboration-framework` as the accepted composite example and preserve
  the daily-driver composer language.

Bridge/integration layers:

- Say a bridge/integration layer connects domains, tasks, protocols, package
  surfaces, or governance layers.
- Use CCDP as a protocol/package bridge and use `engineering-methods` or
  `agent-coordination` only with caveats until implementation clarifies their
  entrypoint behavior.

Application/task bundles:

- Say an application/task bundle is a local arrangement or recipe for a
  workflow, not automatically a full skill kind.
- Use Project03's five-agent concept-card workflow as a task recipe, not as
  the topology of the whole `concept-card-method` skill.

Protocol packages:

- Say protocol packages have their own source and package validation, separate
  from installable skill zips.
- Keep CCDP language tied to `protocols/ccdp/`, `ccdp.zip`,
  `make ccdp-package`, and `make check-ccdp-package`.

Support templates:

- Say support templates are reusable payloads or skeletons that may be
  package-local to their owning skill/component.
- Do not call templates standalone skills unless they gain accepted `SKILL.md`
  entrypoints and package behavior.

## Arc02 Responsibilities

Arc02 must decide the target directory contract before final public language:

- whether framework/operational components live under `knowledge/`, top-level
  component roots, or another source family;
- whether method skills such as `concept-card-method` live under
  `knowledge/`;
- whether atomic and composite skill source roots share one convention;
- how multi-entrypoint roots such as `knowledge/biome/` are represented;
- whether top-level templates remain cross-cutting or move under owning
  component/method roots;
- which current `docs/` files move, remain, or become wrapper docs;
- how generated package roots relate to source roots and frontmatter names;
- how package-local links, package-path exceptions, `AGENTS.md`, `CLAUDE.md`,
  README routes, and CCDP separation are preserved.

## Arc05 Responsibilities

Arc05 should reserve final public wording until after Arc02 and source
implementation evidence exist. It should turn this slice's classifications
into README and docs wording only after:

- Arc02 accepts the directory contract;
- source moves or wrappers are implemented where required;
- `Makefile`, package roots, `ALL_SKILL_FILES`, `INSTALL_ZIPS`, and package
  validators reflect the accepted layout;
- `concept-card-method` is either still explicitly planned or actually
  implemented;
- CCDP still has separate protocol/package validation;
- `collaboration-framework` still reads as the active daily-driver composer.

## Public Language Risks

Risk: README or docs imply `concept-card-method` is already implemented. Impact:
users will look for `knowledge/concept-card-method/` or
`concept-card-method.zip` before they exist. Mitigation: say "planned method
skill" until implementation lands and package validation passes.

Risk: CCDP becomes a skill package accidentally. Impact: protocol package
validation and skill package validation will blur, and `make install` could
overclaim protocol installability. Mitigation: keep CCDP described as a
protocol/package surface with separate `ccdp.zip` and checks.

Risk: `collaboration-framework` sounds deprecated. Impact: it contradicts the
accepted composite architecture and weakens the daily-driver route. Mitigation:
describe specialist components as independently loadable without demoting the
composer.

Risk: public docs collapse kind and topology. Impact: users infer false rules
such as domain equals atomic or framework equals composite. Mitigation: use
skill kind and topology as separate terms wherever both are discussed.

Risk: docs and README claim package roots before Arc02 settles source/package
contracts. Impact: later source moves will require public retractions.
Mitigation: Arc05 owns final public language after directory contract and
package evidence are in place.

## External Rubric Boundary

The external ontology rubric is tested input, not accepted taxonomy. Public
language should not cite it as final authority. If a disputed classification
appears, record a re-entry condition and state what evidence would change it:
load reason, entrypoint shape, package behavior, component ownership, source
root, generated package root, or validation behavior.
