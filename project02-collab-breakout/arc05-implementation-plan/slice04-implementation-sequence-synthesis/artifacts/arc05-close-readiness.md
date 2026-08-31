# Arc05 Close-Readiness

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice04-implementation-sequence-synthesis
status: proposed-done
artifact-status: Arc05 close-readiness
source-files-edited: false
```

## Readiness Verdict

Arc05 will be ready to close after Slice04 CDC verification, assuming CDC
reproduces the Slice04 ledger rows and confirms source files remain untouched.
At that point, the remaining Arc05 action is formal arc close with a
composition check against the arc ledger, not another planning slice.

## Evidence Basis

- Slice01 is verified-closed and produced the implementation surface map plus
  release validation surface map.
- Slice02 is verified-closed and produced the component contract matrix,
  component file layout plan, migration plan, package/source contract
  register, and support adapter dependency plan.
- Slice03 is verified-closed and produced the package target plan, README
  wayfinding plan, skill entrypoint validation plan, package-path/link/
  exception plan, migration compatibility plan, and Slice04 implementation
  sequence inputs.
- Arc04 records the operator-accepted architecture and all eight accepted
  component names.
- Slice04 now provides the implementation sequence roadmap, source-edit risk
  register, validation matrix, acceptance gate plan, and implementation prompt
  packet.

## Remaining Open Questions

These are source implementation decisions, not blockers to Arc05 close:

- Whether the top-level `SKILL.md` compatibility shim expires after one source
  implementation cycle or stays for a named compatibility window.
- Whether the Makefile component-package logic uses a generic helper or
  explicit per-component rules.
- Whether `testing` and `code-auditing` land in one source slice or split into
  two commits for review size.
- Which package-path warnings remain after link repair and therefore require
  bounded exception rows.

## Deferrals

- Source implementation is deferred until Arc05 close or explicit operator
  authorization.
- Memory admission remains deferred future research, not a Project02
  component.
- CCDP changes are deferred unless a later source implementation slice touches
  CCDP surfaces; CCDP separation remains intact.

## Source Files Remain Untouched

This planning slice did not edit source checkout files. The required evidence
is:

```text
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
```

The command passes when the source checkout has no tracked diff. Slice04 also
keeps all durable planning artifacts under the slice-local `artifacts/`
directory.

## Arc05 Close Inputs

Formal Arc05 close should verify:

- A-1 and A-2 input rows from the arc ledger.
- A-3 through A-6 child close rows, including Slice04 CDC verification.
- A-7 composition: all eight components and cross-cutting gates are covered by
  Slice01-Slice04 outputs.
- A-8 boundary: Arc05 preserved the planning-only boundary and source checkout
  cleanliness.

## Ready-To-Close Statement

After CDC verifies Slice04, Arc05 is ready to close as a delivered planning
arc. It has no known remediation slice requirement. Source implementation
should still require a fresh operator go decision because Arc05 planned the
work; it did not start it.
