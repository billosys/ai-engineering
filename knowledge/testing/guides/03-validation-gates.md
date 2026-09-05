# Validation Gates

Load this guide when testing work must be reconciled with project validation,
package, CI, or release gates. It keeps the testing component from treating a
single coverage report as the whole definition of done.

For general testing practice, start with
[`01-testing-discipline.md`](./01-testing-discipline.md). For hard coverage
threshold work, use [`02-coverage-hardening.md`](./02-coverage-hardening.md).

## Gate Selection

Choose gates from the repository, not from habit:

- Makefile targets;
- package scripts;
- CI workflow commands;
- language-native test, lint, format, coverage, and documentation commands;
- package validators;
- generated artifact inspections;
- smoke tests or demonstrations required by the slice ledger.

If the repository has an explicit command surface, prefer it over hand-running
lower-level tools. If the repository has no single gate, state the selected
commands and why they cover the change.

## Minimum Validation Set

Testing-oriented changes commonly need:

- focused tests for the changed behavior;
- full relevant test suite;
- lint and format checks;
- coverage report when coverage is the criterion;
- documentation or doctest checks when public examples changed;
- package or generated-artifact validation when routes, packaging, or release
  files changed.

Do not collapse these into "tests pass" when the ledger names more than tests.
Each gate should have evidence.

## Coverage Gates

When coverage is the explicit objective:

- overall line coverage should reach 95% or the ledger's stricter threshold;
- no module should remain below the accepted floor without a recorded
  deferral;
- ignored tests, justified unreachable lines, and coverage-tool exclusions
  should be disclosed;
- coverage reports should be read, not merely generated.

## Warning, Lint, And Format Gates

Warnings are signals that can become defects, API breaks, or user-facing
confusion. Lint and format failures are not automatically lower priority than
tests; the repository's own policy decides the gate. If a warning is deferred,
record the reason and re-entry condition.

## Package And Release Gates

When testing documentation, skill routes, package lists, or generated artifacts
change, validate the package boundary directly. Source files existing in the
repository do not prove they are present or linked correctly in generated
packages.

For this repository, relevant gates include:

- `make check-skills`;
- `make collab-framework`;
- `make check-package-paths`;
- focused Markdown link checks over touched route surfaces;
- generated zip inspection.

## Gate Evidence

Record the exact command and result. For long outputs, record the summary
lines that prove success: hard-failure count, files scanned, package entries,
coverage percentage, or test totals. If a command cannot be run, record the
blocked command and re-entry condition.

Component history lives in [`../version-history.md`](../version-history.md).
