# CC Iteration01 — finish Slice16 CSS colour corrections

Execute this refinement and return it to CDC Sofie through the Operator. This is
Project10 / Arc02 / Slice16, Two-Contributor Workflow, Expedited Mode. No push,
self-acceptance, next-slice opening, source acquisition or new inquiry.

SOURCE=/Users/oubiwann/lab/billosys/ai-engineering, main baseline
`8f622e4426484eed56c918f69206c429129f9e32`.
PLANNING=SOURCE/.worktrees/planning. Planning predecessor/initial CC return:
`e04d8846d36d194c4766190e28a1d7d2c58d0c86`; issuing commit is the commit adding
this prompt. S=project10-design-foundations/arc02-theory-and-evidence/slice16-css-colour-mechanics.
Current prompt: S/cc-prompt-iteration01.md; preceding prompt S/cc-prompt.md remains
preserved. Confirm the assignment history and both worktrees before edits. Do not
reset/rebase or overwrite drift/unrelated work, including knowledge/lfe/.

## Corrected oracle and retained result

**You were right:** opaque red→blue, componentwise in sRGB at t=0.5, gives
`(0.5,0,0.5,1)`. CDC's `(0.5,0,0,1)` was an arithmetic typo. E00 in the
[CDC review](cdc-verification.md#e00--cdc-assignment-erratum-resolved) resolves it;
no additional Operator approval is pending for that computation. The slice plan
now states the correct value. Do not adopt the false value or rewrite the initial
prompt. This changes no acceptance criterion or interpolation method.

S16-03 is CDC-done at8f622e44/e04d8846. S16-01/02/04 remain open. Native integration,
8/8 package bytes and bounded arithmetic independently pass at that source;
semantic consistency and the complete return do not. Preserve passing changes
and evidence, checking applicability to your actual delta. No wholesale reset,
new extraction, old normalization/Unicode replay or reusable validator is needed.

## Implementation spine — address F01–F03 together

1. **F01: follow each corrected claim through its complete card.** The CDC review's
   F01 table names the surviving contradictions. Correct the corresponding Key
   Properties, Prerequisites, Construction/Recognition, Examples, Relationships,
   Common Errors/Confusions and Verification Notes wherever affected. Do not patch
   just Quick/Core Definition again. Keep useful teaching and all existing section
   headings, source-specific examples and exact Source References. Correct a
   purported quote by marking the corrected example/paraphrase, not silently
   attributing different source bytes. No broader historical research is assigned.
2. **F02: deliver the guide's worked pair procedure.** Under Choose candidate
   values in colour.md, add a short opaque rendered-sRGB example with the decoding,
   luminance and contrast method below, criterion/large-text/exception context and
   primary links. Keep supplied identity, optional token architecture, state and
   actual-rendering guidance. These colours are illustrative, never default tokens.
3. **F03: attach semantic evidence to its actual subjects.** Repair the existing
   twelve-row five-outcome table (Scope means claim generality/attribution/inference,
   not metadata mutation). Map changed/unsupported claims to precise prepared/spec
   passages or explicitly derived premises. For the53 header edges and all body
   relationship statements, record recoverable occurrence membership, endpoint
   revisions, direction/meaning, support/rationale and outcome. For the10 header CQ
   occurrences/five texts and any body questions, locate actual answering components
   in the revised cards/sources and give a bounded supported answer/remaining gap.
   Group entries only when explicit coverage of each member remains clear. No file
   per edge, new schema, copied corpus or hidden blanket 'all reconciled' assertion.
4. Re-read all twelve corrected cards against those statement families, inspect the
   relevant endpoint constructs and revised guide, run affected checks and return
   the three existing evidence files. Correct the additive/mix edge counts and
   Compositing draft status in the same evidence update. Preserve the prior return
   by pin and a short supersession note; retain its hash table as historical and
   append only the new delta. No receipt-only follow-up commit is required.

The complete defect list and evidence are [CDC F01–F03](cdc-verification.md#f01--repeated-card-assertions-still-contradict-the-repairs).
Use that table with the existing initial slice recipe; the following shapes
resolve the consequential implementation/proof choices:

- Current numeric/percentage alpha (including integer1 and clamped255), alias
  functions and modern hue-angle syntax must agree across definitions, recognition
  and errors. Show examples such as `rgb(255 0 0 / 50%)`, `rgba(255,0,0,1)` and
  `hsl(0.5turn 100% 50% / 50%)`; do not claim eight-bit storage follows from syntax.
  Legacy examples remain useful, labelled as legacy where their shape is narrow.
- In the explicitly chosen sRGB example, use opaque `rgb(255 0 0)` and
  `rgb(0 0 255)` to avoid keyword ambiguity. The red/blue midpoint is
  `(0.5,0,0.5,1)`; transparent-white→opaque-black gives `(0,0,0,0.5)` after undoing
  premultiplication. If retaining the green example, name `rgb(0 255 0)`/`lime`;
  CSS `green` is `rgb(0 128 0)`. Separate CSS length/percentage/angle stop syntax
  from normalized SVG offsets; CSS stops are not generally restricted to0–100%.
- For color-burn, state variables Cb (backdrop), Cs (source), both in[0,1]:
  if Cb==1 return1; otherwise if Cs==0 return0; otherwise
  `1 - min(1,(1-Cb)/Cs)`. Keep the branch order. This is a separable blend function,
  not the entire alpha-compositing algorithm; other modes can be non-separable.
- Frozen rigorous mapping labels on gradient/matrix describe bounded exact
  operations: component lerp with stated hue/alpha rules, and homogeneous matrix
  multiplication before clipping. Make the body explain that scope consistently.
  Custom-property dependency injection stays a qualified structural analogy.
  SVG filters use the selected filter space (default linearRGB); CSS filter
  functions operate in sRGB. Similar function names alone do not prove equivalent
  rendering. Do not invent invalid-matrix fallback behavior when the cited rule
  does not establish it.
- Keep the custom-property alias-resolution witness already correct. Give a usable
  optional scoped-theme recipe (direct roles or scoped aliases) that observes it;
  do not reinstate mandatory layers. Correct the missing dot in the copied
  `.div-external` currentColor selector. Frozen extraction-confidence metadata is
  historical; a revised body rationale is not a new silently assigned confidence
  or independent verification. Mark old verification remarks as historical or
  replace them with accurately scoped current notes.
- For an opaque rendered sRGB pair, normalize8-bit components by255, decode each
  u as `u/12.92` when u<=0.04045, else `((u+0.055)/1.055)^2.4`; calculate
  `L=0.2126R+0.7152G+0.0722B`; ratio=`(Lhigh+0.05)/(Llow+0.05)`.
  Black/white21:1; #777/#fff≈4.4780894536:1 fails normal-text AA without rounding
  up. Retain #ffff00/#0000ff≈8.0016366612:1 as the equal-HSL-L contrast example.
  A 1:1 ratio is equal relative luminance, not necessarily identical colours.
  State formula scope and compositing/rendered-context limits; no browser or
  whole-page conformance is inferred from these calculations.

These are targeted repairs within the approved cohort. Wording/layout of the
existing bodies and compact evidence tables is local discretion. If a new issue
requires an unlisted file or new contract/research, report the exact extension
needed and continue independent allowed fixes; do not silently expand scope.

## Required reading and intake

Use SOURCE8f622e44 and the issuing planning commit. Before dependent edits,
load complete required sections, recover truncation and record a concise actual
readback/extents in S/artifacts/batch-record.md. Cover the whole-card consistency
failure and why available local semantics must be checked now. Prior receipts
are identity/context, not a substitute for text missing from this executing context.
Proceed after coherent intake; this is an implementation assignment.

| Kind / order | Material and complete required extent |
|---|---|
| Required-section, project then arc | Project10 project-plan.md: Purpose and authority, Release target, Scope and definition of done including Full-corpus review contract, Evidence and workload economy, Operator deferral, Metadata and rendering addition, Workflow and acceptance; Arc02 arc-plan.md: Accepted inputs and preservation, Complete coverage and source re-entry, Findings and accessibility/typesetting ownership, Workflow and current assignment. Necessary definitions within those sections included. |
| Required-section | Project ledger: all13 criterion rows and Operator source-readiness carryover; Arc02 ledger: all10 criterion rows and Operator execution amendment. Historical roll-up narratives are reference-only. |
| Required-full | SOURCE AGENTS.md; current SOURCE knowledge/collaboration-framework/SKILL.md, knowledge/design/SKILL.md and knowledge/concept-cards/SKILL.md; this iteration, S/slice-plan.md, S/ledger.md, S/cdc-verification.md. |
| Required-section | Initial S/cc-prompt.md: Outcome and implementation spine, Primary technical sections, Exact write/commit scope, Checks and return, with the narrower write/read/check rules in this iteration taking precedence. Earlier parent histories and unrelated closed-slice reports are reference-only. |
| Required-full | The12 primary card bodies/headers at the paths below; current colour guide; S/artifacts/batch-record.md and S/closing-report.md. |
| Required-section | Prepared working-with-colours.md: Color mixing, RGB Values, Hex Values, HSL Values, Color Variables/currentColor, Gradients, Generative Color including Sass/JavaScript examples, Mix Blend Modes, feColorMatrix and Accessibility. Include each complete subsection and required antecedent context; original445-line file is unchanged. Full-source reading remains available if easier. |
| Required-section | concept-cards guides/05-evidence-lifecycle.md: Identify The Subject And Its Evidence through Keep Rich Prose Attached To Its Warrant; guides/06-graph-cq.md: Select Relationship Identity through Rich-Body Relationship And CQ Boundaries. engineering-methods guide07: Required reading and CC intake. work-verification guide05: Evidence During Correction Review. testing guide03: Proportionate Proof and Package And Release Gates. Paths are under SOURCE knowledge/. |
| Required-section | The primary sources in the initial prompt: CSS Color4 §§4.1–4.3,5.1–5.2,7 syntax and13.1/13.4; CSS Images4 §3.5.2; Compositing1 §3.4.2 and10 introduction/multiply/screen/color-burn/non-separable introduction; Filter Effects1 §9.6/§10 and hue-rotate definition; Variables1 computed-value/substitution passages in§§2–3.1; WCAG2.2 SC1.4.1/3/6/11 and glossary contrast ratio/large-scale/relative luminance including notes/exceptions. Complete those selected rules/definitions; record edition/status. Compositing is CRD2024-03-21, not Recommendation. |
| Required-data | Strict parse of all233 accepted Arc01/Slice01 card-source-index.jsonl rows at9cc203380aede19231b7c5119f0b43d9fe3d0e78; compare unique exact-path roster with current SOURCE. Emit primary twelve-member list and all53 header relationship/10 CQ occurrences with source fields/list positions, compare with the existing batch record. Derive body relationship/question occurrence coverage from the full reads. Inspect all results; no sampling or slug-only identity joins. |
| Conditional | Full posts/hsl.md endpoint when a repaired HSL relation/CQ explanation uses it; read before judging that edge. It is read-only. Any other endpoint construct within the primary cohort is already required-full. |

Bind current technical statements to those primary rules. Prepared-source agreement
and historical-capture fidelity stay separate. A page title/link alone is not
support; a role name or pair result is not accessibility conformance. Do not
load new libraries, capture sources, add schema fields or copy method templates.

## Exact mutation and commit scope

SOURCE allowed paths, **body only** for cards; all frontmatter is frozen8f622e44:

```text
knowledge/design/concept-cards/posts/additive-colour-mixing.md
knowledge/design/concept-cards/posts/subtractive-colour-mixing.md
knowledge/design/concept-cards/posts/colour-bit-depth.md
knowledge/design/concept-cards/posts/rgb-colour-model.md
knowledge/design/concept-cards/posts/hex-colour-notation.md
knowledge/design/concept-cards/posts/css-rgba.md
knowledge/design/concept-cards/posts/hsl-css-syntax.md
knowledge/design/concept-cards/posts/css-colour-custom-properties.md
knowledge/design/concept-cards/posts/gradient-colour-interpolation.md
knowledge/design/concept-cards/posts/mix-blend-mode.md
knowledge/design/concept-cards/posts/fecolormatrix.md
knowledge/design/concept-cards/posts/colour-contrast.md
knowledge/design/guides/colour.md
```

Change only needed assertions/procedures/examples/verification scope in the twelve
cards, plus F02 under the guide's Choose candidate values. Preserve complete
literal Source Reference sections and all existing body headings; leave correct
teaching intact. No forced edit where a clause is already sound. No changes to
posts/hsl.md, foundations, design.md, entrypoint/history, sources, helpers,
packaging lists, other221 cards, metadata, exact questions or relation lists.
Keep skill1.0.13 for this unfinished correction; no new release/bump is required.

PLANNING return paths exactly:

```text
project10-design-foundations/arc02-theory-and-evidence/slice16-css-colour-mechanics/artifacts/batch-record.md
project10-design-foundations/arc02-theory-and-evidence/slice16-css-colour-mechanics/ledger.md
project10-design-foundations/arc02-theory-and-evidence/slice16-css-colour-mechanics/closing-report.md
```

Ledger changes: Evidence/Notes only; preserve criteria and statuses (S16-03 done,
others open). Identify this iteration, resolve F01–F03, keep E00's history and
all four proposals explicit. Preserve issued prompts, plan and CDC review. Keep
one supporting batch record; no new file/reporting layer or receipt-only commit.

## Adequate checks and return

- Re-read the full12 revised cards. For each repaired statement family, inspect
  its repetitions in the existing sections; use the concrete F01 contradictions
  as regression checks. Demonstrate correct positive examples and why the actual
  old opposite assertion cannot remain true in that context. Direct review and
  temporary calculations suffice; no secret markers or general mutation suite.
- Reproduce changed numeric examples and formula/branch boundaries above. Retain
  CDC's unchanged arithmetic by named input/result and applicability; do not
  re-run every old proof solely for a receipt. No runtime claims from spec reasoning.
- Check all233 paths; compare this delta with8f622e44: exact allowed source paths,
  all card-header and Source Reference bytes, unchanged other221 cards and sources,
  unchanged named protected guides/entrypoint/history, LF/EOF, local links/fragments
  and both Git whitespace/scope/trailer checks. S16-03's earlier65ed→8f preservation
  can be retained after this delta check; no old transformation replay.
- The changed colour guide invalidates its package-byte proof. Run make help,
  make check-skill-versions, make check-package-paths and separate fresh make design
  from SOURCE; compare all eight Markdown members with committed source and report
  actual warnings/errors/archive hash. CDC's check-skills evidence can be retained
  if its description/metadata inputs are confirmed unchanged; run it if they drift.
  Mandatory changed-input gates are not waived. The ZIP excludes cards.
- Give a complete current four-row report, supporting-artifact inventory and brief
  bubble-up/scope-as-delivered accounting. Preserve the initial return by pin/short
  historical note. Keep missing originals, actual browser/AT/hosted and broader
  full-corpus/release results at their explicit owners; no invented acceptance.

Commit only actual allowed changed source paths on main and the three planning
return paths separately, using scoped staging/git commit --only. Every commit:

```text
Co-authored-by: Codex <noreply@openai.com>

Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Return final source/planning hashes, exact changed paths, findings/row proposals,
actual checks and limits. Do not create a child receipt just to record the commit's
own hash in its body. Do not push. CDC independently reviews before any closure
or advancement.
