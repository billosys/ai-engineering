---
concept: Atom Leak
slug: atom-leak
category: anti-patterns
subcategory: memory
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Memory Leaks"
chapter_number: 7
pdf_page: null
section: "Atom"
extraction_confidence: high
aliases:
  - "Dynamic atom leak"
  - "Atom table exhaustion"
prerequisites:
  - memory-leak-detection
related:
  - code-memory-leak
contrasts_with: []
answers_questions:
  - "Why should I avoid dynamically creating atoms?"
  - "How does an atom leak crash an Erlang node?"
---

# Quick Definition

An atom leak is the slow exhaustion of the global atom table caused by dynamically creating atoms at run time — atoms go into a global table and are cached forever, so they are never reclaimed.

# Core Definition

From section "Atom": "Don't use dynamic atoms! Atoms go in a global table and are cached forever." The anti-pattern is calling functions such as `erlang:binary_to_term/1` and `erlang:list_to_atom/1` on attacker- or input-controlled data, which can generate an unbounded number of atoms. Because the atom table has a fixed limit and atoms are never garbage collected, the table fills until the node crashes.

# Prerequisites

- `memory-leak-detection` — identifying that atom memory is the growing category is the precondition for diagnosing an atom leak.

# Key Properties

1. Atoms go into a single global table and are cached forever — they are never garbage collected.
2. `erlang:binary_to_term/1` and `erlang:list_to_atom/1` are the typical leak sources.
3. Safer variants exist: `erlang:binary_to_term(Bin, [safe])` and `erlang:list_to_existing_atom/1`.
4. The `xmerl` XML library that ships with Erlang can create atoms; open-source SAX parsers or a custom safe parser avoid this.
5. Erlang node names are converted to atoms — using random node names slowly exhausts the atom table.
6. The fix for node names is to generate them from a fixed set, or slowly enough that exhaustion never becomes a problem.

# Construction / Recognition

To recognize: detect that atom memory grows and never drops. To remediate: audit every call site of `binary_to_term/1` and `list_to_atom/1`; switch to the `safe` and `list_to_existing_atom/1` variants; replace `xmerl` with a safe parser; and ensure any generated node names come from a bounded set.

# Context & Application

This is a cross-cutting trap that bites systems handling untrusted or highly variable input — RPC payloads, XML, and cluster tooling. The author cites a real production incident: common tools used random names to connect to nodes remotely, and because node names become atoms, this slowly exhausted the atom table.

# Examples

From section "Atom": "One specific case that bit me in production was that some of our common tools used random names to connect to nodes remotely, or generated nodes with random names that connected to each other from a central server. Erlang node names are converted to atoms, so just having this was enough to slowly but surely exhaust space on atom tables."

# Relationships

## Builds Upon
- `memory-leak-detection` — atom leak is one branch of the leak investigation.

## Enables
Nothing — it is a terminal anti-pattern card.

## Related
- `code-memory-leak` — another category of non-collectable memory growth.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Calling `binary_to_term/1` on external data without the `[safe]` option.
- Using `list_to_atom/1` where `list_to_existing_atom/1` would suffice.
- Generating random node names with no bound, treating node names as harmless strings rather than atoms.

# Common Confusions

- Rising atom memory is only alarming when atoms are created dynamically; a fixed program has a fixed, bounded set of atoms.
- Atoms are not garbage collected like ordinary terms — once created they persist for the life of the node.

# Source Reference

Chapter 7: Memory Leaks, Section "Atom". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Atom."
- Confidence rationale: high — the source explicitly names the anti-pattern and its fixes.
- Uncertainties: none.
- Cross-reference status: Verified
