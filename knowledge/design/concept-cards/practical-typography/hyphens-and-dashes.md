---
concept: "Hyphens and Dashes"
slug: "hyphens-and-dashes"
category: "typography"
subcategory: "type-composition"
tier: "foundational"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Type Composition"
chapter_number: null
pdf_page: null
section: "Hyphens and Dashes"
extraction_confidence: "high"
aliases:
  - "dashes"
  - "en dash"
  - "em dash"
  - "hyphenation marks"
prerequisites:
  - "typewriter-habits"
extends: []
related:
  - "em-unit"
  - "curly-quotes"
  - "sentence-spacing"
contrasts_with: []
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition

Hyphens (-), en dashes (–, U+2013) and em dashes (—, U+2014) are distinct punctuation marks. Butterick's English prose examples use hyphens for compounds, en dashes for ranges/connections and em dashes for sentence breaks; follow the adopting language and editorial style.

# Core Definition

Butterick distinguishes these marks by function:

- **Hyphen (-)**: Word breaks, compounds such as topsy-turvy, and phrasal adjectives such as listener-supported radio. His examples exclude an -ly adverb in closely held company and proper names in Third Circuit docket.
- **En dash (–)**: Ranges such as 1880–1912 and pages 330–39, and connections such as conservative–liberal split and Sarbanes–Oxley Act.
- **Em dash (—)**: A break between sentence parts, chosen for the intended pause and grammatical structure. His judgment that it is underused is editorial advice.

He rejects repeated hyphens (`--` or `---`) as prose-dash approximations. That does not authorize changing literal command options, source code or data sequences. Dash practices and spacing vary by language and style.

# Prerequisites

- **Typewriter Habits** — Checklist item #3 supplies the context for replacing prose-dash approximations, not a universal ban on hyphen sequences.

# Key Properties

1. **Distinct characters and roles**: The hyphen-minus shown as `-` is distinct from – and —; visual similarity does not make their uses interchangeable.
2. **Editorial scope**: The range, compound and sentence-break guidance here follows Butterick's English examples, not a universal punctuation grammar.
3. **Sentence break**: Butterick favors the em dash for a pause when other punctuation does not express the intended relationship.
4. **Range wording**: Use 1880–1912, or from 1880 to 1912; his rule pairs from with to rather than from 1880–1912.
5. **Compound clarity**: Five dollar bills can mean five bills worth one dollar each; five-dollar bills identifies the denomination.
6. **Unit names differ from glyph widths**: Em and en name typographic units, not the letters M and N. The en is half the em, but actual dash advances are font-dependent, not guaranteed 1em/0.5em.

# Construction / Recognition

## To Construct/Create:
1. Insert – with `&ndash;` or the actual UTF-8 character in HTML. The source lists Windows alt+0150 and Mac option+hyphen; verify the current input method/layout.
2. Insert — with `&mdash;` or the actual UTF-8 character. The source lists Windows alt+0151 and Mac option+shift+hyphen, with the same input-method caveat.
3. Choose spacing by language/house style and inspect the face. Butterick typically sets dashes flush but permits added spaces if cramped, and reports Bringhurst's spaced-en-dash alternative.
4. Replace `--`/`---` only when they are intended prose-dash approximations. Preserve literal `--help` and other code/data sequences.

## To Identify/Recognise:
1. Identify the character and intended meaning, not length alone: hyphens join words or mark permitted word breaks.
2. – is the en dash used in this source's range/connection examples; neither its name nor its visible length proves a half-em advance.
3. — is the em dash used in this source's sentence-break example; its actual advance need not be one em.

# Context & Application

- **Typical contexts**: Edited prose and ranges, under the language's grammar and chosen editorial style.
- **Common applications**: Compounds, date/page ranges and sentence asides. Preserve literal code, identifiers, copied data and deliberate transcription.
- **Historical note**: Butterick explains em/en as measurement names and reports the print-shop terms mutton/nut. He explicitly says modern digital dashes run narrower than the historical units; do not convert his naming history into fixed glyph metrics.

# Examples

**Example 1** (hyphens-and-dashes): Five dollar bills suggests a quantity of dollar bills; five-dollar bills makes each bill worth $5. Butterick also distinguishes Sarbanes–Oxley Act (joint names) from his hypothetical compound family name Sarbanes-Oxley.

**Example 2** (hyphens-and-dashes): His sentence illustrates an em-dash pause: “The em dash puts a nice pause in the text—and it is underused in professional writing.” Keep the underuse judgment attributed. His range example is 1880–1912; with from, write from 1880 to 1912.

# Relationships

## Builds Upon
- **Typewriter Habits** — Its item #3 criticizes repeated hyphens used as prose-dash approximations; literal code/data have different requirements.

## Related
- **Em Unit** — The naming connection is to em/en measurement units; the endpoint's unit definition does not fix actual dash glyph widths.
- **Curly Quotes** — Both require choosing punctuation by meaning and language while preserving literal code/data.
- **Sentence Spacing** — Both concern contextual prose-composition conventions; their checklist connection does not establish a universal historical origin.

# Common Errors

- **Error**: Keeping repeated hyphens when a prose dash is intended, or replacing literal `--help` with a dash.
  **Correction**: Use – or — according to meaning and style in prose; retain exact syntax in code and data.

# Common Confusions

- **Confusion**: Em/en are the letters M/N or guarantees that dash widths equal 1em/0.5em.
  **Clarification**: They name units; the en is half the em. Glyph advances are a separate matter. Butterick's historical explanation explicitly notes narrower digital dashes.

# Source Reference

"Hyphens and Dashes" page. "Type Composition" chapter.

# Verification Notes

- Available source: complete prepared hyphens-and-dashes.md, including English grammar examples, spacing alternatives and modern-width qualification. Immutable original/capture fidelity remains P10-11-unresolved.
- Character identity checked against the [Unicode General Punctuation chart](https://www.unicode.org/charts/PDF/U2000.pdf), U+2013/U+2014. No font metrics, browser or assistive-technology behavior tested.
- Historical extraction confidence is preserved, not a new warrant or fidelity result. Four local relationships retain only the premises above; the external Em Unit card is not accepted wholesale.
- CQ1 membership is preserved; these punctuation choices do not establish visual hierarchy or explain all its properties.
