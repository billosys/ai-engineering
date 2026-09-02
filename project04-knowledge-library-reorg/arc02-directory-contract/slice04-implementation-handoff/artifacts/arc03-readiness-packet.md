# Arc03 Readiness Packet

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
slice: slice04-implementation-handoff
artifact: arc03-readiness-packet
artifact-status: implementation handoff input
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Purpose

This Arc03 readiness packet synthesizes verified Arc02 evidence into the
implementation handoff for the future directory reorganization arc. It prepares
Arc03 implementation planning without opening Arc03, creating source-edit
slice packets, or authorizing source checkout edits.

## Verified Inputs

| Input | Status | Handoff use |
|-------|--------|-------------|
| Slice01 decision surface | verified-closed | Supplies the original target-layout decision surface, source/package option matrix, compatibility obligations, and source-edit boundary. |
| Slice02 accepted contract | verified-closed | Supplies the accepted target directory contract, source-package root contract, and operator decision register. |
| Slice03 migration plan | verified-closed | Supplies the migration sequence, validation matrix, and package-path exception policy. |

## Accepted Contract Summary

The accepted target directory contract for Arc03 implementation is:

- `README.md` remains a concise top-level route map.
- `docs/` is user-facing explanation about repository materials.
- `knowledge/` is the default substrate root for domain/tooling,
  framework/operational, method, and source/provenance material.
- `knowledge/<component>/` is the default Project02 component source-root
  family.
- `knowledge/collaboration-framework/` is the target composer source root when
  composer material moves out of top-level selected-file packaging.
- `knowledge/biome/` remains a multi-entrypoint source root.
- `templates/` remains top-level only for cross-cutting support templates.
- `protocols/ccdp/` remains a separate protocol/package surface.
- Top-level `SKILL.md`, `AGENTS.md`, and `CLAUDE.md` remain compatibility
  surfaces unless a later implementation decision changes them with evidence.

The accepted source-package root contract keeps source roots and package roots
separate. Package identity may follow frontmatter, accepted component names,
selected-file packaging, multi-entrypoint package behavior, or protocol
package behavior.

## Migration Sequence And Validation Matrix

The migration sequence starts with preflight/source-status work, then preserves
mechanical moves before prose rewrites. Arc03 should separate compatibility
shim decisions, wrapper and migration note work, package/list updates,
package-local link repair, package-path exception handling, and validation
gates into implementation-sized slices.

The validation matrix requires later source-edit slices to select applicable
gates from:

- source `status --short`;
- source `diff --check`;
- `make check-skills`;
- `make check-package-paths`;
- `make all`;
- `make collab-framework`;
- `make ccdp-package`;
- `make check-ccdp-package`;
- package-local link checks;
- generated package inspection;
- `README.md`, `SKILL.md`, `AGENTS.md`, and `CLAUDE.md` route review.

## Package-Path Exception Policy

The package-path exception policy is repair-before-exception. Persistent
package-path exceptions and accepted warnings require operator approval.
Every exception row must identify owner, reason, validation command,
expiration or no-expiration rationale, evidence pointer, operator approval
status, accepted warning text where applicable, and re-entry condition.

## Arc03 Entry Conditions

Arc03 may be opened after:

- Slice04 is verified-closed by CDC;
- Arc02 formal arc close confirms the target layout, path contract, migration
  plan, compatibility strategy, exception policy, source root, package root,
  atomic, and composite decisions compose;
- the operator authorizes Arc03 source-edit planning or accepts the formal
  Arc02 close as sufficient implementation input.

## Source-Edit Boundaries

This packet is not source-edit authorization. Arc03 implementation slices must
declare source-files-edited intentionally, use the source checkout on `main`,
and avoid mixing mechanical moves with prose rewrites. Arc04 owns end-user docs
prose, and Arc05 owns public vocabulary.

## Operator Gates

- Top-level `SKILL.md` remains unresolved until Arc03 chooses a validated shim,
  replacement route, or explicit no-shim implementation path.
- Persistent package-path exceptions and accepted warnings require operator
  approval.
- Any broad exception that covers more than one owner or package root requires
  operator approval.
- Any CCDP package-policy change requires operator approval.
- Any public-facing skill kind/topology language before Arc05 requires
  operator approval.

## Risks

- Moving composer material before resolving top-level `SKILL.md` compatibility
  could break the daily-driver composer route.
- Updating package lists before files exist could weaken validation.
- Treating package-path exceptions as fixes could hide broken package-local
  links.
- Mixing source moves with README/docs prose rewrites could obscure
  preservation evidence.
- Folding CCDP into installable skill packages would violate the accepted
  protocol separation.

## Re-Entry Conditions

- Re-enter Slice02 if `knowledge/<component>/` cannot preserve Project02
  component roles or composer behavior.
- Re-enter top-level `SKILL.md` decision before composer source moves if no
  validated shim, replacement route, or no-shim implementation path preserves
  load routes.
- Re-enter Slice03 if package-local link repair cannot keep exceptions narrow.
- Re-enter CCDP policy only if protocol validation cannot preserve
  `protocols/ccdp/` separation.
- Re-enter Arc05 if public vocabulary is needed to explain implementation
  behavior before Arc05 opens.

## Arc02 Composition Preparation

This packet prepares, but does not perform, the Arc02 composition check. The
formal arc close should verify that target layout, path contract, migration
plan, compatibility strategy, exception policy, source root, package root,
atomic, and composite decisions are present across the Arc02 artifacts.

This is not arc close.
