# Competency Questions for OTP Efficiency Guide

> STATUS: complete — Phase 0 (45 CQs).
> Source: "Erlang Efficiency Guide" — Ericsson/OTP Team
> Canonical extraction input: `knowledge/erlang/sources/md/otp-efficiency-guide/`

## Definitional (What is X?)
1. What is a refc binary?
2. What is a heap binary?
3. What is a sub binary?
4. What is a match context in binary matching?
5. What is a literal pool in Erlang?
6. What is a small map vs. a large map?
7. What is the HAMT data structure used for large maps?
8. What is loss of sharing when copying terms?
9. What is the `bin_opt_info` compiler option?
10. What is the `recv_opt_info` compiler option?
11. What is erlperf?

## Relational (How does X relate to Y?)
1. How does `fprof` compare to `eprof` and `cprof`?
2. How does wall-clock time measurement relate to CPU time measurement for benchmarking?
3. How do ETS tables compare to Mnesia for non-persistent storage?
4. How does `maps:get/2` compare to map matching syntax for efficiency?
5. How do records compare to maps for performance?
6. How does the `++` operator relate to list copying?
7. How does `ets:select/2` compare to `ets:tab2list/1` for data retrieval?
8. How do body-recursive and tail-recursive list functions compare in performance?
9. How does `erlang:send_after/3` compare to the `timer` module?

## Procedural (How do I do X?)
1. How do I efficiently construct a binary by appending data?
2. How do I profile an Erlang application to find performance bottlenecks?
3. How do I benchmark two implementations to determine which is faster?
4. How do I optimize receive operations to avoid scanning the full message queue?
5. How do I efficiently use maps as an alternative to records?
6. How do I create an index table for efficient ETS lookups on non-key fields?
7. How do I avoid unnecessary list flattening?
8. How do I tune the initial heap size for short-lived processes?
9. How do I avoid accidental data copying when spawning processes with closures?
10. How do I use Mnesia secondary indexes for efficient lookups?
11. How do I use `ets:select/2` instead of `ets:tab2list/1`?

## Prerequisite (What before X?)
1. What must I understand before optimizing binary construction?
2. What must I know before choosing between ETS and Mnesia?
3. What must I understand before profiling a large system?
4. What memory model concepts are needed to understand Erlang data type sizes?

## Diagnostic (What distinguishes X from Y?)
1. What distinguishes a refc binary from a heap binary?
2. What distinguishes `ets:select/2` from `ets:match/2`?
3. What distinguishes `maps:update/3` from `maps:put/3`?
4. What distinguishes the `:=` operator from the `=>` operator in map updates?
5. What distinguishes a small map (flatmap) from a large map (HAMT)?
6. What distinguishes Mnesia transactions from dirty operations?
7. What distinguishes pattern matching errors from clause ordering issues?
8. What distinguishes `lists:flatten/1` from `lists:append/1`?
9. What distinguishes `size/1` from `tuple_size/1` and `byte_size/1`?
10. What distinguishes `length/1` from constant-time size operations?
