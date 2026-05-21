# Competency Questions for Erlang Programming Rules and Conventions

> Source: "Program Development Using Erlang — Programming Rules and Conventions"
> — Klas Eriksson, Mike Williams, Joe Armstrong (Ericsson, EPK/NP 95:035)
> Canonical extraction input: `knowledge/erlang/sources/md/programming-rules/README.md`
> Phase 0 deliverable (per `docs/dev/concept-cards/0010-...-v3.2.md`, Step 0.1).

The source is a single-file mini-book: 56 numbered rules across sections 3-8,
plus a common-mistakes list (section 9) and required-documents list (section 10).

## Definitional (What is X?)

1. What is the error kernel of a system?
2. What is a pure function, and what is a side effect?
3. What is a tagged message?
4. What is a tail-recursive server?
5. What is an interface function for a process?
6. What is a tagged return value?
7. What is the process dictionary?
8. What is a record in Erlang?
9. What is a registered process?
10. What is defensive programming?
11. What is the principle of least astonishment?
12. What is an abstract data type / "leaking" private data structure?

## Relational (How does X relate to Y?)

1. How does "separate error handling from normal code" relate to "one role per process"?
2. How do records relate to selectors and constructors?
3. How does tagging messages relate to flushing unknown messages?
4. How do interface functions relate to hiding the message protocol?
5. How does isolating dirty code relate to eliminating side effects?
6. How does the error kernel relate to defensive programming?
7. How do the comment-level conventions relate to documenting each function?

## Procedural (How do I do X?)

1. How do I keep private data structures from leaking out of a module?
2. How do I write a tail-recursive server loop?
3. How should a server handle messages it does not recognize?
4. How do I structure a module's `-export` declarations?
5. How do I do and undo a resource acquisition safely?
6. How should I name variables, functions, and modules?
7. How do I document a function, a data structure, and a file header?
8. How do I write side-effect-free code?

## Prerequisite (What before X?)

1. What must I understand before designing a system's process structure?
2. What must I know before identifying the error kernel?
3. What must I understand before using `catch`/`throw` or the process dictionary?
4. What concepts underlie writing a correct server loop?

## Diagnostic (What distinguishes X from Y?)

1. What distinguishes a tail-recursive server loop from a non-tail-recursive one?
2. What distinguishes failure from returning an error value?
3. What distinguishes clean code from "dirty" code?
4. What distinguishes a deterministic program from a non-deterministic one?
5. What distinguishes the three comment levels (`%`, `%%`, `%%%`)?
6. What distinguishes a tagged return value from an untagged one?
7. What distinguishes the error kernel from ordinary application code?
