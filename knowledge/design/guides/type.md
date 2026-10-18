# Type Choices from Reading Context

Choose type for the project's language, scripts, content, audience, task and
rendering environment. Preserve supplied typefaces, assets and naming. This
guide offers a method; it does not prescribe a font roster, family count, ratio
or style.

## Start with scripts, content and supplied assets

Record the actual text and languages, writing direction, reading duration,
content density and use context. Identify supplied fonts, licenses, local assets,
platforms, supported browsers, text enlargement and other fixed decisions.
Mark unsupported scripts, missing font files and unknown environments rather
than inferring coverage.

## Assign roles and hierarchy

1. Describe the content roles and outline; choose semantic heading levels from
   the structure, not from the desired CSS size. `em` marks stress and `strong`
   marks importance, seriousness or urgency; neither is defined by italic/bold
   styling, and both meanings can apply to one phrase.
2. Compare supplied faces and available styles on representative project text,
   including relevant scripts, fallback runs and code. Reuse one supplied family
   when it meets the roles; a pairing is optional and useful only when it solves
   an identified need. There is no fixed family count or point-size increment.
3. Choose deliberate visible distinction through available size, weight, spacing
   and colour. Treat caps and bold/italic choices as contextual options, not bans.
4. Review real strings, fallback, enlargement and the complete foreground/
   background colour pairs and states. Density of a text block differs from
   literal colour; route pair contrast checks through sibling `colour.md`.

When genuine small-cap glyphs are intended, this optional request also suppresses
other synthesized styles; it does not supply missing glyphs or prove what the
font or target rendered:

```css
.small-caps { font-variant-caps: small-caps; font-synthesis: none; }
```
Check the supplied font's feature and script coverage, actual output, and a
truthful fallback. `font-synthesis: none` can also suppress synthesized bold or
oblique, so review those roles as well.

## Check candidates and fallbacks

Compare candidate faces using representative text from the actual content.
Check glyph coverage, shaping, diacritics, punctuation, numerals, direction,
line breaking and language-specific conventions. Inspect weights and styles
used in the design, loading behavior, licensing and suitable fallback stacks.
A generic family keyword can be part of a fallback, but its choice depends on
the selected face and script. A Latin sample does not establish multilingual
support. Do not claim font failure, browser coverage or improved readability
without testing the named environment.

## Choose a scale, then judge it optically

A scale may help coordinate hierarchy. One optional construction is
`size(n)=base*ratio^n`; declare the base, ratio, step range and context when
using it. The relationship is a design aid, not proof of typographic harmony,
readability or accessibility. Content, language, actual glyphs and layout may
justify a measured optical adjustment or a non-geometric size. Do not assign
negative steps to functional text by default.

If sizes interpolate between contexts, state the roots, endpoints, interval,
units and rounding. Interpolation is calculated per step and does not
necessarily retain geometric ratios at intermediate widths. The named
[diagnostic fluid-type exercise](layout.md#the-fluid-foundation-a-scoped-arithmetic-illustration) illustrates
arithmetic only; its values are not typography or spacing defaults.

## Use only available axes

Inspect the selected font's actual axis metadata and supported ranges. Choose an
axis only when the asset supplies it and a concrete typographic goal supports
it. Keep values within the declared range, and compare rendered samples at the
sizes and scripts in use. Axis labels and CSS declarations do not show how a
font will look in the target browser.

## Compose readable paragraphs

Start from the reading context, language and actual content. Choose candidate
font, size, leading and measure together, then select one coherent paragraph
separation treatment (or a deliberate combination). Review alignment, language-
aware word breaking and page/column flow in the target output. A width unit or
formula is only a starting point: inspect actual lines with representative text,
fonts, fallbacks, spaces, language and writing mode.

For horizontal prose, this scoped illustration inherits the project's font and
uses example values rather than required tokens. Set the content language on the
surrounding HTML element, for example `<article lang="en">`; use the actual
language for the content.

```css
.prose {
  font-size: 1rem;
  line-height: 1.35;
  max-width: 65ch;
  text-align: start;
}

.prose p { margin: 0; }
.prose p + p { margin-block-start: .75em; }
```

An indent can replace the paragraph gap; change the rule rather than layering
both treatments by default:

```css
.prose p + p {
  margin-block-start: 0;
  text-indent: 1em;
}
```

The `65ch`, `1.35` and `.75em` values illustrate a candidate. `ch` uses the
zero glyph advance with specification fallbacks; it does not promise a character
count. A unitless CSS `line-height` is inherited as a number and multiplies each
element's own font size. A percentage computes from the font size of the element
where it is specified, then the resulting length is inherited. A 20px parent
declaring `150%` computes 30px; a 12px child inherits 30px unless it overrides
that value. If the child explicitly declares `150%`, it computes 18px. Lengths
also compute before inheritance. CSS `em` usually uses the element's
computed font size, but on `font-size` it resolves against the inherited size;
`rem` uses the root size.

Preserve text enlargement and reflow. [WCAG 2.2 Success Criterion 1.4.12](https://www.w3.org/TR/WCAG22/#text-spacing) is AA:
it requires no loss of content or functionality when users apply its specified
spacing overrides: line height at least 1.5 times font size, following-paragraph
spacing at least 2 times font size, letter spacing .12 times font size and word
spacing .16 times font size. Some languages and scripts do not use every spacing
property; the criterion has an exception for those combinations. It does not
require these authored defaults. [Success Criterion 1.4.8](https://www.w3.org/TR/WCAG22/#visual-presentation) is a separate AAA criterion with visual-presentation conditions including
a user mechanism, width limits and non-justified text. This guidance is not a
test or conformance claim; validate user overrides and reflow in the adopting
project without hiding overflow or clamping text height.

## Vary by context and review

Different content, roles, scripts, devices or user preferences may justify
different type choices. Maintain coherence where useful, but do not force every
page into one scale or family roster. Review real passages at intended sizes,
check text enlargement and reflow, and retain the adopting project's regular
browser and accessibility controls. Record exceptions and untested cases.
