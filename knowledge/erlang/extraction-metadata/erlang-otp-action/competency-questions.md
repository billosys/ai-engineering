# Competency Questions for "Erlang and OTP in Action"

> Source: "Erlang and OTP in Action" — Martin Logan, Eric Merritt, Richard Carlsson (Manning)
> Canonical extraction input: `knowledge/erlang/sources/md/erlang-otp-action/`
> Phase 0 deliverable (per `docs/dev/concept-cards/0010-...-v3.2.md`, Step 0.1).

EPUB-origin source: cards cite `book_md_line` / section headings; `pdf_page` is null.

## Definitional (What is X?)

1. What is a process in Erlang?
2. What is the Erlang process model (the actor model)?
3. What is a process link?
4. What is a process monitor?
5. What is trapping exit signals?
6. What is supervision in Erlang/OTP?
7. What is an OTP behaviour?
8. What is the gen_server behaviour?
9. What is a supervisor behaviour?
10. What is a child specification?
11. What is an OTP application?
12. What is the gen_event behaviour?
13. What is ETS (Erlang Term Storage)?
14. What is Mnesia?
15. What is an Erlang release?
16. What is a port?
17. What is a linked-in port driver?
18. What is a NIF (natively implemented function)?
19. What is the magic cookie security system?
20. What is location transparency?
21. What is Jinterface?
22. What is referential transparency?

## Relational (How does X relate to Y?)

1. How do process links relate to supervision?
2. How does a supervisor relate to its child processes?
3. How do OTP applications relate to releases?
4. How does the gen_server behaviour relate to the raw process model?
5. How does Mnesia relate to ETS?
6. How does resource discovery relate to node clustering?
7. How does SASL relate to crash reports and logging?
8. How does the application behaviour relate to the supervision tree?

## Procedural (How do I do X?)

1. How do I create and compile an Erlang module?
2. How do I implement a gen_server callback module?
3. How do I write a supervisor and its child specifications?
4. How do I build and package an Erlang release?
5. How do I start an Erlang node and connect it to a cluster?
6. How do I create and populate Mnesia tables?
7. How do I profile Erlang code with cprof and fprof?
8. How do I integrate C code through a port?
9. How do I implement a NIF?
10. How do I implement a custom gen_event handler?
11. How do I add an HTTP/REST interface to an Erlang service?

## Prerequisite (What before X?)

1. What must I understand before implementing an OTP behaviour?
2. What must I know before working with distributed Erlang?
3. What must I know before using Mnesia for distributed storage?
4. What must I understand before writing a NIF or port driver?
5. What concepts underlie building an OTP release?

## Diagnostic (What distinguishes X from Y?)

1. What distinguishes a port from a NIF from a linked-in driver?
2. What distinguishes the gen_server behaviour from gen_event?
3. What distinguishes a link from a monitor?
4. What distinguishes a synchronous from an asynchronous cache strategy?
5. What distinguishes cprof from fprof?
6. What distinguishes ETS from Mnesia for data storage?
7. What distinguishes an OTP application from an OTP release?
