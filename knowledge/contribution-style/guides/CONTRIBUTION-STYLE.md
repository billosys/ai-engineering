# Contribution Style — voice and discipline for upstream tickets

> The companion *how* doc for upstream contribution tickets — bugs, features,
> doc fixes, and questions filed against open source projects you do not
> maintain. The on-disk template lives at
> [`../templates/CONTRIBUTION-TICKET.md`](../templates/CONTRIBUTION-TICKET.md);
> this document is the voice, the disciplines, and the worked reasoning the
> template rests on.

## Why this exists

A ticket is a public artifact. It is read once by the maintainer who decides
whether to act, then again — sometimes years later — by the next contributor
to find it through search. Both readers have less context than the author.
The job of the ticket is to give them just enough to act, without making them
do the author's reading.

Most tickets fail in one of two directions: they are too thin (a sentence, no
repro, no file references — the maintainer cannot tell whether to believe
it), or too thick (a wall of speculation, multiple problems entangled, the
maintainer cannot tell where the actionable claim ends). Both fail the same
underlying test: *they make the reader do work that was the author's job.*

The methodology in this repo (see
[`../../engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md`](../../engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md))
provides the spine — write to the floor not the ceiling, flag dissonance
early, calibrated honesty as the other face of bold assertion. This document
applies those disciplines to the specific public artifact of an upstream
ticket.

## The voice, in one paragraph

Friendly, specific, calibrated, and respectful of the maintainer's time and
their ownership of the project. *Friendly* because you are asking someone to
spend their attention on your problem. *Specific* because vague tickets get
deferred and forgotten. *Calibrated* because asserting more than you know
will be caught and erode trust; asserting less will get the ticket
discounted. *Respectful of ownership* because the project belongs to the
maintainer — you are proposing, not directing. The voice should sound like a
note from a thoughtful colleague who happens to know this codebase well,
addressing another colleague who knows it much better.

## The shape of every ticket

A ticket has four moves, regardless of whether it is a bug, a feature, a doc
fix, or a question:

**1. Open with warmth and a single-sentence reason for writing.** The
greeting is generic — `Hey 👋` — never named. (Personal greetings read
warmly when the personal relationship is real and badly when it is not; the
generic greeting is the safe default.) Thank the project briefly,
state why you are writing in one sentence, and if you are also offering to do
the work, say so up front.

**2. State the situation specifically.** This is the section where the
maintainer learns what is going on, in their codebase, at their files and
lines. Quote the relevant code. Refer to file:line, including ranges. Be
short — three or four short paragraphs, not a wall — but make every
paragraph carry information the maintainer cannot get without you.

**3. Make the next move cheap.** For a bug, that means a minimal
reproduction: three or four numbered steps, stating what happens today and
what the hoped-for behaviour is. For a feature, a sketched proposal: the
function signatures, the capability bit, the semantic guarantees you'd be
counting on. For a doc fix, the suggested wording. For a question, the
experiment that would settle it. The goal is to let the maintainer act
without having to design the next step themselves.

**4. Close without pressure.** *"Happy to send a PR if it'd help"* —
not *"please prioritise"* or *"this is blocking us."* If you have a
workaround on your side, say so: it makes clear that you are filing this
because the project would be better with the fix landed upstream, not
because you are stuck.

These four moves are the spine. Everything else is variation — a feature
ticket has a richer middle than a doc fix; a question ticket replaces "how
to fix it" with "how to settle the uncertainty." The shape is the same.

## Calibrated honesty: the discipline that does the most work

A ticket that asserts more than the author knows is worse than no ticket at
all — it costs the maintainer attention and erodes trust for future tickets
from the same source. Three habits keep assertion calibrated:

### Mark confidence explicitly

State what you read directly and what you inferred. *"We read the ALSA,
UMP, and CoreMIDI paths directly. We didn't line-by-line re-verify WinMM
and WebMIDI, so we're not claiming anything specific about those two — but
the three above already disagree."* This single sentence converts a ticket
from "we found a problem on all four backends" (overclaim, will be challenged
and rejected) into "we found a problem on three of four; the fourth is open"
(precisely calibrated, easy to verify).

The pattern generalises. For any claim, ask: *did I actually verify this, or
am I extrapolating?* When the answer is "extrapolating," say so.

### Disclose your own bias

When there is more than one reasonable fix and you have a preference, label
your preference as a preference. *"For full transparency about our own bias:
we'd personally love the no-fold version, because our layer wants to own
that normalization in one place — but honestly, consistency either direction
is the real fix here."* The maintainer can now weigh your preference against
their own design taste without having to reverse-engineer it.

This applies to feature design choices, error-handling philosophies, naming,
and any other place where the maintainer's taste is the deciding factor.

### Pre-empt the obvious red herring

If there is a related-looking code path that *isn't* the problem, say so
before the maintainer wastes a minute on it. *"Just to head off a red
herring: the regular `mm_out_send` path uses the same idiom, but it only
ever carries 1–3 byte messages, so it never gets near the limit. This is
really only about big SysEx on the virtual branch."* Five extra seconds for
you; potentially many minutes saved for the reader.

### Question tickets are calibrated honesty's pure form

When you suspect a bug but have not reproduced it, file a *question*, not a
bug — and mark it `DRAFT` in the header so the operator can decide whether
to file now or hold for reproduction. The body says, plainly: here is what I
read, here is what I think it implies, here is why I can't confirm it, here
is the experiment that would settle it. Offer the maintainer the cheap out:
*"If you happen to already know off the top of your head whether X, that'd
answer the whole question."*

A question ticket reads as a contribution because it does the maintainer's
disambiguation work *for* them. A speculative bug report reads as noise
because it asks the maintainer to do it.

## Respect the maintainer's ownership

You did not write this code. You are asking for the maintainer's attention,
their patience with your proposed change, and — if it lands — their future
maintenance burden. Three behaviours follow:

**Propose, do not prescribe.** *"A possible fix"* and *"Suggested wording"*
are the section titles; *"Required change"* and *"Must be implemented as"*
are not. Code suggestions go in fenced blocks labelled as suggestions. End
sections with *"Totally understand if this isn't a priority"* or *"No
pressure on shape or timing — it's your library and your taste; we're glad
to follow your lead on naming and details."* These are not throat-clearing;
they are the explicit acknowledgement that the project belongs to the
maintainer.

**Acknowledge their existing patterns.** Before proposing a new function,
name the analogous pattern the project already has. *"You've already built
this exact pattern once: minimidio already has a parallel door for Universal
MIDI Packets — `mm_in_open_ump`, `mm_out_send_ump`, `mm_ump_callback`, and
`MM_CAP_UMP`. The raw-bytes door is the same idea, one more time."* This
turns your proposal from "please add this new thing I want" into "please
extend a pattern you already chose." The maintainer's decision becomes much
cheaper.

**Cross-link your own work.** If you are filing several related tickets,
say so, and once they are filed, edit each to point at the others by URL.
Make the cluster legible without forcing the maintainer to re-derive the
connections. The "A nice side effect" section — *"a couple of the issues we
filed separately basically disappear once this exists"* — is high-leverage
for exactly this reason.

## What to leave out

- **Named greetings.** `Hey 👋` is the default. Personal greetings are
  for personal relationships, not first contact.
- **Severity labels.** Don't write "critical" or "blocker." Describe the
  consequence and let the maintainer assign the label.
- **Restating the project's own docs at the maintainer.** Assume they know
  the codebase. Cite specific lines, not concepts.
- **Pressure on timing.** *"When you get a chance"* if anything; usually
  nothing.
- **Wall-of-text speculation.** A wall of "this might be related to that,
  which interacts with the other" reads as the author handing the
  reasoning work over to the reader. Stop, do the reasoning yourself,
  file a question ticket if the answer is "I don't know."
- **Multiple problems in one ticket.** If you find three things, file
  three tickets and cross-link them. Bundled tickets fragment the
  discussion, accept ambiguous closure, and rot in backlog.
- **Emojis past about two.** A `👋` and a single domain-appropriate emoji
  at close is plenty. Emoji density is a soft signal of seriousness; keep
  it on the warm side of professional.

## Sizing

The four-shape table in the template gives ballpark lengths:

- **Bug — confirmed:** ~80–120 lines of Markdown. The smaller end of that
  for a focused single-cause bug; the larger end when the bug has multiple
  visible consequences or interacts with related issues.
- **Feature — additive:** ~150–200 lines. Features are necessarily longer
  because they include the proposed shape and the semantics you'd be
  counting on; trim ruthlessly anywhere the maintainer can fill in the
  blank themselves.
- **Doc fix:** ~30–60 lines. *Smaller is better.* A doc fix is the easiest
  kind of ticket to accept; do not make it harder to read than the fix
  itself warrants.
- **Question — unconfirmed:** ~70–100 lines, marked `DRAFT` in the header.

A ticket that runs longer than the upper bound for its shape is usually
trying to do more than one thing — split it. A ticket that runs shorter
than the lower bound is usually missing the file:line specificity that
makes it actionable — flesh out the situation section.

## A note on tone under pressure

The hardest version of this discipline is filing a ticket about a bug that
has cost you significant time. The temptation is to vent, even mildly —
*"this caused us a lot of confusion"*, *"we expected this to just work"*.
Resist it. The maintainer did not cost you time; the world is complicated
and a bug landed where you happened to step on it. A ticket that reads
slightly frustrated will be read as more frustrated than written, because
text always lands a notch hotter than speech. The right move is to describe
the consequence at production volume — *"a downstream consumer can't tell it
actually arrived as a velocity-0 note-on"* — and let the maintainer feel
the cost themselves.

This applies symmetrically: if the maintainer responds tersely, do not
read terseness as hostility. Open source maintainers carry a heavy
correspondence load; brevity is conservation of attention, not signal of
displeasure. Reply with the same calibrated warmth you opened with.

## The relationship to the rest of the framework

Contribution tickets are the methodology applied to its hardest case: a
public artifact, addressed to a stranger, on a project you do not control.
Everything the framework asks for inside the repo — write to the floor,
calibrated uncertainty, disclosed deferral, respect for ownership — applies
with double force when the audience is outside the team.

The applied position in the methodology — *"the question 'LLM or not?' is
the wrong axis"* — also applies here. Whether a ticket was drafted with LLM
assistance is uninteresting; what matters is whether the contributor
understands what they submitted, whether it meets the project's quality
bar, and whether it was produced with the rigour appropriate to its scale.
Hold yourself to that bar, and the question of provenance never has to come
up.
