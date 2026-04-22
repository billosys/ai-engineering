# Competency Questions for Tokio Tutorial

## Definitional (What is X?)
1. What is Tokio?
2. What is a Tokio task?
3. What is the Tokio runtime?
4. What is tokio::select!?
5. What is a Stream in Tokio?
6. What is AsyncRead/AsyncWrite?
7. What is the Future trait?
8. What is a Waker?

## Relational (How does X relate to Y?)
9. How does tokio::spawn relate to task lifetimes and Send bounds?
10. How does Arc<Mutex> relate to shared state between tasks?
11. How do channels relate to message passing between tasks?
12. How does the Future trait relate to async/await?
13. How does select! relate to cancellation?

## Procedural (How do I do X?)
14. How do I set up a Tokio project?
15. How do I spawn concurrent tasks in Tokio?
16. How do I share state between Tokio tasks?
17. How do I use channels for message passing in Tokio?
18. How do I do async I/O with Tokio?
19. How do I implement protocol framing?
20. How do I implement a Future manually?
21. How do I use select! to multiplex operations?
22. How do I work with streams?

## Diagnostic (What distinguishes X from Y?)
23. What is the difference between std::sync::Mutex and tokio::sync::Mutex?
24. What is the difference between mpsc and oneshot channels?
25. When should I use Tokio vs blocking I/O?
