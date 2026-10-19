---
concept: "Curly Quotes"
slug: "curly-quotes"
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
section: "Straight and Curly Quotes"
extraction_confidence: "high"
aliases:
  - "smart quotes"
  - "typographer's quotes"
  - "proper quotation marks"
prerequisites:
  - "typewriter-habits"
extends: []
related:
  - "sentence-spacing"
  - "hyphens-and-dashes"
contrasts_with: []
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
rosetta_stone: []
css_implementation:
  -
    property: "quotes"
    example: "q { quotes: auto; } /* language-sensitive generated delimiters; does not rewrite text or apostrophes */"
    support: "baseline"
---

# Quick Definition

Curly quotation marks are distinct punctuation characters commonly used for English prose quotations: ‘ ’ and “ ”. Choose marks and spacing for the actual language and editorial style; preserve straight characters where they carry literal meaning or syntax.

# Core Definition

Butterick recommends curly rather than straight quotes for typeset prose. His explanation connects straight quotes to restricted typewriter character sets; his broad historical claims and severity judgments are his account, not an independently established history or legibility study.

For his English example, U+2018/U+2019 are the opening/closing single marks and U+201C/U+201D the double marks. U+2019 also serves as a prose apostrophe. These are distinct from straight ASCII delimiters and from prime/double-prime measurement marks. The source acknowledges that other languages use different quotation forms and spacing; “curly” is not a universal orientation rule.

# Prerequisites

- **Typewriter Habits** — Butterick's checklist identifies straight prose quotes as item #1; the checklist supplies context, not a prerequisite for entering characters.

# Key Properties

1. **Distinct characters**: ‘ ’ “ ” are the four forms illustrated by this English source, not a complete inventory for every language.
2. **Contextual recommendation**: Butterick strongly favors curly prose quotes, but explicitly preserves code syntax and permits straight quotes in email.
3. **Apostrophes need judgment**: ’70s and Patent ’211 begin with U+2019, not the opening single quote ‘. Automatic conversion can get these wrong.
4. **Historical software advice**: The source describes smart quotes as typically enabled and nearly 30 years old. Its menus, shortcuts and time-relative rhetoric are source-era reports, not current application guarantees.
5. **Generated versus stored text**: CSS `quotes` selects generated delimiters; it does not convert text characters or apostrophes.
6. **Literal spans**: Code, identifiers, quoted data and deliberate transcription can require exact straight quotes or backticks.

# Construction / Recognition

## To Construct/Create:
1. Identify the language, house style and whether a span is prose, a quotation, an apostrophe, measurement or literal data before changing it.
2. In editable prose, use appropriate characters directly or reviewed smart-quote conversion. Limit replacements to intended prose and inspect pasted text and leading apostrophes afterward.
3. The source lists Mac option+[ / option+shift+[ for double marks and option+] / option+shift+] for single marks. Treat these as source-era keyboard-layout examples; verify the actual input method.
4. HTML can store UTF-8 characters or use `&ldquo;`, `&rdquo;`, `&lsquo;`, `&rsquo;` character references.
5. For phrasing content quoted from another source, optional semantic `<q>` markup can supply generated delimiters, for example `<p lang="en">She said <q>Hello</q>.</p>`. Do not duplicate its delimiting quotation punctuation inside or immediately outside `q`. Explicit quotation punctuation without `q` is also valid. Declare the actual content language; missing `lang` is not equivalent to disabled generation. `q { quotes: auto; }` selects language-sensitive generated marks in the CSS Generated Content Level 3 Working Draft; inspect target output rather than assuming a particular shape.

## To Identify/Recognise:
1. Distinguish the stored character and its role from its visible glyph: straight quotes can be required syntax, and an apostrophe is not necessarily a quotation boundary.
2. For the English example, compare ‘ ’ and “ ”; consult language conventions rather than assigning one opening/closing orientation worldwide.

# Context & Application

- **Typical contexts**: Edited prose in books, reports and web pages, subject to language and house style.
- **Common applications**: Quotation punctuation and prose apostrophes. `q` represents actual quotation, not emphasis, sarcastic framing or every quote-shaped character.
- **Exception**: Keep code, identifiers, exact quoted data, primes and deliberate text literal; Butterick also permits straight email quotes. A global replacement cannot decide these roles safely.

# Examples

**Example 1** (straight-and-curly-quotes): Butterick labels `"That's a 'magic' shoe."` wrong and “That’s a ‘magic’ shoe.” right for his English prose convention. The apostrophe in That’s is U+2019. This is a contextual demonstration, not a multilingual rule.

**Example 2** (straight-and-curly-quotes): His code exception requires literal straight quotes and backticks. Preserve `print("hello")`, JSON `{"message": "hello"}` and the quotes in copied source code. Their delimiters have a different role from the marks in English prose “hello”. Also inspect ’70s and Patent ’211 after conversion; starting position does not make their apostrophe an opening quote.

# Relationships

## Builds Upon
- **Typewriter Habits** — Its item #1 supplies Butterick's context for reviewing straight prose quotes, while preserving literal syntax exceptions.

## Related
- **Sentence Spacing** — Both are prose-composition choices in Butterick's checklist; neither licenses changing protected text indiscriminately.
- **Hyphens and Dashes** — Both distinguish meaningful punctuation characters from typewriter-style approximations, with code/data exceptions.

# Common Errors

- **Error**: Applying quote conversion to every character stream or trusting a leading apostrophe to become correct automatically.
  **Correction**: Restrict the operation to intended prose, preserve protected spans and inspect ’70s, Patent ’211, nesting and language-specific marks.

# Common Confusions

- **Confusion**: Smart quotes or CSS `quotes` will fix all quotes and apostrophes, including code.
  **Clarification**: Source-code delimiters stay literal. CSS `quotes` controls generated quotation punctuation, not stored characters; `q` does not replace apostrophes. The HTML Standard permits explicit quotation punctuation without `q` and forbids duplicated delimiting marks with it.

# Source Reference

"Straight and Curly Quotes" page. "Type Composition" chapter.

# Verification Notes

- Available source: complete prepared straight-and-curly-quotes.md, including language diversity, leading-apostrophe, email and code exceptions. Immutable original/capture fidelity remains unresolved under P10-11.
- Technical correction: [HTML Standard, q](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-q-element); [CSS Generated Content Level 3, §§2.4.1–2.4.2](https://www.w3.org/TR/css-content-3/#quotes-property), a Working Draft; [Unicode General Punctuation chart](https://www.unicode.org/charts/PDF/U2000.pdf), quotation/apostrophe and prime entries. Definitions checked; no browser or assistive-technology behavior tested.
- Historical extraction confidence remains unchanged; it is not a new source-fidelity or evidence-grade result.
- Local relationship support is limited to the stated premises. CQ1 membership is preserved; punctuation conventions alone do not explain visual hierarchy or all its properties.
