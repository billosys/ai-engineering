# CC assignment — Slice21 Font Features and Spacing

Implement the existing Arc02 correction on main and return bounded evidence.
Two contributors; CDC Sofie reviews via Operator relay. Expedited Mode.

## Authority, pin and write boundary

SOURCE is `/Users/oubiwann/lab/billosys/ai-engineering`, branch main, exactly
`52bfa46332592106f9301226571d6f441df8ce2d`. PLANNING is its `.worktrees/planning`,
branch planning; this prompt's adding commit issues the assignment, directly
after `cd32d81b3cec2542a0a7acf10ad76d5129f6fa75` (Slice20 close). Confirm actual pins/status before edits;
unrelated drift requires applicability checking, not automatic rebase/reset.
Preserve the existing untracked `knowledge/lfe/` and unrelated work.

Source allowlist (paths relative to SOURCE), maximum nine:
- `knowledge/design/concept-cards/practical-typography/opentype-features.md`
- `knowledge/design/concept-cards/practical-typography/kerning.md`
- `knowledge/design/concept-cards/practical-typography/letterspacing.md`
- `knowledge/design/concept-cards/practical-typography/ligatures.md`
- `knowledge/design/concept-cards/practical-typography/alternate-figures.md`
- `knowledge/design/concept-cards/practical-typography/optical-vs-metric-spacing.md`
- `knowledge/design/guides/type.md` — only “Check candidates and fallbacks”
- `knowledge/design/SKILL.md` — metadata.version1.0.17→1.0.18 only
- `knowledge/design/version-history.md` — additive1.0.18 entry, preserve history

PLANNING writes only this slice's `artifacts/batch-record.md`, `closing-report.md`
and Evidence/Notes cells of `ledger.md`. No other artifact/registry/tooling;
no edits to plans, prompts, criteria/statuses or CDC records. Create those three
return outputs as needed; the ledger already exists. No push/publication/CC
closure/successor. The deliverable is usable corrected teaching on main plus its
fresh local package; independent acceptance and release remain separate.

## Required reading and preflight

Use complete bounded reads; recover truncation before dependent edits. Record
actual text extents and data queries separately in the sole batch record, then
write a concise source-cited contract readback. A clean preflight permits work;
no new approval gate. Framework/domain dependencies below are repository paths,
relative to SOURCE unless noted. Current unchanged loaded guidance may be retained
in the same context after applicability checks; do not claim a prior context's
reading as current complete loading.

| Order / kind | Material and extent | Purpose |
|---|---|---|
|1 required-full|`AGENTS.md`; `knowledge/collaboration-framework/SKILL.md`; `knowledge/project-management/SKILL.md`, then its `guides/README.md`|Standing scope, workflow and native routes|
|2 required-section|PLANNING Project10 `project-plan.md`: complete active body before Version History, then Arc02 `arc-plan.md` same extent; both parent ledgers' full criterion rows|Current scope/economy,1.1 milestone and open higher gates|
|3 required-full|This prompt, `slice-plan.md`, `ledger.md`|Assignment and four unchanged criteria|
|4 required-section|PM `guides/03-planning-top-down.md`: Planning authority through Agree investigations, and The per-slice open set through Turn the slice into an implementation-ready assignment; engineering-methods `guides/07-implementation-prompt-authoring.md`: Required reading and CC intake; work-verification `guides/01-ledger-discipline.md`: full guide; testing `guides/03-validation-gates.md`: native gates and Proportionate Proof|Coherent intake, ledger discipline and adequate direct checks|
|5 required-full|`knowledge/design/SKILL.md`, `guides/type.md`, `version-history.md`; `knowledge/concept-cards/SKILL.md`|Actual design method, owning history and concept-card routing|
|6 required-section|Concept Cards `guides/05-evidence-lifecycle.md`: Assess Evidence Grade through Record Evidence Gaps; Keep Rich Prose Attached To Its Warrant; `guides/06-graph-cq.md`: Select Relationship Identity through Rich-Body Relationship And CQ Boundaries|Separate attribution, truth, confidence, edges and actual question answers|
|7 required-full|All six allowlisted cards, all six prepared pages named in the slice plan (682 lines total)|All claims, metadata, examples and source context, not a keyword sample|
|8 required-section|Practical-typography endpoint cards `font.md`, `small-caps.md`, `all-caps.md`, `body-text.md`, `typographic-color.md`: Core Definition, Prerequisites, Relationships|Inspect actual endpoint premises; full endpoints remain unaccepted|
|9 required-section|Primary documents below: CSS Fonts4 §§6.3,6.4,6.7,6.12 and7; CSS Text3 §7.2 including7.2.1; Adobe About kerning and tracking: Types of kerning through How kerning and tracking are measured|Current definitions, defaults, interactions and scoped application behavior; skip linked test-source listings, not definition prose/tables|
|10 required-data|At accepted planning9cc20338: Arc01/Slice01 `artifacts/card-source-index.jsonl`, all233 exact paths/current roster comparison. At SOURCE pin: six raw+typed headers, every prerequisite/extends/related/contrasts_with and index, complete Relationships bullets by card/subsection/order, exact answers_questions/index/memberships|Derive population and preserve independent constructs; no sampling|
|reference-only|Slice20 closing/CDC records for accepted results and limits; source-input-actions for P10-11|No copied chronology or repeated readiness assignment|

Expect from the actual pinned query: six cards678 lines/27354 bytes;27 typed
header tuples (8 prerequisite/17 related/2 contrast),25 body statements and9 CQ
memberships/four texts (CQ1=1,CQ5=4,CQ11=1,CQ12=3). Inspect every returned identity
and clause. Different counts must be explained from actual input, not forced.
Empty lists are valid; parse the actual top-level `# Relationships`. Source tree
has161 tracked files including `_conversion-report.txt`, not just160 Markdown.

## Binding recipe and source-grounded decisions

Correct every repeated assertion across complete bodies; freeze headings and
literal Source References. Preserve concrete examples and the distinction between
source reports, current technical support, editorial synthesis and actual tests.
Use concise source-specific Verification Notes; six actual five-dimension results
belong in the batch, not five generic goals mislabeled as review outcomes.

1. **OpenType Features:** retain font/application support and optional feature
   availability, but distinguish features needed for script shaping from Latin
   discretionary refinements. Attribute source-era desktop/mobile/Word/Pages
   support/UI claims rather than present them as current guarantees; no support
   survey is commissioned. Remove “explicitly enabled in most applications” as
   a universal requirement; retain meaningful defaults and feature-varying scope.
2. **Kerning:** retain specific-pair adjustment and the source's visible-gap
   example. “Always use” is Butterick's recommendation, not a universal state or
   current application default. Distinguish font data from the actual shaped
   result; visible gaps alone cannot prove kerning off. Remove optimizeLegibility
   as the recommended kerning control and stale UI as a universal procedure.
3. **Letterspacing:** keep tracking versus kerning, attributed5–12% caps advice,
   source's positive small-text/negative display-text exceptions and judgment
   caveat. No mandatory caps percentage, blanket lowercase ban, or guarantee of
   comfort. Respect scripts/shaping; no claim of uniform insertion between every
   Unicode codepoint. Preserve the Goudy anecdote with the source's disputed
   attribution/blackletter qualification, or clearly summarize that uncertainty.
4. **Ligatures:** retain the source's fi collision and nonconnecting gy example,
   and automated-feature versus manually substituted text distinction. Its
   “only fi is mandatory” and quaintness preferences concern its Latin examples;
   they cannot define required shaping across scripts. The prepared example
   drops font names: do not invent them. Avoid blanket on/off policy and claims
   that CSS changes underlying text or guarantees search/AT results.
5. **Alternate Figures:** retain separate height/form and width choices/four
   combinations (not variable-font axes), TOP40 context, columns, and zero/one
   comparison. Restore the source's lining-height exception and optionality.
   Default-is-never-wrong, mandatory lining/caps and oldstyle superiority are
   attributed preferences, not universal suitability. Equal-width digits help
   alignment but do not align unequal digit counts, decimals or layout by
   themselves; zero/one equal length is a limited clue, not proof for all digits.
6. **Optical vs. Metric Spacing:** retain the source's nu/un and round/flat
   comparison as its reported example, not newly rendered evidence. Attribute
   its anti-optical judgment, price/category rhetoric and patent statement to
   that source context, without current legal/algorithm-implementation claims.
   Use Adobe's definitions; no universal claim that every width is discarded,
   every optical result is worse, or paid fonts make metrics correct. This is
   InDesign-specific comparison, distinct from CSS optical sizing/opsz, not a
   browser toggle. No actual InDesign/font test or UI procedure audit.

Technical boundary (binding; inspect the actual definitions and qualify the draft):
[CSS Fonts4 draft](https://www.w3.org/TR/2026/WD-css-fonts-4-20261016/) defines
`font-kerning:auto/normal/none` for metric kerning; no data means no visible effect.
Common ligatures normally default on; required script ligatures are unaffected
by `font-variant-ligatures:none`. Numeral form and width requests are independent.
Prefer corresponding high-level controls; low-level feature lists can override
those requests and spacing-related suppression. These controls do not supply
missing font features. [CSS Text3 §7.2](https://www.w3.org/TR/css-text-3/#letter-spacing-property)
adds tracking to kerning, scopes typographic units/cursive behavior and optional
ligature suppression; do not flatten those conditions. [Adobe's definitions](https://helpx.adobe.com/indesign/desktop/format-and-style-text/tabs-indents-and-spacing/about-kerning-and-tracking.html)
contrast font-data metrics with shape-based optical adjustment and identify
legitimate optical-use contexts. Their conditional guidance is not performance
proof for an arbitrary font. Current URLs cannot establish original fidelity.

### Exactly seven existing metadata scalar replacements

All paths below are under `knowledge/design/concept-cards/practical-typography/`.
Apply these literal values; retain YAML field order/types and all other bytes.
No changes to `support`, identity/source/confidence/edges/CQs/aliases; no new fields.

| Card | Existing field | Exact new value |
|---|---|---|
| `opentype-features.md` | `css_implementation[0].property` | `font-variant-ligatures, font-variant-numeric` |
| `opentype-features.md` | `css_implementation[0].example` | `.text { font-variant-ligatures: common-ligatures; } .numbers { font-variant-numeric: tabular-nums; } /* requests depend on supplied font and shaping; no feature guarantee */` |
| `kerning.md` | `css_implementation[0].property` | `font-kerning` |
| `kerning.md` | `css_implementation[0].example` | `.text { font-kerning: normal; } /* metric kerning request; inspect actual font and text */` |
| `ligatures.md` | `css_implementation[0].property` | `font-variant-ligatures` |
| `ligatures.md` | `css_implementation[0].example` | `.text { font-variant-ligatures: common-ligatures; } /* requests common ligatures; required script shaping is separate */` |
| `letterspacing.md` | `css_implementation[0].example` | `.caps { letter-spacing: 0.05em; } /* illustrative 5% of font size; choose for the actual script, font, and text */` |

### Packaged integration

Within `guides/type.md`'s “Check candidates and fallbacks” section only, append
one concise practical feature/spacing method (a small subheading is optional):
choose the reading/number role and actual script; inspect supplied font features;
request suitable high-level controls; compare actual strings including fallback,
number alignment and relevant styles; retain meaningful text and check output.
Include a scoped `font-kerning: normal` and/or `font-variant-numeric: tabular-nums`
example explaining its conditions. Keep tracking contextual and preserve the
existing paragraph/user-override method, role/token rules and axes guidance.
Do not translate InDesign Optical into a CSS control or add new defaults/assets.
Bump owner1.0.17→1.0.18 with an additive history entry; preserve existing history
(including its pre-existing1.0.14 ordering). No independent guide version.

## Local semantics and proof

One batch artifact supplies six named rows with five distinct results: available
source fidelity; technical correctness; scope; internal/cross-card consistency;
actual edge/CQ coverage. Missing immutable captures remain P10-11-blocked without
blocking independent technical fixes. Confidence stays historical extraction data.

Give each27 header occurrence a card/field/index/target identity and warranted
premise/type/direction: prerequisite target→card, related/contrast symmetric with
actual basis. Group shared warrants only with exact member identities. Separately
reconcile each25 predecessor body occurrence to final wording/disposition and any
added occurrences; counts/equality/path resolution do not prove semantic support.
Inspect affected metadata, errors and repeated claims alongside these meanings.

For all9 CQ occurrences, preserve question text and attempt answers to all four
actual questions by component, mapped support and real gaps. CQ5 asks anatomy,
not whether kerning/ligatures exist; CQ11 asks a spacing system/padding constraint,
not simply tracking. Do not invent those missing answers or silently drop their
memberships. CQ1/CQ12 have existing Slice20 conceptual support; state this cohort's
specific contribution and limits without falsely requiring a target specimen for
a general explanation. Whole-domain question/edge composition stays later-owned.

Use direct source/arithmetic/specification checks for these discriminating cases;
no new maintained validator/fixture suite or empirical research:
- A font lacking a requested feature: declaration is not evidence of a changed
  glyph. A default-active common feature refutes “must always explicitly enable.”
- Compare kerning versus added tracking; distinguish proportionally spaced text,
  no kerning data and fixed-width digits. Do not promise normal means equal gaps.
- Nonzero tracking with optional Latin ligatures, an explicit low-level override,
  and required-script shaping: preserve each condition/precedence and modality;
  don't derive one global ligature-off rule. Cursive text is not spaced by blindly
  separating codepoints. These are specified cases, not browser observations.
- Source range:0.05em at12pt is0.6pt;0.12em is1.44pt (source's1.4pt is rounded),
  and at20px they give1px/2.4px. Correct arithmetic does not warrant a mandatory
  range; retain source's smaller/larger lowercase exceptions and optical judgment.
- Figure form and advance width are separate; equal digit advances alone cannot
  decimal-align different-length values. Preserve the concrete source examples.
- Butterick's optical comparison versus Adobe's conditional use cases warrants
  qualification, not replacing an anti-optical universal with pro-optical claims.

## Verification and return

Read all six final cards and complete changed guide after editing. Check233
identities against accepted index, raw+typed headers under exactly seven scalar
substitutions,227 unchanged whole cards, six frozen heading/citation sequences,
all161 sources, other five guides and guide-section boundary. Record actual
path/parent/commit scopes and LF/EOF/local links/fragments/whitespace checks.
Native entrypoint `make help`, then sequential `make check-skills`,
`make check-skill-versions`, `make check-package-paths`, separate fresh `make design`;
no concurrent shared-build race. Compare all8 archive Markdown members with
committed source bytes and report ZIP hash. Check whole source/package version
contract; retain warnings and failed/recovered/unrun attempts accurately.

Commit SOURCE allowlisted paths and PLANNING's three allowed return paths
separately with explicit path lists (`git commit --only` for tracked files;
add only named new outputs). Both commit messages need separate trailers:
`Co-authored-by: Codex <noreply@openai.com>` and
`Co-authored-by: Billo AI <ai-engineering@billo.systems>`.

Return exact commits/pins/scopes, four-row proposed outcomes with gaps, sole
artifact inventory and bubble-up against the assigned useful capability. Leave
all ledger statuses/criteria unchanged for CDC. Keep detailed intake/results/
checks in the one batch rather than duplicating them in the closing report.
No browser/AT/font-feature/hosted rendering success, full endpoint/corpus/fidelity
acceptance, release, push/publication, slice close or successor is authorized.
A required input conflict blocks only dependent work; name it and its owner.
