# Testing Split Map

## Source Commit

Source commit:
`120c2ceaf26ca656068d9f2ec34c978eefaf04a5`

## Accepted Guide Set

The three accepted numbered guides now exist:

- `knowledge/testing/guides/01-testing-discipline.md`
- `knowledge/testing/guides/02-coverage-hardening.md`
- `knowledge/testing/guides/03-validation-gates.md`

## Semantic Mapping

| New guide | Source material preserved | Independent load reason |
|---|---|---|
| `01-testing-discipline.md` | Tests-must-pass rule, behavior/contract testing, warnings/lint/format pressure, root-cause triage, weak-test anti-patterns, completion reporting. | Start testing work that is broader than a coverage sprint without loading the full hard-coverage prompt. |
| `02-coverage-hardening.md` | The old `CODE-COVERAGE.md` body, renamed by `git mv`, including 95%+ target, systematic coverage loop, module/integration/error-path coverage, progress reporting, anti-patterns, and sample session. | Drive a hard coverage-threshold effort while preserving the old prompt's quality floor. |
| `03-validation-gates.md` | Repository-native command adaptation, lint/format/test/package gate expectations, coverage gate framing, generated-artifact evidence, and command-result reporting. | Select and record validation gates without loading all coverage tactics. |

## Semantic Preservation

The split preserves the current testing and coverage quality floor:

- hard 95%+ coverage threshold discipline remains in
  `02-coverage-hardening.md`;
- warnings, lint, and format pressure are preserved in all three guides where
  relevant;
- tests must pass and ignored/weak tests must not hide failures;
- root causes must be repaired rather than symptoms;
- systematic coverage work remains module-by-module, then integration paths,
  then edge/error paths;
- progress tracking remains explicit;
- Rust/Cargo commands remain examples to adapt to repository-native tools;
- validation gates include test, lint, format, package, CI, release, and
  generated-artifact checks.

The split does not claim a complete future TDD method. It broadens the public
route from "coverage only" to testing discipline, coverage hardening, and
validation gates.

## Selective Loading

The new entrypoint route supports selective loading:

- start with `01-testing-discipline.md` for general testing quality and
  failure triage;
- load `02-coverage-hardening.md` for hard coverage-threshold work;
- load `03-validation-gates.md` when choosing validation, package, CI, release,
  or generated-artifact gates.
