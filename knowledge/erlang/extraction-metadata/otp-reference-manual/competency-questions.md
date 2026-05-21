# Competency Questions for Erlang Reference Manual

> Source: "Erlang Reference Manual" — Ericsson/OTP Team
> Canonical extraction input: `knowledge/erlang/sources/md/otp-reference-manual/`

## Definitional (What is X?)
1. What is an Erlang term?
2. What is an atom in Erlang?
3. What is a tuple?
4. What is a binary and a bitstring?
5. What is an Erlang process?
6. What is a module in Erlang?
7. What is pattern matching in Erlang?
8. What is a guard sequence?
9. What is a fun (anonymous function)?
10. What is a record in Erlang?
11. What is a type specification (-spec)?
12. What is an opaque type?
13. What is a nominal type?
14. What is a macro in Erlang?
15. What is a port in Erlang?

## Relational (How does X relate to Y?)
1. How do links and monitors differ in Erlang process supervision?
2. How does the match operator relate to pattern matching?
3. How do tuple-based records relate to native records?
4. How do atoms, tuples, and lists form the foundation of Erlang's type system?
5. How does the type specification system relate to Dialyzer?
6. How do exit signals propagate between linked processes?
7. How does a module's export attribute relate to its API design?
8. How do short-circuit operators (andalso/orelse) differ from strict boolean operators (and/or)?
9. How do list comprehensions relate to binary and map comprehensions?
10. How does distributed Erlang's node naming relate to EPMD?

## Procedural (How do I do X?)
1. How do I create and spawn a new Erlang process?
2. How do I send and receive messages between processes?
3. How do I construct and use a map in Erlang?
4. How do I define and use a record?
5. How do I write a type specification for a function?
6. How do I use the try-catch expression for error handling?
7. How do I define and expand macros with the preprocessor?
8. How do I write a list comprehension with filters?
9. How do I connect distributed Erlang nodes?
10. How do I use the maybe expression for conditional matching?

## Prerequisite (What before X?)
1. What must I understand before working with Erlang processes?
2. What must I know before writing type specifications?
3. What must I understand before using the bit syntax?
4. What concepts are needed before understanding distributed Erlang?
5. What must I know before using native records?
6. What must I understand before using guards effectively?
7. What must I know before using opaque types?
8. What concepts are needed before understanding code loading and replacement?

## Diagnostic (What distinguishes X from Y?)
1. What distinguishes error, exit, and throw exception classes?
2. What distinguishes a proper list from an improper list?
3. What distinguishes atoms from strings in Erlang?
4. What distinguishes a link from a monitor?
5. What distinguishes structural typing from nominal typing in Erlang?
6. What distinguishes interactive mode from embedded mode for code loading?
7. What distinguishes a case expression from an if expression?
8. What distinguishes compile-time errors from runtime errors?
9. What distinguishes a hidden node from a visible node?
10. What distinguishes tuple-based records from native records?
