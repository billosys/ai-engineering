# CC implementation — Slice18 Iteration01

Execute this correction and return evidence to CDC Sofie through the Operator.
Two contributors, Expedited Mode. Initial assignment `cc-prompt.md` is preserved;
this is the current assignment. [Independent review](cdc-verification.md)
accepts S18-03/04 and leaves S18-01/02 open. No closure, successor, push or publication.

SOURCE/main pin `c9d98a3ec3d0a24c30a18431d7aeaa13f6451872`; its entire design
tree equals the reviewed candidate `7b20ccc3a7019cfad6f238522314ce8ab70e0a35`.
Planning predecessor `5d8f3a9ffed74dbf69255956e450b855a10a3ed6`; issuing commit
is the commit adding this prompt. External Fennel work is protected. Reconcile
actual drift by path; never reset/rebase unrelated work to recover an old pin.

## Required reading and intake

Before dependent edits, read in this order and record coverage plus a short
contract readback in the existing batch record. Recover truncated output.
Paths beginning `knowledge/` resolve in SOURCE; planning links resolve here.

1. Required-full: current AGENTS and collaboration-framework entrypoint;
   `knowledge/project-management/SKILL.md` then its `guides/README.md`.
   Required-section: project-management guides02 “Slice iteration filenames and
   preservation,”03 “Issuing and executing an iteration”; engineering-methods
   guide07 “Required reading and CC intake”; work-verification guide05 “Evidence
   During Correction Review.” Apply instructions' necessary dependencies.
2. Required-section: [project plan](../../project-plan.md), active body from
   “Purpose and authority” through “Current status,” before Version History;
   then [arc plan](../arc-plan.md), active body before Version History. Required-data:
   their project/arc ledger criterion rows and states, not historical roll-ups.
   Required-full: [slice plan](slice-plan.md), [ledger](ledger.md), this prompt,
   [CDC review](cdc-verification.md) and current [closing report](closing-report.md).
3. Required-full: `knowledge/concept-cards/SKILL.md`, guides05 evidence lifecycle
   and06 graph/CQ; `knowledge/design/SKILL.md` and `guides/colour.md`. Apply the
   distinct-warrant rule, positive teaching and contextual perception boundaries.
4. Required-full: all eleven current Slice18 cards and current batch record.
   These are the small existing endpoint set, not a new corpus review. The
   initial prompt is reference-only for historical intake; this prompt carries
   all current mutation obligations. No unrelated predecessor histories.
5. Required-section: prepared `knowledge/design/sources/md/posts/okhsv-and-okhsl.md`
   106–178 (HSV/HSL),284–307 and745–770 (tables/scope),345–425 (scaled axes and
   curved-top compensation). Source SHA256 remains
   `227d62385a8ca4dfa77e9f5a10d55c9bd8d1c2f29d8964f59a1059bfb67d5d19`.
   Read the actual endpoint sections used by each revised warrant, including
   the complete accepted `hsl-css-syntax.md` endpoint. Required-section: the
   definition/notes in CIE [saturation](https://cie.co.at/eilvterm/17-22-073) and
   [chroma](https://cie.co.at/eilvterm/17-22-074), plus the status/title of the
   frozen [CSS Color4 CRD](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/).
   Reuse unchanged source premises only with their inspected content and scope;
   unavailable inputs block dependent assertions, not unrelated corrections.

## Binding scope

Only these five bodies under `knowledge/design/concept-cards/posts/` may change:

- `hsv.md`
- `okhsv.md`
- `colour-gamut.md`
- `colour-picker-design-principles.md`
- `chroma-vs-saturation.md`

Freeze all233 metadata prefixes byte-for-byte at this source pin, all existing
headings and literal Source Reference sections, the other228 cards,161 source
files, all guides/helpers/schema/Make/package lists and owning SKILL/history.
Keep1.0.15 for this unfinished correction. No new fields or semantic metadata
exceptions; the initial authorized exceptions are already accepted.
Preserve unrelated LFE/Fennel work, including untracked paths if still present.

CC planning writes remain exactly `artifacts/batch-record.md`, `closing-report.md`
and ledger Evidence/Notes. Do not change ledger criteria/statuses, plans, either
issued prompt or CDC review. Keep one supporting artifact and prior observations
at their actual revisions; identify superseded conclusions without silently
erasing them. No fresh corpus copy, software validator or investigation.

## Implement and reconcile

**Binding F01 — HSV/Okhsv repeated claims.** In HSV Example1, retain Ottosson's
reported deep-blue shift as saturation decreases, attributed to the uninspected
figure. Remove the inference that S=0 has a perceived hue; Δ=0 makes hue
powerless. Replace the HSL neutral contrast with the actual chromatic contrast:
for RGB(g,g,g), both S=0 and V=L=g; for encoded RGB(.8,.2,.2), HSV S=.75,V=.8
versus HSL S=.6,L=.5. Reconcile Context/Common Applications in both cards with
the exact model definitions: fixed numeric H/h and S/s controls are possible,
but changing V/v does not guarantee unchanged perceived hue/saturation or a
specified brightness. Retain the useful task of exploring vivid candidates;
scope “most vivid” to the named model/gamut criterion, not universal perception.
In HSV Common Confusions use its exact Δ/M versus HSL formula and distinguish
the article's rough appearance account from the mathematical definition.

**Binding F02 — positive definitions and source-specific repeats.**

- Gamut Example1: horizontal C·L_r/L, vertical L_r; describe the source's
  triangular approximation and remaining curved top/compensation consistently
  with Okhsv. Do not label it a new visual observation or raw Oklab C plot.
  Correct the frozen CSS document's status to Candidate Recommendation Draft
  in this card's note and the batch reading record; retain its date/URL.
- Principles Key Properties: first table's families are HSV,HSL,HSLuv,Lab-like,
  NCS; the later table compares Okhsv/Okhsl. Munsell is historical context,
  not a rated profile. Keep eight named criteria and their qualified ratings.
- Chroma/saturation Core: restore the accepted Slice17 positive distinction,
  accurately paraphrasing CIE. Chroma compares colourfulness with the brightness
  of a similarly illuminated achromatic reference; saturation relates it to
  the area's own brightness. Keep appearance/reference conditions and separate
  Oklab C=hypot(a,b), HSL/HSV S and picker mappings. No universal C/L equation.
  Align Quick Definition/Key Properties where needed so chroma's appearance
  meaning is not lost. Preserve the useful source-specific model examples.

**Binding F03 — actual warrants and answers in the existing batch record.**
The current66 rows preserve correct identities/directions but use template
warrants and broad P1–P8 lists. Replace them with actual connecting reasons,
inspected endpoint sections and precise source/premise support. Compact groups
are recommended: enumerate exact member row IDs and provide a shared substantive
reason when it really applies; individual rows may point to that group. No need
to quote every Core Definition or produce66 separate paragraphs.

Worked example: rows1/2/7 connect HSL/HSV's bounded encoded-RGB transformations
to their specified RGB gamut (gamut Construction item3 and HSL/HSV equations,
with prepared106–178). This is an editorial model/gamut association, not a
literal HSL bullet in gamut's Related section. Row42 connects HSL coordinates
to the accepted CSS-syntax card's normalization/notation rules. It does not use
the historical Munsell/NCS premises. Prerequisites target→card support learning;
extends card→target elaborates the target; related/contrasts are symmetric with
their actual comparison stated. Similar names/source identity are insufficient.
Separate source statements from justified editorial inference; identify any
remaining unsupported member and its actual consequence rather than force a pass.

Keep the66 identities,65 predecessor joins and15 CQ occurrences/three texts.
Update affected body before/after joins and new-statement accounting from actual
final bytes; retain unaffected joins. Add345–425 to P4 when using Okhsv geometry.
The chroma/saturation CQ must actually explain its two CIE references as well
as model coordinates; revise that bounded answer/coverage and affected outcome
rows. Preserve honest partial picker-quality/use judgments and all higher gates.

## Checks and return

Read all five final bodies completely, checking repeated applications/examples/
confusions against Core. Reproduce the chromatic witness and at least two
greys: RGB(.2,.2,.2) and(.5,.5,.5), both S=0,V=L=g with powerless hue.
Check source axes and actual table columns directly; inspect positive CIE
reference distinctions in both the card and CQ answer. Walk every66 warrant
membership against its actual reason, direction and premises; check changed
body joins/answer components, not counts alone. Retain unaffected toe/rational/
Okhwb arithmetic with the independent review pointer and applicability reason.

Check exact changed-path scope, all233 identities, all233 raw headers, five
literal citations/headings, other228 cards/all161 sources and all guides;
LF/EOF, local links/fragments and `git diff --check` in both checkouts. CDC's
fresh native/package results are in its review at c9d98a3e; these five unbundled
card-body changes cannot change the eight package inputs. Check SKILL/history,
eight packaged Markdown source inputs and Make/package dependencies against
that revision before retaining those results. Do not call them fresh runs.
If any relevant input or execution condition has changed, rerun affected gates
sequentially from `make help`; do not silently waive a mandatory gate.

Update the sole batch artifact with intake, F01–F03 changes/observations,
affected outcomes/warrants/CQs, preservation and actual checks/limits. Update
the first-class closing report with this iteration/issue, source and planning
identities, all four dispositions (03/04 CDC-done;01/02 proposals), artifact and
bubble-up. Original capture fidelity/P10-11, full corpus/global/live review,
browser/AT/picker behavior, final hosted views and release remain open.

Commit only actual changed members of the five source files, separately from
exactly the three planning outputs, using explicit paths (`git commit --only`)
and both required separate Codex/Billo AI co-author trailers. Return final hashes
to the Operator; no receipt-only commit chain and no independent self-acceptance.
