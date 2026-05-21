---
# === CORE IDENTIFICATION ===
concept: Child Specification
slug: child-specification

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Supervisors"
chapter_number: 7
pdf_page: 188
section: "The child specification"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "child spec"
  - "ChildSpec"
  - "child_spec()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
extends: []
related:
  - supervisor-specification
  - restart-type
  - shutdown-time
  - worker-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a child specification?"
  - "How do I write a supervisor and define its child specifications?"
---

# Quick Definition

A child specification is the data structure that tells a supervisor everything it needs to start, stop, restart, and delete one child process. It is a tuple (or, on Erlang 18.0+, a map) of six fields.

# Core Definition

The child specification contains all of the information the supervisor needs to start, stop, and delete its child processes. It is a tuple of the format `{Name, StartFunction, RestartType, ShutdownTime, ProcessType, Modules}` (Cesarini & Vinoski, p. 180), or, on Erlang 18.0+, a map:

```erlang
child_spec() = #{id       => child_id(),  % mandatory
                 start    => mfargs(),    % mandatory
                 restart  => restart(),   % optional
                 shutdown => shutdown(),  % optional
                 type     => worker(),    % optional
                 modules  => modules()}   % optional
```

The fields are: `Name`/`id` (any term, unique within the supervisor); `StartFunction`/`start` (an `{M,F,A}` tuple that calls a behavior `start_link`); `RestartType`/`restart` (`permanent`/`transient`/`temporary`); `ShutdownTime`/`shutdown` (milliseconds, `infinity`, or `brutal_kill`); `ProcessType`/`type` (`worker` or `supervisor`); and `Modules`/`modules` (the modules implementing the behavior, or `dynamic`) (pp. 180-182).

# Prerequisites

- **Supervisor** — Child specifications exist only to configure a supervisor's children.

# Key Properties

1. Six fields: `Name`, `StartFunction`, `RestartType`, `ShutdownTime`, `ProcessType`, `Modules`.
2. `Name` (id) must be unique within a supervisor but may be reused across supervisors in the same node.
3. `StartFunction` is an `{M,F,A}` tuple that directly or indirectly calls a behavior `start_link`, expected to return `{ok, Pid}`.
4. Supervisors can start only OTP-compliant behaviors; plain Erlang processes cannot be linked into the tree.
5. The list of child specifications forms the second element of the supervisor specification.
6. `Modules` may be the atom `dynamic` when the implementing modules are not known at compile time (e.g. event managers).

# Construction / Recognition

## To Construct/Create:
1. Choose a unique `Name`/`id` within the supervisor.
2. Provide the `{Module, Function, Args}` start tuple.
3. Choose a restart type (`permanent`/`transient`/`temporary`).
4. Choose a shutdown time (milliseconds, `infinity`, or `brutal_kill`).
5. Set the process type (`worker` or `supervisor`) and the `Modules` list.

## To Identify/Recognize:
1. It is one element of the list returned in a supervisor specification.
2. It is a six-element tuple or a map with `id` and `start` keys.

# Context & Application

- **Typical contexts**: Each statically started child of a supervisor has one; the list is returned from `init/1`.
- **Common applications**: Declaring static children; passed to `supervisor:start_child/2` for dynamic children.
- **Historical/stylistic notes**: `supervisor:check_childspecs/1` validates a list of child specs, returning `ok` or `{error, Reason}` — useful when troubleshooting startup issues (p. 184).

# Examples

**Example 1** (p. 175): `child(Module)` returns `{Module, {Module, start_link, []}, permanent, 2000, worker, [Module]}`.

**Example 2** (p. 177): The same child as a map with `id`, `start`, `restart`, `shutdown`, `type`, and `modules` keys.

## Worked Example

Tuple and map child specifications for the frequency example (pp. 175, 177):

```erlang
%% Tuple form
child(Module) ->
    {Module, {Module, start_link, []},
     permanent, 2000, worker, [Module]}.

%% Map form (Erlang 18.0+) - all fields named
child(Module) ->
    #{id => Module,
      start => {Module, start_link, []},
      restart => permanent,
      shutdown => 2000,
      type => worker,
      modules => [Module]}.
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- **Supervisor** — A supervisor is configured by the list of child specifications.

## Related
- **Supervisor specification** — Child specs form its second element.
- **Restart type** — One field of the child specification.
- **Shutdown time** — One field of the child specification.
- **Worker process** — The `ProcessType` field declares a child a worker.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Reusing the same `id` for two children of the same supervisor.
  **Correction**: `id` must be unique within a supervisor (it may be reused across supervisors).

- **Error**: Specifying a `StartFunction` that does not return `{ok, Pid}`.
  **Correction**: The start function must call a behavior `start_link` and return `{ok, Pid}`; any other value is a startup error.

# Common Confusions

- **Confusion**: Thinking `Modules` is just documentation.
  **Clarification**: `Modules` is used during software upgrades to decide which processes to suspend; set it to `dynamic` when modules are unknown at compile time.

# Source Reference

Chapter 7: Supervisors, "The child specification," pages 180-184.

# Verification Notes

- Definition source: Direct adaptation from pp. 180-182, including the tuple and map type specifications.
- Confidence rationale: HIGH — explicitly defined with field-by-field description.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
