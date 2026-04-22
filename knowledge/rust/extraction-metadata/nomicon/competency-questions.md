# Competency Questions for The Rustonomicon

## Definitional (What is X?)
1. What is the difference between safe and unsafe Rust?
2. What is undefined behavior in Rust?
3. What are Rust's data layout guarantees (repr)?
4. What are lifetimes and how do they work at a low level?
5. What is variance in Rust's type system?
6. What is PhantomData?
7. What is the ownership-based resource management (OBRM) model?
8. What is unwinding and how does it interact with unsafe code?
9. What are Send and Sync at a fundamental level?
10. What is uninitialized memory and how is it handled safely?

## Procedural (How do I do X?)
11. How do I implement Vec from scratch?
12. How do I implement Arc from scratch?
13. How do I do FFI safely?
14. How do I handle type conversions (casts, coercions, transmute)?
15. How do I write exception-safe unsafe code?

## Diagnostic (What distinguishes X from Y?)
16. What is the difference between safe abstractions and unsafe implementations?
17. What is the difference between repr(C), repr(Rust), and repr(transparent)?
18. What is the difference between coercion and transmute?
