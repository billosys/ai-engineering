# Source-Edit Authorization Register

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice01-preflight-source-status-impact-map
artifact: source-edit-authorization-register
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Purpose

This source-edit authorization register distinguishes the current
preflight-only planning work from later source-edit slices. It prevents the
preflight baseline from being mistaken for implementation authorization.

## Current Authorization

| Work item | Authorized now | Boundary |
|-----------|----------------|----------|
| Arc03 Slice01 preflight status and impact map | yes | Planning files only in the Slice01 directory: artifacts, ledger, and closing report. |
| Source checkout edits | no | Not authorized now. The source checkout remains untouched by this slice. |
| Later Arc03 source-edit slices | no | Authorized later only by each slice's accepted prompt and explicit source scope. |
| Arc04 end-user docs | no | Arc04 owns end-user docs; Arc03 must not silently fold that prose work into source moves. |
| Arc05 public vocabulary | no | Arc05 owns public vocabulary; public skill kind/topology language before Arc05 requires operator gate. |

## Proposed Later Slice Register

| Proposed later source-edit slice | Authorized later condition | Required operator gate or evidence |
|----------------------------------|----------------------------|------------------------------------|
| Top-level `SKILL.md` compatibility decision | Authorized later only after a slice chooses and validates one path | Operator gate remains for top-level SKILL.md until Arc03 records a validated shim, replacement route, or no-shim decision. |
| Mechanical collaboration-framework move | Authorized later after compatibility path is resolved | Must preserve daily-driver composer behavior, source prose, `CF_FILES`, and package root behavior. |
| Project02 component root moves | Authorized later after source scope names concrete roots | Must preserve component roles and independent loadability under `knowledge/<component>/`. |
| Method/provenance moves | Authorized later after source scope names concrete Project03-approved material | Must avoid claiming live source for material that remains planning/provenance only. |
| Template ownership pass | Authorized later after source scope distinguishes owner-local and cross-cutting templates | Top-level `templates/` remains for cross-cutting support unless a concrete owner-local move is validated. |
| Biome multi-entrypoint validation pass | Authorized later after source scope names Biome entrypoints | Must preserve Biome multi-entrypoint behavior explicitly. |
| CCDP separation pass | Authorized later after source scope names CCDP routes or package checks | CCDP package-policy changes require operator gate; CCDP remains separate from installable skill packages. |
| Package/list update pass | Authorized later after moved files exist | Must update `Makefile`, `CF_FILES`, `ALL_SKILL_FILES`, `INSTALL_ZIPS`, and package targets only as evidence requires. |
| Package-local link repair pass | Authorized later after package checks identify broken package-local links | Repair before adding exceptions. |
| Package-path exception pass | Authorized later only after repair evidence exists | Persistent package-path exception rows, accepted warning rows, and broad exception rows require operator gate. |
| Arc03 implementation reconciliation | Authorized later after prior source-edit slices produce evidence | Must confirm source status, diff hygiene, validation gates, package roots, and compatibility surfaces compose. |

## Operator Gates

The following decisions are not authorized now and require explicit operator
approval or an accepted later slice:

- top-level SKILL.md compatibility path;
- validated shim for top-level `SKILL.md`;
- replacement route for top-level `SKILL.md`;
- no-shim implementation path for top-level `SKILL.md`;
- persistent package-path exception rows;
- accepted warning rows that remain after repair attempts;
- broad exception rows that cover more than one owner or package root;
- CCDP package-policy changes;
- public-facing skill kind/topology language before Arc05.

## Ordering And Separation

- Source status and impact mapping must precede source edits.
- Top-level `SKILL.md` compatibility must be resolved before composer moves.
- Mechanical moves before prose rewrites.
- Package-local link repair before exceptions.
- CCDP remains separate under `protocols/ccdp`.
- Biome multi-entrypoint behavior remains explicit.
- Arc04 owns end-user docs.
- Arc05 owns public vocabulary.

## Boundary Statement

This source-edit authorization register is not source-edit authorization for
the source checkout. It authorizes only this preflight-only planning packet and
states that later source-edit slices are not authorized now.
