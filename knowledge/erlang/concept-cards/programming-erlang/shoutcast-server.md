---
# === CORE IDENTIFICATION ===
concept: SHOUTcast Server
slug: shoutcast-server

# === CLASSIFICATION ===
category: distribution
subcategory: socket-programming
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Programming with Sockets"
chapter_number: 17
pdf_page: null
section: "A SHOUTcast Server"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "streaming audio server"
  - "SHOUTcast protocol server"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-tcp-module
  - parallel-server
  - spawn
extends:
  - parallel-server
related:
  - active-and-passive-sockets
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I build a streaming audio server in Erlang?"
  - "What is the SHOUTcast protocol?"
  - "How is a parallel server used in a real application?"
---

# Quick Definition

A SHOUTcast server is a streaming-audio server that sends MP3- or AAC-encoded data to media-player clients over HTTP. The chapter builds one in Erlang as a worked example of a parallel TCP server.

# Core Definition

"SHOUTcast is a protocol developed by the folks at Nullsoft for streaming audio data. SHOUTcast sends MP3- or AAC-encoded audio data using HTTP as the transport protocol" ("A SHOUTcast Server"). The protocol is simple: a client (such as XMMS, Winamp, or iTunes) sends an HTTP `GET` request including the `Icy-MetaData:1` header; the server responds and then continuously streams audio data, periodically interleaving metadata. The Erlang implementation is built as a parallel server: it makes a playlist of song titles, spawns a song server process that knows about all the music, and spawns one connection-handling process per client using the parallel-server technique. For each audio file it strips the embedded ID3 tags and streams only the audio data.

# Prerequisites

- **gen_tcp module** — The server listens and accepts connections over TCP.
- **Parallel server** — The SHOUTcast server is a direct application of the parallel-server pattern.
- **spawn** — A new process is spawned per connection and for the song server.

# Key Properties

1. Uses HTTP as the transport protocol for streaming MP3/AAC audio.
2. Built as a parallel server so several streams can be served simultaneously.
3. A dedicated song-server process holds the playlist and chooses audio files at random.
4. Each connection is handled by its own spawned process.
5. ID3 tags are stripped from audio files so only the audio data is streamed.
6. Accepted sockets are reconfigured with `inet:setopts(Socket, [{packet,0}, binary, {nodelay,true}, {active, true}])`.

# Construction / Recognition

## To build the SHOUTcast server:
1. Call `gen_tcp:listen(Port, ...)` to create the listening socket.
2. `spawn` a song-server process that knows the playlist.
3. `spawn` a `par_connect(Listen, PidSongServer)` process.
4. In `par_connect`, accept a connection, immediately spawn the next acceptor, set socket options with `inet:setopts`, and handle the request.
5. Parse the HTTP/SHOUTcast request, then stream audio data (with ID3 tags removed) to the client.

# Context & Application

- **Typical contexts**: Internet radio and streaming-audio services.
- **Common applications**: Demonstrates how the parallel-server pattern scales to a real, continuously streaming application.
- **Historical/stylistic notes**: Presented as the chapter's capstone — "using our newly acquired skills in socket programming."

# Examples

**Example 1** ("The SHOUTcast Protocol"): an XMMS client sends `GET / HTTP/1.1`, `Host: localhost`, `User-Agent: xmms/1.2.10`, `Icy-MetaData:1`.

**Example 2** ("Pseudocode for the SHOUTcast Server"): `start_parallel_server/1` listens, spawns `songs()` as the song server, and spawns `par_connect(Listen, PidSongServer)`.

# Relationships

## Builds Upon
- **Parallel server** — The SHOUTcast server is the parallel-server pattern applied to audio streaming.

## Related
- **Active and passive sockets** — Accepted streaming sockets are set to `{active, true}` mode.

# Common Errors

- **Error**: Streaming ID3 tag bytes along with audio data.
  **Correction**: Strip ID3 tags before streaming; in practice players work better when only audio data is sent.

- **Error**: Spawning the next acceptor after handling the request.
  **Correction**: Spawn the next `par_connect` immediately after `accept` returns so new clients are not blocked.

# Common Confusions

- **Confusion**: Thinking SHOUTcast uses a custom transport protocol.
  **Clarification**: SHOUTcast streams audio over ordinary HTTP, with metadata interleaved.

# Source Reference

Chapter 17: "Programming with Sockets", section "A SHOUTcast Server", subsections "The SHOUTcast Protocol", "How the SHOUTcast Server Works", and "Pseudocode for the SHOUTcast Server".

# Verification Notes

- Definition source: Direct quotes from "A SHOUTcast Server" and subsections.
- Confidence rationale: HIGH — the protocol and server structure are explicitly described; full code is in downloadable sources.
- Uncertainties: Full implementation details are in external source files, not the chapter text.
- Cross-reference status: Verified; canonical slugs used.
- Re-extraction notes: Fresh extraction.
