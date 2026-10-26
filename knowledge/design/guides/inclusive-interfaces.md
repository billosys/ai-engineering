# Inclusive interfaces across languages and scripts

Adapt a real task for the language and writing system people will use. Begin
with the task, content, audience, input methods and delivery context; name the
locale and script in scope. Treat each adaptation as a design and language
decision that needs checking, not a mechanical mirror of the original screen.
This guide offers a bounded method, not a preset palette, translation system,
or claim that one language example covers other locales or scripts.

## Set language and direction in markup

Declare the page language and its base direction on the root `html` element,
for example `<html lang="ar" dir="rtl">` and `<html lang="en" dir="ltr">`.
Language identifies the text; direction establishes its base flow. Keep both
explicit. Use `lang` on a phrase whose language differs from the surrounding
text, and use `dir` when its direction is known. Avoid using CSS to declare a
document's direction.

When a value's direction is not known until someone enters it, give its input
`dir="auto"`; isolate the value when it appears inside another sentence with
`<bdi dir="auto">`. For a known opposite-direction phrase such as an email
address, identifier or reference code, tightly wrap just that phrase in a
`bdi` or `span` with its known `dir`, usually `ltr` for these examples. Keep
surrounding punctuation outside the isolated value. Preserve that nested
markup when moving an error message into a summary or status; copying only
plain text can discard the direction boundary.

Use real language links with `lang`, `dir` and the appropriate `hreflang`
where useful. Make the current language visible and programmatically
identifiable. Explain what navigation does to the current task: a full page
change clears unsaved fields unless the design explicitly transfers them.
When recovery is supported, tell people to save first and restore deliberately
after switching. Do not silently autosave or put form values in a URL to make
language navigation appear seamless.

## Keep the task and its values coherent

Translate the instructions people need at each state: labels, requirements,
hints, field errors, error summaries, pending work, service failures, retry,
draft recovery, confirmation and no-script content. Keep the same meaningful
task and explain the same consequences in every supported language. A language
reviewer should see the actual rendered specimen and source wording, including
less common failure messages, rather than a sample sentence alone.

Separate display wording from submitted values. Keep machine values stable when
labels change; for example, a localized time option may display “صباحا” while
retaining the value `am-101`. If a confirmation needs an example code, render
the code as its own labeled value instead of embedding or parsing it from a
translated option label. Localized digits may help people read a count while
the stored value remains the stable ASCII string `3`; isolate a mixed-direction
code or number where the surrounding sentence needs it.

Use native controls and preserve their DOM order unless the task evidence calls
for a different sequence. Right-to-left direction changes inline flow and
alignment, but does not mean the interaction order should be reversed. Let
logical CSS properties such as `margin-inline-start`, `padding-inline`,
`border-inline-start` and `text-align: start` follow the declared direction.
Avoid left/right offsets, row reversal or mirrored icons unless a specific
control's meaning and observed use justify them. Keep focus order aligned with
the visible task sequence.

## Check real strings in the target

Use actual labels, examples and mixed-script values while composing. Check the
glyphs and shaping supplied by the available font and fallback chain; a source
file cannot show whether every target device has the needed glyphs or shapes.
Do not add tracking to connected Arabic letterforms as if it were an English
uppercase treatment. Inspect headings, labels, options, errors and longer
content after translation, because their relative length and wrapping may
change. Adjust the composition to fit the content rather than shrinking text
or clipping it to preserve a screenshot.

Review the task in both language routes and exercise the likely direction
boundaries: a name containing Arabic and Latin text, an email address, a code,
digits beside translated text, punctuation, errors and confirmations. Test
keyboard focus, native controls, link destinations, narrow and wide viewports,
and enlarged text or a clearly identified text-expansion fixture. If the task
has saving or recovery, check the documented transitions in each language and
state which entries are replaced, retained or cleared.

Include the input methods people are expected to use. A keyboard check does
not establish that speech, switch or other alternate input can identify and
activate the same controls; check the actual method and its names, sequence and
feedback where it matters to the task.

For a form or other multi-step task, check the cognitive load of the content as
well: use familiar words, keep each instruction concise and grouped with the
relevant control, and make the next action and its consequence visible. Do not
make someone rely on memory to correct an error; preserve valid entries and
explain what remains, what changed, and how to continue. Explain data loss
before a navigation or timeout can clear work. These are review questions to
apply where the task needs them, not an extra template or a promise of
cognitive usability. The [W3C COGA Working Group Note](https://www.w3.org/TR/coga-usable/)
offers supplemental patterns, including succinct text (§4.4.5) and avoiding
data loss and timeouts (§4.5.9); it is guidance beyond WCAG requirements and
does not establish WCAG conformance. Evaluate the actual task with relevant
participants when making claims about cognitive usability.

Bring a knowledgeable speaker of the target variety into review of the actual
labels, instructions, errors and outcomes. Record which specimen and states
they reviewed, their corrections, and any unreviewed wording. Study, preference
or a fluent-looking automated draft is not a substitute for that review. A
browser check can establish behavior for its tested engine and inputs; it does
not establish natural wording, native keyboard input, assistive-technology
quality, behavior in other engines, or accessibility conformance.

## Filled example: a fictional library visit

The [language-and-direction text case](using-the-skill.md#language-and-direction)
records how the English and Arabic right-to-left versions ask for the same name, email, visit
window and visitor count. They use the same stylesheet, JavaScript, field IDs,
stable option values and explicitly saved session draft. The pages declare
`en`/`ltr` and `ar`/`rtl`; the language links navigate between them and warn
that unsaved entries will clear. A person can choose Save before switching,
then Restore on the other page. Restore remains explicit and replaces all four
current fields.

The Arabic page displays localized options such as “صباحا” and “٣ زوار” while
retaining `am-101` and `3`. The confirmation labels the example reference
separately and renders `AM-101` in an LTR-isolated value. The entered name uses
automatic direction detection; the email and reference use known LTR
isolation. Static page messages supply the Arabic wording and nested isolation
markup to the shared script, including the error summary and draft feedback.

The example is fictional and sends no request. In root's Chromium review, the
Arabic and English form routes were exercised; layout was observed at 390px and
1280px, and the Arabic error view was checked with authored 32px text and a
separate repeated-label expansion fixture. The English shared-code functional
regression was checked at 390px. These observations do not mean that every
state was crossed with every width or fixture. The review used tool-entered
Arabic, not a native Arabic IME. The Operator separately reviewed the
unchanged Arabic example wording and said, “Reviewed: suitable for this
example”; that verdict does not cover changed text or another service.
Assistive technology, native zoom, other browser engines, real-user research
and accessibility conformance remain separate evidence needs. This one Arabic form does not establish
coverage for other dialects, calendars, scripts or services.

## References

- [W3C: Structural markup and right-to-left text in HTML](https://www.w3.org/International/questions/qa-html-dir.en.html)
- [W3C: Inline markup and bidirectional text in HTML](https://www.w3.org/International/articles/inline-bidi-markup/)
- [W3C: Making Content Usable for People with Cognitive and Learning Disabilities](https://www.w3.org/TR/coga-usable/) (Working Group Note; supplemental guidance)
