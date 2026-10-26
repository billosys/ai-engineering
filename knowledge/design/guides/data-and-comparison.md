# Dense data and truthful comparison

Use a compact summary when people need to compare a few meaningful groups while
working with the underlying records. Begin with the task and the data that can
actually answer it. Choose the display after the population, unit and changing
view are clear.

## Define what each number means

Write down the question in task language: what decision or next action should a
comparison support? Then name the population, unit, grouping, measure and
current scope. A count needs a noun and a boundary. “Seven” is not meaningful
until the reader can tell whether it means seven articles, people, searches or
events, and which records were included.

Keep these cases distinct:

- **Zero** means the measure is available and no records in the stated scope
  have that value.
- **Unavailable** means the system cannot provide a trustworthy value, for
  example because the source failed or the field was not collected. Label that
  state as unavailable; do not substitute zero.
- **Not applicable** means the measure has no meaning for this record or task.
  Explain that state if the distinction affects a decision.

Make the scope visible next to the values. If a filter changes the population,
say whether the comparison follows the current view, the full collection, or a
separate selected cohort. Do not imply a general trend or service-wide result
from a small pinned example.

## Choose the display for the comparison

Use a semantic table when readers need exact values, stable group labels or
side-by-side lookup. Give it a caption and row and column headers that name the
values and their units. Keep meaningful text and numbers in the cells so the
comparison still works when color or decorative styling is unavailable.

Add a chart only when a visual relation helps with the task. For a small set of
counts, a bar beside exact numbers can show relative magnitude without replacing
the table. Start every bar at zero and use one declared reference across all
groups. A fixed reference makes values comparable as filters change; rescaling
each row or using the filtered maximum changes the visual meaning. Label the
reference beside the display. Treat the bar as secondary and decorative when
the table already communicates its meaning.

Do not add percentages when the denominator is small or would distract from the
actual count. A short prose argument does not become a dashboard merely because
it contains several numerals: keep it in prose when the reader needs to follow
an explanation rather than compare a repeated set of values.

## Arrange and format the values

Place the comparison close to the controls and records that define its scope.
Give each heading, label, number and annotation a role. Keep the task's existing
content and supplied identity; a new summary should help readers find their way
through the records rather than compete with them.

Right-align comparable numbers where that makes scanning easier. A CSS request
such as `font-variant-numeric: lining-nums tabular-nums` can request lining and
tabular figures in fonts that provide those features. It does not prove that a
loaded face contains them or that values align as intended. Keep the exact
number and unit available as text, then inspect the actual font, fallback and
rendered column. Decimal alignment is a separate choice; do not claim it from
tabular figures alone.

Allow long labels and headers to wrap. Check the real content at the narrowest
useful width and with enlarged text and spacing. Keep horizontal scrolling
limited to the data region that needs it; a compact summary should not inherit
an unrelated table's minimum width. Do not hide overflow or shrink functional
text just to force a wide comparison onto a small screen.

## Work the current state, not a static picture

For an interactive view, identify which existing state owns each value. Derive
summary numbers from the same records and state used to render the main result.
Recalculate after the established filter, selection, queue, reset and undo
transitions. Do not create a second state store or count hidden records unless
the label explicitly says that it covers the full collection.

Use a simple state table before implementation:

| User action | Population counted | What the display should say |
|---|---|---|
| Filter to one record | Rows that remain visible | One group has one visible record; all other groups remain present at zero. |
| Queue the visible record | Visible rows intersected with the existing queue | The visible count stays one and queued-in-view becomes one. |
| Show only queued records | Rows matching both the current query and queue filter | The same record remains visible and queued-in-view remains one. |
| Enter an unmatched query | No visible rows | Every group shows zero; the existing empty-results message remains. A session-wide queue count, if shown elsewhere, can remain one. |
| Reset the filters | All rows return to view | Original group counts return; the queue follows the task's stated reset rule. |
| Undo the queue batch | Current view with the restored queue | Visible counts stay tied to the view and queued-in-view reflects the restored queue. |

Before shipping, derive the baseline counts independently from the complete
input population. Check that group totals reconcile to the population when the
groups are mutually exclusive and exhaustive. Reconcile filtered and queued
values against the actual state transitions. A screenshot of one state cannot
establish those relationships.

## Worked example: LFE reading desk

The [reading-desk text case](using-the-skill.md#dense-comparison) records a local
task over a pinned snapshot of 16 published LFE articles. Its task is to select
articles for a reading session. A compact summary answers a useful companion
question: which topics are represented in the current view, and how many of
those visible articles are already queued? The runtime specimen is preserved in
the repository outside the skill package; the text case does not run it.

The record unit is one article, grouped by its existing `data-topic` value. The
complete snapshot has 11 tutorials, two languages articles, two announcements
and one news article. These sum to 16. They describe this snapshot, not all LFE
posts, readership, popularity or performance. The summary keeps all four
topics present, including real zeroes after filtering. “Queued in view” is the
intersection of visible article keys with the existing session queue; it is not
the total queue size.

| Current view or transition | Visible by topic | Queued in view | Reason |
|---|---:|---:|---|
| Full snapshot | tutorials 11; languages 2; announcements 2; news 1 | 0 in every topic | The source contains 16 article rows and the session queue is empty. |
| Search for `maps:get/3` | tutorials 1; others 0 | 0 in every topic | One tutorial remains in the filtered view. |
| Queue that tutorial | tutorials 1; others 0 | tutorials 1; others 0 | The visible row's key is in the existing queue. |
| Show queued articles | tutorials 1; others 0 | tutorials 1; others 0 | The topic comparison follows the same filtered result set. |
| Search for unmatched text | 0 in every topic | 0 in every topic | The view is empty even though the session queue still contains one article. |
| Reset filters | tutorials 11; languages 2; announcements 2; news 1 | tutorials 1; others 0 | All rows return; the existing task keeps its queue across filter reset. |
| Undo the last queue batch | tutorials 11; languages 2; announcements 2; news 1 | 0 in every topic | Undo restores the prior queue without changing the current view. |

The example uses a native table for exact values and a restrained horizontal bar
for each visible count. Every bar starts at zero and uses the same 0–16 article
reference. The table remains understandable if the bars or color are absent.
The bar is hidden from the accessibility tree because its value is already
present in the table cell; the caption, headers and row labels carry the
comparison. The summary has its own compact sizing so the article table can
retain its useful horizontal scroll on small screens.

### Source decisions for this example

[Carbon Core's data-table guidance](https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines)
supports organizing records with task-relevant row and column meaning, clear
table content and enough room for dense information. This example adapts those
ideas to its existing native table, narrow summary and article task. Carbon's
component row-height presets, grid placement, action limits and hover-based
truncation rules belong to its component system; they are not requirements for
this standalone reading desk. Long article titles wrap, and the summary has no
toolbar, sorting or batch-action redesign.

[Spectrum 2's type guidance](https://spectrum.adobe.com/foundations/typography/applying-the-type-system)
recommends tabular lining figures and right alignment for comparable
component/table numbers. The example adapts that numerical hierarchy and
alignment while keeping the system font, exact text values and current identity.
It does not import Adobe Clean, Spectrum's type sizes or its native platform
styles. [CSS Fonts Level 4 §6.7](https://www.w3.org/TR/css-fonts-4/#font-variant-numeric-prop)
defines the CSS feature request; the specification explains that an unsupported
font feature has no effect. A declaration therefore does not establish actual
glyph support or rendered alignment.
