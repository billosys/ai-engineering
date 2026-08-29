# Arc 01 Closing Report: Distribution Path Contract

```yaml
project: project01-harmonise-paths
arc: arc01-distribution-path-contract
status: closed
closed-by: CDC
closed-on: 2026-08-29
composition-verdict: delivered
```

## Capability Restated

Arc 01 exists to establish the distribution path contract for ai-engineering
package artifacts: inventory current package-path failures, classify path
semantics, design the validation gate, and make that contract executable.

## Composition Verdict

Composition verdict: delivered.

The three slices compose into the promised capability:

- Slice 01 produced and CDC-verified the package path audit across all 12
  generated skill zips.
- Slice 02 produced and CDC-verified the contract gate design.
- Slice 03 implemented and CDC-verified `make check-package-paths` against
  generated zips, with stable classifications and a transitional exception
  policy.

The implementation gate is verified as a source working-tree diff, not as a
source commit. Planning records this explicitly so downstream work does not
silently assume a committed implementation baseline.

## Slice Walk

### Slice 01: Package Path Audit

Outcome: delivered and CDC-verified.

Evidence:

- `slice01-package-path-audit/2026.08.29-package-path-audit.md`
- `slice01-package-path-audit/cdc-verification.md`

The audit rebuilt and scanned all 12 `INSTALL_ZIPS` archives and reproduced
145 actionable package-context misses.

### Slice 02: Contract Gate Design

Outcome: delivered and CDC-verified.

Evidence:

- `slice02-contract-gate-design/2026.08.29-contract-gate-design.md`
- `slice02-contract-gate-design/cdc-verification.md`

The design selected generated zips as the authoritative validation surface,
`make check-package-paths` as the public entry point,
`scripts/check-package-paths` as the no-suffix parser script, and
`package-path-exceptions.tsv` as the exception policy file.

### Slice 03: Package Path Gate Implementation

Outcome: delivered and CDC-verified.

Evidence:

- `slice03-package-path-gate-implementation/cdc-verification.md`
- `slice03-package-path-gate-implementation/artifacts/`

The gate scans all 12 generated skill zips and currently reports 0 hard
failures, 426 warnings, 3 explicit exceptions, 656 skipped external URLs, and
parser-suppressed material omitted by the Markdown parser.

## Arc Ledger Walk

### A-1

Status: done.

Slice 01 has CDC verification at
`slice01-package-path-audit/cdc-verification.md`.

### A-2

Status: done.

The inventory covers all generated zips. Slice 01 CDC verification reproduced
the full 12-zip audit, and Slice 03 CDC verification reproduced the executable
gate over 12 generated zips and 171 Markdown files.

### A-3

Status: done.

The observed mismatch vocabulary is established and executable:
bundled-reference, source-clone-reference, repo-only/provenance,
example-project path, external URL, parser false positive, plus hard internal
unclassified handling in the gate.

### A-4

Status: done.

The contract routes later changes by fix type: source edits, staging-time
transforms, package layout changes, validation exceptions, and CCDP package
work. Slice 03 makes those categories visible through warnings, explicit
exceptions, and hard-failure behavior.

### A-5

Status: done.

Slice 02 was opened from Slice 01 findings and then CDC-verified.

### A-6

Status: done.

Slice 03 was opened from the verified Slice 02 design and used the default
slice `artifacts/` home for durable implementation evidence.

### A-7

Status: done.

Slice 03 has CDC verification at
`slice03-package-path-gate-implementation/cdc-verification.md`.

## Silent-Drop Diff

Scope as specified:

- package path failure inventory;
- source/package path contract;
- validation gate design;
- executable Make-owned package path gate;
- bubble-up disposition for later harmonisation and CCDP work.

Scope delivered:

- all specified Arc 01 pieces delivered.

Silent drops: none known.

Deferred:

- current warning burn-down and path harmonisation move to Arc 02;
- CCDP package target work remains in Arc 03;
- release-facing workflow documentation remains in Arc 04;
- source implementation commit is outside this planning close unless the
  operator commits the current working-tree implementation separately.

## Bubble-up to Project 01

Arc 01 delivers the distribution path contract capability promised in the
project roadmap.

The project plan should now move Arc 02 from stub to active detailed planning.
Arc 02 should treat the 426 current warnings as visible harmonisation work, not
as resolved package paths. The first Arc 02 slice should target small,
high-confidence bundled-reference reductions where one path spelling works in
both source and package contexts, especially under-developed tooling skill
entrypoints.

No project scope change is required. Arc sequencing remains valid:
distribution contract before skill bundle harmonisation, then CCDP packaging,
then release/adoption hardening.

## What Worked / What Recurred

What worked:

- slice-local `artifacts/` kept durable evidence close to the owning slice;
- generated zips as the validation surface kept the contract tied to the real
  distribution artifact;
- transitional warnings made path debt visible without blocking the first gate.

What recurred:

- source implementation state needs an explicit commit or preserved working
  tree before downstream slices depend on it;
- package warnings are now numerous enough that Arc 02 should burn them down in
  small classes, not one large sweep.

## Closure

Composition verdict: delivered. Gate reviewed by: CDC. Slices: 3, matching the
arc-plan breakdown. Findings dispositioned: 4. Deferred: 4, all routed to Arc
02, Arc 03, Arc 04, or operator source-commit handling.
