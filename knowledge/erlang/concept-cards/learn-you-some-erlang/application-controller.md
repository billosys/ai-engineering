---
concept: Application Controller
slug: application-controller
category: applications-releases
subcategory: applications
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Building Applications the OTP Way"
chapter_number: 19
pdf_page: null
section: "The Application Behavior"
extraction_confidence: medium
aliases:
  - "application_controller"
  - "AC"
  - application master
prerequisites:
  - application-behaviour
extends: []
related:
  - application-behaviour
  - application-start-and-stop
contrasts_with: []
answers_questions:
  - "What is an OTP application?"
---

# Application Controller

## Quick Definition

The application controller is the process started when the VM boots that launches and oversees all applications. For each application it spawns an *application master* that acts as a middleman to that app's supervision tree.

## Core Definition

"Whenever the VM first starts up, a process called the *application controller* is started (with the name `application_controller`). It starts all other applications and sits on top of most of them. In fact, you could say the application controller acts a bit like a supervisor for all applications" (Ch. 19, "The Application Behavior").

"When someone decides to start an application, the application controller (often referred to as *AC*) starts an *application master*. The application master is two processes taking charge of each individual application. They set up the application and act like a middleman between your application's top supervisor and the application controller."

## Prerequisites

- **Application behaviour** — The controller is the generic part of the application behaviour.

## Key Properties

1. Started automatically at VM boot, registered as `application_controller`.
2. Starts all other applications and acts "a bit like a supervisor for all applications."
3. For each started application it spawns an application master (two processes).
4. The application master mediates between the app's top supervisor and the controller.
5. When an application fails, its master "terminates its whole family tree."
6. Exception: the `kernel` application is not under the controller — it starts the `user` process, which is the controller's group leader.

## Construction / Recognition

## To Recognise the Controller's Role

1. It is part of OTP's generic machinery — you never write it.
2. You interact with it indirectly via `application:start/1` and `application:stop/1`.
3. Each running application has an application master beneath the controller.

## Context & Application

The book notes that most Erlang developers "never actually need to care about this," and "very little documentation exists (the code is the documentation)." It is included "for the sake of precision." The key practical takeaway: applications form a layer in the VM above your own supervision trees, and the controller/master layer is what makes `application:start/1` more powerful than calling your module's `start` directly.

## Examples

**Example 1** (Ch. 19): When `application:start(ppool)` runs, the application controller starts an application master for `ppool`, which in turn sets up `ppool`'s top supervisor `ppool_supersup`.

**Example 2** (Ch. 19): The `kernel` application is the documented exception — it starts the `user` process that acts as the controller's group leader.

## Relationships

## Builds Upon

- **Application behaviour** — The controller is the behaviour's generic implementation.

## Related

- **application-behaviour** — The controller and masters are its generic part.
- **application-start-and-stop** — `application:start/1` delegates to the controller.

## Common Errors

- **Error**: Trying to write or replace the application controller.
  **Correction**: It is OTP-provided generic code; you only ever supply `start/2`/`stop/1` callbacks.

## Common Confusions

- **Confusion**: Thinking the application controller sits above *every* process.
  **Clarification**: It oversees most applications, but the `kernel` application is a special case — it starts the `user` process that is the controller's own group leader.

## Source Reference

Chapter 19: "Building Applications the OTP Way," section "The Application Behavior" and the sidebar "The Exception That Confirms the Rule."

## Verification Notes

- Definition: Direct quotes from "The Application Behavior."
- Confidence: MEDIUM — the source itself notes this is sparsely documented and not something developers usually need; the card stays at the level of detail the book provides.
