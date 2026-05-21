---
concept: Raw Erlang Code Base
slug: raw-erlang-code-base
category: applications-releases
subcategory: code-base-types
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "How to Dive into a Code Base"
chapter_number: 1
pdf_page: null
section: "Raw Erlang"
extraction_confidence: high
aliases: []
prerequisites: []
extends: []
related:
  - otp-application
  - otp-release
contrasts_with:
  - otp-application
answers_questions:
  - "How do I dive into an unfamiliar code base?"
  - "What is the difference between raw Erlang and an OTP application?"
---

# Quick Definition

A raw Erlang code base is Erlang code that does not follow the OTP application standard, leaving no predictable structure to guide navigation.

# Core Definition

One of three main types of Erlang code bases you encounter in the wild (alongside OTP applications and OTP releases). From Chapter 1, section "Raw Erlang": "If you encounter a raw Erlang code base, you're pretty much on your own. These rarely follow any specific standard, and you have to dive in the old way to figure out whatever happens in there."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Follows no specific standard directory or file structure.
2. Navigation depends on auxiliary clues: a `README.md` (or similar) pointing to an entry point, or contact information for the author(s).
3. Rarely encountered in practice — usually beginner projects, or once-good projects built by beginners that now need a serious rewrite.
4. Has become rare because tools such as `rebar3` and its predecessors pushed most people toward OTP applications.

# Construction / Recognition

To navigate one: look for a `README.md` or similar file that identifies an entry point and trace execution from there; failing that, look for author contact details and ask questions directly. There is no structural shortcut.

# Context & Application

Recognizing a code base as "raw Erlang" tells you that the structural navigation tips for OTP applications and releases will not apply — you must read the source the hard way.

# Examples

From Chapter 1, section "Raw Erlang": navigation "means hoping for a `README.md` file or something similar that can point to an entry point in the application, and going from there, or hoping for some contact information that can be used to ask questions to the author(s) of the library."

# Relationships

## Builds Upon
Nothing within this source.

## Enables
Nothing — it is a recognition category.

## Related
- `otp-application`, `otp-release` — the other two code-base types.

## Contrasts With
- `otp-application` — an OTP application has a predictable directory structure and app file; a raw code base does not.

# Common Errors

- Assuming OTP-application navigation tricks (app file, supervision tree) apply when no app file exists.

# Common Confusions

- A raw Erlang code base is not the same as a "small" project — size is unrelated; the defining trait is the absence of OTP standards.

# Source Reference

Chapter 1: How to Dive into a Code Base, Section "Raw Erlang". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 1, section "Raw Erlang."
- Confidence rationale: high — explicitly named and described as one of three code-base types.
- Uncertainties: none.
- Cross-reference status: Verified
