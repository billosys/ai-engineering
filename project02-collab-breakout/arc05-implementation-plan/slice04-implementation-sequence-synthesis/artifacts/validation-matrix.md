# Validation Matrix

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice04-implementation-sequence-synthesis
status: proposed-done
artifact-status: validation matrix
source-files-edited: false
```

## Grounding

This validation matrix consumes verified Slice01 release validation evidence,
verified Slice02 package/source contracts, verified Slice03 package target and
package-path plans, and the operator-accepted architecture. It maps commands
to the surfaces and failure modes they prove during future source
implementation.

## Command Matrix

| Command | Run when | Surface proved | Failure mode caught | Required gate |
|---------|----------|----------------|---------------------|---------------|
| `git diff --check` | Every source-edit slice before commit. | Whitespace integrity for the touched implementation plan or source files. | Trailing whitespace, conflict markers, or formatting noise. | Required for every source implementation commit and this planning close. |
| `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | Before Arc05 close and before source implementation entry. | Source checkout cleanliness. | Planning slice accidentally edits source files or source implementation starts from a dirty tree. | Required before Slice04 close and source implementation start. |
| `scripts/check-skill-description.sh <component>/SKILL.md ...` | Before Makefile validation lists include new component entrypoints. | Component `SKILL.md` frontmatter and description length. | New entrypoint too large or malformed before aggregate wiring. | Required in early component source slices. |
| `make check-skills` | After `ALL_SKILL_FILES` includes all eight component entrypoints. | Aggregate skill-entrypoint validation. | Component `SKILL.md` omitted from validation or description too long. | Required after Makefile package integration and before implementation acceptance. |
| `make collab-framework` | After composer files and `CF_FILES` change. | Composer package target and `collaboration-framework.zip` behavior. | Composer package missing `SKILL.md`, posture guides, route table, or package root. | Required for the composer and final acceptance. |
| `make engineering-methods` | After the package target exists. | `engineering-methods.zip` component package. | Missing methods/gates payload, wrong package root, or entrypoint packaging failure. | Required component package target. |
| `make project-management` | After the package target exists. | `project-management.zip` component package. | Missing PM guides/examples or wrong package root. | Required component package target. |
| `make work-verification` | After the package target exists. | `work-verification.zip` component package. | Missing ledger guides or `templates/LEDGER-DISCIPLINE.md`. | Required component package target. |
| `make testing` | After the package target exists. | `testing.zip` component package. | Missing testing/coverage/validation gate guides. | Required component package target. |
| `make code-auditing` | After the package target exists. | `code-auditing.zip` component package. | Missing audit scope, severity, scale, modernization, or handoff guides. | Required component package target. |
| `make agent-coordination` | After the package target exists. | `agent-coordination.zip` component package. | Missing CC/CDC/operator terminology, context packets, delegation, or result integration. | Required component package target. |
| `make contribution-style` | After the package target exists. | `contribution-style.zip` component package. | Missing contribution guides or `templates/CONTRIBUTION-TICKET.md`. | Required component package target. |
| `make all` | After all component package targets are wired. | Full skill-bundle aggregate. | `COMPONENT_ZIPS`, `INSTALL_ZIPS`, aggregate dependency, or generated zip list drift. | Required after package integration and final acceptance. |
| `make check-package-paths` | After Markdown links, package contents, `INSTALL_ZIPS`, `CF_FILES`, or exceptions change. | Generated package Markdown links and package-path contract. | Broken package-local links, unclassified source-only references, generated zip path drift. | Required after README/link/package edits and final acceptance. |
| `scripts/check-package-paths --check-exceptions-only package-path-exceptions.tsv` | After editing package-path exceptions, if the live script supports this mode. | Exception table syntax and classification. | Invalid exception shape or broad exception without explicit classification. | Required when `package-path-exceptions.tsv` changes. |
| `make ccdp-package` | Conditional: only if CCDP source/package surfaces are touched. | `ccdp.zip` generation and freshness. | Protocol package drift or stale assembled CCDP document. | Conditional CCDP gate. |
| `make check-ccdp-package` | Conditional: only if CCDP source/package surfaces are touched. | CCDP package-local link and payload validation. | CCDP package path failures caused by unrelated package work. | Conditional CCDP gate. |

## Makefile Surface Assertions

Future source implementation must reconcile these Makefile fields:

- `COMPONENT_ZIPS` should include `collaboration-framework.zip`,
  `engineering-methods.zip`, `project-management.zip`,
  `work-verification.zip`, `testing.zip`, `code-auditing.zip`,
  `agent-coordination.zip`, and `contribution-style.zip`.
- `INSTALL_ZIPS` should include `COMPONENT_ZIPS` plus existing domain/tooling
  skill zips, but not `ccdp.zip`.
- `ALL_SKILL_FILES` should cover all eight component `SKILL.md` entrypoints
  plus existing domain/tooling entrypoints; any top-level source compatibility
  shim should have an explicit validation decision.
- `CF_FILES` should become composer-local and stop carrying full specialist
  bodies unless the operator records an offline-use exception.

## Acceptance Interpretation

The final source implementation is not accepted merely because the source
files exist. It is accepted when the component package targets build, the
aggregate package target builds, package-path checks pass with no hard
failures, accepted warnings are explicitly dispositioned, source checkout
cleanliness is restored after generated artifacts are cleaned or ignored, and
conditional CCDP gates have run if CCDP was touched.
