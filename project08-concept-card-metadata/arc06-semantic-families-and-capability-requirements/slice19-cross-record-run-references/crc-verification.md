# Slice19 CRC Verification

Current verdict: **accepted after Iteration01**. This is independent CRC review under the
Operator-selected Three-Contributor Workflow, not CDC arc composition or
Operator acceptance. Exactly 19 bounded Set C pairs enter accepted coverage
once. Coverage becomes 279 accepted / 276 remaining / zero assigned before the
successor opens.

Date: 2026-09-24. Final reviewed assignment: `cc-prompt-iteration01.md`.
Source authority and review HEAD:
`a5861c4b8e93af932d18cb571415cc570c758240`. Initial contribution:
`ed9d38b898a021b1d13e77250cf7b3329fcf8e91`; CRC changes-required record:
`ba3850436cf79d5220da21279a5046334986faca`; repair contribution and final
candidate: `30facb12959880144e1a8f0511d8f308ec7d6772`. Both worktrees were clean.
The repair changes exactly the four authorized files, its message has both
required trailers, and `git diff --check ba385043..30facb12` passes.

## Iteration01 Independent Reproduction And Verdict

CRC retrieved every one of the 49 registered evidence rows directly from its
declared repository and authority commit. All paths resolved, all SHA-256
digests matched, all numeric line ranges were ordered and in bounds, and the
inventory's whole-object descriptor matched a 2,124-record minified JSON
object. The registry contains 49 unique evidence IDs, all 19 memberships cite
only declared IDs, and the positive referential-integrity predicate passes.
Injected dangling and duplicate IDs fail the same predicate.

The repaired source-support `run_refs[].id` membership cites the frozen
inventory, the Arc07 extraction-run, all four populated Arc07 source-support
witnesses and the committed semantic projection. It no longer cites the
concept-card-only rich-profile witness. The positive kind-applicability
predicate passes; injecting that wrong-kind witness makes it fail. Comparing
the initial and repaired memberships after removing only evidence links
produces identical meanings, states, consequences, unresolved questions and
dispositions for all 19 members.

CRC independently repeated the native data checks: 49 parsed selected records
across eleven kinds; 26 populated elements with source frequencies 8/7/10/1;
three YAML errors; fifteen no-frontmatter exclusions; and 2,054 bounded
historical records with no `run_refs` root. The four target outcomes remain one
exact extraction-run match, two path-resolved README files without declared
frontmatter identity, and one missing synthetic target whose containing tree
exists. A successful no-match is not rewritten as a tool error.

S19-1 through S19-7 are independently done. The complete artifact inventory,
all issued prompts, the initial failed review and the focused repair remain
preserved. No source, schema, helper, runtime, package, extraction, UAT or
memory surface changed. No silent row, artifact, deferral or no-op drop was
found.

## Initial Alternate-Assignment Reproduction

CRC retrieved the frozen inventory from planning `5e6310b8` and reproduced its
binding SHA-256
`afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b`.
Direct queries independently reproduced:

- exactly 49 parsed selected records across all eleven assigned kinds;
- root-state cells matching the recorded census, including 31 concept cards
  and five source-support records;
- 26 populated elements: 22 concept-card and four source-support references;
- four unique tuples with source-record frequencies 8, 7, 10 and 1;
- three YAML parse errors and fifteen `no-opening-frontmatter` exclusions;
- 2,054 parsed Complete Musician/Erlang records and zero `run_refs` roots.

CRC inspected all four target cases at their declared authority and containing
directory. The Arc07 path resolves to an extraction-run with matching
`record_type`, id and revision. The preserved rich and teaching paths resolve
to README files with no opening identity declaration. The synthetic example's
containing source tree exists while its referenced target does not. Address,
identity, missing-target and tool-error states remain correctly separated.

CRC also reviewed all 19 effective meanings. They preserve kind-local
provenance, root/element/child distinctions and the prohibition on inheriting
actor, source, support, evidence, lifecycle, runtime or contributor authority.
No schema, requiredness or migration policy is adopted. The semantic and
population analysis does not need to be redone for this correction.

## Initial Findings

| ID | Rows | Finding and evidence | Required correction |
| --- | --- | --- | --- |
| R1 | S19-2, S19-6 | The 19 memberships cite 17 evidence IDs absent from `evidence_registry` (`semantic-membership.json`, e.g. lines 45, 71, 214 and 240, versus the registry beginning at line 286). Several registry rows are not one retrievable pinned input: they use pseudo-paths and multi-hash strings (`prompt-and-plan`, bundled card sets, `rerun-targets`, `templates`, `guidance`, `prior-contracts`). Three rows point to CC's ephemeral `/private/tmp` projections with non-Git authority strings (lines 298-300). A fresh reviewer therefore cannot resolve every member citation or replay each registered row from the contribution and pinned inputs. | Make membership citations referentially closed. Register each cited durable input with one unique ID, one actual path, one root, one real authority commit, one SHA-256 and one validated range/descriptor. Split bundled rows where their components are cited separately. Remove temporary projections as evidence inputs and cite the frozen inventory plus committed projections/report sections instead. Add direct checks that reject a dangling ID, duplicate ID, unresolvable path, wrong hash and invalid range. |
| R2 | S19-4, S19-6 | The `run_refs[].id` / `source-support` member cites `rich-profile` (`semantic-membership.json`, lines 221-227), but that witness is a concept-card example and cannot establish a source-support child observation. Other member IDs use undeclared aliases such as `rich-card`, `rich-rerun-card`, `pilot-resolution` and `guidance-*`, so applicability cannot be checked against the registry. | Audit every member's evidence IDs after R1. Each citation must support that exact field/kind or be explicitly shared with a valid applicability statement. Replace the source-support citation with the Arc07 source-support witnesses/inventory/run target; add a direct wrong-kind control proving that a concept-card-only witness cannot satisfy a source-support membership. |

## Initial Row Disposition And Handoff

S19-1, S19-3, S19-5 and S19-7 are independently reproduced. Their results
must remain unchanged, but the slice is not partially accepted. S19-2,
S19-4 and S19-6 remain open for the bounded repairs above. The existing CC
closing report remains a historical proposed-done attestation.

No structural change or CDC escalation is needed: the findings enforce the
existing evidence-registry and kind-specific-applicability contract. The next
assignment is `cc-prompt-iteration01.md`. It preserves the Operator-authorized
direct-check method and does not restore the superseded wrapper, mutation suite
or separate recipe endpoint. Slice20 remains unopened pending a fresh CRC
review and acceptance of this repair.

## Bubble-Up To Arc06

Slice19 delivers directive02 Set C without changing its boundary or any outside
owner. Exactly 19 pairs enter accepted coverage once, producing 279 accepted /
276 remaining / zero assigned before the successor opens. The repaired
evidence registration does not change the arc's architecture or Slice20
boundary, so no structural amendment is required.

Directive02 authorizes fresh Slice20 readiness after this acceptance. Slice21,
the 248-pair later-family complement, P-15, repeated real extraction, UAT and
Operator quality acceptance stay open. Creation-time semantics remain evidence
work only; this acceptance does not establish a global timestamp policy.
