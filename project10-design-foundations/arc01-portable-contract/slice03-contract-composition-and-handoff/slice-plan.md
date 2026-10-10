---
slice: slice03-contract-composition-and-handoff
status: open
depends-on: [slice01-scope-and-portability-contract, slice02-source-and-review-readiness with Operator-deferred S02-08]
---

# Slice03 — Contract Composition and Arc02 Handoff

## Outcome and authority

Compose the portable behavioral contract and five-dimension review procedure
into a concrete planning handoff, with exact population allocation and explicit
source-readiness carryover. The Operator ordered opening on 2026-10-09 after
explicitly deferring S02-08. This is planning/evidence work, not live-skill
implementation, source acquisition, full semantic review or release acceptance.
[Project authority](../../project-plan.md#operator-deferral--2026-10-09),
[Arc01](../arc-plan.md) and [ledger](ledger.md) govern.

Two contributors: Sofie (CDC) selects design and independently reviews; a separate
CC context executes [cc-prompt.md](cc-prompt.md), relayed by the Operator.
Expedited Mode applies. All nine rows started open; no verification or closing
record was pre-created. Initial review accepted five rows; iteration01 review at `ee7b8757` accepts
S03-06/07. Seven rows done; S03-01/09 remain open for iteration02/F05; see
cdc-verification.md. CC commits only its eight listed outputs and proposes
completion; CDC acceptance and formal Arc01 composition remain separate.

## Inputs and preservation

SOURCE `/Users/oubiwann/lab/billosys/ai-engineering`, main at
`dffa504e851b03b8e4746f1941068e4cc850b612`. PLANNING is `.worktrees/planning`,
branch planning. Predecessor close is
`8e0be8d2f11207ba86d605dbb071f0069aea1922`; accepted local CC packet
`759ce2dd116a4cfe03b72d43fd2791f48486251c`, CDC `88c1298f`. Slice01 CC
`9cc20338`, CDC closure `1944d1ed`; shared Project09 audit `795ac75b`.
Record the actual issuing commit when executing; do not guess this opening's hash.
Unrelated SOURCE `knowledge/lfe/` and PLANNING `project12-chcd-protocol/` are
protected. All predecessor records, prompts and artifacts are immutable inputs.

The source baseline is 402 tracked design files: 233 cards, 161 source files,
eight live files (entrypoint, history, six guides). The 233-card index supplies
literal identity/hash/raw fields; Slice02's map supplies exact raw assertions,
typed navigation and caveats. Its accepted method supplies five independent
review dimensions. Current original readiness remains unmet. Historic readiness
reports still say open/partial at their own handoffs: the explicit Operator
closure overrides sequencing, never their original-fidelity observations.

## CDC-selected design for this assignment

These are resolved **planning choices**, subject to independent composition and
the Operator's higher-scale gate; they are not claims of new scientific support
or installed behavior. CC composes these choices rather than selecting a new
house style. Substantive contrary evidence returns to CDC before changing them.

### Portable behavior and principles

Use Slice01 contract §1–3 behavior and the seven candidate formulations as the
selected planning wording: intentional relationships; perception in context;
roles separated from values; task-serving constraints; contextual expression;
multiple grouping cues; useful invariants tested on instances. Preserve their
full caveats, examples and exceptions; headings alone are insufficient.
Label each substantive proposition as mathematical identity, scoped empirical
claim, contextual heuristic, project convention or analogy/inference. Unchecked
scientific/technical attribution remains pending Arc02 evidence; design-policy
selection is not source verification. The compositional ethos remains positive:
relationships, content-led composition, intrinsic layout, proportion, optical
judgment and expressive coherence.

Keep the short profile before styling in the entrypoint's future workflow:
audience/task/content, supplied identity/assets, platform/input, language/script,
accessibility/user preferences, typography/colour/spacing, modes/density, fixed
choices, unknowns/evidence. Detailed explanations belong in the relevant guides.
This is optional brief prose/table, not a new schema/form or prerequisite for a
small edit. Ask consequential questions; otherwise state reversible assumptions.
No C&B profile, case study, palette/token/font defaults or compatibility bridge.
Independent user choices of brown or Fraunces remain legitimate when appropriate.
Space scales need not mirror type scales; no universal 60ch, ratio, token-layer
count, exclusive colour space, breakpoint ban or perceptual guarantee.

Use Slice02's existing local claim-result shape and ordered procedure by reference,
with exact method revision, actor and target/source/claim identities. Do not
migrate Project08 schemas or create a new lifecycle vocabulary/runtime. Context
and applicable qualifications travel with claims; correctness and source fidelity
are separate; typed edge/CQ support and global consistency are reviewed explicitly.

### One illustrative numerical configuration

Select a diagnostic fluid-type example, **not a default or accessibility promise**:
inline range 20rem–80rem; reference root R=16px (nominal 320px–1280px), with R=20px
also checked; small base 1rem and ratio 6/5; large base 9/8rem and ratio 5/4;
integer steps n=-2..4. No named font, palette, token role assignment or spacing
coupling. Small negative steps are arithmetic probes, not recommendations for
functional text. Actual readable roles/accessibility need later specimen checks.

Let a(n)=(6/5)^n and b(n)=(9/8)*(5/4)^n, in rem. Let w be inline extent in px,
R root px, and t=clamp(0,(w/R-20)/60,1). Size in px is
R*((1-t)*a+t*b). Endpoint interpolation is linear **per step**; intermediate
adjacent ratios are generally unequal. For illustrative CSS:
B=100*(b-a)/60; A=a-(b-a)/3;
`--example-step-n: clamp(a rem, calc(A rem + B vi), b rem)`.
Keep exact rational arithmetic as the numerical oracle; serialize a, b, A and B
as six-decimal CSS values, comparing rounded values within 0.001px over the
stated finite test grid. This is equation checking, not browser execution.

At R=16,w=800: steps 0/1/2 are 17,20.85,25.5825px. Adjacent ratios are
417/340 and 3411/2780, unequal. At R=20,w=800, step0 is 125/6px;
the rem interval has moved to 400–1600px, so keeping the old pixel midpoint
would incorrectly return 21.25px. At R=20,w=1000, step0 is 21.25px.
Check all seven steps at w=160,320,800,1000,1280,1600 for both roots; minimum/
maximum saturation and negative steps are included. Root change does not prove
text enlargement compliance; browser zoom/reflow remains Arc03/05 work.

### Complete population allocation

Write one JSONL planning row per baseline card. Preserve exact path/hash and raw
source/author arrays; copy caveat IDs from the accepted map. Reference that card's
locator row and the accepted five-dimension method at exact planning revisions.
Each row explicitly requires all five dimensions and has an Arc02 input gate
originating at S02-08/P10-11. No ready/verified result is created by allocation.

Use a deterministic provisional grouping: sort the eight pairs lexicographically
by `(tuple(source_raw), tuple(authors_raw))`; within each pair sort full card paths.
Start a new group before adding a card if the current group has six cards or
its pinned card-file bytes plus the next card exceed 60,000. Do not split a card
or mix pairs. Assign C01.. sequentially; author reproduction yields 47 groups,
233 rows, maximum 58,666 card bytes. Recompute, report any drift, never force a
count by dropping inputs. These are planning units, not 47 already authorized
slices. Original/context/evidence lengths are not yet known: CDC must check the
actual source reading and review headroom before issuing each Arc02 slice, split
with traceable membership if needed, and preserve the 233-card denominator.

Allocate every byte/line of all eight live files to L01..L08 (sorted full paths,
one whole-file group per file), using baseline hash and inclusive 1..EOF lines.
History has maintenance/provenance review, not an invented teaching body; any
substantive assertions still receive the appropriate review. For guides and
entrypoint, later Arc02 work must read the whole assigned file and enumerate all
substantive/repeated claims. In this slice, heading and fixed-family searches
locate **candidate** repeat occurrences; whole-file allocation preserves claims
outside those searches. Do not claim the search is a complete claim inventory.
Final cross-group card/guide/edge/CQ reconciliation consumes all C/L results and
corrections, including revision-dependent support; a source-group label supplies
neither semantic order nor edge/CQ warrant. Preserve all 16 DES owners and cross-
arc dependencies from the accepted contract/method; no finding is closed here.

### Deferred input and dependent work

Arc02 CDC + Operator own P10-11. Carry the exact input-action categories and every
affected card: 112 Arnheim, 19 Cleland, 19 Tschichold, 37 Butterick and 46 posts
(across four primary article pairs). Originals/page bases, captures/lineage/fidelity
and relevant media/conversion/dependencies remain unmet. External quoted/further-
reading/data sources keep separate roles and need evidence if relied upon.

Order the Arc02 handoff: explicit readiness/re-entry assignment for supplied or
authorized inputs; scoped theory/arithmetic investigation that may proceed on
its own evidence; complete source-based card groups once their required inputs
are adequate; whole live-file claim occurrence review; global relationship/CQ/
consistency and corrected-revision review; composition. No unready group can
acquire source-fidelity acceptance. Planning and source-independent checks may
continue, with blocked dimensions visible. No source-faithfulness/full-corpus/
release completion before independent re-entry satisfies the retained requirement.
Each actual source/preparation/mutation assignment needs fresh pins and exact
allowlists. Do not open Arc02 or claim Arc01 closure inside this CC assignment.

## Deliverables and allowed writes

Six supporting outputs under this slice's artifacts/:
composed-contract.md, example-configuration.md, corpus-allocation.jsonl,
guide-and-finding-allocation.md, arc02-handoff.md and execution-notes.md.
CC also writes closing-report.md and updates ledger.md evidence/notes only,
leaving statuses/criteria open for CDC. Exactly eight allowed paths; slice-plan.md,
cc-prompt.md, all parents/predecessors and SOURCE are protected. No acquisition,
conversion, private scan, schema migration, live card/guide repair, package build
or new maintained validator. Small inline checks/receipts belong in execution
notes; preserve literal fields and historical records.

## Verification and exit

The prompt provides construction shapes and contrasting controls. Reconcile the
full 233-path/hash/pair/caveat set and independently derived groups, all eight
whole live files and exact 16 DES rows. Verify explicit source gates and per-
use result limits; walk generic, existing identity, independently chosen brown,
dense/breakpoint/optical and missing-source cases against the composed contract.
Reproduce finite numerical/CSS-expression cases, raw escaping and local links;
check protected bytes, exact writes, final newlines and git diff --check. Structural
and arithmetic results are bounded; five-dimension execution, browser/AT, source
fidelity and package gates remain unrun here. All nine rows require independent
CDC review before closure. Arc01 composition remains a later attributed gate.

## Assignment history

Current assignment: [cc-prompt-iteration02.md](cc-prompt-iteration02.md), issued
2026-10-09 for F05 / S03-01/09. Receipt-only correction; no source authority
or slice closure assigned. Previous execution was iteration01, now reviewed.

- Initial [cc-prompt.md](cc-prompt.md), issued 2026-10-09 at `c0332475` after
  predecessor closure `8e0be8d2`: CC returned `c58c89e`; CDC independently accepted
  S03-02/03/04/05/08 and found intake/verifier/handoff evidence defects. Disposition:
  returned/reviewed, superseded for current execution; immutable initial preserved.
- Iteration01, issued 2026-10-09, predecessor initial prompt/candidate `c58c89e`:
  returned at `ee7b8757` and independently reviewed; superseded for execution.
  Restored source-action header, aligned dependent-scope
  re-entry, consume printed artifact in the verifier and recover incomplete reads.
  Four exact output files; S03-06/07 newly accepted, earlier five retained.
  Fresh intake introduced F05 counts; S03-01/09 still open.
- Iteration02 [cc-prompt-iteration02.md](cc-prompt-iteration02.md), issued2026-10-09,
  predecessor iteration01/ee7b8757: active, not yet executed; three receipt/return
  outputs. Second assigned correction pass; substantive artifacts unchanged.

## Author readiness — 2026-10-09

CDC inspected the actual project/arc/closed-child contracts, complete Slice01
portable contract (recovering the truncated eight-file map), accepted Slice02
method/input actions, per-identity/current readiness sections, raw index schema,
all-card size/pair projections and full live entrypoint. Source witnesses:
layout.md 127–196 (modular scale/Utopia), design.md 93–173 (principles I–III),
type.md 133–151 and 451–499 (contradictory ratio/harmony claims), HSL frontmatter/
reference and Cleland hue-circle frontmatter distinguish identity/role/page bases.
These are scoped witnesses, not full guide or card semantic review. Source/installed
method guidance informed exact locator/use and recoverable-result boundaries;
concept-cards graph/CQ guidance informed the required final global pass.

Actual group arithmetic reproduces 47 groups with all 233 identities; exact
rational example checking gives the stated midpoint/root-change contrary values.
All 84 finite-grid cases pass the rounded-expression comparison; maximum observed
error is 0.000012px against the 0.001px bound. Seven planning files pass local
link/fragment and EOF checks; nine open rows and eight exact CC outputs reconcile.
These are author arithmetic/packet checks, not executed CC work or browser tests.
The selected policy uses accepted candidate wording with its caveats; profile and
example decisions are resolved here, while scientific support and original
readiness remain evidence-dependent. Current guides are inspected as flawed inputs,
not treated as authority over the portable correction. No current web API/source
system version or browser support claim is adopted from memory.

This packet requires approximately 100,000 characters of prose/witnesses plus
lossless structured-data projections and queries, not the 2,015,516-byte full card
corpus or full prepared books. Whole-guide claim enumeration remains explicitly
allocated to Arc02. It fits one planning context with recovery headroom; actual
semantic groups need fresh sizing. Initial large source/contract output was
truncated and relevant extents recovered in bounded reads. A guessed separate
source-change-map.md and hue-circle.md did not exist; actual map is contract §4
and witness is munsell-hue-circle.md. One source read used the planning cwd and
failed; it was rerun from SOURCE. None is counted as a successful original read.
No consequential choice, source acquisition or runtime design is left to CC.

## Version History

- 1.2 (2026-10-09): Slice03 iteration01 `ee7b8757` independently accepted for
  handoff rows S03-06/07; seven done/two open. Issued receipt-only iteration02
  for F05 inaccurate fresh counts; substantive design/source/arc gates unchanged.

- 1.1 (2026-10-09): CDC reviewed initial Slice03 `c58c89e`; independently accepted
  five rows and issued iteration01 for four open rows/F01–04. Planning scope,
  example/allocation, original-readiness and independent arc gates unchanged.

- 1.0 (2026-10-09): Operator opened Slice03 after deferring S02-08; CDC selected
  portable planning wording/profile/example and complete gated allocation method.
