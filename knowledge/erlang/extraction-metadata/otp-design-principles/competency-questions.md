# Competency Questions for OTP Design Principles (System Documentation)

> STATUS: complete
> Source: "OTP Design Principles" — Ericsson AB / OTP Team
> Canonical extraction input: `knowledge/erlang/sources/md/otp-design-principles/`

## Definitional (What is X?)
1. What is a supervision tree?
2. What is a behaviour in OTP?
3. What is a callback module?
4. What is gen_server?
5. What is gen_statem?
6. What is gen_event?
7. What is a supervisor in OTP?
8. What is a child specification?
9. What is a restart strategy?
10. What is an OTP application?
11. What is a release in OTP?
12. What is a special process?
13. What is a distributed application?
14. What is an included application?
15. What is release handling?

## Relational (How does X relate to Y?)
1. How do workers and supervisors relate in a supervision tree?
2. How does a behaviour module relate to a callback module?
3. How does gen_server:call relate to handle_call?
4. How does gen_server:cast relate to handle_cast?
5. How do restart strategies affect child processes?
6. How does the application controller relate to the application master?
7. How do .app files relate to .rel files in a release?
8. How do .appup files relate to .relup files?
9. How does gen_statem's state_functions mode differ from handle_event_function?
10. How do event handlers relate to event managers in gen_event?

## Procedural (How do I do X?)
1. How do I implement a gen_server callback module?
2. How do I implement a gen_statem state machine?
3. How do I implement a gen_event event handler?
4. How do I define a supervisor with child specifications?
5. How do I create an OTP application?
6. How do I create a release?
7. How do I perform a release upgrade?
8. How do I write an .appup file?
9. How do I implement a special process using proc_lib?
10. How do I configure distributed application failover?
11. How do I use postponing events in gen_statem?
12. How do I use state enter calls in gen_statem?

## Prerequisite (What before X?)
1. What must I know before implementing a gen_server?
2. What must I know before designing a supervision tree?
3. What must I know before using gen_statem?
4. What must I know before creating a release?
5. What must I know before implementing release handling?
6. What must I know before writing a special process?

## Diagnostic (What distinguishes X from Y?)
1. What distinguishes gen_server from gen_statem?
2. What distinguishes one_for_one from one_for_all restart strategies?
3. What distinguishes permanent, transient, and temporary restart types?
4. What distinguishes a library application from a regular application?
5. What distinguishes synchronous (call) from asynchronous (cast) requests?
6. What distinguishes state_timeout from event_timeout in gen_statem?
7. What distinguishes a primary application from an included application?
8. What distinguishes failover from takeover in distributed applications?
9. What distinguishes simple code replacement from synchronized code replacement?
10. What distinguishes a functional module from a residence module?
