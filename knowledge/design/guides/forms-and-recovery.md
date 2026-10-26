# Forms and recovery

A form is a route through a task, not a list of fields. Begin with what a person
is trying to do and what information the service needs to respond. Ask only for
information that serves that task. Mark a field required only when the service
cannot complete the request without it, and explain any requirement that may
not be obvious. Use optional fields sparingly and say when they are optional.
When adapting recovery from another system, use [Patterns and contextual
adoption](patterns-and-adoption.md) to check task fit, evidence and the next
owner before carrying a local choice into a service.

## Name and explain each field

Use the control that matches the value and action: a text input for a name, an
email input for an email address, and a native select when a person chooses
from a short, fixed set. Associate every control with a visible label. Put
format rules, examples and reasons beside the relevant control as instructions;
a placeholder can offer an example but cannot replace the label. Group related
controls with a `fieldset` and a concise `legend` when that relationship helps
someone understand the request. The [WAI labels tutorial](https://www.w3.org/WAI/tutorials/forms/labels/)
covers explicit label associations and predictable label placement.

Use familiar words for choices. Keep each option's internal value stable when
its visible wording may need translation or revision. Show enough context to
distinguish similar choices. Do not ask for sensitive or identifying details
just because the form could accept them.

## Explain and locate errors

Validate after submission or at another deliberate point in the task. Choose
when to validate based on the consequences of an error and the person's ability
to correct it; do not make a live error appear on every keystroke by default.
Keep valid entries when another field needs correction.

For each invalid field, explain what needs attention and how to fix it. Mark the
control invalid and associate the message with it while retaining any existing
hint association.
When a submitted form has multiple errors, put a short summary before the fields.
Name each affected field in the summary and link its message to that control.
After submission, move focus to the summary so it is encountered before the
form; activating a summary link should focus its actual field. Do not rely on
red text or a border alone to communicate an error. The [WAI notifications
tutorial](https://www.w3.org/WAI/tutorials/forms/notifications/) describes
overall and inline feedback, linked error lists and field-message associations.

## Keep validation and service failure distinct

An invalid value means the form cannot yet make a useful request. A service
failure means the request could not be completed after the values were accepted.
Give these states different messages and next steps. For a recoverable service
failure, keep the entered values, restore usable controls and explain whether
retry or revision is available. Do not call a failed request successful or
promise that retry is safe unless the service contract supports it.

If a submission takes long enough to matter, show that work is underway. Decide
which controls need to be unavailable while it runs and prevent duplicate
submissions. Focus a meaningful status when disabling a control would otherwise
leave focus unclear. On a service response, explain the outcome and put focus
where the person can continue. A heading that names completion or a retryable
failure can serve this purpose; do not trap keyboard focus.

For a real service, client-side checks improve feedback but cannot establish
that the request is accepted, authorized, available or stored. The server owns
those decisions. Confirmations should reflect the actual server result, and
research or service-owner review should establish that the questions, required
fields and choices fit the service. A prototype, local simulation or code review
does not provide that evidence.

## Recover interrupted work deliberately

Offer draft recovery only when the task benefits from it. Separate Save,
Restore and Clear actions from form submission; do not save every keystroke by
default. Explain where the draft is held, what can access it, how long the
example will accept it, whether it can be unavailable, and what Restore will
replace. Use fictional or non-sensitive content in a prototype.

Read and validate the complete draft before changing any field. Check its
shape, field types, known option values and age. Preserve raw incomplete values
when saving, and state a size limit without silently trimming. A missing,
malformed, expired or unavailable draft should leave both current entries and
stored bytes untouched and offer a clear next step. Rejecting an expired draft
does not remove it; let the person explicitly clear only the example's own
entry. Report success only after the storage operation succeeds, and do not
claim that clearing guarantees browser-level deletion or private storage.

Keep Restore explicit after a reload. Disable Save and Restore while a request
is pending or after it completes if changing the request is no longer
available; a separate Clear action can remain available. If successful
completion also tries to remove a draft and that cleanup fails, keep the
confirmed outcome and report that the draft may still remain. Treat browser
storage as best-effort: browser policy, user clearing and session restoration
can affect whether or how long bytes remain, independently of the example's
own rule for accepting a draft.

## Worked example: a library visit request

The [library visit text case](using-the-skill.md#forms-and-recovery) records the
fictional form. It uses four required fields: Name, Email, Visit time and Visitors. Example values
to enter are Sam Reader, `reader@example.com`, Morning (reference AM-101) and 2
visitors. The example instructs people to enter fictional details and says
that it sends nothing. Because it requests a name and email, the example does
not establish that those details are nonsensitive or set a real service's
privacy policy. Unsaved entries clear on reload;
draft recovery is explicit. Its local completion is a simulation, not a booking
or service response.

| From | Action and result | What the example communicates and where focus goes |
|---|---|---|
| Ready with empty fields | Submit. | Show all four field errors and a summary above the form; focus the summary. Each summary link names a field and focuses its control. |
| Valid Name, Visit time and Visitors with an invalid Email | Submit with those values. | Retain every value. Show only the email error and keep its hint association. |
| All four values valid | Submit. | Capture the submitted values, disable the fieldset and submit control briefly, prevent duplicates and focus the pending status. |
| Pending with simulated unavailability enabled | Simulation completes with an error. | Restore the fields, retain the values, explain the retry action and focus the service-error heading. |
| Service error | Turn off the example's unavailable toggle and submit again. | Complete the local simulation and focus “Demo complete — nothing was sent.” The confirmation displays the captured values. |
| Confirmation | Choose “Change details.” | Reopen the form with its values retained and focus Name. |
| Incomplete form entries | Choose “Save draft.” | Save the four raw values by explicit action, even with a blank Visitors field or invalid Email. Do not trim or validate them as a submission. A serialized draft over 16,384 code units is rejected without replacing the previous saved value. |
| Saved draft after reload | Choose “Restore draft.” | Do not restore automatically. A valid draft replaces all four entries together, clears old form errors and focuses Name. The button description warns that current unsaved entries will be replaced. |
| Missing draft | Choose “Restore draft.” | Report that no draft was found and leave the current entries unchanged. |
| Malformed or older-than-24-hour draft | Choose “Restore draft.” | Reject it without changing current entries or removing saved bytes; offer Clear draft or saving the current entries. The 24-hour rule limits restoration, not storage lifetime. |
| Any current form state | Choose “Clear draft.” | Remove only this example's key and leave the current entries unchanged. If storage is unavailable, report that a draft may remain. |
| Valid request pending | Observe the draft controls, then let the simulation complete. | Disable Save and Restore while pending, leave Clear available, and try to remove the saved key after local completion. If removal fails, keep the completion and report that the draft may remain. |

These transitions and details are retained from the earlier runnable specimen;
this Markdown case does not execute a form. In that specimen, static form and
draft messages were kept in each language page's HTML separately from shared
behavior. Known-direction markup in those messages was cloned into the error
summary and status so mixed-script values kept their isolation. The draft used
a versioned record with a timestamp and the four field values in that tab's
`sessionStorage`; it did not autosave. Records older than 24 hours were
rejected but were not automatically removed. Stored values remained accessible
to same-origin scripts, and browser policy or session restoration could affect
storage lifetime. The storage-outage checkbox injected an error before browser
storage access; it did not test real quota or privacy policy.

An independent Chromium review at the runnable checkpoint saved and restored
incomplete fictional values across reload, focused Name after Restore, and
checked missing, malformed and 25-hour-old drafts without replacing current
entries. It also checked draft cleanup on completion, the unavailable-storage
notice, normal 390px and 1280px layouts, and an authored 32px text-size error
state at 390px. The malformed and expired values came from ignored reviewer
fixtures, not shipped example controls. These checks do not establish real
browser-policy or quota behavior, a real service, assistive technology, native
zoom, another browser engine, user research or accessibility conformance.
The [inclusive-interfaces guide](inclusive-interfaces.md) describes how to
adapt the task across languages and writing directions. The earlier runnable
[Arabic right-to-left form specimen](using-the-skill.md#language-and-direction)
and its English counterpart were recorded as sharing this behavior and draft
format. In those specimens, native language links navigated between pages,
cleared unsaved entries, left an explicitly saved draft available, and
explained how to restore it after switching. The Markdown cases preserve these
observations as text; they do not themselves run the form. The Arabic example
used localized labels and static status messages, `dir="auto"` for entered
names, and explicit LTR isolation for email and reference values. Root's
independent Chromium check at
`a349b0ccee1ba59b3834b3387d8e0427b3e7dd37`
exercised both language routes, Arabic errors and recovery, and an English
shared-code regression. It observed layout at 390px and 1280px, checked the
Arabic error view with authored 32px text plus a separate repeated-label
expansion fixture, and checked the English functional regression at 390px.
These observations do not mean every state was crossed with every width or
fixture. The Operator reviewed the actual Arabic page's labels, errors, draft
instructions/messages and completion: “Reviewed: suitable for this example.”
This wording verdict applies only to the unchanged illustrative text. Native
Arabic input, assistive technology, native zoom, other browser engines, user
research and accessibility conformance remain untested.
