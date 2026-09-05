# Upstream Ticket Workflow

This guide owns the practical workflow for drafting, checking, filing, and
retaining upstream contribution tickets. Load it after
[01-contribution-style.md](./01-contribution-style.md) when the task is no
longer "what should this sound like?" but "how do we produce the artifact?"

The reusable authoring skeleton remains the package-local
[CONTRIBUTION-TICKET.md](../templates/CONTRIBUTION-TICKET.md) template. This
guide explains how to use it; the template remains the copyable artifact.

## Ticket Spine

Every ticket has four moves, regardless of whether it is a confirmed bug,
additive feature request, documentation fix, or unconfirmed question.

1. Open with warmth and a single-sentence reason for writing.
2. State the situation specifically, close to the maintainer's files, lines,
   examples, or observed behavior.
3. Make the next move cheap: a reproduction, proposal, suggested wording, or
   settling experiment.
4. Close without pressure on shape or timing.

The middle changes by ticket shape, but the spine does not.

## Local Drafts

Draft locally first, one ticket per file. Use a project-side `issues/`,
`docs/upstream/issues/`, or similar directory and confirm the location with the
operator on the first ticket of a project. The project-wide default for
upstream contribution drafts remains deferred to the project-management
maintenance surface.

Name the file after the ticket:

```text
NN-<kind>-<slug>.md
```

Examples:

```text
01-bug-coremidi-virtual-sysex-256-cap.md
02-feature-raw-midi-bytes-door.md
03-doc-fix-null-return-contract.md
04-question-webmidi-timestamp-normalization.md
```

The on-disk file is the canonical authoring source. The tracker is the public
conversation; the local file is the artifact you can re-read, revise, and use
as a voice reference later.

## Header And Paste Boundary

Keep the local operator header as a blockquote at the top of the file. It
stores the title suggestion, label suggestions, line-reference baseline, and
filing note for the operator. It is not intended for the maintainer.

The `---` separator below the header is mandatory because it marks the tracker
paste boundary. When filing the issue, strip the blockquote header and paste
only the body below the separator.

For an unconfirmed question, use the draft header shape from the template. The
header should make the uncertainty explicit and preserve the operator's choice
to file as a friendly question or hold until reproduction turns it into a
confirmed bug.

## Line References

Use file-line references in the body, including ranges when the relevant
evidence spans multiple lines. Re-check line references against current `HEAD`
immediately before pasting. The header's "worth a quick re-check" wording is a
courtesy to the operator, not permission to post stale evidence.

Quote relevant code in fenced blocks. Keep snippets to the minimum that shows
the issue or proposed shape.

## One Ticket Per Problem

Do not bundle several problems into one issue. Bundled tickets fragment the
discussion, accept ambiguous closure, and rot in backlog. If you find three
problems, draft three tickets and cross-link them where the relationship
matters.

Cross-link related tickets by URL after they are filed. If a ticket depends on
another or becomes easier because of another, say that explicitly. Do not leave
the relationship implicit.

## Shape-Specific Workflow

For a confirmed bug, include what is happening, how to see it, what happens
today, and what behavior would be better. Keep the reproduction minimal.

For an additive feature, include the proposed capability, the smallest useful
shape, the existing project pattern it aligns with, and the semantics you
would be counting on.

For a documentation fix, keep the mismatch and suggested wording close
together. A doc fix should not be harder to read than the patch it proposes.

For an unconfirmed question, state what you read, why it raises the question,
what would settle it, and why you are not claiming a confirmed bug.

## Template Use

Start from [CONTRIBUTION-TICKET.md](../templates/CONTRIBUTION-TICKET.md), pick
one of the four shapes, and delete what does not apply. The template carries:

- the local blockquote header;
- the paste boundary;
- the shared ticket spine;
- calibrated-honesty reminders;
- the four shape variants;
- the filing workflow checklist.

Keep the template reusable. If a project needs a one-off ticket, create the
draft under that project's chosen issue-draft directory; do not edit the
template into the one-off ticket.

## Filing Checklist

Before filing:

1. Confirm the ticket is one problem.
2. Re-check file-line references against current `HEAD`.
3. Confirm confidence claims match what was actually verified.
4. Strip the blockquote header and keep the body below `---`.
5. Apply labels and title from the header, adjusted for the tracker.
6. Cross-link related filed tickets by URL.
7. Keep the local draft as the canonical authoring artifact.
