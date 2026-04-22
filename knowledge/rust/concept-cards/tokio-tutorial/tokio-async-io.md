---
concept: Tokio Async I/O
slug: tokio-async-io
category: async-io
subcategory: null
tier: intermediate
source: "Tokio Tutorial"
source_slug: tokio-tutorial
authors: "The Tokio Team"
chapter: "I/O"
chapter_number: 6
pdf_page: null
section: "AsyncRead and AsyncWrite"
extraction_confidence: high
aliases:
  - "async read write"
  - "tokio io"
  - "asynchronous io in tokio"
  - "echo server"
prerequisites:
  - tokio-spawn
  - tokio-runtime
extends: []
related:
  - tokio-framing
  - future-trait-in-depth
contrasts_with: []
answers_questions:
  - "How does I/O work in Tokio compared to std?"
  - "What are AsyncRead and AsyncWrite?"
  - "How do I split a TcpStream into a reader and writer?"
  - "Why should I allocate buffers on the heap in async tasks?"
  - "How do I handle EOF correctly when reading from a socket?"
---

# Quick Definition

Tokio's I/O mirrors `std` but operates asynchronously through the `AsyncRead` and `AsyncWrite` traits, used via extension methods on `AsyncReadExt` and `AsyncWriteExt`. Key operations include `read()`, `read_to_end()`, `write()`, and `write_all()`. Helper functions like `io::copy` and `io::split` simplify common patterns. Buffers in async tasks should be heap-allocated (`Vec<u8>`) because stack arrays bloat the task's future state.

# Core Definition

"I/O in Tokio operates in much the same way as in `std`, but asynchronously. There is a trait for reading (`AsyncRead`) and a trait for writing (`AsyncWrite`). Specific types implement these traits as appropriate (`TcpStream`, `File`, `Stdout`). `AsyncRead` and `AsyncWrite` are also implemented by a number of data structures, such as `Vec<u8>` and `&[u8]`." (Ch. 6, opening)

The traits are not called directly (similar to how `Future::poll` is not called directly). Instead, the extension traits `AsyncReadExt` and `AsyncWriteExt` provide ergonomic async methods. All methods are `async` and must be used with `.await`.

# Prerequisites

- **tokio-spawn** -- async I/O is performed within spawned tasks; understanding the `Send` bound and task lifecycle is important for buffer allocation decisions
- **tokio-runtime** -- the runtime drives I/O readiness notifications that make async reads and writes possible

# Key Properties

1. `AsyncReadExt::read(&mut buf)` reads data into a buffer and returns the number of bytes read; `Ok(0)` means the stream is closed (EOF)
2. `AsyncReadExt::read_to_end(&mut vec)` reads all bytes until EOF into a `Vec<u8>`
3. `AsyncWriteExt::write(&buf)` writes some bytes and returns the count written (may not write all)
4. `AsyncWriteExt::write_all(&buf)` writes the entire buffer, retrying as needed
5. `io::copy(&mut reader, &mut writer)` copies all bytes from reader to writer
6. `io::split(stream)` splits any `AsyncRead + AsyncWrite` into independent reader/writer handles using `Arc` + `Mutex` internally
7. `TcpStream::split(&self)` is a zero-cost alternative that borrows the stream, but both handles must stay on the same task
8. `TcpStream::into_split(self)` consumes the stream and returns handles that can move across tasks (using only an `Arc`, no `Mutex`)
9. Forgetting to break on `Ok(0)` from `read()` causes a 100% CPU infinite loop -- the read returns immediately and the loop spins forever
10. Buffers used across `.await` should be heap-allocated (`vec![0; 1024]`) because stack arrays are stored inline in the task struct, bloating its size

# Construction / Recognition

## To Build an Echo Server with io::copy:
1. Bind a `TcpListener` and accept connections in a loop
2. For each connection, spawn a task
3. Split the socket with `socket.split()` (zero-cost, same task) or `io::split(socket)` (cross-task)
4. Call `io::copy(&mut rd, &mut wr).await` to pipe reads back as writes

## To Build an Echo Server Manually:
1. Allocate a heap buffer: `let mut buf = vec![0; 1024]`
2. Loop: `match socket.read(&mut buf).await`
3. On `Ok(0)`: return (EOF, connection closed)
4. On `Ok(n)`: call `socket.write_all(&buf[..n]).await`
5. On `Err(_)`: return (socket error)

# Context & Application

The distinction between `io::split` and `TcpStream::split` is important for performance. The generic `io::split` works on any `AsyncRead + AsyncWrite` but uses `Arc` and `Mutex` internally, adding overhead. When reader and writer stay on the same task, `TcpStream::split` borrows the stream at zero cost. When handles must move to different tasks, `TcpStream::into_split` uses only an `Arc` (no `Mutex`).

Buffer allocation strategy matters for async tasks. All data that lives across `.await` calls is stored in the task's future struct. A stack buffer (e.g., `[u8; 4096]`) stored inline makes the future very large (page-sized), leading to awkward allocation sizes. Using `vec![0; 1024]` places the buffer on the heap, keeping the future struct small with just a pointer, length, and capacity.

The `Ok(0)` EOF handling is a common source of bugs. "Forgetting to break from the read loop on EOF is a common source of bugs" and "usually results in a 100% CPU infinite loop situation."

# Examples

**Example 1** (Ch. 6, "Using io::copy()"): Echo server using `TcpStream::split` and `io::copy`:
```rust
tokio::spawn(async move {
    let (mut rd, mut wr) = socket.split();
    if io::copy(&mut rd, &mut wr).await.is_err() {
        eprintln!("failed to copy");
    }
});
```

**Example 2** (Ch. 6, "Manual copying"): Echo server with explicit read/write loop:
```rust
let mut buf = vec![0; 1024];
loop {
    match socket.read(&mut buf).await {
        Ok(0) => return,  // EOF: remote closed
        Ok(n) => {
            if socket.write_all(&buf[..n]).await.is_err() {
                return;
            }
        }
        Err(_) => return,
    }
}
```

**Example 3** (Ch. 6, "Splitting a reader + writer"): Using `io::split` for cross-task reader/writer:
```rust
let (mut rd, mut wr) = io::split(socket);
tokio::spawn(async move {
    wr.write_all(b"hello\r\n").await?;
    Ok::<_, io::Error>(())
});
let mut buf = vec![0; 128];
loop {
    let n = rd.read(&mut buf).await?;
    if n == 0 { break; }
    println!("GOT {:?}", &buf[..n]);
}
```

# Relationships

## Builds Upon
- **tokio-spawn** -- I/O operations run within spawned tasks; buffer allocation and `Send` concerns apply
- **tokio-runtime** -- the runtime provides the I/O driver that makes async reads/writes non-blocking

## Enables
- **tokio-framing** -- framing builds directly on the read/write primitives covered here

## Related
- **future-trait-in-depth** -- `AsyncRead`/`AsyncWrite` are analogous to `Future` in that the low-level poll methods are not called directly

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Not handling `Ok(0)` from `read()`, causing an infinite loop.
  **Correction**: Always check for `Ok(0)` and break/return from the read loop. This signals the remote peer closed the connection.

- **Error**: Trying to pass both `&mut socket` as reader and writer to `io::copy`.
  **Correction**: Split the socket first. Use `socket.split()` for same-task usage or `io::split(socket)` for cross-task usage.

- **Error**: Using a large stack-allocated buffer (`[u8; 4096]`) in an async task.
  **Correction**: Use `vec![0; 1024]` (heap allocation). Stack buffers are stored inline in the task's future struct, making it page-sized and inefficient.

# Common Confusions

- **Confusion**: Thinking `io::split` and `TcpStream::split` are interchangeable.
  **Clarification**: `io::split` is generic but uses `Arc` + `Mutex` internally. `TcpStream::split` is zero-cost but both handles must stay on the same task. `TcpStream::into_split` moves handles across tasks using only `Arc`.

- **Confusion**: Thinking `write()` always writes the entire buffer.
  **Clarification**: `write()` may write only a prefix of the buffer, returning the count. Use `write_all()` to guarantee the entire buffer is written.

# Source Reference

Chapter 6: I/O. Covers `AsyncRead`/`AsyncWrite` traits and extension methods (`read`, `read_to_end`, `write`, `write_all`), helper functions (`io::copy`, `io::split`), echo server implementation (both `io::copy` and manual approaches), splitting reader/writer handles, buffer allocation for async tasks, and EOF handling.

# Verification Notes

- Definition source: Directly from Ch. 6 opening paragraph and "AsyncRead and AsyncWrite" section
- Key Properties: All from explicit statements and code examples in the chapter
- Confidence rationale: HIGH -- the source provides complete echo server implementations with detailed commentary
- Uncertainties: None for the core content
- Cross-reference status: tokio-spawn and tokio-runtime from Agent A; future-trait-in-depth from Agent C; tokio-framing from this extraction set
