# Visual Design Concept Card Extraction Prompt

Version: 3

**Copy this prompt and fill in the bracketed fields for each new source.**

**Changelog from v2:**

- Typed relationship semantics clarified: `prerequisites` vs `extends` vs `related` vs `contrasts_with` with examples (Section 9.2, item 10)
- Added guidance for prescription-heavy sources (Section 9.2, item 11)
- Tier assignment explicitly documented as absolute, not source-relative (Section 9.2, item 12)
- Relationship field comments added to Combined Concept Card Template
- CQ phrasing consistency validation added (Section 10.2.1)
- New CQ 56 added: typographic correctness/composition
- Practical Typography added to Section 6.2 source-specific notes

**Changelog from v1:**

- Output directory changed to per-source (`concept-cards/[source-slug]/`) for map-reduce harmonisation
- Added source assessment step (Phase 0.5) before analysis
- Added small-source protocol (scaling agent count to source size)
- Subagent architecture changed: agents return card content as text; coordinator writes files
- Added OCR quality assessment to source assessment
- Slug naming conventions made explicit
- Cross-Domain Connections body section template tightened
- Two-pass extraction within agents (foundational first)

---

## Source to Process

- **Source title**: [TITLE]
- **Authors**: [AUTHORS]
- **Source slug**: [source-slug]
- **Source location**: `sources-md/[source-slug]/`
- **Output location**: `concept-cards/[source-slug]/`  ← NOTE: per-source directory, NOT visual-design/
- **Extraction wave**: [1/2/3/4]

### What This Source Covers

[2-4 sentences describing what this source contributes and what categories/tiers to expect. Copy from 0009 if listed, or write your own after the source assessment in Phase 0.5.]

---

## Phase 0.5: Source Assessment

**Before reading any methodology files**, spend 10-15 minutes assessing the source material itself.

### Step 0.5.1: Structural Scan

Read through `sources-md/[source-slug]/` and document:

1. **Total size**: Approximate page count, number of chapters/sections
2. **Prose style**: Does the source use formal definitions? Section headings? Bullet lists? Or is it discursive/narrative prose requiring synthesis?
3. **Structural features**: Are concepts introduced with clear boundaries, or embedded in flowing text?
4. **Illustration/figure dependency**: Does the source rely heavily on visual examples that may not have survived PDF conversion?

### Step 0.5.2: OCR Quality Assessment

Scan for common conversion artifacts:

```bash
# Check for repeated text blocks (likely OCR errors)
for file in sources-md/[source-slug]/*.md; do
  echo "=== $file ==="
  # Find any line that appears 3+ times in close proximity
  awk 'seen[$0]++ == 2 {print NR": "$0}' "$file" | head -5
done

# Check for garbled characters
grep -rn '[^\x00-\x7F]' sources-md/[source-slug]/ | grep -v '—\|–\|"\|"\|'\|'\|é\|ö\|ü\|á\|à\|ñ' | head -20
```

Flag any problematic sections for careful cross-referencing during extraction.

### Step 0.5.3: Size Assessment and Agent Scaling

Estimate the total concept card count, then choose the extraction architecture:

| Estimated Cards | Architecture | Rationale |
|----------------|-------------|-----------|
| Under 25 | **Serial**: Extract from main conversation, no subagents | Parallelisation overhead exceeds benefit |
| 25-50 | **Light parallel**: 2-3 agents | Moderate parallelism |
| 50-100 | **Standard parallel**: 3-4 agents | Good parallelism/overhead balance |
| 100+ | **Full parallel**: 5 agents | The designed-for scale |

### Step 0.5.4: Write Source-Specific Notes

If this source is NOT listed in 0009, write brief extraction notes covering:

- OCR quality issues found (with chapter/page references)
- Prose style and definition extraction difficulty
- Key chapters for extraction (highest concept density)
- Any unusual features (non-standard terminology, heavy cross-referencing, historical context needed)

Save these notes — they become the source-specific guidance for agent instructions.

---

## Phase 1: Understand the Domain Requirements

**Read these files** (in this order):

1. `crates/design/dev/0004-phase-0-section-1-background.md` — Target user profile and project context.
2. `crates/design/dev/0005-phase-0-section-2-domain-taxonomy.md` — The 13 categories across 4 layers. Every card gets exactly one `category`.
3. `crates/design/dev/0006-phase-0-section-3-tier-definitions.md` — Foundational / intermediate / advanced criteria and per-category tier table.
4. `crates/design/dev/0007-phase-0-section-4-competency-questions.md` — The 56 CQs. Every card must list at least one in `answers_questions`. Note high-priority CQs in Section 4.4.

**After reading**: You should know the taxonomy, tier criteria, CQs, and target user. You do not need to hold these files in context for the rest of the process — re-read specific sections as needed.

## Phase 2: Understand the Extraction Methodology

**Read these files:**

1. `crates/design/dev/concept-cards/0002-a-guide-for-parallel-concept-card-extraction-v3.md` — General extraction methodology (Phase 1: analysis & planning, Phase 2: extraction, post-processing).
2. `crates/design/dev/concept-cards/0003-howto-concept-card-extraction-with-claude-code.md` — Card quality guidance: golden rules, field-by-field frontmatter, body section best practices, quality checklist.

## Phase 3: Read Domain-Specific Extraction Instructions

**Read these for extraction-time reference:**

1. `crates/design/dev/0008-phase-0-section-5-notation-conventions.md` — Colour, typography, spacing, responsive, and mathematical notation standards.
2. `crates/design/dev/0012-phase-0-section-9-extraction-specific-instructions.md` — Card template extensions and domain-specific agent instructions.
3. `crates/design/dev/0010-phase-0-section-7-the-rosetta-stone-framework.md` — Cross-domain mapping tables. Check each concept against these during extraction.

**Keep 0010 accessible for lookup during extraction.**

---

## Phase 4: Analyse the Source and Plan Extraction

Apply Phase 1 from the general methodology (0002) to the source material.

### Step 4.1: Analyse the Source

Read through `sources-md/[source-slug]/` and produce:

1. **Source metadata** — title, authors, type, scope
2. **Chapter/section inventory** — all divisions with titles, descriptions, complexity
3. **Concept inventory** — concept list per chapter with estimated card counts
4. **Category assignment** — map concepts to taxonomy categories (from 0005)
5. **Tier assignment** — foundational/intermediate/advanced (from 0006)
6. **Cross-reference mapping** — concepts in multiple chapters, prerequisite chains

### Step 4.2: Map Competency Questions

- Which CQs does this source help answer?
- Which concepts are needed for each CQ?
- Are high-priority CQs (Section 4.4) addressed?
- Coverage gaps? (Expected — no single source covers all 56 CQs.)

### Step 4.3: Plan Agent Assignments

Based on the size assessment from Phase 0.5:

**Serial extraction (under 25 cards):** Skip agent assignment. Proceed directly to Phase 5 and extract all cards from the main conversation in two passes (foundational first, then intermediate/advanced).

**Parallel extraction (25+ cards):** Divide among agents per the scaling table. For each agent:

1. Chapter assignments with titles
2. Category guidance
3. Tier assignments
4. CQs to address
5. Cross-reference alerts
6. Source-specific notes (from Phase 0.5)

**Agent verification checklist:**

- [ ] Every chapter assigned to exactly one agent
- [ ] No gaps in coverage
- [ ] Card count estimates balanced (±20%)
- [ ] Thematic coherence within each agent's scope

---

## Phase 5: Extract

### Subagent Architecture (IMPORTANT)

Due to current permission constraints, subagents **cannot write files directly**. Use this workflow:

1. **Launch agents** with their compiled instructions and the combined template (below)
2. **Agents draft cards as text** in their context windows — complete, template-conformant markdown for each card
3. **Agents return all card content** to the coordinator
4. **Coordinator writes files** to `concept-cards/[source-slug]/` from the main conversation

For serial extraction: simply write cards directly from the main conversation.

### Two-Pass Extraction Order

Whether serial or parallel, extract in dependency order:

**Pass 1 — Foundational cards**: Extract all concepts with tier `foundational` first. These have no prerequisites within the source. Verify each card is complete before proceeding.

**Pass 2 — Intermediate and advanced cards**: Extract remaining concepts. For each card, verify that all slugs listed in `prerequisites` exist from Pass 1 (or are flagged as cross-source references to be resolved during harmonisation).

### Slug Naming Conventions

Apply this test to every concept:

> **Would this concept exist with the same definition outside this particular source/system?**

- **YES → generic slug**: `hue`, `chroma`, `value`, `complementary-colours`, `simultaneous-contrast`
- **NO → source-prefixed slug**: `munsell-hue-circle`, `munsell-notation`, `munsell-colour-solid`, `itten-seven-contrasts`

The boundary case: when a source gives a specific definition to a universal concept (e.g., Munsell's precise 5-principal-hue system for "hue"), use the generic slug (`hue`) but document the source-specific definition in the card body. The harmonisation phase will reconcile multiple sources' definitions of the same generic concept.

### Combined Concept Card Template

```markdown
---
# === CORE IDENTIFICATION ===
concept: [Concept Name - properly capitalised]
slug: [lowercase-hyphenated, following naming conventions above]

# === CLASSIFICATION ===
category: [from 0005 taxonomy - one of: visual-elements, visual-perception, design-principles, colour-theory, typography, layout-composition, interaction-design, motion-design, information-architecture, data-visualisation, imagery, design-systems, accessibility, visual-identity]
subcategory: [optional finer classification]
tier: [foundational/intermediate/advanced - per 0006 criteria]
layer: [0-perception/1-principles/2-domain/3-implementation]

# === PROVENANCE ===
source: "[Source Title]"
source_slug: [source-slug]
authors: "[Authors]"
chapter: "[Chapter Title]"
chapter_number: [number]
pdf_page: [page number or null]
section: [section heading or null]

# === CONFIDENCE ===
extraction_confidence: [high/medium/low]

# === VARIANTS ===
aliases:
  - [alternative names, abbreviations, notational forms]

# === TYPED RELATIONSHIPS ===
prerequisites:       # B requires understanding A — "you need A first"
  - [concept-slug]
extends:             # B is a specialisation of A — "B is a kind of A"
  - [concept-slug]
related:             # A and B inform each other — lateral, no dependency
  - [concept-slug]
contrasts_with:      # A and B are easily confused or represent opposing approaches
  - [concept-slug]

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "[CQ from 0007 that this card helps answer]"

# === VISUAL DESIGN EXTENSIONS (optional) ===
rosetta_stone:
  - domain: [engineering/music/mathematics/art]
    concept: "[concept name in source domain]"
    rating: [rigorous/structural/loose]
    note: "[brief description]"

css_implementation:
  - property: "[CSS property or technique]"
    example: "property: value;"
    support: [baseline/partial/experimental]
---

# Quick Definition

[1-2 sentences maximum. For quick reference by someone who knows the concept.]

# Core Definition

[Precise technical definition with source attribution. Quote directly where the source provides a clear definition. For discursive sources that embed definitions in narrative, synthesise and note "Synthesised from discussion on pp. X-Y" in Verification Notes.]

# Prerequisites

- **[Prerequisite]** — [Why it's needed for understanding this concept]

[Or: "This is a foundational concept with no prerequisites within this source."]

# Key Properties

1. [Property 1 — verifiable, specific]
2. [Property 2]
3. [Property 3]

# Construction / Recognition

## To Construct/Create:
1. [Step]
2. [Step]

## To Identify/Recognise:
1. [Step]
2. [Step]

[If construction/recognition doesn't apply, describe the typical procedure or workflow involving this concept.]

# Context & Application

- **Typical contexts**: [Where this appears in design practice]
- **Common applications**: [How it's used]
- **Historical/stylistic notes**: [If relevant]

## Cross-Domain Connections

[Include this subsection ONLY if the concept has entries in the rosetta_stone frontmatter field. Use this structure:]

**[Source Domain] → [RIGOROUS/STRUCTURAL/LOOSE]**: [1-2 sentences describing the mapping.]
[1-2 sentences explaining WHY this mapping holds (for RIGOROUS), what structural parallel exists (for STRUCTURAL), or where the analogy breaks down (for LOOSE).]

[Example for a colour space concept:]
**Mathematics → RIGOROUS**: Colour space conversions are 3×3 matrix multiplications — sRGB → XYZ, XYZ → LMS, LMS → Oklab. Each step is a linear transform, and the chain collapses to a single matrix per Grassmann's additivity law. This is literal linear algebra, not metaphor.

**Music Theory → RIGOROUS**: The problem OKLAB solves — uniformising a perceptually non-uniform space — is mathematically identical to the problem equal temperament solves. Both compromise physical accuracy for perceptual uniformity across the entire space.

# Examples

**Example 1** (p. XX): [Specific example FROM THE SOURCE TEXT with citation]

**Example 2** (p. XX): [Another source example]

## Worked Example

[If the source provides a step-by-step walkthrough, reproduce it with citation. If not, omit this subsection — do NOT invent examples.]

# Relationships

## Builds Upon
- **[Concept]** — [How this concept elaborates it]

## Enables
- **[Concept]** — [Why this is a prerequisite for it]

## Related
- **[Concept]** — [Nature of the non-hierarchical relationship]

## Contrasts With
- **[Concept]** — [Key distinguishing feature]

# Common Errors

- **Error**: [Procedural mistake when applying this concept]
  **Correction**: [How to do it correctly]

# Common Confusions

- **Confusion**: [Conceptual misunderstanding about what this IS]
  **Clarification**: [The correct understanding]

# Source Reference

Chapter X: [Title], [Section X.X if applicable], pages XX-XX. [Include figure, table, or example references if relevant.]

# Verification Notes

- Definition source: [Direct quote from p. X / Synthesised from pp. X-Y / Inferred from context]
- Confidence rationale: [Why high/medium/low — be specific]
- Uncertainties: [Aspects needing review, OCR issues, ambiguous source text]
- Cross-reference status: [Verified slug references exist / Unverified — to be resolved in harmonisation]
- Rosetta Stone check: [Checked against 0010 tables / No mappings found / Mapping added: (domain, rating)]
- OCR issues: [Note any source text quality problems that affected extraction]
```

### Agent-Level Quality Requirements

Each card MUST have:

- [ ] All required frontmatter fields populated (null/empty array where N/A)
- [ ] `category` from the 0005 taxonomy (exact slug match)
- [ ] `layer` matches category's layer assignment in 0005
- [ ] `tier` consistent with 0006 tier table for this category
- [ ] `slug` follows naming conventions (generic vs. source-prefixed)
- [ ] Quick Definition ≤ 2 sentences
- [ ] Core Definition with source attribution
- [ ] At least one example from source text with page citation
- [ ] Prerequisites section (even if "foundational, no prerequisites")
- [ ] At least one CQ from 0007 in `answers_questions`
- [ ] `rosetta_stone` populated if concept appears in 0010 mapping tables
- [ ] `css_implementation` populated if concept has a CSS realisation
- [ ] Mathematical formulation included if one exists (per 0008 conventions)
- [ ] Verification Notes with confidence rationale AND Rosetta Stone check confirmation AND OCR issue notes
- [ ] Cross-Domain Connections body section present if and only if rosetta_stone frontmatter is populated

### File Naming

- Filename: `[slug].md` (lowercase, hyphenated, no numerical prefix)
- Output to: `concept-cards/[source-slug]/`
- ✅ `visual-hierarchy.md`, `munsell-hue-circle.md`, `gestalt-proximity.md`
- ❌ `001-visual-hierarchy.md`, `Visual_Hierarchy.md`

---

## Phase 6: Validate

After all cards are written, run validation.

### Structural Validation

```bash
SOURCE_SLUG="[source-slug]"

# Required frontmatter check
for file in concept-cards/$SOURCE_SLUG/*.md; do
  for field in concept slug category tier layer extraction_confidence; do
    grep -q "^${field}:" "$file" || echo "MISSING $field: $file"
  done
done

# Valid category check
VALID_CATS="visual-elements visual-perception design-principles colour-theory typography layout-composition interaction-design motion-design information-architecture data-visualisation imagery design-systems accessibility visual-identity"
for file in concept-cards/$SOURCE_SLUG/*.md; do
  cat=$(grep "^category:" "$file" | sed 's/^category: *//')
  echo "$VALID_CATS" | grep -qw "$cat" || echo "INVALID category '$cat' in $file"
done

# Slug-to-filename match
for file in concept-cards/$SOURCE_SLUG/*.md; do
  slug=$(grep "^slug:" "$file" | sed 's/^slug: *//')
  expected="$(basename "$file" .md)"
  [ "$slug" != "$expected" ] && echo "SLUG MISMATCH: '$slug' vs filename '$expected' in $file"
done

# Valid tier check
for file in concept-cards/$SOURCE_SLUG/*.md; do
  tier=$(grep "^tier:" "$file" | sed 's/^tier: *//')
  echo "foundational intermediate advanced" | grep -qw "$tier" || echo "INVALID tier '$tier' in $file"
done

# Valid layer check
for file in concept-cards/$SOURCE_SLUG/*.md; do
  layer_val=$(grep "^layer:" "$file" | sed 's/^layer: *//')
  echo "0-perception 1-principles 2-domain 3-implementation" | grep -qw "$layer_val" || echo "INVALID layer '$layer_val' in $file"
done
```

### Consistency Validation

```bash
# Internal cross-references (within this source)
ls concept-cards/$SOURCE_SLUG/*.md | xargs -n1 basename | sed 's/.md$//' | sort > /tmp/existing-slugs.txt

# Extract all referenced slugs from relationship fields
grep -A 50 "^prerequisites:" concept-cards/$SOURCE_SLUG/*.md | grep "^  - " | sed 's/^  - //' | sort -u > /tmp/prereq-refs.txt
grep -A 50 "^extends:" concept-cards/$SOURCE_SLUG/*.md | grep "^  - " | sed 's/^  - //' | sort -u >> /tmp/prereq-refs.txt
grep -A 50 "^related:" concept-cards/$SOURCE_SLUG/*.md | grep "^  - " | sed 's/^  - //' | sort -u >> /tmp/prereq-refs.txt
grep -A 50 "^contrasts_with:" concept-cards/$SOURCE_SLUG/*.md | grep "^  - " | sed 's/^  - //' | sort -u >> /tmp/prereq-refs.txt
sort -u /tmp/prereq-refs.txt -o /tmp/prereq-refs.txt

# Find references to concepts not in this source
# NOTE: These are NOT necessarily errors — they may be cross-source references
# to be resolved during harmonisation. Flag but do not fail.
comm -23 /tmp/prereq-refs.txt /tmp/existing-slugs.txt > /tmp/external-refs.txt
if [ -s /tmp/external-refs.txt ]; then
  echo "EXTERNAL REFERENCES (to be resolved in harmonisation):"
  cat /tmp/external-refs.txt
fi
```

### CQ Coverage Report

```bash
# Extract all answered CQs from this source
grep -h "answers_questions:" -A 20 concept-cards/$SOURCE_SLUG/*.md | grep "^  - " | sed 's/^  - //' | sort -u > /tmp/answered-cqs.txt
echo "CQs answered by this source:"
wc -l < /tmp/answered-cqs.txt
echo "---"
cat /tmp/answered-cqs.txt
```

This is a **report**, not a pass/fail. No single source is expected to cover all 56 CQs.

### Rosetta Stone Coverage

```bash
# Check which cards have rosetta_stone entries
echo "Cards with Rosetta Stone mappings:"
grep -l "^rosetta_stone:" concept-cards/$SOURCE_SLUG/*.md | xargs -n1 basename
echo "---"
echo "Cards WITHOUT Rosetta Stone check in verification notes:"
for file in concept-cards/$SOURCE_SLUG/*.md; do
  grep -q "Rosetta Stone check:" "$file" || echo "  $(basename $file)"
done
```

### Quality Sampling

Sample 3-5 cards (or all cards if under 10) and verify:

- [ ] Definitions accurate to source
- [ ] Confidence scoring justified in Verification Notes
- [ ] Prerequisites form valid chains (no circular dependencies within source)
- [ ] Examples cite specific source locations
- [ ] Rosetta Stone mappings correctly rated
- [ ] Generic vs. source-prefixed slugs correctly applied
- [ ] OCR-affected content correctly reconstructed (cross-reference with original if possible)

---

## Phase 7: Post-Mortem

After validation, write a brief post-mortem covering:

1. **Difficulties encountered** — OCR issues, ambiguous definitions, category assignment challenges
2. **Source-specific notes for future reference** — What would help someone re-extracting this source?
3. **CQ coverage summary** — Which CQs were addressed, which weren't (and why)
4. **Rosetta Stone discoveries** — Any cross-domain mappings found that aren't in the 0010 tables?
5. **Suggested additions to 0009** — Source-specific extraction notes to add for future reference
6. **Card count and extraction statistics** — Total cards, by category, by tier, by confidence level

Save to: `concept-cards/[source-slug]/POST-MORTEM.md`

---

## Context Management Notes

**To stay within context limits:**

- Phase 0.5 (source assessment) needs only the source files
- Phase 1 files (0004-0007) establish your mental model — release before extraction
- During extraction, agents need only: their assigned chapters, the combined template, their agent instructions, and 0010 (Rosetta Stone) for lookup
- For serial extraction: work through chapters sequentially, writing each card before moving to the next, keeping only the current chapter and template in active context
- Post-validation (Phase 6) needs only the output cards and the validation scripts
- Do NOT load the full Phase 0 spec into agents — compiled agent instructions contain everything needed

**To maintain quality:**

- Two-pass extraction: foundational first, then intermediate/advanced
- When uncertain about category, re-read just the relevant scope description in 0005
- When uncertain about tier, check only the relevant row in 0006's per-category table
- When uncertain about Rosetta Stone rigour rating, check criteria in 0010 Section 7.2
- When a concept spans multiple chapters, create ONE card citing all locations
- Never invent examples — if the source provides none, state that explicitly
- For discursive sources without formal definitions, set `extraction_confidence: medium` and document synthesis in Verification Notes

---

## Checklist Before Starting

- [ ] Source files are in `sources-md/[source-slug]/` as chapter-level `.md` files
- [ ] Output directory `concept-cards/[source-slug]/` exists (or will be created)
- [ ] All bracketed fields at the top of this prompt are filled in
- [ ] Source-specific notes from 0009 reviewed (if listed) or will be written in Phase 0.5
- [ ] You understand the target user: senior engineer, art background, deeply mathematical, needs vocabulary + systematic frameworks

Begin with Phase 0.5.
