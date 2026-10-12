---
slice: slice06-colour-pipeline-source-fixes
status: open
---

# Arc02 Slice06 — Colour-Pipeline Source Fixes

## Deliverable and authority

Install the three accepted live corrections distinguishing linear matrix stages
from a complete nonlinear conversion. Preserve the system's mathematical teaching
and remaining content. Deliver source commits and a freshly inspected package in
one slice, using the Operator's [amended project](../../project-plan.md),
[current arc](../arc-plan.md) and Expedited Mode. CDC Sofie independently reviews
separate CC execution via Operator; no self-acceptance or new theory packet.

Planning predecessor `fdb073f5ab9ad2b8a076f2e76ea21a38868d00c1`. The commit containing this open
set is the issue revision; identify it at intake. SOURCE/main is
`314e580282d2c801e41f6decfbbf07483957268c`. Mutation authority covers exactly the three source
paths below. All three old teaching targets are byte-identical to their accepted
Slice02 baseline `dffa504e851b03b8e4746f1941068e4cc850b612`; inspect actual drift at
intake before applying. An externally changed non-target file is not a reason to
repin the entire assignment or overwrite it.

| Source mutation path | Baseline SHA-256 |
|---|---|
| `knowledge/design/SKILL.md` | `57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63` |
| `knowledge/design/guides/foundations-of-design.md` | `f4cff1c1edc0ece2a368ff81f3bb1909db9b50c1767281300223f88b83f54aa4` |
| `knowledge/design/version-history.md` | `d137a660d11fe9cfa6ddd51917dc03abc80f6578c7bdab5a63c4a5d3c5f9a943` |

## Decisions and applicability

Use the accepted [staged proof](../slice02-nonlinear-colour-pipeline/artifacts/colour-conversion-proof.md) and [independent closure](../slice02-nonlinear-colour-pipeline/cdc-verification.md).
Correct `LIVE-SKILL-001::clause`, `LIVE-FOUND-002::clause`, and
`LIVE-FOUND-004-MATRIX`; remove the unsupported Grassmann attribution within
that changed paragraph without deciding Grassmann's broader historical claims.
Only adjacent linear maps compose; encoded sRGB requires decoding and the Oklab
pipeline includes a componentwise real cube root between matrices. No numerical
palette, endpoint or compatibility decision is needed for these prose fixes.

Retain the already accurate XYZ → M₁ → cube root → M₂ explanation. The attached
music/perceptual-uniformity analogy and other surrounding universal brightness,
CIE/ΔE, accessibility and ranking claims remain separately owned by Arc02's
content/technical review; preserving their bytes is not accepting them. Cards
and their relationship/CQ review remain in the full233-card work. This slice
closes only these three teaching occurrences, not all DES-007 or either full file.
C&B removal remains the next portable-default batch. No originals/captures are
acquired here, and source-independent math does not close P10-11 fidelity.

## Implementation recipe

Apply the three unique substring changes below; preserve all other teaching
bytes. They share one meaning but use appropriate entrypoint/detail levels.
No new links, code snippets, framework mechanism or maintained checker is needed.

### Change 1 — `knowledge/design/SKILL.md`

Replace this exact unique substring:

```text
**Colour space conversions are 3×3 matrix multiplications** (linear algebra).
```

with:

```text
**Colour-space conversions combine linear and nonlinear stages**. Linear stages use 3×3 matrices; a complete conversion can also include sRGB decoding and componentwise cube roots.
```
### Change 2 — `knowledge/design/guides/foundations-of-design.md`

Replace this exact unique substring:

```text
**colour space conversions are 3×3 matrix
multiplications** --- this is literally linear algebra, not metaphor.
```

with:

```text
**linear colour-space conversion stages use 3×3 matrices** --- literal
linear algebra. Complete conversions can also include nonlinear decoding
and componentwise cube roots.
```
### Change 3 — `knowledge/design/guides/foundations-of-design.md`

Replace this exact unique substring:

```text
**Linear algebra → colour space transformations (RIGOROUS).** Colour
space conversions are 3×3 matrix multiplications. sRGB → XYZ, XYZ → LMS,
LMS → Oklab --- each step is a matrix multiply, and the chain can be
collapsed into a single matrix per Grassmann\'s additivity law.
```

with:

```text
**Linear algebra → colour space transformations (RIGOROUS).** Matrix
stages are literal linear algebra. To convert encoded sRGB to Oklab,
first decode to linear sRGB. Transform linear sRGB to XYZ and then LMS
using the D65 matrices, apply a componentwise real cube root, and use a
final matrix to obtain Oklab. Adjacent linear stages can be composed into
one matrix; the complete pipeline cannot be collapsed across its
nonlinear operations.
```

### Owning skill version and history

Current authority is `metadata.version: "1.0.0"` in `knowledge/design/SKILL.md`.
Set it to `"1.0.1"` and add the matching correction entry to the sibling
`version-history.md`, dated2026-10-12. Explain the three source corrections;
preserve the prior entry. This is a compatible correction, not the final project
release. Keep version numbers out of guides and entrypoint prose; inspect the
whole owning tree and fresh package under the repository version contract.

## Required reading and execution

Read SOURCE/main instructions and installed `collaboration-framework` first.
Load current `knowledge/project-management/SKILL.md`, its guide README and the
relevant top-down/closure routes; read engineering-methods' prompt-authoring/intake
and testing's proportionate validation-gate guidance. All source guidance paths
belong to main, not the orphan planning tree. Use this scoped manifest for domain
and assignment contents; record completion concisely in the batch record.

| Required input | Exact scope / reason |
|---|---|
| Planning AGENTS, project AGENTS, project plan and project ledger | Instructions plus current project body through Version History; all thirteen criteria; retain full-corpus and source-readiness boundaries. Historical plan entries are lookup-only. |
| Arc plan and ledger | Current arc body through Version History; all ten criteria and latest Slice05/06 roll-up. Older histories are lookup-only. |
| This plan, ledger and issued prompt | Full contents; exact edits, outcomes, allowed paths and handoff. |
| SOURCE `knowledge/design/SKILL.md` and sibling history | Full contents; ownership, three-stage correction context, remaining claims and version authority. |
| SOURCE foundations guide | Full paragraphs/bridge context at baseline234–258 and420–460, including neighboring prose; inspect other repeats using an entire live-guide search. |
| Accepted Slice02 proof, handoff and CDC record | Proof in full; handoff's named LIVE rows above with qualifiers; final Operator-approved repair/independent closure and row dispositions. Earlier diagnostics are lookup-only. |
| SOURCE prepared `knowledge/design/sources/md/posts/a-perceptual-colour-space.md` | Complete Implementation section through the matrix-update note (baseline71–164); distinguish XYZ M₁ from combined linear-sRGB A, nonlinear roots and inverse cubes. This is technical context, not historic-fidelity acceptance. |

1. Check main/planning identities, exact targets and pre-existing work. Record
   one concise contract readback and necessary exceptions; resolve changed target
   bytes before mutation. Preserve `knowledge/lfe/` and `project12-chcd-protocol/`.
2. Read and apply the recipe; compare complete changed contexts and search all
   live design guides/entrypoint for equivalent matrix-collapse claims. Unexpected
   scope stays an owned follow-up, not an unreviewed additional mutation.
3. Verify the literal source diff, unchanged neighboring teaching, correct stage
   order and compatible version/history. Reuse accepted math after confirming
   target/source applicability; do not rerun the large closed evidence packet.
4. Start at `make help`. Run `make check-skills` and `make check-package-paths`;
   the latter includes fresh source/package skill-version checks. Run fresh
   `make design`, inspect the actual zip's entrypoint, foundations and history,
   and confirm the corrected claims/version are shipped. Record exact commands,
   outcomes and warnings; fix hard failures within the authorized scope or report
   a concrete outside-scope blocker. Do not install or publish.
5. Commit exactly the three source files on main with both required trailers.
   Record the resulting source commit and inspected package in the compact batch
   record. Commit only the three CC planning outputs below on planning; provide
   proposed per-row completion and a silent-drop/Arc02 bubble-up in the report.
   No receipt-only child is required. Return through Operator for CDC review.

## Proof, outputs and gates

Four result criteria are in [the ledger](ledger.md). Human inspection verifies
actual meaning/stage order and complete changed paragraphs; diff/byte checks
verify scope and preservation. Fresh build/package checks verify shipped content,
not browser behavior or source fidelity. No runtime behavior was changed and no
new software test suite or keyword truth oracle is assigned.

CC planning writes exactly `artifacts/batch-record.md`, `ledger.md` evidence/notes
only, and `closing-report.md`. The first is the sole supporting output; record
intake, before/after occurrence pointers, prior-proof applicability, checks,
failures/recoveries/unrun scope and explicit unresolved owners there. Do not create
additional proof/inventory/registry/handoff files. Leave criteria/statuses, this
plan, issued prompt, prior artifacts and independent records unchanged. CDC alone
accepts in `cdc-verification.md` and closes/advances. All parent gates remain.

## Author readiness and history

CDC inspected actual full entrypoint/history, both complete guide contexts,
accepted proof/closure, prepared implementation and current upstream Oklab
implementation. An entire live-file search found these three matrix assertions.
The proposed substrings each match once; virtual composition preserves the
accurate earlier pipeline and entrypoint analogy. An independent small white
witness using the published A/B coefficients gives L(white)=0.9999999934735461
and L(white/8)=0.49999999673677303, rejecting whole-pipeline linear scaling.
This author check is not acceptance of CC's future diff or final package.
A broader source-version search initially included provenance/card prose because
its exclusion globs were wrong; the corrected entrypoint/guides/history search
found only the owning metadata/history version declarations. A nonexistent
`templates/` path was discarded; it is not an owned directory or required input.

## Version History

- 1.0 (2026-10-12): Opened the first actual source-fix batch after independent
  Slice05 closure. Three accepted colour-pipeline occurrences; compact evidence,
  compatible skill correction and fresh package checks; no parent-scope reduction.
