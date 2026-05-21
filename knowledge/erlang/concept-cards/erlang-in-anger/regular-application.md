---
concept: Regular Application
slug: regular-application
category: applications-releases
subcategory: code-base-types
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "How to Dive into a Code Base"
chapter_number: 1
pdf_page: null
section: "Regular Applications"
extraction_confidence: high
aliases:
  - "Application (callback)"
prerequisites:
  - otp-application
  - app-file
extends:
  - otp-application
related:
  - library-application
  - supervision-tree-navigation
  - behaviour-as-navigation-clue
contrasts_with:
  - library-application
answers_questions:
  - "What differentiates an application from a library application?"
  - "What is a regular OTP application?"
---

# Quick Definition

A regular application is an OTP application whose app file contains a `mod` tuple — it implements the `application` behaviour and starts a top-level supervisor when launched.

# Core Definition

One of the two varieties of OTP application. From Chapter 1, section "OTP Applications," a regular application's app file looks like:

```erlang
{application, dispcount, [
  {description, "A dispatching library for resources and task "
                "limiting based on shared counters"},
  {vsn, "1.0.0"},
  {applications, [kernel, stdlib]},
  {registered, []},
  {mod, {dispcount, []}},
  {modules, [dispcount, dispcount_serv, dispcount_sup,
             dispcount_supersup, dispcount_watcher, watchers_sup]}
]}.
```

The defining trait is the `{mod, ...}` tuple. From section "Regular Applications": there are two potential entry-point modules — `appname` (a library-style entry point) and `appname_app` (which implements the `application` behaviour and "will represent the top of the application's process hierarchy"). Sometimes one file plays both roles.

# Prerequisites

- `otp-application` — a regular application is a variety of OTP application.
- `app-file` — the `mod` tuple in the app file is what identifies it.

# Key Properties

1. Its app file contains a `{mod, {Module, Args}}` tuple naming the callback module.
2. The callback module (`appname_app`) implements the `application` behaviour and is the top of the process hierarchy.
3. On start it launches a top-level supervisor and returns the supervisor's pid.
4. The top-level supervisor contains the specifications of all child processes it starts.
5. Two entry points exist: use `appname` if you only depend on the app; use `appname_app` if you need to maintain or fix it.

# Construction / Recognition

To recognize one: find a `mod` tuple in the app file. To navigate it: start from `appname_app`, follow the top-level supervisor it starts, and explore the supervision tree top-down (depth-first, in start order).

# Context & Application

Regular applications are the runnable units of an Erlang system. They are the right starting point when you must maintain or debug an application, since `appname_app` exposes the whole process hierarchy.

# Examples

From Chapter 1, section "OTP Applications": the `dispcount` application — "A dispatching library for resources and task limiting based on shared counters" — with a `{mod, {dispcount, []}}` tuple and multiple modules including supervisors, is the book's example of a regular application.

# Relationships

## Builds Upon
- `otp-application` — a variety of OTP application.

## Enables
- `supervision-tree-navigation` — its top-level supervisor is the entry point for top-down navigation.

## Related
- `behaviour-as-navigation-clue` — worker behaviours reveal each process's role.

## Contrasts With
- `library-application` — a library application has no `mod` tuple and starts no processes.

# Common Errors

- Starting analysis from `appname` when you actually need to fix the application — use `appname_app` to reach the process hierarchy.

# Common Confusions

- A regular application's app file may name a `dispcount` module *and* have `{mod, {dispcount, []}}`; the same module name can serve as both interface and callback module.

# Source Reference

Chapter 1: How to Dive into a Code Base, Section "Regular Applications". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 1, sections "OTP Applications" and "Regular Applications."
- Confidence rationale: high — explicitly defined and contrasted, with an app-file example.
- Uncertainties: none.
- Cross-reference status: Verified
