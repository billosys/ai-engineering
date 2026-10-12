---
slice: slice08-token-conventions-source-fixes
status: open
---

# Arc02 Slice08 — Token Conventions Source Fixes

## Result and authority

Apply the accepted Slice03 token corrections that still remain in the live
payload, preserving the new portable methods. This is source delivery plus
checks in one batch, not another evidence/handoff phase. Current project/arc
plans and Operator execution amendment authorize it. CDC Sofie + separate CC,
Two-Contributor Workflow, Expedited Mode; no source self-acceptance.

SOURCE/main `52f0b5208b538d9e1e351e22aa3e2c88e620014f`, accepted Slice07 return.
Planning predecessor 7a135d80934ce7c4fc376ba86336f166a1547c61; the commit introducing
this open set is the issue. Preserve unrelated work and inspect drift before edits.

| Exact main write path | Intake SHA-256 |
|---|---|
| `knowledge/design/SKILL.md` | `813083e7c386e6bca92927cc14a10c2a806debfa48c47e8289b1d5938ded66e9` |
| `knowledge/design/version-history.md` | `7eeb7ffecd93e57088995dc4fef8dffb9b8631112bf44237a17b06e642a82a6b` |
| `knowledge/design/guides/design.md` | `505e16d8fd6f30220ac56526b09fa34b648cdc845e350151b61b49dfbee90a8a` |
| `knowledge/design/guides/foundations-of-design.md` | `9f2a5caa5cc1db573fca5cfb37eab8cc8aebb048d2d2a8e3091ea7e81632094e` |

Only those four paths change. Entrypoint changes are limited to metadata version;
its brief/routes/three corrected teachings and primitive CSS remain exact.
Version history preserves all prior entries and adds the matching correction.
All other guides, cards/originals, README/Makefile/package lists and other skills
are unchanged. No export/tooling harness, new source file, installation or publication.

## Accepted inputs and reconciliation

Reuse [Slice03's handoff](../slice03-token-system-conventions/artifacts/correction-handoff.md),
[source comparison](../slice03-token-system-conventions/artifacts/source-comparison.md)
and [independent closure](../slice03-token-system-conventions/cdc-verification.md)
at 3817d83c: 42 selected token assertions/21 non-overlapping proposed actions.
Those are bounded accepted evidence, not current source instructions to restore
obsolete examples. The historical original baseline is dffa504e. Slice07's
independently accepted rewritten payload takes precedence over old proposed text.

CDC's current 21-action query finds seven literal targets still present, each
exactly once: ACT-10/11/16 in design.md, ACT-18/19/20/21 in foundations. The other
14 are rewritten/removed: ACT-01–09/12–15/17. Semantic inspection confirms the
new entrypoint/colour/design contexts remove their old fixed profile, mandatory
layer/direct-value bans, automatic propagation and formal type-equivalence claims.
CC checks and records this applicability; substring absence alone is insufficient.
Keep a compact 21-row disposition table in the one batch record, with current
heading/context pointers and changed/preserved/superseded reasons. Do not copy
42-result/114-unit datasets, regenerate their validator or replace historical evidence.

## Binding implementation recipe

Retain supplied identity and optional token architecture. Separate interchange
format/types from architecture layers and from project-defined semantic names.
DTCG stability is not W3C standards status; named systems/generations and selected
examples do not prove one universal or dominant architecture. Layering does not
guarantee legibility, propagation or effortless onboarding. Preserve local choices
and explain their cost rather than impose another system's policy.

Replace the seven surviving targets with the text below. Line wrapping may vary;
meaning, examples and source links are binding. Match each actual old block from
the accepted handoff at this new source pin before replacement, not old line numbers.
ACT-10/11 retain the adjacent type/spacing/tonal-scale assertions for later T/L
review; no claim is made that these assertions are supported. Rename design's
“The Convergence Thesis” heading to “Comparing Design Systems.”
ACT-16 replaces the complete current closing paragraph of “The Deeper Structure,”
including its adjacent “The structure is dictated by human perception…” sentence.
This bounds that unsupported inference from token convergence; it does not prove
or broadly rewrite the separate perception argument earlier in the section.
ACT-18 preserves the first visual-style-category sentence, which remains under
L/Arc04 review; the corrected DTCG description is separate. ACT-20 preserves
adjacent hex/OKLCH and CSS-relative-colour sentences for T/L/browser review.
ACT-21 removes the unsupported Material 3 naming example, keeping DTCG structure
and Utopia as distinct subjects. Do not add an end-user notice about our failed
research retrieval; preserve that gap in planning evidence instead.

### ACT-10

```text
Material Design, Carbon and Polaris name distinct products and generations.
Compare their token models only after identifying the product, generation,
page date and token category. The available examples do not establish that
these systems share one architecture.
```

### ACT-11

```text
[Material Web's theming documentation](https://material-web.dev/theming/material-theming/)
distinguishes reference, system and component tokens, and allows concrete
component values. [Fluent 2's token documentation](https://fluent2.microsoft.design/design-tokens)
presents global and alias layers. These are bounded documentation examples,
not evidence that every design system requires the same layer count.
```

### ACT-16

```text
Comparisons between Material Design, Carbon and Polaris need an identified
product generation and token category. Their available examples do not
establish one shared token architecture. A token-model comparison also does
not establish a universal law of perception.
```

### ACT-18

```text
**Universal visual style categories** across all five systems: colour,
typography, spacing/layout, motion, icons, and elevation/depth.
[The DTCG 2025.10 Format Module](https://www.designtokens.org/tr/2025.10/format/)
is a stable Final Community Group Report intended for implementation, not a
W3C Standard or Standards Track document. It specifies a JSON interchange
format with value types: `color`, `dimension`, `fontFamily`, `fontWeight`,
`duration`, `cubicBezier`, and `number`; composite types include `strokeStyle`,
`border`, `transition`, `shadow`, `gradient`, and `typography`. These type
categories describe value structure, not a required token-layer architecture.
```

### ACT-19

```text
## Token Architecture Choices
```

### ACT-20

```text
One possible notation uses primitive values (`color.blue.500`), semantic
aliases (`color.primary`, `color.surface.default`), and component bindings
(`color.button.primary.background.hover`). This example is not evidence that
three tiers are the dominant industry pattern. Choose reusable values when
reuse helps, semantic aliases when shared meaning or theme variation benefits,
and component bindings when local control warrants their maintenance.
Additional layers add indirection; fewer can couple consumers to shared values.
A value change reaches only consumers whose references resolve through it;
local literals and separate mappings need their own review.
```

### ACT-21

```text
DTCG 2025.10 defines a typography composite with `fontFamily`, `fontSize`,
`fontWeight`, `lineHeight`, and `letterSpacing` values or appropriately typed
references. Composite value structure is separate from token naming and layers.
Utopia's calculator example uses numbered steps such as `--step--2` and
`--step-5`; its method and prefix are configurable. Choose names and scale
construction for the adopting project rather than treating an example as a
universal convention.
```


## Version, validation and useful-method checks

Current skill metadata is 1.0.2. Update only metadata to 1.0.3 and add a neutral
matching sibling history entry for these scoped token corrections; no final 1.5
release or duplicate owned-tree version label. Preserve source history entries,
all three colour corrections, three entrypoint CSS blocks and the unchanged
layout diagnostic expression, parameters and Type fragment. Retain other research
as unassessed at its current Arc02 owner rather than imply whole-file acceptance.

Start with main `make help`; run `make check-skills`, `make check-package-paths`
(including source/fresh-package version checks), fresh `make design`, and source/
planning `git diff --check`. Inspect all eight actual packaged Markdown members
against committed source. Check all changed contexts and original 21 actions;
confirm seven repairs, no restored superseded profile and no broken Markdown
neighbors/routes. No Makefile/README packaging change is needed: paths are stable.
Report actual warnings, not a frozen expected count or a fabricated clean result.

Use the delivered prose in three analytic cases: an existing two-layer token
system, a local component value without a shared role, and one shared value
reached by both direct and transitive aliases plus an independent local literal.
The guide must permit the first two; the third changes only dependent consumers.
Retain Slice03's accepted button=new/badge=new/fixed=old witness with an explicit
model applicability check; no browser/renderer or actual export claim. An alleged
universal three-layer rule, “DTCG requires these semantic names,” or “every
consumer updates” must fail human review of the same cases. Test unchanged
literal teaching by direct source comparisons; no new software-test framework.

## Reading and execution manifest

Required-full: this slice plan, its ledger and initial prompt; current main
SKILL/history and colour guide; Slice03 source-comparison artifact; Slice07 I1
independent closure section. Required-section: current project Scope/DoD,
Immediate sequence, Evidence economy, Recorded Operator decisions and Workflow;
current arc Capability, Complete coverage, Findings ownership and Workflow;
all 13/ten project/arc ledger criteria. Governing framework/project-management,
prompt-authoring/intake and work-verification routes remain required as applicable.

Required-section source reads: design's complete “Comparing Design Systems”
(currently “The Convergence Thesis”), “Name the Role, Not the Value,” “The Deeper
Structure” and “On Tools and Technology”; foundations' complete documentation
organization section and Section 6 token/spacing/typography/responsive notation,
plus both protected colour paragraphs. Review actual Type diagnostic route and
layout's full arithmetic illustration for preservation only. Other source context
is conditional: any query match needed to interpret one of the21 action outcomes.

Required-data: accepted handoff at 3817d83c, all 21 ACT headings/path/old-target/
proposed-target/unit/owner entries. Extract those fields without clipping, compare
all 21 old targets to source 52f0b520, emit complete dispositions, and read complete
current counterpart contexts for semantic judgments. Load selected ACT-10/11/16/
18–21 prose/rationale/adjacent-boundary definitions in full. Do not interpret
boundary IDs or substring counts as semantic acceptance.

Reference-only: the earlier 42 claim results/checker and inaccessible Material 3/
historical Polaris passages; load a particular assessment if applicability is
contested. The accepted primary comparison supports these bounds. CDC refreshed
DTCG 2025.10 Status/§4/§9.8 and complete short Material Web/Fluent 2 token pages on
2026-10-12; no drift invalidated the selected corrections. CC need not repeat
unavailable-generation acquisition. If exact evidence no longer supports a
proposed claim, record the discrepancy and stop that dependent edit for CDC.
Current URLs still do not establish historical fidelity or full-source readiness.

Record concise intake/readback in `artifacts/batch-record.md`; recover truncated
required reads before edits. Resolve meaningful drift/conflict, then execute the
recipe under existing authority. Prose wrapping and local temporary check mechanics
are discretionary; selected meaning, scope and gates are binding.

## Outputs, commits and return

One sole supporting artifact: `artifacts/batch-record.md`, containing 21-action
applicability, seven before/after context pointers, source/package identities,
analytic cases, actual checks/warnings/failures and remaining owners. Planning
write allowlist is exactly that file, `ledger.md` evidence/notes only and
`closing-report.md`. Keep four statuses open for CDC review; preserve criterion
text. The report covers all four rows, one-artifact inventory and Arc02 bubble-up.
Commit exactly the four main paths, then three planning outputs. Both need
separate Codex/Billo AI trailers. Record source commit/package identity in the
same planning return; no receipt-only chain. Preserve issued/reviewer/parent
files and all unrelated work. No broad source rewrite or new evidence registry.

Complete 233-card/five-dimension/eight-live review, P10-11 originals/fidelity,
actual fresh-context tasks, accessibility/browser behavior, metadata/GitHub and
final package/release/Operator gates remain under their existing owners. Remaining
unqualified type/perception/spacing/colour-trend/tooling claims get exact pointers
and re-entry owners in the batch record. This source batch does not close them.

## Author readiness and assignment history

CDC inspected the accepted handoff/comparison/closure, all 21 literal targets,
current counterpart methods and complete affected paragraphs. Fourteen obsolete
old targets are semantically superseded; seven surviving targets have unique
matches. Applied optional roles/layers and supplied-identity guidance from the
current entrypoint/colour and accepted Slice03 policy. A temporary virtual patch
of all seven replacements and required heading/neighbor composition preserves
Markdown block delimiters and both protected foundations colour passages, and
removes the surviving old targets; main was not edited. First query helper
mistook the ACT-19 fenced heading for a new action boundary, failed and was
corrected to split only on actual ACT headings. The corrected full 21 query passed.
Fresh primary reads confirm named bounds; no source acquisition/fidelity inference.
The recipe is source-grounded, design-complete and falsifiable with contextual
layer/direct-value/propagation cases; no consequential design is delegated to CC.

Final open-set checks pass: ten planning paths only, unchanged 13 project/ten
arc criteria and statuses, five preserved Slice07 criteria now done, four new
open rows, four source pins and seven exact recipe blocks; 128 local destinations
and 44 fragments resolve across the ten files. LF/EOF and diff checks pass.
The first formatting-helper invocation used an unavailable `python` command;
rerunning with `python3` completed it and the link check successfully.

## Assignment history

- Initial `cc-prompt.md`, issued at `5f7c11ed`, returned at source `d644db46` /
  planning `a2972783` after rebase onto byte-identical live inputs. CDC accepts
  S08-02/03; S08-01/04 remain open for F01.
- **Current assignment:** `cc-prompt-iteration01.md`, issued 2026-10-12 by this
  introducing commit, predecessor `cc-prompt.md`; active for separate CC.
  Rename the missed design heading and update its existing return records.
  I1 source allowlist is only design.md; planning allowlist is only the existing
  batch record, ledger evidence/notes and closing report. Its narrow delta scope
  supersedes the initial four-source mutation instruction, not its four criteria.
  Preserve all seven corrections and all other bytes; complete the same 1.0.3
  correction. Full I1 reading/check/return contract is in that preserved prompt.

### I1 author readiness

CDC inspected the actual unique heading, complete Section I, accepted replacements
and eight-file route union, and applied current domain guidance on contextual
comparisons and no universal architecture. A virtual exact one-line change
passes the same heading check that rejects the current and duplicate-new-heading
specimens; every other source byte is preserved. No live inbound fragment needs
repair. This resolves the entire remaining source decision; new theory inquiry
is unnecessary. Current source/package/row checks and contextual cases are
independently reproduced in cdc-verification.md; I1 reruns only affected checks
and preserves accepted evidence after byte applicability. One artifact, roles,
original criteria and all parent obligations remain unchanged. Final author checks
confirm six planning writes, unchanged issued prompt/CC return/parent ledgers,
four preserved criteria with two done/two open, 34 local destinations and four
fragments resolved, LF/EOF and diff checks passed. Main remains unchanged.

## Version History

- 1.1 (2026-10-12): Initial review accepts S08-02/03; issued one-line I1 for the
  omitted design heading and accurate return scope. Accepted token corrections,
  original criteria and all parent gates preserved.

- 1.0 (2026-10-12): Opened the next ready source batch after Slice07 closure;
  apply seven residual token corrections and reconcile 21 accepted actions without
  recreating analysis packets. All parent/corpus/behavior/release gates retained.
