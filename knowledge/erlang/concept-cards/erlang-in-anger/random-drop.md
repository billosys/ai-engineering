---
concept: Random Drop
slug: random-drop
category: production-ops
subcategory: overload
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Planning for Overload"
chapter_number: 3
pdf_page: null
section: "Random Drop"
extraction_confidence: high
aliases: []
prerequisites:
  - load-shedding
extends:
  - load-shedding
related:
  - queue-buffer
  - stack-buffer
contrasts_with:
  - queue-buffer
answers_questions:
  - "How do I shed load by randomly dropping messages?"
  - "What is the simplest way to drop messages under overload?"
---

# Quick Definition

Random drop is the simplest load-shedding implementation: each message is kept or dropped based on a random number compared against a threshold rate, ideally at the producer.

# Core Definition

From Chapter 3, section "Random Drop": "Randomly dropping messages is the easiest way to do such a thing, and might also be the most robust implementation, due to its simplicity. The trick is to define some threshold value between 0.0 and 1.0 and to fetch a random number in that range":

```erlang
-module(drop).
-export([random/1]).

random(Rate) ->
    maybe_seed(),
    random:uniform() =< Rate.

maybe_seed() ->
    case get(random_seed) of
        undefined -> random:seed(erlang:now());
        {X,X,X} -> random:seed(erlang:now());
        _ -> ok
    end.
```

# Prerequisites

- `load-shedding` — random drop is a load-shedding implementation.

# Key Properties

1. Simplest and arguably most robust load-shedding implementation.
2. A threshold `Rate` between 0.0 and 1.0 sets the fraction of messages kept.
3. To keep 95% of messages: `case drop:random(0.95) of true -> send(); false -> drop() end`, or `drop:random(0.95) andalso send()`.
4. `maybe_seed()` installs a good seed in the process dictionary only if absent, avoiding frequent calls to `now()` (which takes a global lock).
5. Critically, dropping must happen at the *producer* level, not the receiver level — Erlang has no bounded mailboxes, so dropping at the receiver just makes that process spin wildly fighting the schedulers.
6. The threshold can be tuned dynamically via an ETS table or `application:set_env/3`, read by any process via `application:get_env/2`; different drop ratios can be used for different message priorities.

# Construction / Recognition

Implement a `drop:random/1` function comparing `random:uniform()` against a rate. Call it at every producer before sending. Optionally store the rate in ETS or application env so a monitor process can raise or lower it based on observed load.

# Context & Application

Random drop is the load-shedding method of choice when overload is a roughly constant stream needing thinning, and you do not need fine control over *which* messages are dropped.

# Examples

From Chapter 3, section "Random Drop": the `drop` module above is given verbatim, along with the usage forms and the producer-vs-receiver "gotcha": "dropping in the receiving process only guarantees that this process will be spinning wildly, trying to get rid of messages, and fighting the schedulers to do actual work."

# Relationships

## Builds Upon
- `load-shedding` — a concrete implementation.

## Enables
Dynamic, load-adaptive drop rates via ETS / application env.

## Related
- `stack-buffer` — another load-shedding implementation.

## Contrasts With
- `queue-buffer` — a queue buffer gives more control over *which* messages are dropped; random drop trades that control for simplicity.

# Common Errors

- Dropping at the receiver instead of the producer — the receiver process spins wildly and fights the schedulers.
- Calling `now()` for a seed on every drop decision, taking a global lock too often — `maybe_seed()` avoids this.

# Common Confusions

- The threshold is the *keep* rate, not the drop rate: `drop:random(0.95)` keeps ~95% of messages.
- Random drop is "most robust" because of simplicity, not because random selection is inherently better than buffer-based selection.

# Source Reference

Chapter 3: Planning for Overload, Section "Random Drop". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 3, section "Random Drop."
- Confidence rationale: high — code and usage shown verbatim.
- Uncertainties: the `random` module shown is the legacy API; modern Erlang uses `rand`.
- Cross-reference status: Verified
