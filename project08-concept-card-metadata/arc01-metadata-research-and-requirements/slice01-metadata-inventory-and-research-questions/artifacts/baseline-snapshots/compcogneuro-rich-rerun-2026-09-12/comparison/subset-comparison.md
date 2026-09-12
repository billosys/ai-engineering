# CompCogNeuro Subset Comparison

## Executive Verdict

The post-Arc09 rich-profile rerun is better than the Arc07 baseline for this
same subset, with one important caveat: the improvement is in card usefulness,
review readiness, and relationship/CQ scaffolding, not in independent semantic
verification. Source discipline did not regress in the inspected cards.

Recommendation: proceed to operator review of this subset. If the operator
agrees these cards are qualitatively good enough, open a new scoped full-book
effort. If the operator finds the cards still weaker than the older rich-card
standard, do another skill iteration before any full-book run.

## Compared Sets

| Condition | Location | Count | Source |
| --- | --- | ---: | --- |
| Arc07 baseline | `.worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/` | 10 cards | `CompCogNeuro/book` commit `e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d` |
| Rich-profile rerun | `workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/` | 10 cards | same commit and subset |

The source subset is the same: Chapter 1 lines 31-60 and Chapter 7 lines
5-166, excluding the Chapter 7 appendix, full bibliography resolution, and
full figure audit.

## Structural Comparison

| Measure | Arc07 baseline | Rich-profile rerun | Interpretation |
| --- | --- | --- | --- |
| Card count | 10 | 10 | Comparable. |
| Total card body size | 493 lines | 1,382 lines | Rerun has substantially more review material. |
| Required rich sections | Absent or partial. Slice02 cards have six body sections; Slice04 cards have three. | Present in all ten cards. | Clear improvement. |
| Claim/source support discipline | Strong for compact candidates; Slice02 has separate support records, Slice04 inline support tables. | Strong enough for candidate stage; support maps remain locator-bound and caveated. | No observed regression. |
| Lifecycle boundaries | Explicit. | Explicit. | Stable. |
| Relationship/CQ affordances | Mostly absent or deferred. | Present in every card as candidate navigation/CQ material. | Clear improvement, still unverified. |

## Rubric Scores

Scale: 0 absent/regressed, 1 vague or weak, 2 useful with limits, 3 strong and
review-ready.

| Measure | Arc07 baseline | Rich-profile rerun | Evidence |
| --- | ---: | ---: | --- |
| Source fidelity | 3 | 3 | Rerun preserves qualifications such as consolidation caveats, figure/citation limits, and no operator acceptance. |
| Rich profile completeness | 1 | 3 | Rerun includes concept boundary, definitions, prerequisites, recognition, context, examples, errors/confusions, support map, claims, relationships/CQs, provenance, lifecycle, and handoff sections in every card. |
| Evidence discipline | 3 | 3 | Rerun keeps locators, support scope, uninspected citations/figures, and lifecycle boundaries separate. |
| Concept boundary | 2 | 3 | Rerun makes exclusions and adjacent concepts clearer, especially for CLS, recognition, priming, and episodic binding. |
| Examples and confusions | 1 | 3 | Rerun adds source-specific examples and common-error material without generic filler. |
| Relationships and CQs | 1 | 2 | Rerun adds useful candidate relationships/CQs but does not create verified graph edges or answerability results. |
| Review readiness | 2 | 3 | Rerun gives an operator enough local context to accept, revise, split, or reject each card. |

## Card-Level Observations

| Card | Improvement | Residual Risk |
| --- | --- | --- |
| `cc-model-data-constraints` | Adds recognition cues, methodological context, and a useful CQ about trust in models. | May need splitting if "golden middle" modeling strategy becomes its own concept. |
| `cc-emergent-explanation` | Separates reductionism, reconstructionism, and gear analogy limits. | Philosophical background may be less central to the memory-protocol subset. |
| `cc-memory-forms` | Turns a compact taxonomy into a usable navigation card. | Broad top-level card may be too general for final memory admission. |
| `cc-complementary-learning-systems` | Much stronger tradeoff explanation; connects hippocampus, neocortex, consolidation, and pattern separation without overclaiming. | Figures and cited CLS papers remain uninspected. |
| `cc-episodic-binding` | Adds pathway detail, anti-modularization caveat, and useful CQ. | Anatomy figure was not independently audited. |
| `cc-pattern-separation` | Preserves the old source discipline while adding prerequisites, examples, confusions, and tradeoff links. | May need splitting into sparseness, conjunctive representation, and interference in full-book work. |
| `cc-pattern-completion` | Better distinguishes completion from separation and records the completion/separation tradeoff. | Cited model paper and Executive Function cross-reference remain unresolved. |
| `cc-memory-consolidation` | Keeps the crucial "some extent, some situations" caveat prominent while adding examples and semanticization relationship. | Bibliography and cited studies remain unresolved. |
| `cc-recognition-dual-process` | Clarifies familiarity versus recollection and conscious-readout caveat. | Underlying recognition studies and Learning chapter reference remain uninspected. |
| `cc-priming-forms` | Adds behavioral example, duration distinction, and relationship to memory forms and recognition. | The simulation and external priming literature were not inspected. |

## Regression Check

No source-support regression was found in this comparison. The rerun did not:

- turn source-reported claims into world-verified claims;
- remove caveats about uninspected figures, citations, studies, or simulations;
- claim operator acceptance, independent semantic verification, reconciliation,
  preservation, memory admission, runtime ingestion, graph/RAG/MCP delivery, or
  full-book coverage;
- silently widen the source subset.

The main risk is verbosity: the new cards are much longer. In this subset, the
extra material is useful because it is structured and source-tethered. A
full-book run should still control length by enforcing the same section shape
and source-specific content requirements.

## Full-Book Decision Gate

Proceed to full-book planning only if operator review agrees with this
comparison's main judgment: the rerun cards are at least as useful as the older
rich-card standard and better than the Arc07 baseline.

If the operator disagrees, do not process the whole book. Instead, update the
`concept-cards` skill again, likely in these areas:

- better defaults for how much explanatory prose belongs in each rich section;
- clearer guidance for when to split broad cards into multiple concepts;
- stronger examples of common errors/common confusions from real cards;
- a review rubric for "good enough for full-corpus extraction";
- optional prompts for producing consistent relationship/CQ candidates without
  implying graph verification.

## Recommended Next Step

Open a new full-book planning effort only after a quick operator review of
three representative rerun cards:

1. `cc-complementary-learning-systems.md`
2. `cc-pattern-separation.md`
3. `cc-memory-consolidation.md`

Those three cards stress the main risks: broad mechanism boundaries, source
qualification, evidence caveats, and relationship usefulness.
