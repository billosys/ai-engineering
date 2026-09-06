# Testing Version History

## Version 1.1.1 - 2026-09-06

Updated the component entrypoint to reflect that testing now ships both inside
`collaboration-framework.zip` and as standalone `testing.zip`.

## Version 1.1.0 - 2026-09-04

Split the testing guide surface into three selective-load guides:
`01-testing-discipline.md`, `02-coverage-hardening.md`, and
`03-validation-gates.md`. The old guides/CODE-COVERAGE.md path was renamed
with `git mv` to `guides/02-coverage-hardening.md`; general testing discipline
and validation-gate material were extracted into companion guides. The
component now routes to testing discipline, coverage hardening, and validation
gates without claiming a complete TDD method.

## Version 1.0.1 - 2026-09-04

Seeded the sibling component history for Arc08 Slice05. The current component
routes to the coverage-hardening guide at guides/CODE-COVERAGE.md; broader
testing-discipline and validation-gate guide decomposition remains deferred for
operator review.

Future changes to `SKILL.md`, `guides/`, `templates/`, or `examples/` for this
component should be recorded here.

## Version 1.0.0 - 2026-09-04

Initial framework component entrypoint for testing and coverage hardening,
created during the Project04 framework component breakout. The component
preserves the coverage prompt lineage while giving it the broader `testing`
component name accepted by the operator.
