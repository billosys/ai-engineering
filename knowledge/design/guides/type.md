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

Describe the hierarchy the task needs: for example, display, section heading,
long-form text, interface label, code or metadata. These are contextual roles,
not a requirement for a separate family per role. Reuse a supplied family across
roles when it works; select different families only when they solve an
identified reading, language, hierarchy or identity need. Keep existing
semantic token names and relationships.

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

## Vary by context and review

Different content, roles, scripts, devices or user preferences may justify
different type choices. Maintain coherence where useful, but do not force every
page into one scale or family roster. Review real passages at intended sizes,
check text enlargement and reflow, and retain the adopting project's regular
browser and accessibility controls. Record exceptions and untested cases.
