# CONTRIBUTION-TICKET.md

> Authoring template for a single upstream contribution ticket (bug, feature,
> doc fix, or question). For voice, scope, and the disciplines this template
> rests on, read [`../docs/CONTRIBUTION-STYLE.md`](../docs/CONTRIBUTION-STYLE.md)
> first — that doc is the *why*; this file is the *shape*.
>
> Pick one of the four shapes below (they share a spine) and delete what
> doesn't apply. A short ticket is a feature; trim aggressively. Sections
> marked _optional_ are exactly that.

---

## Header block (top of every ticket, before the post itself)

This block lives at the very top of the Markdown file and is for the operator
filing the ticket — not the maintainer reading it on the tracker. Keep it as a
blockquote so the paste boundary is obvious. Drop it (or just don't paste it)
when posting to the issue tracker.

```markdown
> **Paste-ready GitHub issue.** Title suggestion:
> *"<concise, search-friendly title — start with subsystem if relevant>"*
>
> Labels you might want: `<label>`, `<label>`. Line references are against
> `<branch>` at `<short-SHA>` — worth a quick re-check against current HEAD.
```

For a question or speculative ticket that is **not** confirmed, replace the
first line with a calibrated marker:

```markdown
> **DRAFT — your call whether to file this yet.** This is reasoning from the
> source, not a confirmed bug. We've written it as a *question* on purpose.
> Two reasonable options: (a) file as-is as a friendly "have you run into
> this?", or (b) hold it until reproduction, then file a proper bug.
```

The `---` separator below the block is mandatory — it visually marks where
the paste-into-tracker text starts.

---

## 1. Body — bug / feature / doc / question (shared spine)

```markdown
Hey 👋

<One short paragraph: thanks for the project + the one-sentence reason you're
writing. If the maintainer has previously signalled openness to this kind of
change, quote them briefly. Friendly but not gushing.>

<Optional second short paragraph: who "we" are, in one or two sentences, only
if relevant to why this matters. If you're offering to do the work, say so
here in plain language — *"this is a feature request plus an offer to do the
work — happy to send the PR."*>
```

### What's going on  *(bug / question)*  **or**  What we'd propose adding  *(feature)*  **or**  The mismatch  *(doc fix)*

A few short paragraphs of the actual content. Stay close to the code:

- Reference specific files and lines as `` `path/file.h:LINE` `` (and a range
  when it spans, `` `:LINE-LINE` ``). The maintainer's tracker will not
  resolve these as hyperlinks, but they're searchable and unambiguous.
- Quote the relevant code in fenced blocks. Keep snippets to the minimum that
  shows the issue or the proposed shape — three to fifteen lines, not a wall.
- If a bug has more than one consequence, enumerate them — but keep the
  enumeration short and labelled with what the consumer experiences, not just
  what the code does.

> **Tone:** Describe the situation; don't litigate it. *"So if an `F8` shows up
> mid-SysEx, two things go wrong: (1) the clock is lost — it never gets
> delivered, so anything trying to stay in sync misses a tick; (2) the SysEx
> is corrupted."* — not *"this is a critical bug that breaks…"*

### How to see it  *(bug / feature acceptance)*

A minimal, reproducible recipe. Three or four numbered steps is plenty. State
what happens today and what the hoped-for behaviour is, side by side:

```markdown
1. Open a virtual source and a virtual destination in one process.
2. Send a 300-byte SysEx (`F0` … 298 data bytes … `F7`).
3. Watch what comes back.

Today you get `MM_ERROR` and nothing arrives. The hoped-for behaviour is the
full 300 bytes round-tripping through.
```

For a doc fix this section is usually unnecessary; skip it.

### A possible fix  *(bug / feature)*  **or**  Suggested wording  *(doc fix)*

A *suggestion*, not a prescription. One paragraph or a short snippet showing
the shape of the change you have in mind. End with the maintainer's
discretion intact: *"Totally understand if X isn't a priority — happy to send
a PR if it'd help."*

For a feature, this section can be richer: include the proposed function
signatures or types in a fenced block, and a short bullet list of the
non-obvious shape decisions. Keep it close to existing convention in the
codebase — if you're adding a parallel door, **name the pattern the project
already has and align to it**.

### A nice side effect  *(optional, when applicable)*

If this change cleans up other reported problems or composes with other open
issues, name them and cross-link briefly. This is high-leverage when filing a
cluster of related tickets: it makes the cluster legible without forcing the
maintainer to re-derive the connections.

### We're happy to do the work  *(when offering a PR)*

One short paragraph, low-key: you've thought about it, you're not blocked
because you have a workaround on your side, and you'd rather land this
upstream than carry the workaround forever. No pressure on shape or timing —
the project belongs to the maintainer; you're glad to follow their lead on
naming and details.

### Closing line

Warm, brief, optionally an emoji that matches the project's domain.

```markdown
Thanks again, and for being open to the no-opinion door. 🎹
```

---

## 2. Calibrated honesty — non-negotiable

Three habits separate a useful ticket from a noisy one. Apply all three:

**1. Mark confidence explicitly.** Say what you read directly and what you
inferred. *"We read the ALSA, UMP, and CoreMIDI paths directly. We didn't
line-by-line re-verify WinMM and WebMIDI, so we're not claiming anything
specific about those two — but the three above already disagree."* This is
the difference between a contribution and a complaint.

**2. Disclose your own bias.** If you have a preference among the possible
fixes, label it as such. *"For full transparency about our own bias: we'd
personally love the no-fold version, because our layer wants to own that
normalization in one place — but honestly, consistency either direction is
the real fix here."*

**3. Pre-empt the obvious red herring.** If there's a related-looking code
path that *isn't* the problem, say so before the maintainer wastes a minute
on it. *"Just to head off a red herring: the regular `mm_out_send` path uses
the same idiom, but it only ever carries 1–3 byte messages, so it never gets
near the limit. This is really only about big SysEx on the virtual branch."*

For a **question** (unconfirmed) ticket, calibrated honesty is the *whole
ticket*: write it as a question, not a bug report; state what would settle
it; and offer the maintainer the cheap out — *"if you happen to already know
off the top of your head, that'd answer the whole question."*

---

## 3. What to leave out

- **No named greetings.** Just `Hey 👋`. The maintainer will read the
  greeting before they see the body — if it's wrong, it's the first thing
  that sets a sour note.
- **No pressure on timing.** The project belongs to the maintainer.
- **No litigating severity.** Don't write "critical" or "blocker"; describe
  the consequence and let them assign the label.
- **No restating their docs back at them.** Assume they know the codebase.
- **No essays.** A ticket that takes ten minutes to read is a ticket the
  maintainer will set aside. The four-confirmed tickets in our worked
  example are each ~150 lines of Markdown; the question-ticket is shorter.
  Aim for *enough to act on, nothing past that.*
- **No silent dependencies on other tickets.** If this ticket only makes
  sense alongside another, cross-link explicitly — don't let the connection
  be implicit.
- **No claim of correctness for code you haven't run.** The header's "worth
  a quick re-check against current HEAD" is honest hedging, not boilerplate;
  use it whenever your line references are against a snapshot you read but
  did not just rebase.

---

## 4. The four shapes, at a glance

| Shape | Distinctive sections | Typical length |
|---|---|---|
| **Bug — confirmed** | What's going on / How to see it / A possible fix | ~80–120 lines |
| **Feature — additive** | What we'd propose adding / Why this should be a small change / The semantics we'd be counting on / A nice side effect / We're happy to do the work | ~150–200 lines |
| **Doc fix** | The mismatch / Suggested wording | ~30–60 lines |
| **Question — unconfirmed** | What we're wondering about / Why we *suspect* it but can't confirm / How someone could settle it | ~70–100 lines, marked DRAFT in the header |

Each shape shares the same spine — friendly opener, situation, what to do
about it, no-pressure close. The shape changes which middle sections carry
the weight.

---

## 5. Filing workflow (for the operator)

1. **Draft locally**, one ticket per file, in a project-side `issues/`,
   `docs/upstream/issues/`, or similar directory — confirm the location
   with the operator on the first ticket of a project (the project-wide
   default for upstream-contribution drafts is still deferred; see
   Part VIII of
   [`../../project-management/docs/PROJECT-MANAGEMENT.md`](../../project-management/docs/PROJECT-MANAGEMENT.md)).
   The on-disk filename mirrors the title:
   `NN-<kind>-<slug>.md` — e.g. `01-bug-coremidi-virtual-sysex-256-cap.md`.
2. **Re-check line references** against current `HEAD` before pasting; the
   header block's hedge ("worth a quick re-check") is a courtesy, not a
   permission slip.
3. **Strip the blockquote header** when pasting into the tracker; everything
   above the `---` separator stays on disk only.
4. **Apply the suggested labels** the header recommends, and edit the title
   to match the header's suggestion (or close).
5. **Cross-link related tickets** by URL once they're filed, in any tickets
   that reference them as "filed separately."
6. **Keep the on-disk file** as the canonical authoring source. The tracker
   is the public conversation; the file is the artifact you can re-read and
   reuse the voice from next time.
