# Author Reconnaissance

Date: 2026-10-09. CDC author: Sofie, current planning context.
Source: `dffa504e851b03b8e4746f1941068e4cc850b612`.
Planning before opening: `290b21ffa084ed5b892e5b5c5dd295622b77c8bb`.
These are assignment-preparation observations, not CC delivery or independent
acceptance of the earlier audit.

## Direct observations

| Surface | Observed state | Consequence |
|---|---|---|
| `knowledge/design/SKILL.md` | Full entrypoint read; `metadata.version` is `1.0.0`; description and normative palette/type/workflow rules prescribe C&B | Map requirements to portable method/project input; no source edit in Slice01 |
| `knowledge/design/guides/design.md`, opening through Principle II | Generality is asserted despite project origin; universal ratio/token/perceptual claims appear explicitly | Proposed replacement wording must distinguish methods, empirical claims and analogy |
| `guides/colour.md` and `guides/type.md` headings | Brand Brown, Three Sites, Three Voices and per-site tuning organize the live guides | Renaming brands alone cannot produce a transferable method |
| `Makefile:245–263`, design target at 323–324 | Package selects entrypoint, history and guides; does not select cards/sources | Corpus scope is larger than installable payload; do not conflate them |
| `knowledge/design/sources/md/` | Existing source home; no `sources-md/` directory | No directory migration is needed for this corpus |
| Source Git status | Only untracked `knowledge/lfe/` observed | Excluded; no clean-all/reset/stage-all operation |

Filesystem enumeration found 402 design files: 233 cards, 161 source files
(160 Markdown plus one conversion report), and eight live files (entrypoint,
history, six guides). This is a baseline expectation to remeasure, not a semantic
review claim.

| Card collection | Count |
|---|---:|
| art-and-visual-perception | 112 |
| munsell-colour-system | 19 |
| posts | 46 |
| practical-typography | 37 |
| the-new-typography | 19 |

Across every card's frontmatter, the literal `source` values identify eight
titles: Arnheim 112, Cleland/Munsell 19, Butterick 37, Tschichold 19; and within
`posts`, Working With Colors Guide 12, More Meaningful Typography 10,
A Perceptual Color Space for Image Processing 13, Okhsv and Okhsl 11.
All cards contain the inspected `source`, `source_slug`, `authors`, `chapter`,
`pdf_page` and `section` keys. Some values are explicit nulls; presence does not
establish source or locator validity. `source_slug: posts` is a collection name,
not a unique source identity. Preserve literal Unicode escapes in this inventory;
their correction belongs to an authorized source-edit slice.

Source holdings observed: `sources/md/practical-typography/` contains 156 Markdown
pages plus a conversion report; `sources/md/posts/` contains four articles. The
design source tree contains no corresponding Arnheim, Cleland or Tschichold
originals. This does not establish that the Operator lacks them elsewhere.
Slice01 searches the designated tree, names the gap and requests the appropriate
later acquisition action; it does not scan private storage or invent locations.

## Atomic witness and interpretation boundary

`knowledge/design/concept-cards/munsell-colour-system/munsell-hue-circle.md`
has SHA-256 `6893b56903b9b662a5b29c7abff176be6050159844ea6be166a4ae896ab639fa`.
Its frontmatter names Cleland's source, chapter `I. Hue` and `pdf_page: 4`;
the body contains a `Source Reference` section and cross-domain algebra claims.
This witnesses the card's membership and its *asserted* provenance. It does not
witness that Cleland supports every assertion or that page 4 has a verified
physical/printed-page interpretation. The prompt's index must preserve that
distinction. The full card was inspected in this conversation during scope
clarification; it is not independently verified here.

The local Brown article at
`knowledge/design/sources/md/posts/more-meaningful-typography.md:266` explicitly
describes optical adjustment outside its scale. That passage supports retaining
room for judgment when correcting the skill; it does not validate every card
derived from the article. The complete post and all other original sources have
not been reread for this assignment preparation.

## Applied method and checks

- Project-management guides 01–03/06: use the approved planning layout and a
  complete slice open set; detail later slices only when ready.
- Engineering-methods prompt-authoring: exact populations/representations and
  unresolved-result policy for evidence work, with no invented source conclusions.
- Concept-cards, `Perform Semantic Verification` and `Prevent False Upgrades`:
  preserve the difference between source presence, source support, correctness
  and independent acceptance; full semantic review is still mandatory later.
- Document-extraction `Homes And Identity`, `Locator Semantics`, and `Readiness
  By Intended Use`: use `sources/md/`, scope locators and report availability gaps.
- Testing `Proportionate Proof`: use direct enumeration, hashes, comparisons and
  scenario inspection. Do not commission a reusable validator for this packet.

Commands: source/planning Git status and revisions; filesystem enumeration;
literal frontmatter aggregation; focused source reads; `make help` (exit 0).
No new package build, browser test, source acquisition or all-card semantic
review was run for this opening. The earlier audit's build is historical
evidence, not a fresh validation result for Slice01.

Opening self-checks also compared all 402 current tracked design files byte for
byte with the pinned Git blobs. All matched. The eight projected scalar keys
occurred exactly once in each card, with no detected block-style multiline value;
each of the 233 cards had exactly one `# Source Reference` heading. These checks
support the proposed inventory procedure, not source fidelity or semantic truth.
The eight Project10 Markdown files passed trailing-whitespace/newline checks;
all 13 local Markdown links resolved. Arc/slice open-set composition was checked,
with no CC output or close-set record pre-created.
