# Interaction and Content

Design an interaction as a connected route through meaningful content, tasks,
actions and states. Start with what people need to find or change. Then decide
which interface elements make that work possible, what each state communicates,
and how people can continue, recover or leave.

This method complements [From a Brief to a Revised Design](design-workflow.md)
and [Layout](layout.md). It helps with search, forms, filters, navigation,
selection and other content-bearing flows. It is a design aid, not a widget
specification or an accessibility-conformance test.

## Design a form through its outcome

Choose fields because each one enables the task, give each control a visible
label and useful instruction, and decide how invalid input, pending work,
service failure and completion affect values and focus. The [Forms and
recovery](forms-and-recovery.md) method applies these choices to the illustrative
[library visit text case](using-the-skill.md#forms-and-recovery). Its simulated
completion is not evidence about a real service.

## Model the content before the controls

Name the content entities the interface presents or changes. For each one,
record the attributes people need to recognize, compare or act on. State how
entities relate and which relationships are navigable. Use the real nouns and
values where they are available; mark assumptions and missing content.

| Content question | Design consequence |
|---|---|
| What is one item: an article, person, product, message or result? | Choose a unit that can be named, previewed and acted on consistently. |
| Which attributes identify or distinguish it? | Show enough title, summary, date, category or other context for the task. |
| Which items relate, and how? | Make those relationships visible through labels and destinations. |
| Which values can be absent, long, repeated or unfamiliar? | Decide how the actual content wraps, truncates, sorts or explains itself. |
| Which content is unavailable or stale? | Give it an honest state and a useful next action when one exists. |

Do not let a card shape define the content model. A result, for example, may
need a title, excerpt, category and destination even if the visual treatment is
plain text. Keep identity and hierarchy understandable when imagery, colour or
position is unavailable.

## Turn tasks into actions and transitions

Write each important task as an outcome: “find an article about X,” “change a
filter,” or “return to the topic.” Identify the action that advances it and the
content it needs. For each action, name the prior state, resulting state, visible
feedback and a way to continue. Include cancel, clear, back or retry when the
flow actually supports them.

A transition table makes missing steps visible before selecting controls:

| From | Action | To | Feedback and next step |
|---|---|---|---|
| Ready | Submit or change a query | Loading | Preserve the query; signal that work is underway. |
| Loading | Results arrive | Results or empty | Announce the outcome and expose the next useful action. |
| Any editable state | Clear or reset | Ready | Show that the value and dependent content were cleared. |
| Error or interruption | Retry, revise or leave | Loading, ready or previous route | Explain what happened and keep a usable recovery path. |

This is a prompt for design decisions, not a claim that every product has these
states. If loading is imperceptible, a persistent loading panel may be worse
than no indicator. If a failure has no safe retry, do not invent one. Describe
what the system actually does and what remains to be designed.

## Assign state, semantics and focus

For each state, decide who owns the value and who owns its visible status. A
field may own the current query, while a results component owns the result list
and a concise status message reports a changed count or empty outcome. Avoid
competing announcements or a second visual value that can drift from the real
control.

Use controls whose native role matches the action: links navigate, buttons
perform actions, and form controls accept values. Provide a visible label or a
programmatic name that stays associated with the control. Placeholder text can
show an example, but should not be the only name. The [WAI Forms Labels
tutorial](https://www.w3.org/WAI/tutorials/forms/labels/) explains label
associations. For dynamic feedback, review the [WAI status message
technique](https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA22.html); use a
status role only when its announcement behavior fits the update.

Choose a keyboard order that follows the visible task. After a result update,
keep focus in place unless the user requested navigation or a move is necessary
to complete the task. Do not autofocus a page-level search field simply because
it exists. Preserve native arrow, Enter, Escape and clear behavior when the
component provides it, and check the real route through an actionable item.

A URL can make a view repeatable and shareable. Decide which state belongs in
it, how empty values behave, and whether edits create history entries. Keep
unrelated path, parameters and fragment state when updating one query. Make
reload behavior and Back behavior part of the interaction decision, then verify
them in the browser; do not infer them from a URL string alone.

## Design the state vocabulary

The labels below are prompts for review. A product may combine or omit states
when that reflects its actual behavior.

| State | Decide what people need to know | Useful question |
|---|---|---|
| Ready or idle | Current value, available action, scope | Can someone begin without guessing what is accepted? |
| Loading | That work is underway, if delay is noticeable | Can the current task continue, or should duplicate actions wait? |
| Results | Count or scope, item identity, available actions | Can someone distinguish a relevant item and reach it? |
| Empty | What was searched or selected and why nothing is shown | Can someone revise the value or clear the constraint? |
| Error | What failed and what remains safe | Is retry available, or is another route needed? |
| Interrupted | Whether work or input was retained | Can the person resume, check status or leave safely? |

Empty and error are different: a completed request with no matches is not a
failure. Keep the query visible when revising it is useful. Use plain, specific
language and pair a status with the relevant control or content. If a result
count changes dynamically, determine whether and how it is announced; visual
text alone does not establish announcement behavior.

## Components do not make a complete flow

A search box may accept text but provide no useful results, URL behavior, clear
route, loading feedback or recovery. A menu may expose links but leave the
current location unclear. A form field may have a label while its error and
success transitions remain unspecified.

For each supplied component, inspect its supported attributes, events, focus
rules and status behavior in primary documentation or source. Treat those as
component capabilities. Separately design the surrounding task: what content is
queried, how changes are submitted, what URL state persists, how results are
identified, where keyboard focus stays and which failures can be recovered.
Do not add private properties or synthetic events when a documented public API
exists. If the API does not cover the needed transition, record the gap before
choosing an adapter or replacement.

## Worked example: LFE blog search

This example applies the model to the isolated LFE search route. It is grounded
in the source and CDC's browser observations. It does not report user research
or assistive-technology testing.

### Content and tasks

| Content or task | Current reading |
|---|---|
| Entity | An indexed blog page: an article, tag, archive, category or blog landing view. |
| Useful attributes | The actual page title and visible excerpt; title and page type help distinguish the destination. |
| Relationship | A result links to its indexed destination; an article, tag or archive view can lead to related blog content. |
| Find task | Enter a query, inspect the matching pages, and open a useful destination. |
| Continue task | Return from an article or index view with the query and results available. |
| Clear task | Clear the search and remove its query from the URL while preserving other view state. |
| Assumption | Search visitors may arrive from a bookmark or shared link; this was not researched with visitors. |

### Observed transitions and decisions

| Before → after | Browser observation | Design decision |
|---|---|---|
| Open `?q=rebar3` → results | The actual input contained `rebar3`; the summary reported 15 results. The first result was `Tag: rebar3`; results also included an archive, category and Blog views, plus LFE and rebar3 articles. Reload restored the query and results. | Hydrate the real field and make the URL a repeatable search state. Verify the field, summary and destinations, not a component attribute. |
| Type `LFE & rebar3` → updated results | The URL encoded the ampersand and reloaded as the same plain-text query. | Preserve user text and let URL encoding handle reserved characters. |
| Clear → ready | The field emptied and `q` was removed. A whitespace-only query also removed `q` while preserving `view=example` and `#content`. | Treat blank input as no search; update only the query parameter. |
| Search exact phrase `"qyvxjzkwmptn"` → empty | The page showed “No results” and no result links. | Give a completed empty outcome its own state. Do not call every unfamiliar query empty: the unquoted arbitrary phrase returned a Docker result under the vendor search behavior. |
| Search → keyboard result → destination → Back | ArrowDown moved from input to a tag and then to actual LFE/rebar3 article results; Enter opened an article; Back restored the URL, field and results. | Preserve the component's keyboard route and make return to the task possible. |
| 390px / 1280px → readable search | At 390px the corrected section and page fit the viewport; field and titled results were visible. At 1280px the centered section fit within the page. | Constrain the search section to its available width while retaining the site's spacing and readable result text. |

The search field used the component's existing associated label. The page did not
autofocus it; after reload, focus remained on the body. The observed states used
the existing Pagefind field, summary and results components. These observations
support this case only. The query adapter used the documented instance search
API and URL history replacement; the browser checks above verify the listed
outcomes, not all possible URLs or failure conditions.

### Still to check

The recorded checks did not exercise a live indexing or network error, retry,
assistive technology, native browser zoom, another browser engine or a visitor
study. They do not certify accessibility conformance. Before extending this
pattern to another site, inspect its component API and content, test its own
empty and failure routes, and verify labels, dynamic status announcements,
keyboard behavior and reflow in its target environment.

## Worked example: LFE reading desk

The [reading-desk text case](using-the-skill.md#dense-comparison) summarizes a
small local task over the published LFE source snapshot, pinned at revision
`1a64666cd7273ee97380bff163ed7642d13356df`.
It lists the 16 most recent non-draft posts by publication date, with each
post’s title, explicit permalink, publication date and first frontmatter
category. The native table caption names the collection; column and row headers
identify each value and article. The Select checkbox sits beside its article
and has a name derived from that title. This is a simple data table, so it uses
native table structure rather than grid roles or custom keyboard navigation.
See the [WAI Tables Tutorial](https://www.w3.org/WAI/tutorials/tables/) for
caption and header relationships. For a compact group comparison that follows
these filters and queue states, use [Dense data and comparison](data-and-comparison.md).

The permalink is the stable key for identifying an article. Queue membership,
filters and checkbox selection are separate, in-memory task state. The example
does not copy article bodies, infer publication status from a URL, verify an
article’s contents, or change the source site. The displayed records form a
pinned snapshot; the task state resets on reload and is not sent anywhere.

| Transition | State decision |
|---|---|
| Type a title or topic filter, or change All / Available / Queued | Clear every checkbox selection before showing the new result set. Report that selection was cleared; never carry a hidden choice into a later batch. |
| Queue selected visible articles | Apply the action only to checked rows that are currently visible. With no visible selection, preserve queue state and the one-step undo and explain how to continue. Adding an already queued article is idempotent. |
| Queue one or more new articles | Save the queue state from immediately before that changing batch, then add the selected keys and clear selection. The next changing batch replaces this single undo snapshot. |
| Queue only already queued articles, change a filter, or attempt an empty action | Do not replace the snapshot. Keep the no-change outcome distinct from an empty filter result. |
| Undo the last changing batch | Restore its prior queue set without selecting rows. Keep the current filter and selection; if no snapshot exists, say there is nothing to undo. |
| Reset filters and selection, or reload | Reset clears filters and checks but keeps the in-session queue and undo. Reload clears all in-memory task state, as the visible explanation promises. |

The table rows and controls remain in place while filtering and queue status
change. This avoids replacing a focused checkbox or action button. A concise
status message reports each result; the example makes no claim that a screen
reader announced it. On narrow screens, Select and Article remain adjacent, the
long title wraps, and the remaining columns can be read by scrolling the
focusable table region. At a wide viewport all columns are visible together.

The independent browser check exercised a 390px viewport, a 1280px viewport,
an authored 32px root-text fixture, and a native keyboard batch: select two
articles, move to Queue, and activate it. Focus remained on the action button.
The authored text fixture is not browser zoom. The observed browser used its
dark preference; a separate forced-light palette fixture checked the light
control boundary, not an operating-system preference switch. These checks do
not cover assistive technology, other browser engines, user research, network
or live indexing failures, a real backend, or accessibility conformance.
