---
concept: Tokio Framing
slug: tokio-framing
category: networking
subcategory: null
tier: advanced
source: "Tokio Tutorial"
source_slug: tokio-tutorial
authors: "The Tokio Team"
chapter: "Framing"
chapter_number: 7
pdf_page: null
section: "Buffered reads"
extraction_confidence: high
aliases:
  - "protocol framing"
  - "tokio framing"
  - "buffered io"
  - "connection abstraction"
prerequisites:
  - tokio-async-io
extends:
  - tokio-async-io
related:
  - tokio-streams
contrasts_with: []
answers_questions:
  - "What is framing and why is it needed for protocols?"
  - "How do I implement buffered reads with BytesMut?"
  - "Why is BytesMut better than Vec<u8> for protocol buffers?"
  - "How do I build a Connection abstraction over TcpStream?"
  - "How does BufWriter reduce write syscalls?"
---

# Quick Definition

Framing is the process of converting a raw byte stream into a stream of discrete frames -- protocol-level units of data transmitted between peers. A `Connection` struct wraps a `TcpStream` with a `BytesMut` read buffer and a `BufWriter` for write buffering, implementing `read_frame()` and `write_frame()` to handle partial reads, multi-frame reads, and efficient writes. This pattern is the foundation for implementing any protocol (Redis, HTTP, etc.) over TCP in Tokio.

# Core Definition

"Framing is the process of taking a byte stream and converting it to a stream of frames. A frame is a unit of data transmitted between two peers." (Ch. 7, opening)

A single `TcpStream::read()` may return an arbitrary amount of data: a partial frame, an entire frame, or multiple frames. The framing layer must buffer incoming data, attempt to parse frames from the buffer, and manage partial data across multiple reads. The `Connection` struct encapsulates this:

```rust
pub struct Connection {
    stream: BufWriter<TcpStream>,
    buffer: BytesMut,
}
```

The `read_frame()` method loops: try to parse a frame from the buffer; if insufficient data, read more from the socket; if `read` returns 0 with data in the buffer, return an error ("connection reset by peer"); if the buffer is empty on EOF, return `None`.

# Prerequisites

- **tokio-async-io** -- framing builds directly on `AsyncRead`/`AsyncWrite`, `read()`/`write_all()`, and the buffering concepts from Ch. 6

# Key Properties

1. A single `TcpStream::read()` may return a partial frame, a complete frame, or multiple frames -- the framing layer must handle all three cases
2. `BytesMut` is used as the read buffer; it tracks capacity and cursor position internally, avoiding manual cursor management needed with `Vec<u8>`
3. `BytesMut` capacity is uninitialized (unlike `Vec<u8>` which must be zero-filled), avoiding the cost of initialization
4. `read_buf(&mut self.buffer)` automatically updates `BytesMut`'s internal cursor, unlike `read()` which requires manual cursor tracking
5. The `Buf` trait provides "byte iterator" style APIs (e.g., `get_u8()`) that advance an internal cursor -- used with `std::io::Cursor<&[u8]>` for parsing
6. Parsing is two-phase: first `Frame::check()` to verify a complete frame is buffered (advancing cursor to find the end), then `Frame::parse()` to extract it
7. After successful parsing, `self.buffer.advance(len)` discards the consumed bytes from the buffer
8. `BufWriter<TcpStream>` buffers writes to reduce syscalls; individual `write_u8()` and `write_all()` calls go to the buffer, not directly to the socket
9. `flush()` must be called after writing a frame to ensure buffered data reaches the socket
10. The frame type is purely data (no semantics) -- command parsing happens at a higher layer

# Construction / Recognition

## To Implement read_frame():
1. Loop: attempt to parse a frame from `self.buffer` via `parse_frame()`
2. If a frame is parsed, return it
3. Otherwise, call `self.stream.read_buf(&mut self.buffer).await?`
4. If `read_buf` returns 0 and buffer is empty: return `Ok(None)` (clean EOF)
5. If `read_buf` returns 0 and buffer is non-empty: return `Err` (connection reset mid-frame)
6. Continue the loop to try parsing again with the new data

## To Implement parse_frame():
1. Create a `Cursor<&[u8]>` over `self.buffer`
2. Call `Frame::check(&mut cursor)` -- if `Err(Incomplete)`, return `Ok(None)` (need more data)
3. Record `cursor.position()` as the frame length
4. Reset cursor to 0 and call `Frame::parse(&mut cursor)` to extract the frame
5. Call `self.buffer.advance(len)` to discard consumed bytes

## To Implement write_frame():
1. Match on the frame type and write the protocol encoding (type prefix, length, data, CRLF)
2. Use `write_u8()`, `write_all()` for individual components
3. Call `self.stream.flush().await` to ensure all buffered data is sent

# Context & Application

The `BytesMut` + `read_buf` combination eliminates two pain points of manual buffered I/O with `Vec<u8>`: (1) no manual cursor tracking -- `BufMut` advances the internal cursor automatically when `read_buf` writes to it, and (2) no zero-initialization cost -- `BytesMut` capacity is uninitialized, which is safe because the abstraction prevents reading uninitialized memory.

The contrast is shown explicitly in the tutorial: with `Vec<u8>`, you need a `cursor: usize` field, must pass `&mut self.buffer[self.cursor..]` to `read()`, manually increment the cursor, and manage buffer growth. With `BytesMut`, you simply call `self.stream.read_buf(&mut self.buffer).await`.

For writes, `BufWriter` wraps the `TcpStream` and intercepts `write` calls, storing data in an internal buffer. This is critical because frame encoding involves many small writes (`write_u8(b'+')`, then `write_all(data)`, then `write_all(b"\r\n")`); without buffering, each would be a separate syscall. The trade-off is that `flush()` must be called explicitly to ensure data reaches the socket.

The alternative of deferring `flush()` to the caller (rather than calling it at the end of `write_frame()`) would allow batching multiple small frames into a single syscall but complicates the API. Mini-Redis chooses simplicity.

# Examples

**Example 1** (Ch. 7, "Buffered reads"): The `read_frame` loop with `BytesMut`:
```rust
pub async fn read_frame(&mut self) -> Result<Option<Frame>> {
    loop {
        if let Some(frame) = self.parse_frame()? {
            return Ok(Some(frame));
        }
        if 0 == self.stream.read_buf(&mut self.buffer).await? {
            if self.buffer.is_empty() {
                return Ok(None);
            } else {
                return Err("connection reset by peer".into());
            }
        }
    }
}
```

**Example 2** (Ch. 7, "Parsing"): Two-phase parsing with `Cursor` and `Buf`:
```rust
fn parse_frame(&mut self) -> Result<Option<Frame>> {
    let mut buf = Cursor::new(&self.buffer[..]);
    match Frame::check(&mut buf) {
        Ok(_) => {
            let len = buf.position() as usize;
            buf.set_position(0);
            let frame = Frame::parse(&mut buf)?;
            self.buffer.advance(len);
            Ok(Some(frame))
        }
        Err(Incomplete) => Ok(None),
        Err(e) => Err(e.into()),
    }
}
```

**Example 3** (Ch. 7, "Buffered writes"): Writing a frame with `BufWriter`:
```rust
async fn write_frame(&mut self, frame: &Frame) -> io::Result<()> {
    match frame {
        Frame::Simple(val) => {
            self.stream.write_u8(b'+').await?;
            self.stream.write_all(val.as_bytes()).await?;
            self.stream.write_all(b"\r\n").await?;
        }
        Frame::Bulk(val) => {
            self.stream.write_u8(b'$').await?;
            self.write_decimal(val.len() as u64).await?;
            self.stream.write_all(val).await?;
            self.stream.write_all(b"\r\n").await?;
        }
        // ... other frame types
        _ => {}
    }
    self.stream.flush().await;
    Ok(())
}
```

# Relationships

## Builds Upon
- **tokio-async-io** -- framing uses `AsyncRead`/`AsyncWrite`, `read_buf`, `write_all`, `BufWriter`, and the buffering concepts from Ch. 6

## Enables
- **tokio-streams** -- framing produces a logical stream of frames that can be consumed as an async stream

## Related
- None explicitly beyond the above

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Using `read()` with `Vec<u8>` and forgetting to track the cursor position.
  **Correction**: Use `BytesMut` with `read_buf()`, which manages the cursor automatically. If using `Vec<u8>`, maintain a `cursor: usize` and always read into `&mut buffer[cursor..]`.

- **Error**: Not checking for "connection reset by peer" when `read_buf` returns 0 with a non-empty buffer.
  **Correction**: If `read` returns 0 (EOF) but the buffer still has data, a partial frame was in flight when the peer disconnected. Return an error rather than silently dropping the incomplete data.

- **Error**: Forgetting to call `flush()` after writing a frame to a `BufWriter`.
  **Correction**: Always call `self.stream.flush().await` after encoding a frame. Without this, the data may remain in the `BufWriter`'s internal buffer and never reach the socket.

# Common Confusions

- **Confusion**: Thinking `BytesMut` and `Vec<u8>` are interchangeable for buffered reads.
  **Clarification**: `BytesMut` avoids two costs: (1) zero-initialization -- `vec![0; 4096]` writes zeros to every byte, while `BytesMut::with_capacity(4096)` leaves capacity uninitialized; (2) manual cursor management -- `read_buf` advances `BytesMut`'s internal cursor automatically.

- **Confusion**: Thinking `write_u8` and `write_all` go directly to the socket when using `BufWriter`.
  **Clarification**: `BufWriter` intercepts writes into an internal buffer. Only `flush()` or a full internal buffer triggers an actual write to the underlying `TcpStream`. "It would not be advisable to issue single byte writes without the intermediate buffer."

- **Confusion**: Thinking framing and command parsing are the same layer.
  **Clarification**: "The frame only consists of data without any semantics. The command parsing and implementation happen at a higher level." The `Connection` produces `Frame` values; a separate layer interprets them as commands.

# Source Reference

Chapter 7: Framing. Covers the framing concept, `Connection` struct with `BytesMut` read buffer, `read_frame()` loop with `read_buf`, `Buf`/`BufMut` traits, two-phase parsing (`Frame::check` + `Frame::parse`), `BufWriter` for write buffering, and `write_frame()` implementation. The Redis protocol frame types and HTTP frame analogy illustrate the general applicability of the pattern.

# Verification Notes

- Definition source: Directly from Ch. 7 opening paragraph
- Key Properties: All from explicit statements and code examples throughout the chapter
- Confidence rationale: HIGH -- the source provides complete implementation with detailed comparison to the `Vec<u8>` alternative
- Uncertainties: The `Frame::Array` variant is left unimplemented in the tutorial's `write_frame`; the full implementation is linked externally
- Cross-reference status: tokio-async-io from this extraction set; tokio-streams from Agent C
