---
concept: Deno HTTP Server
slug: deno-http-server
category: server
subcategory: HTTP
tier: intermediate
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/http_server.md"
chapter_number: null
pdf_page: null
section: "Writing an HTTP Server"
extraction_confidence: high
aliases:
  - "Deno.serve"
  - "deno serve"
  - "Deno HTTP server API"
prerequisites:
  - deno-configuration
extends: []
related:
  - deno-web-framework-support
  - deno-opentelemetry-support
contrasts_with: []
answers_questions:
  - "How do I create an HTTP server in Deno?"
  - "What is Deno.serve?"
  - "How does Deno handle WebSockets?"
---

# Quick Definition

`Deno.serve` is Deno's built-in HTTP server API that takes a handler function, supports HTTP/1.1 and HTTP/2, provides automatic body compression, WebSocket upgrades, HTTPS via TLS certificates, and streaming responses.

# Core Definition

Deno's built-in HTTP server is accessed through the `Deno.serve()` API, which takes a handler function that receives a `Request` and returns a `Response` (or `Promise<Response>`). It supports both HTTP/1.1 and HTTP/2 automatically, with no additional configuration needed for HTTP/2.

Key features:

- **Handler-based**: A single function receives requests and returns responses using standard Web API types (`Request`, `Response`).
- **Configurable port**: Default port is `8000`; customizable via `{ port: N }` options.
- **HTTPS**: Provide `cert` and `key` options with TLS certificate and private key contents.
- **Automatic compression**: Response bodies are automatically compressed with gzip or brotli when the client supports it, the content type is compressible, and the body exceeds 64 bytes.
- **Streaming responses**: Response bodies can be `ReadableStream` instances for server-sent events or long-running streams.
- **WebSocket support**: `Deno.upgradeWebSocket(req)` upgrades an HTTP request to a WebSocket connection, returning a standard `WebSocket` object.
- **Default fetch export**: An alternative pattern where a module exports a `fetch` function, runnable via `deno serve`.

# Prerequisites

- `deno-configuration` — server may use configuration for tasks and permissions

# Key Properties

1. **Web-standard APIs**: Uses `Request` and `Response` from the Fetch API — no framework-specific types.
2. **HTTP/2 automatic**: HTTP/2 is handled transparently; no special server setup required.
3. **Compression conditions**: Auto-compression requires: client `Accept-Encoding` support, compressible `Content-Type`, body > 64 bytes, and no existing `Content-Encoding`, `Content-Range`, or `Cache-Control: no-transform`.
4. **WebSocket limitation**: WebSockets are only supported on HTTP/1.1 currently.
5. **`deno serve` command**: An alternative to `Deno.serve()` that uses a default `fetch` export pattern with `Deno.ServeDefaultExport` interface.

# Construction / Recognition

Hello World server:

```ts
Deno.serve((_req) => {
  return new Response("Hello, World!");
});
```

Run with: `deno run --allow-net server.ts`

Server with options:

```ts
Deno.serve({ port: 4242, hostname: "0.0.0.0" }, handler);
```

WebSocket upgrade:

```ts
Deno.serve((req) => {
  if (req.headers.get("upgrade") != "websocket") {
    return new Response(null, { status: 426 });
  }
  const { socket, response } = Deno.upgradeWebSocket(req);
  socket.addEventListener("message", (event) => {
    if (event.data === "ping") socket.send("pong");
  });
  return response;
});
```

Default fetch export pattern:

```ts
export default {
  fetch(request) {
    return new Response(`User Agent: ${request.headers.get("user-agent")}`);
  },
} satisfies Deno.ServeDefaultExport;
```

# Context & Application

`Deno.serve` is the foundation for HTTP handling in Deno. For simple APIs and static file servers, it can be used directly. For more complex applications with routing, middleware, and other features, frameworks like Oak, Hono, or Fresh build on top of this API. The documentation recommends Oak for building web servers with middleware support.

# Examples

**Streaming response** (from `runtime/fundamentals/http_server.md`):
```ts
Deno.serve((req) => {
  let timer: number;
  const body = new ReadableStream({
    start(controller) {
      timer = setInterval(() => {
        controller.enqueue("Hello, World!\n");
      }, 1000);
    },
    cancel() { clearInterval(timer); },
  });
  return new Response(body.pipeThrough(new TextEncoderStream()), {
    headers: { "content-type": "text/plain; charset=utf-8" },
  });
});
```

**HTTPS server** (from `runtime/fundamentals/http_server.md`):
```ts
Deno.serve({
  port: 443,
  cert: Deno.readTextFileSync("./cert.pem"),
  key: Deno.readTextFileSync("./key.pem"),
}, handler);
```

# Relationships

- **Related**: `deno-web-framework-support` — frameworks build on top of `Deno.serve`
- **Related**: `deno-opentelemetry-support` — auto-instrumentation creates spans for `Deno.serve` requests

# Common Errors

1. **Not handling stream cancellation**: When using `ReadableStream` responses, the `cancel` callback must clean up resources (timers, connections) or the server will leak memory.
2. **Not handling body read failures**: `req.text()`, `req.json()`, etc. can fail if the client disconnects mid-request.
3. **Missing `--allow-net`**: The server requires network permission to listen.

# Common Confusions

- **`Deno.serve` vs `deno serve`**: `Deno.serve()` is a runtime API called in code; `deno serve` is a CLI command that runs a module with a default `fetch` export.
- **WebSocket HTTP version**: WebSockets only work over HTTP/1.1 in Deno, not HTTP/2.

# Source Reference

Source: "Deno Documentation", file `runtime/fundamentals/http_server.md`, all sections.

# Verification Notes

All API details and behaviors described are explicitly documented in the source file. Extraction confidence is high.
