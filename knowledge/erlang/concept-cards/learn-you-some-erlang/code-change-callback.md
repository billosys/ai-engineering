---
concept: code_change Callback
slug: code-change-callback
category: production-ops
subcategory: code-upgrades
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Leveling Up in the Process Quest"
chapter_number: 22
pdf_page: null
section: "Updating code_change Functions"
extraction_confidence: high
aliases:
  - "code_change/4"
  - "code_change/3"
  - "code_change function"
  - "state migration callback"
prerequisites:
  - hot-code-loading
  - gen-server
  - record
extends: []
related:
  - appup
  - relup
contrasts_with: []
answers_questions:
  - "What is the code_change callback?"
  - "How do I migrate process state during a code upgrade?"
  - "How do I handle upgrades and downgrades differently?"
---

# code_change Callback

## Quick Definition

`code_change` is the OTP callback that migrates a process's internal state when its module is upgraded or downgraded during a controlled code upgrade. OTP suspends the process, calls `code_change`, then resumes it.

## Core Definition

When an appup instruction `{update, Mod, {advanced, Extra}}` runs, OTP suspends all processes running `Mod`, calls the module's `code_change` function with `Extra` as the last argument, and then resumes them (Ch. 22, "Adding Appup Files"). The job of `code_change` is to transform the process's old-version state into the new-version state. OTP passes different arguments depending on direction: an upgrade passes a plain version number, while a downgrade passes `{down, Version}`, letting you match on each case (Ch. 22, "Updating code_change Functions").

## Prerequisites

- **Hot-code-loading** — `code_change` is the controlled-upgrade hook
- **Gen-server** — `code_change` is a behaviour callback (here, `gen_fsm`'s `code_change/4`)
- **Record** — State is often a record; migration requires understanding records' tuple form

## Key Properties

1. OTP calls `code_change` between suspending and resuming the process
2. The first argument distinguishes direction: `{down, Version}` for downgrade, a plain version for upgrade
3. The `Extra` argument is supplied from the appup file and is chosen by the developer
4. You cannot blindly match the old state as `#state{}` — the record definition has already changed to the new shape
5. The safe technique is to expand the record to its underlying tuple form and rebuild the other version's record explicitly
6. For `gen_fsm` the arity is `code_change/4` (OldVsn, StateName, State, Extra); for `gen_server` it is `code_change/3`

## Construction / Recognition

### To write a code_change for an incompatible state change

1. Add a `code_change({down, _}, ...)` clause for downgrades
2. Add a `code_change(_OldVsn, ...)` clause for upgrades
3. In each clause, match the incoming state in its raw tuple form (not as a record), since the record definition differs between versions
4. Rebuild the state in the target version's shape, supplying defaults for any new fields

## Context & Application

`code_change` is only needed when a module's state representation changes incompatibly between versions. Modules whose changes do not affect state (e.g. only adding a new message clause) need no suspension and only a `load_module` appup instruction.

## Examples

**Example** (Ch. 22): The Process Quest `pq_player` record gained a `quest` field. The `code_change/4` converts between tuple forms in both directions —

```erlang
code_change({down, _}, StateName,
            #state{name=N, stats=S, exp=E, lvlexp=LE, lvl=L, equip=Eq,
                   money=M, loot=Lo, bought=B, time=T}, _Extra) ->
    Old = {state, N, S, E, LE, L, Eq, M, Lo, B, T},
    {ok, StateName, Old};
code_change(_OldVsn, StateName,
            {state, Name, Stats, Exp, LvlExp, Lvl, Equip, Money, Loot,
             Bought, Time}, _Extra) ->
    State = #state{name=Name, stats=Stats, exp=Exp, lvlexp=LvlExp,
        lvl=Lvl, equip=Equip, money=Money, loot=Loot,
        bought=Bought, time=Time, quest=pq_quest:fetch()},
    {ok, StateName, State}.
```

## Relationships

### Builds Upon

- **Hot-code-loading** — `code_change` is invoked by the controlled-upgrade machinery

### Related

- **Appup** — The `{update, Mod, {advanced, Extra}}` instruction triggers `code_change` and supplies `Extra`
- **Relup** — Relups orchestrate the upgrades that drive `code_change` calls

## Common Errors

- **Error**: Matching the old state with `#state{}` in `code_change`.
  **Correction**: Match the raw tuple form, because the compiled record definition is already the new shape.
- **Error**: Forgetting a downgrade clause.
  **Correction**: Provide a `code_change({down, _}, ...)` clause; OTP passes `{down, Version}` for downgrades.

## Common Confusions

- **Confusion**: Thinking every module upgrade needs a `code_change`.
  **Clarification**: Only incompatible state changes need it; pure logic or new-clause changes use `load_module` with no suspension.
- **Confusion**: Assuming `Extra` is meaningful by default.
  **Clarification**: `Extra` comes from the appup file and is `[]` unless you choose to pass release-specific data.

## Source Reference

Chapter 22, "Leveling Up in the Process Quest," section "Updating code_change Functions." See the `pq_player` record change and the `code_change/4` listing.

## Verification Notes

- Definition: Direct adaptation from "Updating code_change Functions" and "Adding Appup Files"
- Key Properties: All explicit in source
- Confidence: HIGH — the chapter shows the exact callback and its argument semantics
- Cross-references: `hot-code-loading`, `appup`, `relup` planned this chapter; `gen-server`, `record` shared slugs
