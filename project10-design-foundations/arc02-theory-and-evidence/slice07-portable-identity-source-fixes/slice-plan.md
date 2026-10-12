---
slice: slice07-portable-identity-source-fixes
status: open
---

# Arc02 Slice07 — Portable Identity Source Fixes

## Result, authority and exact baseline

Remove the accidentally inherited publishing/arts identity from the entire live
skill and package. Replace its palette/font/site presets with usable methods
that start from the adopting project's brief and preserve supplied identity.
The Operator already authorized removal, Git-only historical retention and no
compatibility bridge. The [current project](../../project-plan.md), [arc](../arc-plan.md)
and accepted [Arc01 composed contract](../../arc01-portable-contract/slice03-contract-composition-and-handoff/artifacts/composed-contract.md)
provide authority; historical proposal/pending labels are superseded by the
Arc01 Operator acceptance `38b66d0d`, not retroactively edited.

Two contributors, CDC Sofie plus separate CC via Operator; Expedited Mode.
Planning predecessor `e8076bec92d2c777358bc882baafd6d75d519589`. The commit introducing this prompt
is the issue. SOURCE/main `3658f79a06cd3d28ebca5e05622e02c229bd29b6` contains the accepted Slice06
corrections. Preserve those three corrected teachings exactly. Exactly eight
source paths are mutable below; originals/cards, Makefile, README, package lists
and other skills are unchanged. Existing names/paths remain; no archive/profile,
new source helper or new template tree. History lives in Git and the neutral
owning skill change record, not a retained adopter case study.

| Main write path | Intake SHA-256 |
|---|---|
| `knowledge/design/SKILL.md` | `f4f352f5859513c120c9f7230a316626e0eb6fcf82cb8c0f61b6d3cd63d9bba3` |
| `knowledge/design/version-history.md` | `e941ab16e859c7575db5fb9a950f55598f7d27d7273cc9842abeadd9de2c5066` |
| `knowledge/design/guides/breaking-the-layout-monoculture.md` | `76d209306a8ade1da51f62ad86fb7f01f103f0f4d033e7235c3b4b023397b845` |
| `knowledge/design/guides/colour.md` | `7187dabc5ca00d5d7c48c2a70dd2155731cbf68716c7cb8b1a0d3579285a0aea` |
| `knowledge/design/guides/design.md` | `e4953fd1452102c98df6f0fcf33bc17bd3732f011180475daa8fd256e70e687b` |
| `knowledge/design/guides/foundations-of-design.md` | `922c78c65a0e659bafa637e23f3bc152a8fae99a0f1c1d6fe5d90b559fedb45c` |
| `knowledge/design/guides/layout.md` | `361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec` |
| `knowledge/design/guides/type.md` | `8a9f1ab35dee3373ebbf1460416e334adffcd908f095463fa015c6ef0a5f5d7c` |

## Binding decisions and implementation route

The adopted contract's brief/profile is a short contextual aid, not a schema or
mandatory questionnaire. Ask only consequential questions; mark unknowns or
state reversible proposals. Respect supplied tokens, fonts, logos, content,
languages and fixed decisions. Do not infer a publishing platform, three sites,
three fonts, warm neutrals, brown palette or universal scale/endpoints. A user
may independently select any of those choices; no colour/font blacklist follows.

1. **Entrypoint.** Neutralize the description and project-specific introduction.
   Add a short brief-first/preserve-identity instruction before task routes.
   Keep the compositional ethos and six useful guide routes. Replace the colour
   guide's palette/three-site summary and the type guide's named-font/axis summary
   with the new methods. Replace the palette, fixed semantic-to-brown mappings,
   three-font role/step/axis tables and domain override snippets. Roles are
   contextual examples, never prescribed palette/font names or a required number.
   Update the fixed three-font/one-accent and three-site principles/mistake checks
   wherever they enforce this profile. Token layering is optional project
   architecture; existing semantics win over renaming/re-layering. Make route
   references explicit package-relative links under `guides/` when rewritten.
2. **Colour guide.** Replace the adopter-specific swatch/table/demo document
   with ordinary Markdown teaching in this order: supplied context/identity →
   required surface/text/interaction/state roles → choosing candidate values →
   optional primitive/semantic/component aliases → themes and actual pair checks.
   Delete Brand Brown, warm-neutral presets, three site accents, numerical
   profile mappings and all site demos; renaming them is not removal. Keep
   OKLCH as a useful tool with context-dependent perceptual limits, not an exact
   brightness or contrast guarantee. Explain complete rendered foreground/
   background/state pairs, compositing/gamut and actual checks. If no palette is
   supplied, propose a task-specific candidate only with reasons/assumptions;
   the guide itself supplies no new default palette. Example semantic mappings
   use supplied tokens and demonstrate role separation, not selected colours.
3. **Type guide.** Replace the original three-font sales/specimen/site/alternative
   document with ordinary Markdown teaching in this order: script/content/reading
   context and supplied assets → roles/hierarchy → candidate/fallback checks →
   scale and optical judgment → available axes → context variation and review.
   Remove the Fraunces/Literata/Plex assignments, publishing samples, per-site
   axis presets and Newsreader selection narrative; do not retain that roster
   as an anonymized example. No mandatory family count, ratio or musical/scientific
   harmony guarantee. Keep the scale relationship `size(n)=base*ratio^n` as an
   optional construction, with declared parameters and reasonable optical
   exceptions. Axis choices depend on the selected asset; do not assign unsupported
   axes or claim font-failure/script/browser outcomes without actual testing.
4. **Scoped numeric illustration, not a replacement preset.** Remove the old
   C&B-derived endpoint/ratio/clamp blocks in the entrypoint and layout's
   `The Fluid Foundation` section. Their replacement illustrates the accepted
   [diagnostic configuration](../../arc01-portable-contract/slice03-contract-composition-and-handoff/artifacts/example-configuration.md):
   bases1rem/1.125rem, ratios1.2/1.25, interval20rem–80rem. These are explicitly
   *arithmetic illustration inputs*, not recommended fonts/roles/spacing or
   adopting-project defaults. Show this single supported expression:

   ```css
   --example-step-0: clamp(1.000000rem, calc(0.958333rem + 0.208333vi), 1.125000rem);
   ```

   Explain that R=16px gives nominal320–1280px endpoints, while R=20px moves
   them to400–1600px; interpolation is per step, not generally a geometric
   progression at intermediate widths. Do not assign negative steps to functional
   text. Type may use the same named exercise instead of another configuration.
   Keep independent existing primitive CSS, but remove adjacent instructions
   forcing every spacing/gutter/size from the example or implying universal zoom
   compliance. Ratios and shared spacing are local choices. This exercises and
   applies accepted evidence; it does not settle every remaining T assertion.
5. **Other affected guide contexts.** Across all six guides remove the inherited
   monogram/root-home links and branded footer elements; preserve neutral
   attribution/license facts. In layout remove C&B manifesto/identity language,
   perfect-fourth prescription, automatic family-recognition test and publishing
   identity assumptions. Describe composable relationships and context-led
   examples instead. A generic book content composition may remain only as a
   method example without inherited identity, assets, font/palette presets or
   promises that it handles every possible viewport without inspection. In design
   replace the publishing-collective origin and the mandatory profile in
   Constraint/Unity paragraphs with scoped constraints/coherence from the accepted
   contract. An isolated named variable-font teaching example may remain as a
   clearly optional example; it must not prescribe the old font roster.
6. **Presentation dependencies.** Delete guide-author styling attributes that
   depend on the removed `--brand-*`, `--neutral-*`, `--books-*`, `--art-*` or
   `--home-*` presentation palette. Do not remap them to disguised brown aliases.
   Preserve non-profile layout teaching/CSS; distinguish author presentation
   markup from code examples. Foundations has four such layer attributes; layout
   has28 card/layer attributes including the hardcoded warm backdrop. Inspect
   all affected paragraph/markup neighbors after editing. Preserve the Slice06
   nonlinear-conversion prose and substantive unrelated research; broader R/T/C/L/G
   assertions retain current Arc02 owners, not implicit acceptance.
7. **Version/history.** Current owning metadata is1.0.1. Apply compatible bug
   correction1.0.2 and add the matching neutral sibling history entry, preserving
   prior entries. No inherited profile/case study in live history, no duplicate
   skill-version prose, and no version bump to the final project release yet.

CC has local discretion over clear prose, headings and illustrative token names
within those binding decisions. Do not rewrite unrelated research/theory claims
or blindly preserve a profile under new nouns. Newly noticed outside-scope claims
get exact contexts, owners and re-entry in the compact batch record. Portable
method must remain usable; wholesale deletion of useful guidance is not success.

## Reading, work and observable checks

Load repository/planning/project instructions and current collaboration-framework,
project-management entrypoint/wayfinder, top-down/close and prompt-authoring/intake
routes. Follow the current project/arc body and all13/ten criteria, this entire
open set and the following bounded source manifest. Recover truncated required
reads before dependent edits; record concise extent/readback in the batch record.

- Full main entrypoint, colour guide, type guide and sibling history.
- All six guide hero/footer contexts and complete paragraphs matched by whole-live
  identity/profile queries. Include spelling/Unicode variants of Cowboys & Beans,
  C&B, cnbb, monogram, publishing/arts collective, brand browns/warm neutrals,
  site palettes and named-font/axis/default-role tables. Inspect every author-style
  line using the removed palettes. Counts/hits are navigation, not semantic proof.
- Layout baseline1–69,263–269,354–443,446–529, all card/layer presentation lines,
 780–827 and846–913; design baseline28–49,185–241 and349–355. Foundations'
  header/footer and four layer attributes plus the three preserved Slice06
  conversion contexts. Remaining guide content is lookup-only unless a new
  coupling match or edited context makes it required; full semantic review is later.
- Accepted composed contract's binding decisions, adopting-project inputs, eight
  live-file map, warning against anonymized defaults and worked contract cases;
  Arc01 Operator closure. Diagnostic configuration in full and its accepted
  Slice03 arithmetic/closure, retained by source/model applicability. Slice06
  independent closure and exact three current corrected passages.

Inspect drift against the eight hashes first. Then read → apply removal and
portable replacement → inspect complete changed contexts and the full eight-file
live/package union → run existing checks → commit. Use `make help`,
`make check-skills`, `make check-package-paths` (includes source/fresh-package
version gates) and fresh `make design`. Inspect all eight actual Markdown members
of the final zip for identity/default leakage and changed source equality. Report
warnings by actual result; do not silently suppress the existing ones. No
installation, publication or original acquisition/conversion is assigned.

Use three explicit analytic specimens against the *delivered guidance*: (a) a
literary page with no supplied identity, (b) an existing interface supplying
`--client-surface`, `--client-ink`, `--client-action` and its chosen typeface,
(c) an independently supplied brown palette and Fraunces. Show consequential
choices, preserved inputs and cited guidance; reject inherited palettes/rosters,
forced renaming and a font/colour blacklist. Include a renamed-brown-preset
counterexample: removal of brand words alone must fail human review. These are
contract walks, not fresh-model performance or browser tests. Actual fresh-context
specimens remain required by A02-09/P10-02 and final composition; no new harness
or experiment is assigned here, and this source batch cannot close those gates.

Reuse the accepted diagnostic arithmetic after verifying its literal parameters.
At R=16/w=800, step0 is17px; at R=20/w=800 it is125/6px, before six-decimal
rounding. This is an oracle for accidental changed coefficients/root semantics;
if code is copied, check actual source and package expressions against the named
exercise. No large theory replay or maintained transformation validator is needed.
Human inspection checks meaning, preservation and anonymous default leakage;
mechanical scans/checks verify identifiers, changed bytes, routes and version.

## Outputs, return and scope boundaries

The main commit contains exactly the eight named source files. The planning
commit contains exactly `artifacts/batch-record.md`, `ledger.md` evidence/notes
only and `closing-report.md`. One supporting record covers intake, removed/
retained method, source-before/after pointers, analytic cases, checks/warnings/
failures and pending owners. The closing report walks all five proposed rows,
inventories that one artifact and supplies the Arc02 bubble-up/silent-drop check.
No separate new palette/specimen/inventory/validator/handoff files or receipt-only
commit chain. Both commits require the standard Codex and Billo AI trailers.
Do not change criteria/statuses or issue/reviewer files; CDC independently accepts.

Full233-card/five-dimension/eight-live semantic reconciliation, original fidelity,
actual accessibility/browser and fresh-context behavior, metadata/GitHub rendering,
remaining findings, final package/release and Operator gates remain. Explicitly
mark not-assessed/blocked/unrun work rather than declaring complete portability
or DES closure from a zero-name scan.

## Author readiness and assignment history

CDC applied the adopted brief/identity contract to actual current source: full
entrypoint/history and the colour/type material, complete identity-bearing
paragraphs across the other guides, layout's specific default/code/craft contexts
and all palette-styled presentation matches. This is coupling reconnaissance,
not full eight-file/five-dimension semantic acceptance. A virtual layout witness
removed exactly28 palette-dependent author attributes while preserving all other
lines and CSS teaching. The two prescribed bad alternatives are anonymized
inherited presets and deletion of reusable method; supplied brown/font choice
is valid. The diagnostic example's configuration is explicit and accepted, so
no unresolved global endpoint choice is delegated to CC. CDC also exercised
the literal six-decimal step0 expression at the two named root/width witnesses:
16.999992px and20.833324px are within0.001px of the accepted model; the old
0.9015/0.4924 expression fails both comparisons. Full source/package
inspection and the three analytic cases remain CC execution plus independent
review; neither reading receipts nor this author witness proves future behavior.

## Version History

- 1.0 (2026-10-12): Opened authorized identity/preset removal on source3658f79a
  after Slice06 closure. Reuse accepted portable contract and arithmetic; compact
  source/package delivery, with all fresh-context/corpus/release gates retained.
