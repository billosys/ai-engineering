# Slice15 CRC Verification

Current verdict: **changes required**. This is independent CRC review of the
initial `cc-prompt.md` packet, not CDC composition review or Operator acceptance.
No pair is accepted; coverage remains 200/355/8/347 and Slice16 stays unopened.

Date: 2026-09-17. CC contribution `678a8c76`; recipe follow-up `89568110`;
handoff/closing HEAD `178f1e6e`. Source HEAD
`76a69fd9c295e78f23faa651746c2e36646e0ebd`. Both worktrees were clean
before this review. The opening-to-CC diff contains exactly the six authorized
Slice15 files; `git diff --check` found no whitespace errors.

## Independent Checks

- Read the current project/arc/slice contracts, directive, ledger, six-file
  contribution, eight member meanings, native template/example witnesses,
  and CC handoff. No member conflates card actors with CQ roles, run worker
  scopes, source authors, or verification authority.
- Extracted the literal Bash route from `REPLAY_COMMIT=89568110` and ran it
  against `CC_COMMIT=678a8c76`, not the live working-tree code. Exit status 0.
  It reproduced 37 selected mappings, 2,054 legacy mappings, three YAML
  errors, 15 no-frontmatter records, all 39 registered hashes/ranges, the
  exact eight-pair subset, and the source/plan preservation checks.
- Wrong mode, wrong role, swapped children, absence-as-null, invalid member,
  dangling reference and invalid ranges rejected with status 1. Real no-match
  returned `[]`/0; missing input returned status 2. These are structural
  observations; the bounded semantic interpretations were checked separately.

## Findings

| ID | Row | Finding | Required correction |
| --- | --- | --- | --- |
| R1 | S15-5 | The issued prompt's S15-5 oracle explicitly requires a wrong-hash mutation to reject. The literal route recomputes all 39 hashes on a valid registry, but contains no mutated-hash case. Thus the required negative oracle is unrun, even though positive hash verification passes. | Add a candidate-registry hash verifier or equivalent reuse of the production hash predicate; alter one registered SHA-256 value and show nonzero rejection without modifying a registered source file. Keep all 39 positive checks and pinned endpoints. |
| R2 | S15-2, S15-5 | `semantic-evidence.md` and `closing-report.md` claim a wrong YAML-exclusion negative control. The route derives the actual three paths and compares them to the authored list, but does not submit an altered three-path list to that same predicate. This is an evidence overclaim, not a census error. | Add a wrong-exclusion mutation and show the same exact-set predicate rejects it, or remove the unperformed-control claims and explicitly record the limitation if the binding S15-2 oracle is still satisfied. Prefer the direct mutation because it is small and guards a prior Slice14 regression. |
| R3 | S15-5 | `closing-report.md` says the final report must record a "stale valid-recipe rejection," but its recorded stale/foreign check uses revisions where the Slice15 recipe path is absent. The actual status-2 missing-path result is real; no valid but stale recipe was tested. | Correct the wording so it describes the observed missing-path/foreign-endpoint rejection without claiming a valid stale-recipe test. A genuine valid stale-recipe case is optional only if supported by an actual earlier recipe; do not fabricate one. |

S15-1, S15-3, S15-4 and S15-6 have no independent finding in this pass. The
native census of S15-2 is reproduced, but its exclusion-control claim needs
repair. S15-5 remains open. No row is partially accepted and no scope, schema,
source, package, runtime, memory or UAT authority changes. The existing
contract can resolve these findings; CDC escalation is not needed.

## Bubble-up To Arc06

The eight-pair semantic scope and ownership of Slice16/17 remain as approved.
The correction is evidence integrity inside Slice15, not a new arc requirement
or plan change. The 347 outside pairs, P-15, CDC composition review, and UAT
remain open. The next CC assignment is `cc-prompt-iteration01.md` in this
slice root; CRC will independently replay its returned packet before any
coverage transfer or Slice16 opening.
