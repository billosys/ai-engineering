# Competency Questions for Designing for Scalability with Erlang/OTP

> Source: "Designing for Scalability with Erlang/OTP" — Francesco Cesarini & Steve Vinoski (O'Reilly)
> Canonical extraction input: `knowledge/erlang/sources/md/design-scale-erlang-otp/`
> Phase 0 deliverable (per `docs/dev/concept-cards/0010-...-v3.2.md`, Step 0.1).

## Definitional (What is X?)
1. What is an OTP behavior?
2. What is a generic server (gen_server)?
3. What is a supervisor?
4. What is a supervision tree?
5. What is an OTP application?
6. What is a finite state machine behavior (gen_statem)?
7. What is an event handler (gen_event)?
8. What is a release?
9. What is a child specification?
10. What is the error kernel of a system?
11. What is a special process?
12. What is a callback module?
13. What is a process skeleton?

## Relational (How does X relate to Y?)
1. How does a behavior relate to its callback module?
2. How do supervisors relate to the worker processes they manage?
3. How does an application relate to its supervision tree?
4. How does a release relate to the applications it bundles?
5. How do links relate to monitors?
6. How does gen_server message passing work under the hood?
7. How does the sys module relate to OTP behaviors?
8. How does distributed Erlang relate to scaling a system out?

## Procedural (How do I do X?)
1. How do I implement a gen_server callback module?
2. How do I write a supervisor and define its child specifications?
3. How do I structure an OTP application?
4. How do I perform a release upgrade?
5. How do I handle synchronous versus asynchronous messages in a gen_server?
6. How do I implement a finite state machine with gen_statem?
7. How do I trace and inspect an OTP process with the sys module?
8. How do I design a system around the error-kernel pattern?
9. How do I package, start, and configure a release?
10. How do I monitor a production system and provide preemptive support?

## Prerequisite (What before X?)
1. What must I know before implementing a gen_server?
2. What concepts are needed before building a supervision tree?
3. What must I understand before performing release upgrades?
4. What do I need to know before designing distributed architectures?
5. What foundational Erlang concepts underpin the OTP behaviors?

## Diagnostic (What distinguishes X from Y?)
1. What distinguishes a gen_server from a gen_statem?
2. What distinguishes links from monitors?
3. What is the difference between synchronous and asynchronous message passing?
4. What distinguishes a supervisor from a worker process?
5. What is the difference between the one_for_one and one_for_all restart strategies?
6. What distinguishes an OTP application from a release?
