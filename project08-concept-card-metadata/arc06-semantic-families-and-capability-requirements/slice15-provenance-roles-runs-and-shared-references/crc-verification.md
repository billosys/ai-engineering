# Slice15 CRC Verification

Current verdict: **accepted** after independent Iteration01 review below.
The initial changes-required findings remain as historical review evidence.
This is a CRC slice verdict, not CDC composition or Operator acceptance.

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

## Iteration01 Independent Review: Accepted

Date: 2026-09-17. Current assignment `cc-prompt-iteration01.md`. CC
contribution `610bdcb4`, replay record `02fb4ef8`, closeout `db4f719f`.
Current source HEAD `ce3f77103eff5e07b3533a03c65f158684fc1039` and
planning HEAD `db4f719f` were clean before CRC edits. The five changed files
from `ea200f07` through CC closeout are within the original six-file output
fence; no source implementation file changed. Source movement from the
initial Slice15 baseline touches neither `knowledge/concept-cards` nor
`knowledge/document-extraction`; the two changed framework/prompt-guide
evidence rows were repinned to their actual current bytes. The other 37
evidence registrations retain their previous authorities.

I executed the literal recipe extracted from `REPLAY_COMMIT=02fb4ef8` with
`CC_COMMIT=610bdcb4`. It exited 0 and independently reproduced all 39
registered hashes and reading ranges, the 37 selected/2,054 legacy native
census, three exact YAML-error paths, 15 no-frontmatter records, eight exact
memberships, source/plan preservation, and the five-file Iteration01 diff.
The same production hash predicate rejected a single wrong SHA-256 candidate
with status 1; the same exact-set exclusion predicate rejected a wrong
three-path candidate with status 1. Wrong mode, wrong role, swapped children,
absence-as-null, invalid member, dangling evidence, out-of-bounds and
reversed ranges all rejected with status 1. Real no-match returned `[]`/0;
missing input returned status 2. `git diff --check ea200f07..db4f719f`
passed; both worktrees were clean at review intake.

R1 and R2 are resolved by those same-predicate controls. R3 is resolved by
accurate prose: the older/foreign endpoint checks are status-2 missing-path
rejections, not tests of a present valid stale recipe. No prior valid
Slice15 recipe is claimed. The supported meanings remain bounded to exact
kind/family/revision observations and distinguish actor from CQ role arrays,
worker scopes, source authors and review authority; replay success alone is
not the semantic rationale.

| Row | CRC disposition |
| --- | --- |
| S15-1 | Done: exact eight-pair remaining-set subset, no overlap or owner transfer. |
| S15-2 | Done: 37 selected by kind/family/state, 2,054 legacy absent parents, exact three YAML exclusions and 15 no-frontmatter records reproduced. |
| S15-3 | Done: eight member/shared interpretations inspected against template, synthetic and populated bodies; unknown vocabulary/authority remains explicit. |
| S15-4 | Done: native positive and wrong-value/state controls and no-match versus error behavior reproduced. |
| S15-5 | Done: pinned separate replay, all registered hashes/ranges, new and retained mutations, preservation, exact scope and whitespace reproduced. |
| S15-6 | Done: handoff retains Slice16/17, all outside families, P-15 and UAT; no source/schema/memory claim. |

The CC close report accounts for six opening rows and the durable four-file
artifact inventory. It has no separately titled bubble-up section, but its
handoff and final section account for all unresolved scope. This format gap
does not hide an owner or change the arc. **Bubble-up to Arc06:** no arc-plan
scope amendment is needed. Exactly eight pairs move to accepted coverage:
208 accepted / 347 remaining / zero assigned / 347 outside at this close.
Slice16's twelve pairs are approved for a separate readiness check, not
accepted or opened by this verdict. Slice17 still needs CDC sizing; all A6
rows, P-15 and UAT remain open.
