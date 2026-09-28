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

## Proportionate Proof

Choose the smallest adequate set of checks that establishes the acceptance
criteria and satisfies mandatory repository gates. Match effort to the changed
behavior, credible failure modes and consequences of failure. A real execution
path, an existing test, a bounded query or static inspection may suffice for a
claim; state what it does and does not prove. An unavailable integration check
remains a disclosed gap, not a reason to substitute a simulated success.

Before commissioning a new wrapper, reusable validator, replay protocol or broad
mutation suite, identify the required property that existing checks cannot
establish. Include the tool's implementation, review and maintenance in the
scope decision. When the validator is itself the requested product, its public
contract needs behavioral tests. An incidental query does not thereby acquire
a reusable product's interface, configuration and compatibility obligations.

When rejection behavior needs proof, use focused negative controls for credible
failures through the same predicate as valid inputs. Do not multiply controls
to exercise optional machinery introduced solely for verification. If repairing
that machinery becomes new
work, reassess whether an existing adequate check can replace it within the
assignment's authority. Changes to binding methods or acceptance go to their
owner; this rule does not authorize skipping gates or weakening evidence.

## Minimum Validation Set

Select the applicable checks below; this list is not a requirement to add every
kind of check to every task. Testing-oriented changes commonly need:

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
