# Competency Questions for ERTS (Erlang Runtime System)

> STATUS: complete
> Source: "ERTS User's Guide & Reference" — Ericsson AB / OTP Team
> Canonical extraction input: `knowledge/erlang/sources/md/otp-erts/`

## Definitional (What is X?)
1. What is Erlang monotonic time?
2. What is Erlang system time?
3. What is a time warp in ERTS?
4. What is a match specification?
5. What is an Erlang crash dump?
6. What is the external term format?
7. What is the Erlang distribution protocol?
8. What is EPMD (Erlang Port Mapper Daemon)?
9. What is an Erlang driver?
10. What is a NIF (Native Implemented Function)?
11. What is erts_alloc?
12. What is the Erlang abstract format?
13. What is an escript?
14. What is a distribution carrier?

## Relational (How does X relate to Y?)
1. How does Erlang monotonic time relate to Erlang system time?
2. How does OS system time relate to Erlang system time?
3. How do match specifications relate to ETS and tracing?
4. How does EPMD relate to the distribution protocol?
5. How do drivers relate to NIFs as FFI mechanisms?
6. How does the external term format relate to distribution?
7. How does erts_alloc relate to process heaps and ETS storage?

## Procedural (How do I do X?)
1. How do I interpret an Erlang crash dump?
2. How do I write a match specification?
3. How do I implement a NIF library?
4. How do I implement an Erlang driver?
5. How do I implement an alternative distribution carrier?
6. How do I implement alternative node discovery?
7. How do I start the Erlang runtime system with erl?
8. How do I write and run an escript?
9. How do I configure inet for hostname resolution?

## Prerequisite (What before X?)
1. What must I know before writing a NIF?
2. What must I know before implementing a custom distribution carrier?
3. What must I know before interpreting crash dumps?
4. What must I know before using time warp modes?

## Diagnostic (What distinguishes X from Y?)
1. What distinguishes a NIF from a driver?
2. What distinguishes monotonic time from system time?
3. What distinguishes the three time warp modes?
4. What distinguishes simple code replacement from synchronized code replacement in the distribution?
5. What distinguishes multi-block carriers from single-block carriers in erts_alloc?
6. What distinguishes the erl command flags from emulator flags?
