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
   Keep existing semantic token names and relationships.
3. Choose deliberate visible distinction through available size, weight, spacing
   and colour. Treat caps and bold/italic choices as contextual options, not bans.
4. Review real strings, fallback, enlargement and the complete foreground/
   background colour pairs and states. Density of a text block differs from
   literal colour; route pair contrast checks through the [colour guide](colour.md).

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

Make the check concrete: record the asset or actual family name, source and
license/readiness; render representative real strings with the intended styles,
then deliberately fail loading and inspect the fallback. For a supplied variable
font, read axis tags and ranges from that file's metadata, request values within
those ranges, and inspect the loaded face and rendered result. A computed CSS
request alone proves neither the glyph face actually used nor a feature or axis.
Record the environment, observed outcomes, failures and unavailable cases.

Check 200% text enlargement, text-spacing overrides and a narrow viewport both
separately and together, with no clipped essential content or lost controls.
An authored CSS enlargement is a useful diagnostic, distinct from actual browser
zoom, native font preferences and assistive-technology checks. Record which was
performed; keep the base responsive to user enlargement rather than resetting
it to defeat their choice.

### Check feature and spacing choices in context

Choose the reading or number role and actual script. Inspect the supplied font's
features, then use a suitable high-level control supported by the target. Compare
representative strings in the face and fallback, including number alignment and
the styles in use; keep the text meaningful and inspect the rendered output.

For a column that needs equal digit advances, this scoped request can be a
starting point when the font and shaping environment support tabular figures:

```css
.number-column { font-variant-numeric: tabular-nums; }
```

It does not align decimal separators or values with different digit counts by
itself. `font-kerning: normal` can request metric kerning for proportionally
spaced text when appropriate; a font without kerning data may show no change.
Tracking is contextual and script-sensitive. These declarations are requests,
not evidence of available features or successful output.

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

## Preserve punctuation and meaningful text

Identify the actual language and house style, then distinguish editable prose,
quoted content, apostrophes, code and data. Choose punctuation for meaning: an
English prose quotation can use “hello”, while `print("hello")`, JSON
`{"message": "hello"}` and a literal `--help` option retain their exact syntax.
Preserve protected spans, deliberate transcription and meaningful spaces; review
smart-quote conversion, leading apostrophes such as ’70s, and dash substitutions.
An en/em dash's name does not guarantee its glyph width.

For quoted phrasing, optional semantic `q` markup can generate delimiters;
explicit quotation punctuation without `q` is also valid. Do not duplicate the
quoted span's delimiting marks inside or immediately outside `q`. Declare the
actual content language. CSS `quotes: auto` selects language-sensitive generated
marks; it does not rewrite stored quotes or apostrophes, and missing language
information is not the same as disabled generation. See the [HTML q definition](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-q-element)
and [CSS Generated Content Level 3 Working Draft](https://www.w3.org/TR/css-content-3/#quotes-property).

Choose the sentence-space convention for the prose and house style. In web
output, CSS can collapse or preserve spaces for rendering without rewriting the
document data; two stored spaces do not guarantee a visibly doubled gap. See
[CSS Text Level 3](https://www.w3.org/TR/css-text-3/#white-space-property).
Check generated quotes, apostrophes, dash spacing and preserved/collapsed spaces
in the target output with the actual font and content. Record untested behavior.

## Compose editorial structures

Choose the semantic content structure first: a section quoted from another
source, a data table with row/column relationships, or ordinary page content.
For example, compare each person's answers to the same questions with a semantic
HTML table and meaningful headers; arrange an article beside its navigation with
appropriate content markup and CSS Grid/Flexbox. Visual tracks do not supply
missing table semantics. See the [HTML table definition](https://html.spec.whatwg.org/multipage/tables.html#the-table-element).

Choose candidate measures, margins, column widths/gaps and alignment references
for the medium, content and available area. A conceptual grid need not use CSS
Grid; neither a column count nor an inch/rem value establishes quality. For data
tables, check caption, headers/associations, cell padding and essential boundaries
before reducing borders. For quotations, preserve exact content/context and place
attribution outside the quoted section; inherited size/leading and smaller indents
may suit tight measures. Use a decorative CSS rule without false thematic-break
semantics; check essential marks against their actual adjacent colours.

Then inspect actual reading order and column transitions, enlarged text, narrow
widths and fallback output. Keep meaningful source order when visually placing
items; [CSS Grid reordering](https://www.w3.org/TR/css-grid-2/#order-accessibility)
cannot replace it. Record untested browser/assistive-technology behavior and
remaining output checks rather than infer them from markup or geometry.

## Vary by context and review

Different content, roles, scripts, devices or user preferences may justify
different type choices. Maintain coherence where useful, but do not force every
page into one scale or family roster. Review real passages at intended sizes,
check text enlargement and reflow, and retain the adopting project's regular
browser and accessibility controls. Record exceptions and untested cases.
