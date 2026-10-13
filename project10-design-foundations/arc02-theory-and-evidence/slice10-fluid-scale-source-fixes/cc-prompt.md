# CC assignment — Arc02/Slice10 fluid-scale source fixes

Execute the initial assignment in `slice-plan.md`, not another evidence-only
handoff. Deliver corrected usable source on main and return concise evidence
to CDC Sofie through the Operator. Two-Contributor Workflow; Expedited Mode.
All S10-01–04 remain open until independent CDC review. No closure or next slice.

## Authority, pins and output allowlists

Operator2026-10-12 authorized combined review/fix batches; on2026-10-13 the
Operator accepts the Arc06 composition at planning1fffb9dc/source589d7c21 and
instructs continuation of Arc02. This is that next source-scoped assignment.
Locate worktrees; read the active project contract before arc/slice contracts.
Pin issuing planning HEAD containing this prompt. Its preparation predecessor is
`1fffb9dc578b948d21d00ab9bf451682fccb7861`.
Assigned source HEAD: `589d7c21bd6c9a415b921b80479822561861fa79`.
Use committed source bytes for input checks; compare current HEAD/worktree and
stop only affected edits if a conflict is present. Do not fetch/rebase/reset or
push as part of this batch. Preserve unrelated untracked/staged work.

Source output allowlist, on main only:

| Path | Assigned SHA-256 | Permitted change |
|---|---|---|
| `knowledge/design/guides/layout.md` | `af50575508c1f44cd870b480f729ff64897943293576f047ac9737875941822c` | L10-01 and L10-02 only |
| `knowledge/design/guides/foundations-of-design.md` | `347378644c54e53bf4a3ab8025b8449e74b6cdd50bbd1050661297dc7696c60a` | F10-01, F10-02 and F10-03 only |
| `knowledge/design/SKILL.md` | `0c17bf269c904756d44cff4777ecb7754a677694137a5145b2e04c4c8d81c2fa` | Only metadata.version1.0.6→1.0.7 |
| `knowledge/design/version-history.md` | `9e4d160c0d7002511fd111095b7dbb3fc6add0932973ff678782adcd8d12045b` | Append matching owning micro-release entry; retain history |

Planning output allowlist, relative to this slice directory on planning:

- `artifacts/batch-record.md` — one compact supporting record.
- `ledger.md` — evidence/notes only; preserve four criteria and open statuses.
- `closing-report.md` — proposed outcomes, exact commit receipts and limits.

All plans, issued prompts, accepted artifacts and verification records are
protected. No additional report/helper/test-framework files. Source originals,
all233 cards and every source byte outside the exact five blocks/version/history
change are protected. This includes type.md and design.md, the layout diagnostic
at assigned lines350–371, existing Utopia explanation at140–154, ratio principle,
and adjacent colour bridges. No missing metadata is filled; no schema adoption,
font/default scale, spacing roster or C&B identity is reintroduced.

## Required reading and intake

Load these texts completely within their declared scope. Recover truncated
output. A hash identifies bytes, not a read; distinguish text receipts from
structured-data query coverage. Record extents/source revisions and a concise
source-cited contract readback in `artifacts/batch-record.md` before editing.
Connect optional ratios, exact-versus-rounded numbers, finite saturation and
conditional geometry to the prescribed changes, preservation and review limits.
No extra preflight approval is required once coherent.

1. Repository AGENTS.md in full; current collaboration-framework skill and
   project-management SKILL/README, applying their relevant implementation/intake
   and planning boundary routes. Use current repo copies when installed copies lag.
2. This project's `project-plan.md`: complete current body before Version History;
   retain history as reference if an authority dispute needs it. Then Arc02
   `arc-plan.md`: complete current body before Version History, and complete
   Arc02/project ledger criterion tables (10/13 rows, not all historical logs).
   This slice's plan, ledger and prompt in full.
3. Source `knowledge/design/SKILL.md`, `guides/type.md` and `version-history.md`
   in full. Source layout.md: the required bounded contexts are lines90–160,
   270–295,344–375 and762–779 at the assigned pin. Read each declared range
   completely; these contain the relevant prose, principle and diagnostic.
   Foundation required complete
   typography context lines257–287 and music bridge context lines430–461.
   All five old blocks below must be read with their surrounding prose wrappers.
   Other whole-guide review is outside this bounded correction, not claimed done.
4. `../slice01-fluid-scale-arithmetic/artifacts/fluid-scale-proof.md` in full;
   its `correction-handoff.md` sections “Live-guidance changes”, numerical
   qualification/remaining ownership and limits where applicable. Use headings
   actually present; read the handoff fully if section names differ. Query its
   `claim-results.jsonl` for complete subject/assertion fields of LAY-12/13/14
   and FND-02/04 (five unique results); compare original to current targets.
   Consume the historical36 IDs/population only to verify context, not as a new
   dataset to produce. Original source spans are historical, not edit coordinates.
5. CSS Values4 [viewport relative units §6.1.2.2](https://www.w3.org/TR/css-values-4/#viewport-relative-lengths)
   and [comparison functions §10.2](https://www.w3.org/TR/css-values-4/#comp-func)
   definitions of logical `vi` and ordered finite `clamp()` bounds. Author checked
   these primary definitions on2026-10-13; retained exact historical source
   fidelity is not established by a current specification/page.

Conditional: inspect a source or protected guide beyond these scopes only if a
claimed dependency/check needs it. Report any additional defect with owner and
next action; do not broaden edits or commission an unapproved investigation.
The required reading is bounded to current contracts, the declared source
contexts, accepted proof and existing handoff; no full corpus re-extraction.

## Implementation recipe: five exact replacements

Resolve all target blocks against the assigned SHA-256/source pin, exactly once.
Preserve surrounding blank lines/div wrappers and every other byte. The start/end
lines below are inclusive at that pin; replacement text is literal UTF-8 Markdown.
Apply by matched blocks, not post-edit offsets. Do not change prose merely to
make a search produce zero hits: retained historical quotations or unrelated
analogy claims are not this batch's acceptance scope.

### L10-01 — `knowledge/design/guides/layout.md`:116–123

Replace the complete block beginning `The **Modular scale** chapter introduces the mathematical foundation` with:

```markdown
The **Modular scale** chapter offers one way to generate proportional
values: `size(n) = base × r^n`. For an increasing perfect-fourth scale,
`r = 4/3`; `1.333` is a displayed approximation, not that exact ratio.
With a `1rem` base, steps 0–3 round to `1.000rem`, `1.333rem`,
`1.778rem`, and `2.370rem` at three decimal places. Compute with the
selected ratio before rounding the displayed result. These proportions
are a construction choice; arithmetic alone does not establish
perceptual harmony, readability or a requirement that all spacing be geometric.
```

### L10-02 — `knowledge/design/guides/layout.md`:766–776

Replace the complete block beginning `The fluid interpolation in Utopia\'s `clamp()` declarations is a linear` with:

```markdown
With ordered finite bounds, `clamp(min, preferred, max)` limits its
preferred calculation to those bounds. When that calculation is linear
in the selected inline extent, the result changes linearly only inside
its unsaturated interval and is fixed at a bound outside it; there is
no asymptotic approach.

For positive endpoint bases `a`, `b`, positive ratios `r`, `q`, integer
step `n`, and a shared clamped parameter `t` in `[0,1]`, each interpolated
step is `s_n = (1-t)a r^n + t b q^n`. At an interior parameter (`0<t<1`)
this is geometric across steps only when `r = q`; either endpoint retains
its own geometric sequence. Each step's change depends on its own endpoint
difference, so higher steps need not grow faster.

`vi` is a logical inline viewport unit. It does not alone establish
browser text enlargement, reflow or WCAG conformance. Declare the roots
and interval, then test the actual interface and user settings.
```

### F10-01 — `knowledge/design/guides/foundations-of-design.md`:266–272

Replace the complete block beginning `**Tim Brown\'s modular scale** is the critical bridge between` with:

```markdown
**Tim Brown\'s modular scale** connects typographic proportion with
web implementation. A modular scale generates values by repeated
multiplication by a selected ratio. Musical intervals can supply such
ratios: low-to-high pairs `15:16`, `4:5`, `3:4` and `2:3` correspond to
increasing multipliers `16/15 ≈ 1.067`, `5/4 = 1.250`, `4/3 ≈ 1.333`
and `3/2 = 1.500`, respectively. The pair notation names the smaller and
larger values; the multiplier is the larger divided by the smaller.
Brown quotes Bringhurst: \"A modular scale, like a musical scale, is a
prearranged set of harmonious proportions.\" This attributed description
does not prove that every constructed scale is visually harmonious,
readable or accessible; judge it with the project's content and conditions.
```

### F10-02 — `knowledge/design/guides/foundations-of-design.md`:281–286

Replace the complete block beginning `**Utopia (James Gilyead & Trys Mudford)** provides the mathematical` with:

```markdown
**Utopia (James Gilyead & Trys Mudford)** offers one approach to fluid
responsive design: choose endpoint bases, ratios and an interpolation
interval, then calculate each step independently. A linear preferred
expression supplies interpolation; `clamp()` bounds that expression.
With positive endpoint bases and ratios and a shared interior parameter,
the interpolated steps form a geometric sequence only when the endpoint
ratios are equal. Each step's slope depends on its own endpoint difference,
so higher headings do not necessarily grow faster than body text.
These calculations do not establish visual harmony or accessibility.
```

### F10-03 — `knowledge/design/guides/foundations-of-design.md`:431–438

Replace the complete block beginning `#### Music Theory → Visual Design: Three Rigorous Connections` with:

```markdown
#### Music Theory → Visual Design: Three Connections

**Musical intervals → type scale ratios (SHARED CONSTRUCTION).** Brown's
modular-scale discussion uses musical ratios as one source of proportions.
An increasing perfect-fourth scale uses `4/3 ≈ 1.333`; a perfect-fifth
scale uses `3/2 = 1.500`. The common mathematics is repeated multiplication
by a chosen ratio. The golden ratio `φ = (1 + sqrt(5))/2 ≈ 1.618` is another
possible geometric multiplier, not a musical interval. Shared arithmetic
does not transfer auditory harmony into a guarantee of visual harmony,
readability or suitability for a project's content.
```

The music bridge heading loses its blanket “Rigorous” label because the changed
first connection is a scoped shared construction. Other two connection bodies
are preserved pending their own Arc02 review. Brown's existing Bringhurst quote
is retained as attribution, not promoted to freshly verified original-source
fidelity. Neither interval convention nor arithmetic proves perceptual harmony.

After the five guide replacements, change only the owning SKILL metadata version
from1.0.6 to1.0.7 and append its matching sibling history entry describing these
corrections. No independent guide version, embedded history, new version authority
or duplicate skill version label. Preserve all earlier history.

## Observable checks and preservation

Use exact Fractions/Rationals for decisive arithmetic; use high-precision decimal
round-half-even only for displayed three-place values. Do not compute a4/3 scale
by recursively multiplying the truncated display1.333.

- Ratio orientation: the four increasing multipliers are16/15,5/4,4/3,3/2.
  Exact4/3 differs from1333/1000. Powers at steps−2…5 round to
  `0.562, 0.750, 1.000, 1.333, 1.778, 2.370, 3.160, 4.214`.
  The negative-step tie9/16 rounds half-even to0.562. Reject the old printed
  steps2/3=`1.777,2.369` under this exact model; verify the new literal prose.
- Shared-parameter interpolation: for positive bases/ratios and integer steps,
  `s_n=(1-t)a*r^n+t*b*q^n`. At a16,b20,r6/5,q4/3,t1/2 the steps0–2
  determinant `s0*s2-s1*s1` is64/45>0; a universal interior-geometric claim fails.
  Equal endpoint ratios and either t0/t1 retain determinant zero. Include n−2
  for positive determinant with unequal ratios at a genuine interior.
- Growth: with a16,b20,r4/3,q6/5, the endpoint changes at n0/n1 are4 and8/3;
  higher-step-always-faster fails. Each slope depends on its own endpoint delta.
- Saturation: `max(0,min(t,1))` at t−1,0,1/2,1,2 gives0,0,1/2,1,1.
  The bounded finite result reaches its endpoint, rather than approaching it
  asymptotically. Check ordered-bound prose and retain valid geometric cases.
  These arithmetic witnesses are not browser or WCAG tests.

Inspect all five new passages in their complete composed context. Reverse the
five replacements in memory and require byte equality to the assigned guides;
this verifies that wrappers, examples and unrelated text survive. Separately
compare layout's complete diagnostic350–371, all233 whole card blobs, unchanged
other live files and source originals to the assigned pin. Check the heading
rename against actual live link references; a historical allocation's heading
string is provenance, not a file to rewrite. Do not count equality as semantic
review. Record predecessor/current applicability of the five named old claims
and the two new repeat contexts concisely; do not duplicate the old36 records.

From main, start with `make help`; run `make check-skills`,
`make check-skill-versions`, `make check-package-paths` and a fresh `make design`.
Inspect the actual fresh ZIP: all eight Markdown members must equal committed
source bytes, with the current owning version/history. Record archiveSHA-256,
commands/statuses/denominators and existing soft warnings rather than calling
warnings-free success. Use package-native gates; no installation or publication.
Check named diffs, LF/final newlines, local links/fragment applicability and
`git diff --check` in both worktrees. Retain failed/recovered/unrun attempts.
Accepted84 diagnostic cases and52 old deltas are unchanged and need an explicit
applicability check, not a fresh replay claim. No hosted rendering or browser
conformance suite is required for protected card bytes and arithmetic prose.
P10-13 still retains final-revision applicability at final composition.

## Commit and return

Commit exactly the four source paths in the table on main and exactly the three
planning outputs in their allowlist on planning. Use named `git commit --only`
paths; stage only new named files as needed. Inspect other staged work first.
Each assistant-authored commit includes separate trailers:

```text
Co-authored-by: Codex <noreply@openai.com>

Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

The proposed closing report identifies this initial prompt and issuing commit,
assigned/actual source parents and commits, actual source/three-path planning
scope, four-row proposed walk, five changes and meaningful checks. Record actual
commit identities after committing without forcing a separate receipt-only
commit chain; exact current planning return ID may be reported in the Operator
handoff when unavailable inside its own commit. CC must leave statuses open.

Return a usable integrated source correction for independent CDC review, with
clear remaining fidelity/full-corpus/actual-browser/final-release owners. Do not
close the slice/arc/project, accept your own work, open the next slice or push.
