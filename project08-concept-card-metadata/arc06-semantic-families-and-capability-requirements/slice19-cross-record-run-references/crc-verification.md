# Slice19 CRC Verification

Current verdict: **changes required**. This is independent CRC review under the
Operator-selected Three-Contributor Workflow, not CDC arc composition or
Operator acceptance. No Set C pair enters accepted coverage; accounting stays
260 accepted / 295 remaining / 19 assigned / 276 outside.

Date: 2026-09-24. Active reviewed assignment: `cc-prompt-alt.md`. Source
authority and review HEAD: `a5861c4b8e93af932d18cb571415cc570c758240`.
Planning contribution and review HEAD:
`ed9d38b898a021b1d13e77250cf7b3329fcf8e91`. Both worktrees were clean.
The contribution changes exactly the six authorized files, its message has
both required trailers and `git diff --check` passes.

## Independent Reproduction

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

## Findings

| ID | Rows | Finding and evidence | Required correction |
| --- | --- | --- | --- |
| R1 | S19-2, S19-6 | The 19 memberships cite 17 evidence IDs absent from `evidence_registry` (`semantic-membership.json`, e.g. lines 45, 71, 214 and 240, versus the registry beginning at line 286). Several registry rows are not one retrievable pinned input: they use pseudo-paths and multi-hash strings (`prompt-and-plan`, bundled card sets, `rerun-targets`, `templates`, `guidance`, `prior-contracts`). Three rows point to CC's ephemeral `/private/tmp` projections with non-Git authority strings (lines 298-300). A fresh reviewer therefore cannot resolve every member citation or replay each registered row from the contribution and pinned inputs. | Make membership citations referentially closed. Register each cited durable input with one unique ID, one actual path, one root, one real authority commit, one SHA-256 and one validated range/descriptor. Split bundled rows where their components are cited separately. Remove temporary projections as evidence inputs and cite the frozen inventory plus committed projections/report sections instead. Add direct checks that reject a dangling ID, duplicate ID, unresolvable path, wrong hash and invalid range. |
| R2 | S19-4, S19-6 | The `run_refs[].id` / `source-support` member cites `rich-profile` (`semantic-membership.json`, lines 221-227), but that witness is a concept-card example and cannot establish a source-support child observation. Other member IDs use undeclared aliases such as `rich-card`, `rich-rerun-card`, `pilot-resolution` and `guidance-*`, so applicability cannot be checked against the registry. | Audit every member's evidence IDs after R1. Each citation must support that exact field/kind or be explicitly shared with a valid applicability statement. Replace the source-support citation with the Arc07 source-support witnesses/inventory/run target; add a direct wrong-kind control proving that a concept-card-only witness cannot satisfy a source-support membership. |

## Row Disposition And Handoff

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

The reproduced semantics and later ownership remain consistent with
directive02. Slice20, Slice21, the 248-pair complement, P-15, repeated real
extraction, UAT and Operator quality acceptance stay open. These findings do
not change the arc plan; they prevent non-replayable evidence links from
entering accepted coverage.
