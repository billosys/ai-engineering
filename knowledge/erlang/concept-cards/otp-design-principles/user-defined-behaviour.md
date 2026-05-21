---
# === CORE IDENTIFICATION ===
concept: User-Defined Behaviour
slug: user-defined-behaviour

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: custom-behaviours
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "sys and proc_lib"
chapter_number: null
pdf_page: null
section: "User-Defined Behaviours"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "custom behaviour"
  - "non-standard behaviour"
  - "user-defined behavior"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - special-process
  - proc-lib
  - sys-module
  - callback-attribute
extends:
  - behaviour
related:
  - gen-server
  - gen-statem
  - gen-event
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a special process?"
  - "What must I know before writing a special process?"
---

# Quick Definition

A user-defined behaviour is a custom OTP behaviour module implemented using special process techniques, which defines a callback interface with `-callback` attributes that implementing modules must satisfy.

# Core Definition

To implement a user-defined behaviour, write code similar to a special process but call functions in a callback module for handling specific tasks. The behaviour module defines expected callbacks using `-callback` attributes (or alternatively the `behaviour_info/1` function). When the compiler encounters `-behaviour(Behaviour)` in a module, it calls `Behaviour:behaviour_info(callbacks)` and warns if any required callback is missing. Optional callbacks are specified with `-optional_callbacks`. The `-callback` attribute is recommended over `behaviour_info/1` because the extra type information can be used by tools for documentation and discrepancy detection. Contracts specified with `-callback` in the behaviour module can be refined with `-spec` in callback modules; each `-spec` contract should be a subtype of the respective `-callback` contract. (Source: spec_proc.md, "User-Defined Behaviours")

# Prerequisites

- **[Special Process](/concept-cards/otp-design-principles/special-process.md)** -- User-defined behaviours are built on special process techniques.
- **[proc_lib](/concept-cards/otp-design-principles/proc-lib.md)** -- Used for process startup.
- **[sys Module](/concept-cards/otp-design-principles/sys-module.md)** -- Used for debugging support.
- **[Callback Attribute](/concept-cards/otp-design-principles/callback-attribute.md)** -- Defines the callback interface.

# Key Properties

1. **Callback interface**: Defined using `-callback` attributes with type specifications.
2. **Compiler warnings**: The compiler warns about missing callback implementations.
3. **Optional callbacks**: Specified with `-optional_callbacks([Name/Arity, ...])`.
4. **Behaviour info**: Tools can query `Behaviour:behaviour_info(optional_callbacks)`.
5. **Contract refinement**: Callback modules can add `-spec` attributes that are subtypes of the `-callback` contracts.
6. **OTP-compliant**: Uses proc_lib and sys like any special process.

# Construction / Recognition

## To Construct/Create:
1. Create the behaviour module with `-callback` attributes defining expected callbacks.
2. Optionally specify `-optional_callbacks([...])`.
3. Implement the behaviour module similarly to a special process, using `proc_lib` for start and `sys` for debugging.
4. Call functions in the user's callback module for specific tasks.

## To Identify/Recognize:
1. Look for `-callback` attributes in a module.
2. Look for modules that use `-behaviour(CustomModule)`.
3. Look for `proc_lib` and `sys` usage combined with callback dispatching.

# Context & Application

User-defined behaviours allow library authors to create reusable frameworks similar to gen_server or gen_statem. They encapsulate common patterns (process lifecycle, message handling, debugging) while delegating domain-specific logic to callback modules. This is useful when gen_server's request-response pattern or gen_statem's state machine pattern do not fit the application's needs.

# Examples

**Example 1** (spec_proc.md, "User-Defined Behaviours"): A user-defined behaviour module:

```erlang
-module(simple_server).
-export([start_link/2, init/3, ...]).

-callback init(State :: term()) -> 'ok'.
-callback handle_req(Req :: term(), State :: term()) -> {'ok', Reply :: term()}.
-callback terminate() -> 'ok'.
-callback format_state(State :: term()) -> term().

-optional_callbacks([format_state/1]).

start_link(Name, Module) ->
    proc_lib:start_link(?MODULE, init, [self(), Name, Module]).

init(Parent, Name, Module) ->
    register(Name, self()),
    ...,
    Dbg = sys:debug_options([]),
    proc_lib:init_ack(Parent, {ok, self()}),
    loop(Parent, Module, Dbg, ...).
```

**Example 2** (spec_proc.md, "User-Defined Behaviours"): A callback module implementing the behaviour:

```erlang
-module(db).
-behaviour(simple_server).

-export([init/1, handle_req/2, terminate/0]).
...
```

**Example 3** (spec_proc.md, "User-Defined Behaviours"): Callback module with refined specs:

```erlang
-module(db).
-behaviour(simple_server).

-record(state, {field1 :: [atom()], field2 :: integer()}).
-type state()   :: #state{}.
-type request() :: {'store', term(), term()};
                   {'lookup', term()}.

-spec handle_req(request(), state()) -> {'ok', term()}.
```

# Relationships

## Builds Upon
- **[Special Process](/concept-cards/otp-design-principles/special-process.md)** -- User-defined behaviours use special process infrastructure.
- **[Callback Attribute](/concept-cards/otp-design-principles/callback-attribute.md)** -- Defines the expected callback interface.

## Enables
- Custom reusable process frameworks.
- Compile-time verification of callback implementations.

## Related
- **[gen_server](/concept-cards/otp-design-principles/gen-server.md)** -- A standard OTP behaviour; user-defined behaviours follow similar patterns.
- **[gen_statem](/concept-cards/otp-design-principles/gen-statem.md)** -- Another standard OTP behaviour.
- **[gen_event](/concept-cards/otp-design-principles/gen-event.md)** -- Another standard OTP behaviour.

## Contrasts With
- Standard OTP behaviours are provided by OTP; user-defined behaviours are application-specific.

# Common Errors

- **Error**: Using `behaviour_info/1` function with `-optional_callbacks` attribute.
  **Correction**: The `-optional_callbacks` attribute cannot be combined with the `behaviour_info()` function. Use `-callback` attributes instead.

# Common Confusions

- **Confusion**: User-defined behaviours require OTP team involvement.
  **Clarification**: Any developer can create a user-defined behaviour. It is just a module with `-callback` attributes and special process infrastructure.

- **Confusion**: `-callback` and `behaviour_info/1` are interchangeable.
  **Clarification**: The source recommends `-callback` over `behaviour_info/1` because the type information can be used by tools for documentation and discrepancy detection. `behaviour_info/1` is automatically generated by the compiler from `-callback` attributes.

# Source Reference

spec_proc.md, "User-Defined Behaviours" section.

# Verification Notes

- Definition source: Directly from spec_proc.md, "User-Defined Behaviours" section.
- Confidence rationale: High -- explicitly described with complete examples.
- Uncertainties: None.
- Cross-reference status: References special-process, callback-attribute, proc-lib, sys-module, gen-server, gen-statem, gen-event.
