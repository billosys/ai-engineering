# Phase 0 - Section 11 - Appendices

## Appendix A: The Six Developer Design Mistakes

These six mistakes, validated across multiple sources (primarily Refactoring UI, supplemented by Laws of UX and NNGroup research), account for the majority of the perceived quality gap between developer-built and designer-built interfaces. They should drive extraction priorities and diagnostic competency questions.

1. **No visual hierarchy** — Everything has equal visual weight. Headers don't stand out from body text. Primary actions look the same as secondary actions. The eye has no entry point and no reading path.

2. **Inconsistent spacing** — No spacing system. Values are arbitrary (13px here, 17px there, 22px somewhere else). No relationship between internal padding and external margins. No differentiation between structural and content spacing.

3. **Unconstrained colour** — Too many unrelated hues. Every state gets its own colour. No palette discipline. No semantic colour layer. The "clown car" problem.

4. **No type scale** — Random font sizes with no systematic relationship. No modular scale. Sizes chosen by "looks about right" rather than by ratio.

5. **Data-model-driven information architecture** — UI mirrors the database schema instead of user tasks. A "Users" page shows all user columns because that's what the `users` table has. Navigation matches table names, not workflows.

6. **Equal-weight buttons** — Every action is a filled, primary-styled button. No visual distinction between primary ("Submit Order"), secondary ("Save Draft"), and tertiary ("Cancel") actions. The user can't quickly identify the intended action.

---

## Appendix B: Source Acquisition Checklist

| # | Source | Format | Est. Cost | Status |
|---|--------|--------|-----------|--------|
| 1 | Refactoring UI | PDF | $79-149 | ☐ Acquired |
| 2 | Laws of UX (website) | Web | Free | ☐ Captured |
| 3 | The Vignelli Canon | PDF | Free | ☐ Downloaded |
| 4 | Atomic Design (website) | Web | Free | ☐ Captured |
| 5 | Practical Typography (website) | Web | Free | ☐ Captured |
| 6 | Utopia blog + calculators | Web | Free | ☐ Captured |
| 7 | ModernCSS.dev | Web | Free | ☐ Captured |
| 8 | Interaction of Color (Albers) | Print | ~$25 | ☐ Acquired |
| 9 | Elements of Typographic Style (Bringhurst) | Print | ~$25 | ☐ Acquired |
| 10 | Design of Everyday Things (Norman) | Ebook | ~$15 | ☐ Acquired |
| 11 | Thinking with Type (Lupton, 3rd ed) | Print | ~$25 | ☐ Acquired |
| 12 | Grid Systems (Müller-Brockmann) | Print | ~$50 | ☐ Acquired |
| 13 | Elements of Color (Itten) | Print | ~$30 | ☐ Acquired |
| 14 | Don't Make Me Think (Krug) | Print/ebook | ~$20 | ☐ Acquired |
| 15 | Every Layout | Web (paid) | ~$70 | ☐ Acquired |
| 16 | Art and Visual Perception (Arnheim) | Print | ~$25 | ☐ Acquired |
| 17 | Information Visualization (Ware, 4th ed) | Print | ~$60 | ☐ Acquired |

**Total estimated cost for all paid sources**: ~$450-520
**Wave 1 cost (free + Refactoring UI)**: $79-149

---

## Appendix C: Directory Structure

```
project-root/
├── extraction-metadata/
│   └── visual-design/
│       ├── phase-0-domain-specification.md    ← THIS DOCUMENT
│       ├── competency-questions.md            ← Extracted from Section 4
│       └── extraction-log.md                  ← Per-wave tracking
├── sources-md/
│   ├── refactoring-ui/
│   ├── laws-of-ux/
│   ├── vignelli-canon/
│   ├── atomic-design/
│   ├── practical-typography/
│   ├── utopia/
│   ├── moderncss-dev/
│   ├── interaction-of-color/
│   ├── elements-of-typographic-style/
│   ├── design-of-everyday-things/
│   ├── thinking-with-type/
│   ├── grid-systems/
│   └── ... (additional sources)
├── concept-cards/
│   └── visual-design/
│       └── (all extracted concept cards, flat directory)
└── guides/
    └── visual-design/
        ├── pattern-language/
        ├── decision-frameworks/
        ├── critique-protocols/
        └── rosetta-stone/
```
