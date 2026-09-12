# Teaching-Profile Comparison

## Question

Does the post-`1.8.1` teaching-profile iteration move the CompCogNeuro subset
closer to the best Complete Musician cards while preserving v4 evidence
discipline?

## Compared Sets

| Set | Location | Count | Total Lines | Average |
| --- | --- | ---: | ---: | ---: |
| Arc09 rich rerun | `workbench/compcogneuro-rich-rerun-2026-09-12/candidate-cards/` | 10 | 1,382 | 138 |
| Teaching-profile rerun | `workbench/compcogneuro-teaching-rerun-2026-09-12/candidate-cards/` | 10 | 1,216 | 122 |
| Complete Musician corpus | `/Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/` | 390 | 28,374 | 73 |

Complete Musician remains shorter on average. The teaching-profile cards still
carry v4 metadata, support-map and lifecycle sections, so exact length parity is
not expected. The better comparison is whether the main teaching sections read
more like concept cards and less like review packets.

## Observations

- The new cards keep all fourteen rich sections across the ten-card subset.
- The teaching sections are more direct: quick definition, core definition,
  properties, recognition, examples and common confusions now carry less repeated
  caveat text.
- Review caveats are mostly consolidated into source/support, provenance,
  extraction notes, lifecycle and handoff sections.
- Relationship/CQ material is shorter and more navigational.
- Source caveats are still present: figures, bibliography, cited studies,
  semantic verification, operator acceptance, memory admission and runtime work
  remain explicitly unclaimed.

## Representative Improvement

`cc-pattern-separation.md` now reads more like a usable concept card:

- definition: sparse, low-overlap encoding reduces interference;
- properties: sparse activity, low overlap, interference reduction, completion
  tradeoff;
- example: the source's low-activation versus high-activation probability
  comparison;
- common confusions: sparse does not mean weak, separation is not all of recall,
  cited figures are not independently reviewed.

The prior rich version contained the same source discipline, but the new version
keeps the concept in the foreground.

## Residual Gap

The new cards are still somewhat heavier than the best Complete Musician cards.
That heaviness now comes mainly from the v4 control layer rather than bloated
teaching prose. If the operator wants cards even closer to Complete Musician,
the next iteration should consider a two-surface output:

- a compact concept card as the primary artifact;
- sibling claim/support/lifecycle records or appendices for detailed review.

## Recommendation

Review three representative teaching-profile cards before approving full-book
work:

1. `candidate-cards/cc-complementary-learning-systems.md`
2. `candidate-cards/cc-pattern-separation.md`
3. `candidate-cards/cc-memory-consolidation.md`

If those feel good enough, plan the full-book extraction with the `1.8.1`
teaching profile. If they still feel too heavy, iterate once more toward a
two-surface card-plus-record packet.

