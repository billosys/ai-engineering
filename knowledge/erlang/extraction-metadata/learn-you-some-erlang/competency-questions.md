# Competency Questions for Learn You Some Erlang for Great Good!

> Source: "Learn You Some Erlang for Great Good!" — Fred Hébert
> Canonical extraction input: `knowledge/erlang/sources/md/learn-you-some-erlang/`
> Phase 0 deliverable per `docs/dev/concept-cards/0010-...-v3.2.md`, Step 0.1.
> 54 CQs across 5 types.

## Definitional (What is X?)

1. What is an atom?
2. What is a tuple?
3. What is a list comprehension?
4. What is the bit syntax?
5. What is a module?
6. What is pattern matching?
7. What is a guard?
8. What is tail recursion?
9. What is an anonymous function (fun)?
10. What is a closure?
11. What is a record?
12. What is a map (associative key-value store)?
13. What is a process?
14. What is a link?
15. What is a monitor?
16. What is selective receive?
17. What is the gen_server behaviour?
18. What is a finite-state-machine behaviour (gen_fsm / gen_statem)?
19. What is the gen_event behaviour?
20. What is a supervisor?
21. What is an OTP application?
22. What is an Erlang release?
23. What is an ETS table?
24. What is Mnesia?
25. What is a type specification?
26. What is Dialyzer?
27. What is a distributed Erlang node?

## Relational (How does X relate to Y?)

1. How does fold relate to map and filter?
2. How do links relate to monitors?
3. How does gen_server relate to the client/server pattern?
4. How do supervisors relate to the "let it crash" philosophy?
5. How does an OTP application relate to a release?
6. How do records relate to tuples?
7. How does selective receive relate to the process mailbox?
8. How does Dialyzer relate to type specifications?
9. How do ETS and Mnesia relate?
10. How does tail recursion relate to accumulators?
11. How does a behaviour relate to its callback module?

## Procedural (How do I do X?)

1. How do I create and compile a module?
2. How do I write a recursive function?
3. How do I handle exceptions with try ... catch?
4. How do I spawn a process and send it messages?
5. How do I implement a stateful process?
6. How do I write a gen_server?
7. How do I write a supervisor?
8. How do I structure an OTP application?
9. How do I build an Erlang release?
10. How do I open a TCP socket?
11. How do I write EUnit tests?
12. How do I write Common Test suites?
13. How do I create and use an ETS table?
14. How do I set up a Mnesia database?
15. How do I connect Erlang nodes?
16. How do I write type specs for Dialyzer?

## Prerequisite (What before X?)

1. What must I know before writing a gen_server?
2. What must I understand before using supervisors?
3. What concepts precede building an OTP application?
4. What must I know before doing distributed Erlang?
5. What must I understand before using Dialyzer effectively?
6. What must I know before writing concurrent programs?

## Diagnostic (What distinguishes X from Y?)

1. What distinguishes a list from a tuple?
2. What distinguishes errors, exits, and throws?
3. What distinguishes a link from a monitor?
4. What distinguishes gen_server from a finite-state-machine behaviour?
5. What distinguishes EUnit from Common Test?
6. What distinguishes ETS from DETS?
7. What distinguishes temporary, transient, and permanent child restart?
8. What distinguishes dynamic typing from static typing?
9. What distinguishes spawn from spawn_link?
10. What distinguishes a list comprehension from a binary comprehension?
