# Audit To Hardening Handoff

Use this guide when turning a completed diagnosis-only code audit into follow-up
work. It preserves the boundary that the audit does not modify code while
making the next testing or hardening slice actionable.

For audit setup and map, load
[`01-audit-scope-and-map.md`](./01-audit-scope-and-map.md). For finding format,
load [`02-findings-and-severity.md`](./02-findings-and-severity.md). For testing
and validation follow-up, load
[`../../testing/guides/01-testing-discipline.md`](../../testing/guides/01-testing-discipline.md)
and then the coverage or validation guide needed for the work.

## Boundary

The audit is diagnosis-only. A follow-up round applies fixes. Do not stage,
commit, or edit source files as part of the audit.

The handoff exists to keep diagnosis useful without silently converting audit
scope into remediation scope.

## Handoff Packet

Create a short handoff section in the index or a separate planning artifact for
the follow-up work. Include:

- Audit index path and date.
- Per-language report paths.
- Modernization synthesis path.
- Findings grouped by implementation owner or subsystem.
- Blocker and High findings first.
- Any finding that needs test coverage before implementation.
- Any modernization move that requires a compatibility layer or explicit
  behavior-change approval.
- Negative findings that should protect against unnecessary churn.

## From Finding To Work Item

Each implementation item should cite:

- Finding ID.
- File:line evidence.
- Severity.
- Scale.
- Concrete fix direction.
- Required validation gates.
- Whether the fix is local, cross-language, or project-wide.

Do not collapse multiple unrelated findings into one vague cleanup item. Do
group findings that share one root cause and can be fixed atomically.

## Testing And Validation Routing

Use the testing component after diagnosis:

- Load testing discipline for behavior-focused test design and failure triage.
- Load coverage hardening when audit findings reveal untested behavior or when a
  hard coverage threshold is part of acceptance.
- Load validation gates when selecting repository-native commands, CI checks,
  package checks, release checks, or generated-artifact inspections.

Root-cause repair remains the floor. Do not hide audit findings behind ignored
tests, softened assertions, broad mocks, or lower thresholds.

## Final Verification Checklist

Before treating the audit and handoff as complete, confirm:

- The audit map covers the repository shape and names generated/vendored
  exclusions.
- Every audited language had its matching skills and guides loaded.
- Detected languages without matching skills are listed in the index.
- Every finding has a stable ID, severity, scale, and file:line evidence.
- Every per-language report includes at least five negative findings.
- The modernization synthesis cites finding IDs and distinguishes local
  refactors, compatibility-layer work, and explicit behavior changes.
- The handoff keeps diagnosis separate from remediation.
- No source files were modified by the audit pass.
