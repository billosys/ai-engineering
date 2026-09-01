# Slice 03: Skill Kind and Topology Classification

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | A decision instrument defines skill or knowledge kind separately from composition topology, with source/evidence questions for each axis | `rg -n "kind axis|topology axis|atomic|composite|bridge/integration|application/task bundle|evidence question|classification rule|do not collapse" artifacts/skill-kind-topology-decision-instrument.md` | serious | slice-plan | open | | The instrument must prevent "atomic = domain" and "composite = framework" shortcuts. |
| F-2 | The classification matrix covers current packaged skill surfaces from the live source checkout and identifies source-backed evidence for each | `rg -n "knowledge/rust|knowledge/go|knowledge/cpp|knowledge/js|knowledge/erlang|knowledge/cobalt|knowledge/design|knowledge/tailwindcss|knowledge/deno|knowledge/biome|SKILL.md|source-backed|current packaged" artifacts/skill-kind-topology-classification-matrix.md` | serious | slice-plan | open | | Current surfaces come from source checkout evidence, not imported proposals. |
| F-3 | The classification matrix covers planned Project02 framework components and planned Project03 concept-card-method surfaces separately from current source surfaces | `rg -n "planned Project02|collaboration-framework|engineering-methods|project-management|work-verification|testing|code-auditing|agent-coordination|contribution-style|planned Project03|concept-card-method|not yet implemented|not live source" artifacts/skill-kind-topology-classification-matrix.md` | serious | slice-plan | open | | Planned surfaces must be labeled as planned, not current. |
| F-4 | Anchor and edge cases are tested explicitly: Rust, collaboration-framework, concept-card-method, Biome, JS/Deno/Biome, CCDP, and templates/support | `rg -n "Rust|collaboration-framework|concept-card-method|Biome|JS/Deno/Biome|CCDP|templates/support|edge case|candidate atomic|accepted composite" artifacts/skill-kind-topology-classification-matrix.md artifacts/public-language-implications.md` | serious | slice-plan | open | | Edge cases should expose taxonomy stress, not disappear into broad buckets. |
| F-5 | Public-language implications state vocabulary to use, vocabulary to avoid, and what Arc02 versus Arc05 should decide | `rg -n "vocabulary to use|vocabulary to avoid|Arc02|Arc05|skill kind|atomic|composite|public language|directory contract|README|docs" artifacts/public-language-implications.md` | correctness-grade | slice-plan | open | | Arc05 owns final public wording; Arc02 owns target directory contract. |
| F-6 | The artifacts preserve the external ontology rubric as tested input, not accepted taxonomy, and identify re-entry conditions for disputed classifications | `rg -n "external ontology rubric|tested input|not accepted taxonomy|re-entry condition|borderline|disputed classification|evidence would change" artifacts/skill-kind-topology-decision-instrument.md artifacts/public-language-implications.md` | correctness-grade | slice-plan | open | | Avoid turning prior research into authority without repository fit. |
| F-7 | No source checkout files are edited by this slice | `git -C /Users/oubiwann/lab/billosys/ai-engineering status --short` | serious | slice-plan | open | | Expected result: no output from the source checkout status command. |

## Closure

Slice remains open.

Rows: 7. Done: 0. Deferred: 0. No-op: 0.
