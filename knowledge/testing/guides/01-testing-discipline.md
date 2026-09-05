# Testing Discipline

Load this guide when the work is about testing quality in general: writing
tests that prove behavior, repairing weak tests, preserving a hard quality
floor, and choosing repository-native validation commands. It is the testing
component's broad entry guide, not a full TDD method.

For focused coverage work, use
[`02-coverage-hardening.md`](./02-coverage-hardening.md). For release,
package, and validation command gates, use
[`03-validation-gates.md`](./03-validation-gates.md).

## Quality Floor

Testing work is complete only when tests prove the intended behavior and all
required validation gates pass. Cosmetic coverage is not enough. The testing
discipline preserves these rules from the former coverage prompt:

- tests must pass with zero unresolved failures;
- ignored or weakened tests require explicit justification and should not hide
  defects;
- warnings, lint, and format failures are quality pressure, not background
  noise;
- failing tests are evidence of a violated assumption, a bad test, or a real
  implementation bug;
- fixes should address root causes, not the first symptom that makes the test
  runner turn green;
- coverage progress should be reported concretely when coverage is the goal.

## Use Repository-Native Tools

Rust/Cargo commands in the coverage-hardening guide are examples. In live work,
use the active repository's own Makefile, package scripts, CI config, language
tooling, and documented validation commands as the authority.

Examples:

- use `make test`, `make lint`, `make format`, or project-specific targets
  when the repository provides them;
- use Cargo, Go, Deno, npm, pytest, or other language-native commands when
  they are the local source of truth;
- use package validators and generated artifact inspection when testing changes
  affect packaging or release behavior;
- request approval for commands that need network, GUI, or out-of-workspace
  writes instead of silently skipping them.

## Test Behavior And Contracts

Prefer tests that demonstrate externally meaningful behavior:

- public API contracts;
- error behavior and diagnostics;
- boundary values;
- empty/null/invalid inputs where applicable;
- state transitions;
- concurrency or async behavior where applicable;
- resource cleanup and side effects;
- integration paths that connect modules.

Avoid tests that only pin private implementation details, execute code without
assertions, broaden assertions to hide failure, or special-case production code
for test convenience.

## Failure Triage

When a test fails:

1. Read the failure completely.
2. Identify expected versus actual behavior.
3. Trace the path that produced the result.
4. Ask which assumption is violated.
5. Decide whether the test, implementation, or design assumption is wrong.
6. Fix the cause and rerun the relevant validation.

Do not change implementation just to satisfy a test until the contract is
understood. Do not change the test merely to match the implementation unless
the test's expectation is demonstrably wrong.

## Completion Reporting

A testing report should state:

- commands run;
- test counts or relevant summary;
- coverage before/after when coverage is in scope;
- modules or paths still below threshold;
- blockers and re-entry conditions;
- any ignored tests or justified uncovered lines;
- remaining risk.

Component history lives in [`../version-history.md`](../version-history.md).
