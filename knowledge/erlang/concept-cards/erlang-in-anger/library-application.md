---
concept: Library Application
slug: library-application
category: applications-releases
subcategory: code-base-types
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "How to Dive into a Code Base"
chapter_number: 1
pdf_page: null
section: "Library Applications"
extraction_confidence: high
aliases: []
prerequisites:
  - otp-application
  - app-file
extends:
  - otp-application
related:
  - regular-application
  - behaviour-as-navigation-clue
contrasts_with:
  - regular-application
answers_questions:
  - "What differentiates an application from a library application?"
  - "What is a library application?"
---

# Quick Definition

A library application is an OTP application whose app file has no `mod` tuple — it provides modules and functions but starts no top-level process of its own.

# Core Definition

One of the two varieties of OTP application. From Chapter 1, section "OTP Applications," a library application's app file looks like:

```erlang
{application, useragent, [
  {description, "Identify browsers & OSes from useragent strings"},
  {vsn, "0.1.2"},
  {registered, []},
  {applications, [kernel, stdlib]},
  {modules, [useragent]}
]}.
```

The defining trait is the *absence* of a `{mod, ...}` tuple. From section "Library Applications": "Library applications will usually have modules named `appname_something`, and one module named `appname`. This will usually be the interface module that's central to the library."

# Prerequisites

- `otp-application` — a library application is a variety of OTP application; you must understand the umbrella concept first.
- `app-file` — the distinction from a regular application is read directly from the app file.

# Key Properties

1. Its app file has no `mod` tuple, so it does not implement the `application` behaviour and starts no callback process.
2. Conventionally exposes one central interface module named `appname`, plus supporting modules named `appname_something`.
3. If a module adheres to a behaviour (`gen_server`, `gen_fsm`, etc.), you are expected to start a process under one of your own supervisors and call it that way.
4. If no behaviour is included, it is most likely a functional, stateless library — its exported functions reveal its purpose.

# Construction / Recognition

To recognize one: check the app file for the absence of a `mod` tuple. To navigate it: read the central `appname` module; its exported functions give a quick way into most of the functionality. Check whether modules implement behaviours to learn how they are meant to be used.

# Context & Application

Library applications are dependencies you pull into your own system. You decide where their processes (if any) run by placing them under your own supervisors.

# Examples

From Chapter 1, section "OTP Applications": the `useragent` application — "Identify browsers & OSes from useragent strings" — with a single `useragent` module is the book's example of a library application.

# Relationships

## Builds Upon
- `otp-application` — it is a variety of OTP application.

## Enables
Nothing structural.

## Related
- `behaviour-as-navigation-clue` — whether modules implement a behaviour tells you how to use the library.

## Contrasts With
- `regular-application` — a regular application has a `mod` tuple and starts a top-level supervisor; a library application does not.

# Common Errors

- Assuming a library application starts its own processes. It does not; you must start any of its behaviour processes under your own supervision tree.

# Common Confusions

- The presence of a `gen_server` module inside a library application does not make it a regular application — what matters is the `mod` tuple in the app file.

# Source Reference

Chapter 1: How to Dive into a Code Base, Section "Library Applications". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 1, sections "OTP Applications" and "Library Applications."
- Confidence rationale: high — explicitly defined and contrasted with regular applications, with an app-file example.
- Uncertainties: none.
- Cross-reference status: Verified
