---
# === CORE IDENTIFICATION ===
concept: Functions Internal to the Server
slug: server-internal-functions

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: process-design
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Behaviors"
chapter_number: 2
pdf_page: 72
section: "Functions Internal to the Server"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - internal functions
  - server helper functions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - the-server-loop
extends: []
related:
  - generic-vs-specific-code
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are functions internal to a server?"
  - "Is a server's business logic generic or specific?"
---

# Quick Definition

Functions internal to the server are the unexported helper functions that perform the server's actual work. They are entirely specific — pure business logic with no generic counterpart.

# Core Definition

"The functions that actually perform the work ... within the server are not 'visible' outside the server module itself, and so we call them internal to the server" (Cesarini & Vinoski, p. 65). In the frequency example, `allocate/2` and `deallocate/2` move frequencies between the available and allocated lists. When asked which parts are generic, the book answers: "this should have been an easy question to answer, as these internal functions are all specific to our frequency server. When did you last allocate and deallocate frequencies when working with a key-value store or a window manager?" (p. 66). The "trick question" footnote underscores that internal server functions have no generic part at all.

# Prerequisites

- **The server loop** — Internal functions are the helpers the server loop calls to handle each request.

# Key Properties

1. They are not exported — invisible outside the server module.
2. They perform the server's actual business computation.
3. They are entirely specific; they have no generic counterpart.
4. The server loop calls them to compute new state and replies.
5. They typically return a tuple of new loop data plus a reply.

# Construction / Recognition

## To Construct:
1. Write unexported helper functions for each unit of business logic.
2. Have them take the loop data (and request data) and return updated loop data plus any reply.
3. Call them from the matching server-loop clause.

## To Recognize:
1. Unexported functions invoked only from the server loop's clauses.

# Context & Application

- **Typical contexts**: The business-logic core of any server.
- **Common applications**: `allocate/2` and `deallocate/2` in the frequency server.
- **Historical/stylistic notes**: Because they are wholly specific, internal functions stay in the callback module when generic code is extracted.

# Examples

**Example 1** (p. 66): The frequency server's internal functions:

```erlang
allocate({[], Allocated}, _Pid) ->
    {{[], Allocated}, {error, no_frequency}};
allocate({[Freq|Free], Allocated}, Pid) ->
    {{Free, [{Freq, Pid}|Allocated]}, {ok, Freq}}.
deallocate({Free, Allocated}, Freq) ->
    NewAllocated = lists:keydelete(Freq, 1, Allocated),
    {[Freq|Free], NewAllocated}.
```

`allocate/2`'s first clause matches an empty available list and returns `{error, no_frequency}`; the second moves a frequency to the allocated list.

# Relationships

## Builds Upon
- **The server loop** — Internal functions are invoked from the loop's clauses.

## Enables
- *(none specific in scope)*

## Related
- **Generic versus specific code** — Internal functions are the clearest example of purely specific code.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Exporting internal helper functions, exposing implementation detail.
  **Correction**: Keep business-logic helpers unexported so the server module's public surface stays minimal.

# Common Confusions

- **Confusion**: Looking for a generic part within the server's business logic.
  **Clarification**: Internal server functions are entirely specific — there is no generic component to extract.

# Source Reference

Chapter 2: Behaviors, Section "Functions Internal to the Server," pages 65-67.

# Verification Notes

- Definition source: Direct quotes from pp. 65-66.
- Confidence rationale: MEDIUM — the term is introduced briefly and the concept is more a classification than a formally defined construct; definition synthesized from the section's discussion.
- Uncertainties: None significant; the section is short.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
