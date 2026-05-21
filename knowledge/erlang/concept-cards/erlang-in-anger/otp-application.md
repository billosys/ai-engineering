---
concept: OTP Application
slug: otp-application
category: applications-releases
subcategory: code-base-types
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "How to Dive into a Code Base"
chapter_number: 1
pdf_page: null
section: "OTP Applications"
extraction_confidence: high
aliases:
  - "OTP App"
prerequisites: []
extends: []
related:
  - app-file
  - library-application
  - regular-application
  - otp-release
  - supervision-tree-navigation
contrasts_with:
  - raw-erlang-code-base
  - otp-release
answers_questions:
  - "What is an OTP application?"
  - "How do I dive into an unfamiliar code base?"
  - "What is the difference between raw Erlang and an OTP application?"
---

# Quick Definition

An OTP application is a self-contained, standardized unit of Erlang code that shares a predictable directory structure and is described by an app file.

# Core Definition

The most common type of Erlang code base encountered in the wild. From Chapter 1, section "OTP Applications": OTP applications "usually all share a directory structure" and "Each OTP application should contain an *app file*." A typical layout is:

```text
doc/
ebin/
src/
test/
LICENSE.txt
README.md
rebar.config
```

There may be slight differences, but the general structure stays the same. From Chapter 2: "If what you're writing is a stand-alone piece of code that could be used by someone building a product, it's likely an OTP application."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Has a predictable directory structure (`doc/`, `ebin/`, `src/`, `test/`, plus config and metadata files).
2. Contains an app file, either `ebin/<AppName>.app` or, more often, `src/<AppName>.app.src`.
3. Comes in two varieties: a library application and a regular (callback) application.
4. OTP applications usually share no state between them, so dependency relationships can be read from the app file alone.
5. They are "the vast majority of the open source code people will encounter" (Chapter 2).
6. A stand-alone piece of code meant to be used inside someone else's product is, by this book's rule of thumb, an OTP application (as opposed to a release).

# Construction / Recognition

To recognize an OTP application: look for the standard directory structure and the app file. To navigate it: read the app file to learn the application's identity, dependencies, and (for regular applications) its callback module; then explore the entry-point modules and the supervision tree top-down.

# Context & Application

OTP applications are the unit of code reuse and dependency management in Erlang. They are packaged together to form OTP releases. The chapter recommends navigating them top-down by exploring supervision subtrees.

# Examples

From Chapter 1, section "OTP Applications," a library-application app file for `useragent` and a regular-application app file for `dispcount` are given as the two varieties (see the `app-file` card). Chapter 2 notes that "many people who would need to build an OTP release would do so as one umbrella OTP application."

# Relationships

## Builds Upon
Nothing within this source.

## Enables
- `otp-release` — releases are collections of OTP applications.
- `library-application`, `regular-application` — the two varieties.

## Related
- `app-file` — the metadata file every application carries.
- `supervision-tree-navigation` — the recommended way to explore a regular application.

## Contrasts With
- `raw-erlang-code-base` — no standard structure.
- `otp-release` — a release is a packaged set of applications, ready to boot standalone.

# Common Errors

- Looking for an app file in the wrong place; it may be `ebin/<AppName>.app` or `src/<AppName>.app.src` depending on the build stage.

# Common Confusions

- An OTP application is not necessarily a runnable program; a library application has no callback module and starts no processes of its own.
- An application is not a release: a release packages multiple applications so they boot without manual `application:start/2` calls.

# Source Reference

Chapter 1: How to Dive into a Code Base, Section "OTP Applications". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 1, section "OTP Applications," and Chapter 2.
- Confidence rationale: high — explicitly defined with structure and examples.
- Uncertainties: none.
- Cross-reference status: Verified
