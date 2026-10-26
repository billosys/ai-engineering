# Use the Visual Design Skill

Start with **task → small brief → focused method → alternatives → actual
check → revision**. The skill is a set of portable Markdown methods and cases;
using it does not require this repository, an artwork bundle, a running example
app or the complete research corpus.

For a small brief, note only what could change the decision: who will use the
work and for what task, which content and supplied identity must remain, the
relevant reading conditions, language or input, and any consequential
unknowns. Separate source facts from assumptions. Pick the focused method below,
write down a plausible alternative, check the actual content or implementation
against the task, and revise the proposal where the check exposes a mismatch.

Research is optional and question-led. Confidence that a source was extracted
correctly does not verify every present-day claim. A historical excerpt is not
current setup advice, and unresolved fidelity to an original source is not a
completed review. For a consequential factual claim, consult relevant available
primary support and keep its scope visible; do not make routine skill use depend
on acquiring or loading the full research corpus.

## Editorial reading

**Task.** Help someone read a passage while keeping useful context close enough
to interpret it.

**Small brief.** Record the passage, its source and date, the reader's purpose,
the supplied type and identity, and whether contextual notes need to remain
beside the passage. A historical excerpt can illustrate reading choices, but
does not become current product or setup guidance.

**Focused method.** Use [Compose editorial hierarchy for the reading task](type.md#compose-editorial-hierarchy-for-the-reading-task): assign distinct roles to title, author/date, body, code, attribution and contextual note; retain one meaningful source order; compare arrangements with the same content.

**Alternatives.** A focused reading column can place context after the passage;
a wider composition can place context alongside it. The first keeps the
argument continuous; the second keeps explanation near the passage it
interprets. Neither arrangement is a universal reading measure.

**Actual check.** Review the same excerpt in both arrangements at the available
reading width, with enlarged text and spacing. Check hierarchy, wrapping,
measure, relation between note and passage, and source order. The earlier LFE
runtime study recorded a real 2016 excerpt and two arrangements; this text case
does not claim that a Markdown rendering was browser-tested or more readable.

**Revision.** If two columns crowd the text or separate a note from its passage,
stack them while preserving the meaningful order. See the optional [LFE
homepage workflow case](examples/lfe-workflow.md) for a separate, source-bounded
example of alternatives, critique and revision.

## Dense comparison

**Task.** Choose articles for a reading session while seeing which topics are
present in the current view and already queued.

**Small brief.** The retained LFE snapshot contains 16 published articles:
11 tutorials, 2 languages, 2 announcements and 1 news. These counts describe
that snapshot, not all LFE posts or reader behavior. A queued-in-view count is
the intersection of visible records and the existing session queue.

**Focused method.** Follow [Dense data and truthful comparison](data-and-comparison.md): use complete records, stable group labels and exact values; derive the summary from the same filtered view and queue as the table.

**Alternatives.** Use an exact table with a shared 0–16 reference and restrained
bars for quick comparison. A story-sized heading or image gallery would spend
attention away from repeated values and task status; percentages add little to
this small snapshot.

**Actual check.** Reconcile all four topic totals to 16, then follow the real
state transitions: filter, queue one visible item, show queued items, enter an
unmatched query, reset, and undo. At an unmatched query the visible rows and
queued-in-view values are zero even while the session queue still contains one
article. An empty view is not an empty session queue. The existing runtime
observation tested these distinctions; this text case records them without
claiming a new runtime execution.

**Revision.** If the summary follows hidden records or treats an empty view as
an empty queue, derive it from the current visible set and queue intersection.
See [the full reading-desk method](data-and-comparison.md#worked-example-lfe-reading-desk)
for the recorded transition table and evidence limits.

## Forms and recovery

**Task.** Let someone make a fictional library visit request, recover an
interrupted draft deliberately, and understand that a local demo sends nothing.

**Small brief.** The specimen has four required fields: Name, Email, Visit time
and Visitors. Its sample inputs are fictional, and completion is local to the
example; it is not a live booking or service policy.

**Focused method.** Use [Forms and recovery](forms-and-recovery.md) to keep
validation errors, service unavailability, successful local completion and
interrupted work as distinct states. Saving, restoring and clearing are
separate, explicit actions. Explain where the example stores a draft, what
Restore replaces and the limits of browser storage.

**Alternatives.** Keep the example's unsaved entries in the current page and
offer explicit Save/Restore/Clear actions when interruption recovery is useful.
Do not autosave by default or present a local confirmation as a service result.
For a real service, its owners must decide whether this storage and recovery
policy fits the task and deployment.

**Actual check.** Exercise missing, malformed and expired drafts; confirm that
rejected restores leave current fields and stored bytes untouched. Check
pending, unavailable, retry, completion and draft-cleanup failure separately.
Earlier browser checks covered the stated specimen and conditions, including
English and Arabic routes; they do not establish real storage policy,
assistive-technology behavior or service behavior.

**Revision.** Keep Restore explicit and no-clobber on failure. Preserve a
confirmed completion if cleanup fails, and tell the person that a draft may
remain. For the complete fictional state sequence and limits, see the [form
recovery method](forms-and-recovery.md#worked-example-a-library-visit-request).

## Image composition

**Task.** Guide a reader through an image-led collection while preserving the
subject, the article path and a useful at-rest experience.

**Small brief.** Identify the image's role, the subject region that must remain
visible, its relation to the article, and what should happen if the image or
stylesheet is unavailable. Keep the project's supplied identity and image
source in charge; this skill package does not ship the LFE artwork.

**Focused method.** Use [Image Composition and Accessible Exploration](image-composition.md)
to choose the frame, crop, alternative text, caption and links from the image's
meaning in context. These have different jobs: alternative text conveys the
image's relevant meaning, a caption relates it to the story, and a link name
describes its destination or action.

**Alternatives.** A prominent crop can suit an atmospheric lead image when its
important subject remains visible. Keep a technical diagram whole when labels
or relationships matter; provide a nearby text explanation instead of cropping
away information. Secondary illustrations can retain their full proportions.

**Actual check.** Inspect the subject at each intended frame, the image's
alternative and caption separately, article and full-image links, focus and
return paths, and the page with missing images and without styling. The prior
LFE collection review kept the luminous opening in its cropped lead image,
and retained the secondary illustrations' proportions. Those are retained
observations of that specimen, not a new image inspection here. The warning
against cropping a labeled graph is a methodological counterexample: labels
and relationships may carry essential information. No crop experiment on such
a graph is claimed.

**Revision.** Change the frame or focal position if the subject is lost; provide
an ordinary full-image link where a crop removes context. Keep headings,
summaries, dates and article links useful when images are absent. If motion is
offered, make it optional and finite: the earlier collection kept navigation
and focus immediate, left a static arrival marker at rest, and used a one-shot
450 ms cue only after opt-in. That is a specimen parameter, not a comfort rule;
the reduced-motion preference takes priority. See [Purposeful motion](motion.md)
for the method and its limits.

## Language and direction

**Task.** Adapt the same fictional library visit task for English left-to-right
and Arabic right-to-left reading without changing the meaning of entered values.

**Small brief.** Keep the forms' field IDs, option values and shared behavior
coherent across language versions. The retained pages declare `en`/`ltr` and
`ar`/`rtl`; no new translation is proposed in this text case.

**Focused method.** Follow [Inclusive interfaces across languages and scripts](inclusive-interfaces.md)
and the form's [recovery method](forms-and-recovery.md). Language direction is
declared on the page. Use automatic direction for a person's name where its
script may vary; isolate known left-to-right email and reference values.

**Alternatives.** A whole page can use its language's base direction while
individual mixed-script values keep their own direction. Do not mirror
everything mechanically: names, dates, numbers, icons and controls need review
in their actual context.

**Actual check.** Check labels, errors, status and recovery wording with a
qualified language reviewer, and inspect the real script, mixed-direction
values, expanded text and focus order in the target. The Operator's existing
Arabic wording verdict applies only to the unchanged illustrative wording.
Prior Chromium checks used tool-entered Arabic, not a native Arabic keyboard;
they do not establish native input, other scripts, assistive technology or
conformance.

**Revision.** Correct wording only with appropriate review. Keep page direction,
automatic name direction and known LTR value isolation scoped to their roles;
do not infer that one example covers other dialects, calendars or scripts.

## Supplied identity

**Task.** Change an existing semantic link and focus intent across a supplied
light/dark system while keeping a component-specific code treatment intact.

**Small brief.** The retained LFE example owns its name, values, public role
names, modes and code component. Preserve those boundaries; this is not a
default palette or token architecture for another project.

**Focused method.** Trace ownership and consumers with [Semantic system
evolution](system-evolution.md), then use [Migrate a Semantic Design System
Between Owners](system-migration.md) for a receiving-owner contract and
rollback. The [filled LFE handoff](examples/lfe-system-handoff.md) records the
separate implementation projection and limits.

**Alternatives.** In the accepted local change, the ordinary `--lfe-link` and
`--lfe-focus` roles alias a mode-local `--lfe-interactive-accent`. The code
component keeps its separate `--lfe-code-link` and `--lfe-code-focus` values.
Replacing every gold value would erase an intentional exception, so the
system-wide replacement was declined.

**Actual check.** Compare resolved light and dark consumers, normal and
keyboard-focus states, and the code exception. Check the source projection
against the actual owned declarations and inspect the target before integration.
The accepted observation recorded light `#624900`, dark `#f0d477`, and unchanged
code `#e9ca66` on its dark code surface; it did not claim a token-format
round-trip or a new browser run.

**Revision.** Change only the owned aliases, preserve the code roles, and give
the receiving maintainer a bounded review and rollback path. See the [LFE
workflow case](examples/lfe-workflow.md) for the supplied homepage identity and
the [LFE semantic handoff](examples/lfe-system-handoff.md) for the migration
record.
