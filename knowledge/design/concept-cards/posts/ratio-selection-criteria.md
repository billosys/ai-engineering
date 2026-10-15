---
concept: "Ratio Selection Criteria"
slug: "ratio-selection-criteria"
category: "typography"
subcategory: "type-scale"
tier: "intermediate"
layer: "2-domain"
source: "More Meaningful Typography"
source_slug: "posts"
authors: "Tim Brown"
chapter: "Creating a modular scale for web design"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "medium"
aliases:
  -
    - "choosing a scale ratio"
    - "ratio selection"
    - "ratio justification"
prerequisites:
  - "scale-ratio"
  - "modular-scale"
extends:
  - "scale-ratio"
related:
  - "golden-ratio"
  - "musical-interval-typographic-ratio"
  - "modular-scale-construction"
contrasts_with: []
answers_questions:
  - "How do you select an appropriate scale ratio for a given design context?"
  - "What makes a type hierarchy feel harmonious vs arbitrary?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition

Ratio selection is the contextual decision to declare a positive scale ratio for a particular use. Brown gives one worked rationale; the prepared article does not provide an exhaustive candidate menu, universal cultural checklist, or experimentally established optimum.

# Core Definition

Brown says scale inputs can be meaningful to a project's design or content, then explains why he chose 1:1.618 for a particular text and typeface: he describes a historical association between Renaissance page proportions and Minion's Renaissance references, and says the subject concerned typographic tradition. This records Brown's rationale, not independent confirmation of the historical claims or a general rule that a typeface lineage determines a ratio.

The article's opening names broad domains—geometry, music, nature, and history (prepared source, lines 109–112)—but does not enumerate every permissible ratio or supply a complete interval/application table. The later passage about “easily divisible” numbers and viewport sizes concerns choosing composition widths in that context (lines 346–356). It does not show that selecting a ratio for arithmetic simplicity is invalid. Contrast, optical fit, content, task, implementation, and accessibility can be editorial considerations; they should not be attributed to Brown as a tested selection framework unless a cited passage supports them.

# Prerequisites

- **Scale ratio** — The input being selected.
- **Modular scale** — The structure in which the ratio is used.

# Key Properties

1. **Context is stated**: Explain the project's purpose and constraints that inform a ratio choice. This is a useful documentation practice, not a measured predictor of preference.
2. **The ratio controls progression**: Its value affects the multiplicative distance between indexed values in a strand. This mathematical fact alone does not determine whether the resulting hierarchy is useful or harmonious.
3. **Candidates are not exhausted here**: Brown names broad domains and demonstrates one choice. These passages do not establish a closed list or a complete mapping from subject domain to ratio.
4. **Tradeoffs remain project-specific**: Contrast, optical fit, task needs, content, and implementation can inform an editorial decision. No universal ranking or automatic cultural prescription follows from this card.

# Construction / Recognition

## To Construct/Create:
1. State the task and constraints for the scale, including any required range, density, or implementation limits.
2. Choose a positive ratio and record why it is suitable for this use. If the choice is provisional or convenient, say so.
3. Inspect the resulting values in their actual content and context. This step can inform an editorial decision; it does not by itself establish a universal optimum or empirical harmony.
4. If comparing candidates, define the candidates and the basis of comparison. The Brown article does not provide that comparison protocol or a complete candidate list.

For example, a designer might declare a 16px starting value and `r=1.25` for a dense interface because a modest step is a candidate to inspect against its content and space constraints. These numbers are illustrative only: this is not a default, recommendation, tested rendering, or cultural lineage claim. Brown's contrasting contextual example is Minion at 18px with 1:1.618 and a 190px h2; he also describes improvising values when they better served his project.

## To Identify/Recognise:
1. Look for the stated ratio and the reason it was selected.
2. Separate a source's explicit rationale from your own editorial inference.
3. If suitability or “harmony” is claimed empirically, identify the actual comparison, participants or observations, content, and conditions. A rationale or mathematical sequence alone does not answer that question.

# Context & Application

- **Typical contexts**: Recording why a scale ratio was chosen and what constraints the choice serves.
- **Common applications**: Brown's one contextual example; separately, a designer may document a provisional candidate and inspect its consequences in the actual task.
- **Historical/stylistic notes**: Brown's article opening invokes “ratios rooted in geometry, music, nature, and history” as broad domains. It does not give a full candidate list or prove a rule such as golden ratio for Renaissance work or musical ratios for editorial work.

# Examples

**Example 1** (from source, “Creating a modular scale for web design”): “I chose the golden mean (1:1.618). It is a beautiful proportion with historical and cultural connections that make sense for the typefaces I've chosen and the text I'm setting. Although it is a contemporary design, Minion draws upon Renaissance ideals, in everything from its humanist structure to the ways in which parts of letters reveal a history in pen and ink. Page and textblock proportions in Renaissance works were based on the golden mean, too, and because the subject of my text is about the craft of typesetting and looking to tradition for guidance, it made sense to use a proportion meaningful to our typographic roots.” This is Brown's attributed rationale; the prepared article is not independent historical or perceptual verification.

**Example 2** (from source, opening): “This and other meaningful ratios rooted in geometry, music, nature, and history can be expressed as modular scales and put to work on the web.” The broad framing does not enumerate candidates or an application table.

# Relationships

## Builds Upon
- **Scale ratio** — Selection presupposes knowing what a ratio is.

## Enables
- **Modular scale construction** — The construction procedure uses a selected ratio with its other inputs. This relation does not prescribe a candidate or establish that the result is harmonious.

## Related
- **Golden ratio** — Brown's worked example selects the decimal approximation 1.618 in its project context; the example does not establish universal suitability.
- **Musical interval ↔ typographic ratio** — The source bibliography and opening mention music broadly, but the proposed full candidate table is not established by the inspected passage. The music/application card and referenced talk remain uninspected; no table or recommendation is verified here.

## Contrasts With
- **Undocumented selection** — A ratio may be used without recording its rationale. Stating a rationale improves traceability but does not prove suitability.

# Common Errors

- **Error**: Treating Brown's example as an exhaustive menu or as a rule to select a ratio from a typeface's historical lineage.
  **Correction**: The example reports one contextual decision. It does not establish automatic golden-for-Renaissance, musical-for-editorial, or any other domain-to-ratio mapping.

- **Error**: Applying Brown's critique of composition-width choices to reject ratio selection for arithmetic convenience.
  **Correction**: The cited passage addresses viewport-sized composition widths in context. It does not establish a prohibition on convenient ratio choices.

- **Error**: Calling a hierarchy harmonious or optimal solely because its ratio has a mathematical or cultural rationale.
  **Correction**: Keep rationale separate from empirical judgment. The existing harmony question retains an unanswered empirical component; no comparison is supplied here.

# Common Confusions

- **Confusion**: Any positive ratio generates a mathematical sequence, so the specific choice does not matter.
  **Clarification**: A chosen ratio changes the sequence's multiplicative spacing, so it matters mathematically and may matter to a design task. This does not make one ratio universally meaningful or establish perceived harmony. A convenient choice can be valid when declared and suitable for the stated constraints.

# Source Reference

“Creating a modular scale for web design” — More Meaningful Typography, Tim Brown (A List Apart, May 2011)

# Verification Notes

- Definition and examples: Brown's prepared article opening (lines 109–112), ratio discussion (lines 133–189), and composition-width passage (lines 346–356). The article supplies a contextual example and broad framing, not an exhaustive selection method.
- Available-evidence review: Prepared-source support is limited to the cited rationale and scope; mathematical progression is distinct from editorial suitability; the links to the ratio and construction concepts express input dependency, while the musical mapping endpoint is unresolved; the first existing selection question has a procedural answer, while its harmony question remains empirically unanswered.
- Exceptions: Brown's historical and aesthetic statements are retained as attribution, not independently verified. The edge to the musical mapping card is not asserted as a verified table; that card and talk are later/uninspected endpoints. The width critique is not transferred into a ratio-selection rule.
- Legacy evidence: “Medium,” “Verified,” and OCR observations describe inherited extraction history, not current semantic or original-fidelity acceptance. No immutable original capture or lineage was reviewed; CDC review remains pending.
