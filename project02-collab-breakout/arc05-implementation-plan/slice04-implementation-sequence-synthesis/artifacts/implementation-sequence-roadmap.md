# Implementation Sequence Roadmap

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice04-implementation-sequence-synthesis
status: proposed-done
artifact-status: implementation sequence roadmap
source-files-edited: false
```

## Grounding

This roadmap consumes verified Slice01 implementation surface evidence,
verified Slice02 component contract and file-layout evidence, verified
Slice03 package target, README wayfinding, skill-entrypoint, package-path,
and migration compatibility evidence, and the Arc04
operator-accepted architecture recorded in
`operator-accepted-architecture.md`.

The ordered source-edit slices below are a future implementation plan only.
They do not authorize source edits from this planning slice.

## Accepted Components

The source implementation must cover all eight accepted components:

- `collaboration-framework`
- `engineering-methods`
- `project-management`
- `work-verification`
- `testing`
- `code-auditing`
- `agent-coordination`
- `contribution-style`

## Sequencing Rules

1. Establish component roots and compatibility before removing or moving old
   source paths.
2. Create component `SKILL.md` files and sibling `version-history.md` files
   before wiring `ALL_SKILL_FILES`.
3. Perform mechanical move and copy work before broad new prose so preservation
   can be reviewed separately from rewrite decisions.
4. Change Makefile package targets, `INSTALL_ZIPS`, `CF_FILES`, and generated
   zip behavior only after component payloads exist.
5. Update README route text after package roots, installed routes, and source
   paths are stable.
6. Repair package-local links before adding any `package-path-exceptions.tsv`
   row.
7. Validate generated zip output after Makefile targets and package-local
   links exist.
8. Keep CCDP separation throughout; CCDP gates are conditional on touching
   CCDP source or package surfaces.

## Ordered Source-Edit Slices

| Order | Source-edit slice | Dependency | Scope | Commit boundary | Validation checkpoint |
|-------|-------------------|------------|-------|-----------------|-----------------------|
| 1 | Component skeletons and source compatibility baseline | Arc05 CDC verification and explicit operator authorization to begin source implementation. | Create the eight component roots, component-local `SKILL.md` entrypoint stubs, sibling `version-history.md` files, initial `guides/`, `templates/`, and `examples/` directories where planned. Keep top-level `SKILL.md` as a transitional source-checkout compatibility shim that routes to `collaboration-framework/SKILL.md`; do not package the shim as the generated composer payload. | One commit containing only skeleton files plus the top-level compatibility shim change if the operator confirms the shim. | `scripts/check-skill-description.sh` on new entrypoints, `git diff --check`, and source checkout cleanliness before staging. |
| 2 | Mechanical move of direct-mapping components | Slice 1 skeletons. | Move or copy direct source material for `project-management`, `work-verification`, and `contribution-style`: PM guides/examples, ledger template and work-verification guides, contribution guides, and `CONTRIBUTION-TICKET.md`. Preserve old source path lineage in version histories. | One commit for mechanical move/copy and package-local link repair for these direct components. | `git diff --check`, source/provenance review, package-local link scan, and direct entrypoint description check. |
| 3 | Composer posture extraction and route table | Slices 1-2, with direct components available as route targets. | Build `collaboration-framework/SKILL.md` as the daily-driver composer, extract posture guides from current `SKILL.md` and `docs/AI-CONSTITUTION-SUPPLEMENT.md`, add `guides/component-route-table.md`, and route to every specialist component by installed-skill wording rather than cross-package relative links. | One commit for composer and posture files. | `scripts/check-skill-description.sh collaboration-framework/SKILL.md`, package-local link review, `git diff --check`. |
| 4 | Engineering methods and release-gate guides | Slices 1-3, Project01 package-path contract, Slice03 package plan. | Split `docs/AI-ENGINEERING-METHODOLOGY.md` into `engineering-methods` guides, add `guides/05-component-boundary-analysis.md`, and add `guides/06-source-package-release-gates.md` covering source/package/release gates, package-path policy, generated zip rules, and component contract obligations. | One commit for `engineering-methods` source and version history. | Entry point check, route/link scan, `git diff --check`; no Makefile list change yet unless the implementation slice explicitly includes it. |
| 5 | Testing and code-auditing components | Slices 1-4. | Move/split `docs/CLAUDE-CODE-COVERAGE.md` into `testing` guides and `docs/CODE-AUDIT.md` into `code-auditing` guides. Preserve old prompt name references as migration compatibility notes while making accepted component names primary. | One commit, or two commits if the source diff is large enough that testing and code-auditing should be reviewed separately. | Entry point checks, source-prose preservation review, package-local link scan, `git diff --check`. |
| 6 | Agent coordination expansion | Slices 1-5. | Move/split `docs/SUBAGENT-DELEGATION-POLICY.md` into `agent-coordination/guides/01-when-to-delegate.md`, add new context-packet and result-integration prose, and carry CC/CDC/operator terminology in `agent-coordination/SKILL.md`. | One commit for agent-coordination source and version history. | Entry point check, terminology search for CC/CDC/operator, `git diff --check`. |
| 7 | Makefile component package integration | Component payloads from slices 1-6. | Add component package targets for `engineering-methods`, `project-management`, `work-verification`, `testing`, `code-auditing`, `agent-coordination`, and `contribution-style`; keep `make collab-framework` for the composer; update `COMPONENT_ZIPS`, `INSTALL_ZIPS`, `ALL_SKILL_FILES`, `CF_FILES`, aggregate behavior, install behavior, and help text. | One commit for Makefile/package mechanics only. | `make check-skills`, every component package target, `make collab-framework`, `make all`, and `git diff --check`. |
| 8 | README wayfinding and migration notes | Stable component roots, package roots, installed routes, and Makefile target names. | Update README for composed use, standalone component usefulness, source checkout, generated zip, unzipped/install, installed skill routes, old source path migration, old prompt names, and CCDP separation. | One commit for README and migration notes. | README link scan, `make check-package-paths`, `git diff --check`. |
| 9 | Package-path exceptions and link hardening | README and package-local links from slices 2-8. | Repair package-local links in all component packages, then update `package-path-exceptions.tsv` only for intentional source-only, provenance, example-project, external URL, or checker false-positive cases with a reason and expiration. | One commit for link repairs and explicit exception rows. | `scripts/check-package-paths --check-exceptions-only package-path-exceptions.tsv` if supported by the live script, `make check-package-paths`, and accepted-warning review. |
| 10 | Generated package acceptance sweep | All source/package/README/link changes. | Build final generated zip artifacts, inspect zip roots and payloads, confirm `collaboration-framework.zip` is composer-only, confirm all seven specialist generated zips exist, and confirm `ccdp.zip` remains outside skill install behavior. Generated zips remain ignored release artifacts unless release policy explicitly changes. | One commit only if source fixes are needed; otherwise no source commit. | `make all`, `make collab-framework`, component package targets, `make check-skills`, `make check-package-paths`, source checkout cleanliness after cleanup, and conditional `make ccdp-package` / `make check-ccdp-package` only if CCDP changed. |

## Dependency Rationale

The sequence front-loads compatibility and mechanical preservation so source
readers and reviewers can separate move/copy preservation from new component
writing. It delays Makefile and README work until package roots and
entrypoints exist, which reduces `INSTALL_ZIPS`, `ALL_SKILL_FILES`, and
`CF_FILES` drift. It delays `package-path-exceptions.tsv` until after link
repair because exceptions should record intentional package-contract decisions,
not avoidable broken links.

## Component Coverage Check

| Component | First source slice | Package slice | Reader route slice |
|-----------|--------------------|---------------|--------------------|
| `collaboration-framework` | Slice 1 skeleton, Slice 3 composer/posture. | Slice 7 keeps `make collab-framework` and composer zip. | Slice 8 README and installed `/collaboration-framework` route. |
| `engineering-methods` | Slice 1 skeleton, Slice 4 methods/gates. | Slice 7 adds `engineering-methods.zip`. | Slice 8 README and installed `/engineering-methods` route. |
| `project-management` | Slice 1 skeleton, Slice 2 mechanical move. | Slice 7 adds `project-management.zip`. | Slice 8 README and installed `/project-management` route. |
| `work-verification` | Slice 1 skeleton, Slice 2 mechanical move/copy. | Slice 7 adds `work-verification.zip`. | Slice 8 README and installed `/work-verification` route. |
| `testing` | Slice 1 skeleton, Slice 5 coverage split. | Slice 7 adds `testing.zip`. | Slice 8 README and installed `/testing` route. |
| `code-auditing` | Slice 1 skeleton, Slice 5 audit split. | Slice 7 adds `code-auditing.zip`. | Slice 8 README and installed `/code-auditing` route. |
| `agent-coordination` | Slice 1 skeleton, Slice 6 expansion. | Slice 7 adds `agent-coordination.zip`. | Slice 8 README and installed `/agent-coordination` route. |
| `contribution-style` | Slice 1 skeleton, Slice 2 mechanical move/copy. | Slice 7 adds `contribution-style.zip`. | Slice 8 README and installed `/contribution-style` route. |
