---
concept: Application Behaviour
slug: application-behaviour
category: applications-releases
subcategory: applications
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Building Applications the OTP Way"
chapter_number: 19
pdf_page: null
section: "The Application Behavior"
extraction_confidence: high
aliases:
  - "application behavior"
  - "application behaviour"
prerequisites:
  - otp-behaviour
  - otp-application
extends:
  - otp-behaviour
related:
  - application-callback-module
  - application-controller
  - application-start-and-stop
contrasts_with: []
answers_questions:
  - "What is an OTP application?"
  - "How does a behaviour relate to its callback module?"
---

# Application Behaviour

## Quick Definition

The application behaviour is the OTP behaviour for applications. Its generic part — the application controller and application masters — is complex; its specific part is just two callbacks: `start/2` and `stop/1`.

## Core Definition

"Remember that behaviors are always about splitting generic code away from specific code. ... In the case of applications, this generic part is quite complex and not nearly as simple as other behaviors" (Ch. 19, "The Application Behavior"). The callback module "requires very few functions to be functional: `start/2` and `stop/1`."

## Prerequisites

- **OTP behaviour** — The application behaviour is one of the OTP behaviours.
- **OTP application** — The behaviour wraps an OTP application.

## Key Properties

1. The generic part comprises the *application controller* and per-application *application masters*.
2. The specific part is two required callbacks: `start/2` and `stop/1`.
3. `start(Type, Args)` — `Type` is normally `normal`; `Args` comes from the `{mod, {Mod, Args}}` tuple.
4. `start/2` initialises the app and returns `{ok, Pid}` or `{ok, Pid, State}`, where `Pid` is the top supervisor.
5. `stop/1` receives the state returned by `start/2` and does cleanup; it runs *after* the app has stopped.
6. An optional `prep_stop/1` callback runs before `stop/1`, while the app is still alive (Ch. 20).

## Construction / Recognition

## To Use the Application Behaviour

1. Add `-behavior(application).` to the callback module.
2. Implement `start(normal, _Args)` returning `{ok, Pid}` from the top supervisor's `start_link`.
3. Implement `stop(_State)` returning `ok` (or doing cleanup).
4. Name the module in the `.app` file's `{mod, {Module, Args}}` tuple.
5. Start the app with `application:start(AppName)`.

## Context & Application

When the VM starts, it launches the `application_controller` process, which "acts a bit like a supervisor for all applications." When an application is started, the controller spawns an *application master* — "two processes taking charge of each individual application," acting as a middleman between the app's top supervisor and the controller. The book describes the application master as the app's "nanny" that "terminates its whole family tree" when things go wrong.

The application behaviour is current in modern OTP, unchanged.

## Examples

**Example 1** (Ch. 19): `ppool` becomes an application callback module — `-behavior(application).`, `start(normal, _Args) -> ppool_supersup:start_link().`, `stop(_State) -> ok.`

**Example 2** (Ch. 20): `erlcount` does the same: `start(normal, _Args) -> erlcount_sup:start_link().`

## Relationships

## Builds Upon

- **OTP behaviour** — Generic application machinery factored out by OTP.

## Related

- **application-callback-module** — The module implementing `start/2` and `stop/1`.
- **application-controller** — The generic process that starts and oversees applications.
- **application-start-and-stop** — How applications are started and stopped.

## Common Errors

- **Error**: Returning something other than `{ok, Pid}`/`{ok, Pid, State}` from `start/2`.
  **Correction**: `start/2` must return the top supervisor's pid in one of those two forms.

## Common Confusions

- **Confusion**: Thinking `stop/1` does the actual shutdown work.
  **Clarification**: `stop/1` runs *after* the application has already terminated — it only does final cleanup. Use `prep_stop/1` for work that must happen while the app is still alive.

## Source Reference

Chapter 19: "Building Applications the OTP Way," section "The Application Behavior"; `prep_stop/1` in Chapter 20, "Complex Terminations."

## Verification Notes

- Definition: Direct quotes from "The Application Behavior."
- Key Properties: Synthesised from the callback descriptions and the controller/master discussion.
- Confidence: HIGH — explicitly defined with code.
