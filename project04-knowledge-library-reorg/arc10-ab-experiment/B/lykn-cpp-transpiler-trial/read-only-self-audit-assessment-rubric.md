# Third-Party Assessment Rubric For Rust Self-Audit Reports

Use this rubric after both framework conditions have produced their
`rust-self-audit-report.md` files from the matched read-only audit prompt.

This rubric assesses audit quality. It does not score which implementation is
better except where implementation issues reveal whether the audit noticed,
classified, and explained them well.

## Evidence Inputs

For each condition, review:

- the final `rust-self-audit-report.md`;
- the project plan and Arc 03 close evidence used by that auditor;
- the implementation files cited in findings;
- validation command outputs recorded in the report, reproduced when needed;
- any contamination or deviation notes.

Do not use earlier comparison reports to decide initial scores. They may be
used after scoring to interpret trends.

## Scoring Scale

| Score | Meaning |
| --- | --- |
| 0 | Absent, contradicted, or unusable. |
| 1 | Present but vague, incomplete, or not actionable. |
| 2 | Actionable and mostly complete, with gaps or weak evidence. |
| 3 | Complete, specific, and supported by inspectable evidence. |

## Measures

| Measure | 0.4.1 | Main pre-0.5.0 | Evidence | Notes |
| --- | --- | --- | --- | --- |
| Framework isolation |  |  |  | Did the auditor use only the assigned framework condition and disclose deviations? |
| Audit-map completeness |  |  |  | Did the map cover crate targets, API, CLI, parser, AST, codegen, errors, tests, fixtures, examples, and exclusions? |
| Source coverage |  |  |  | Did the auditor inspect all first-party Rust source and test files, plus enough fixtures/examples to assess behavior? |
| Validation discipline |  |  |  | Were format, check, clippy, tests, and C++17 smoke checks run or explicitly dispositioned? |
| Finding specificity |  |  |  | Did every finding cite concrete file/line evidence and a real failure mode? |
| Severity calibration |  |  |  | Were severities neither inflated nor softened? Were open questions kept out of findings? |
| Rust-idiom grounding |  |  |  | Did findings reflect Rust API, error, ownership, module, CLI, and test idioms rather than generic advice? |
| Generated-C++ boundary handling |  |  |  | Did the report treat generated C++ as Rust codegen policy, not as a separate C++ audit? |
| Negative evidence quality |  |  |  | Were at least five concrete clean checks reported? |
| Coherence/architecture insight |  |  |  | Did the audit notice useful multi-file patterns, layering issues, or consistency strengths? |
| Hardening handoff quality |  |  |  | Did the report give an actionable follow-up packet without implementing changes? |
| Limitation honesty |  |  |  | Did the auditor disclose missing evidence, uncertainty, contamination, and scope limits? |

## Finding Reconciliation

After initial scoring, compare the finding sets:

| Finding Topic | Found By 0.4.1 | Found By Main | Confirmed? | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

Classify each material finding:

- `true-positive`: supported by source evidence and a plausible failure mode.
- `false-positive`: not supported, contradicted by source, or materially
  overstated.
- `missed-by-other`: present in one report and independently confirmed, but not
  reported by the other.
- `style-only`: possibly useful, but not a defect or meaningful hardening item.
- `open-question`: needs more evidence before being called a finding.

## Final Comparative Verdict

Answer these questions:

1. Which audit report is more useful to a maintainer?
2. Which report better preserves the diagnosis-only boundary?
3. Which report gives better hardening guidance?
4. Which report is more scientifically inspectable?
5. Are any differences explained by implementation state rather than framework
   audit quality?
6. Is there evidence of regression in main/pre-0.5.0 relative to 0.4.1?

## Decision Language

Use one of these verdicts:

- `main-improved`: main/pre-0.5.0 is clearly better on audit quality.
- `main-slightly-improved`: main/pre-0.5.0 is better, but the margin is modest
  or partly confounded.
- `no-material-difference`: the audit outputs are effectively equivalent.
- `mixed-result`: each condition has distinct strengths with no clear winner.
- `possible-regression`: main/pre-0.5.0 is weaker on at least one important
  audit-quality measure.
- `inconclusive`: missing or contaminated evidence prevents a fair comparison.

Record the verdict with the strongest supporting evidence and the main threat
to validity.
