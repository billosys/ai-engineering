# Competency Questions for Stuff Goes Bad: Erlang in Anger

> Source: "Stuff Goes Bad: Erlang in Anger" — Fred Hébert (Heroku)
> Canonical extraction input: `knowledge/erlang/sources/md/erlang-in-anger/`
> Phase 0 deliverable per `docs/dev/concept-cards/0010-...-v3.2.md`, Step 0.1.
> 48 CQs across 5 types.

## Definitional (What is X?)

1. What is the "let it crash" philosophy?
2. What is an OTP application?
3. What is the difference between a library application and a regular OTP application?
4. What is an OTP release?
5. What is an app file (`.app` / `.app.src`)?
6. What is back-pressure?
7. What is load-shedding?
8. What is a *true bottleneck*?
9. What is an Erlang crash dump?
10. What is a reference-counted (refc) binary?
11. What is a reduction?
12. What is scheduler wall time / scheduler utilization?
13. What is a port (the Erlang data type)?
14. What is the Job Control Mode (JCL)?
15. What is memory fragmentation in the Erlang VM?

## Relational (How does X relate to Y?)

1. How do supervisor restart strategies reflect the relationships between child processes?
2. How does an OTP application's directory structure differ from an OTP release's?
3. How does back-pressure relate to load-shedding?
4. How do pid specifications and trace patterns combine to determine what gets traced?
5. How does scheduler utilization relate to OS-reported CPU usage?
6. How does `erlang:memory()` relate to the memory the OS reports for the VM?
7. How do per-scheduler sub-allocators relate to `mseg_alloc` / `sys_alloc`?
8. How does runaway process memory growth relate to refc binary leaks?

## Procedural (How do I do X?)

1. How do I dive into an unfamiliar Erlang code base?
2. How do I build an OTP release with `rebar3`?
3. How do I specify dependencies in `rebar.config`?
4. How do I connect to a running remote Erlang node?
5. How do I get a global view of the VM's memory?
6. How do I find the top memory-consuming processes on a node?
7. How do I read and analyze a crash dump?
8. How do I detect a refc binary memory leak?
9. How do I monitor long garbage collections?
10. How do I find CPU and scheduler hogs?
11. How do I trace function calls safely in production with `recon_trace`?
12. How do I safely inspect a process in a production system?
13. How do I control where a crash dump is written?
14. How do I shed load by randomly dropping messages?

## Prerequisite (What before X?)

1. What must I understand before navigating an OTP application's supervision tree?
2. What concepts must I know before diagnosing memory leaks?
3. What must I know before applying back-pressure via synchronous calls?
4. What must I understand before tuning the VM's memory allocation strategies?
5. What must I know before tracing a production node?

## Diagnostic (What distinguishes X from Y?)

1. What distinguishes a raw Erlang code base from an OTP application?
2. What distinguishes back-pressure from load-shedding?
3. What distinguishes a queue buffer from a stack buffer?
4. What distinguishes a memory leak from memory fragmentation?
5. What distinguishes the `permanent`, `transient`, and `temporary` application start types?
6. What distinguishes `recon:proc_count/2` from `recon:proc_window/3`?
7. What distinguishes a heap (ProcBin) binary from a refc binary?
8. Why can't you trust `top` / `htop` for Erlang CPU usage?
