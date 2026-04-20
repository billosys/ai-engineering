---
concept: OpenTelemetry Support
slug: deno-opentelemetry-support
category: development
subcategory: observability
tier: advanced
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/open_telemetry.md"
chapter_number: null
pdf_page: null
section: "OpenTelemetry"
extraction_confidence: high
aliases:
  - "Deno OTEL"
  - "OTEL_DENO"
  - "Deno OpenTelemetry"
  - "Deno observability"
prerequisites:
  - deno-configuration
  - deno-http-server
extends: []
related:
  - deno-debugging
  - deno-http-server
contrasts_with: []
answers_questions:
  - "How do I enable OpenTelemetry in Deno?"
  - "What does Deno auto-instrument with OpenTelemetry?"
  - "How do I add custom metrics and traces in Deno?"
---

# Quick Definition

Deno has built-in OpenTelemetry support activated via `OTEL_DENO=true`, providing automatic instrumentation of HTTP requests, console logs, and runtime metrics, plus user-defined traces and metrics via the `npm:@opentelemetry/api` package — all exported over OTLP without additional SDK configuration.

# Core Definition

Deno integrates OpenTelemetry natively, enabling observability through traces, metrics, and logs. It is activated by setting the `OTEL_DENO=true` environment variable:

```sh
OTEL_DENO=true deno run my_script.ts
```

This automatically collects and exports data to an OTLP endpoint at `localhost:4318` using Protobuf over HTTP.

**Auto-instrumentation** (instrumentation scope: `deno`):

- **Traces**: Automatic spans for incoming `Deno.serve` requests (server spans) and outgoing `fetch` requests (client spans), with HTTP method, URL, status code attributes.
- **Metrics**: Histograms for `http.server.request.duration`, `http.server.request.body.size`, `http.server.response.body.size`, and a gauge for `http.server.active_requests`.
- **Logs**: All `console.*` output, runtime debug logs, and fatal errors are exported as OTEL logs with span context when applicable.

**User-defined telemetry** uses `npm:@opentelemetry/api@1` with zero configuration — Deno sets up providers and context managers automatically:

- **Traces**: `trace.getTracer("my-app").startActiveSpan()` creates spans with attributes, events, links, and status.
- **Metrics**: `metrics.getMeter("my-app")` creates counters, up-down counters, gauges, histograms, and their observable variants.
- **Context propagation**: Uses `AsyncContext` internally; the `context` API supports `context.with()` for scoped context, and propagators inject/extract trace context across HTTP boundaries.

# Prerequisites

- `deno-configuration` — environment variables configure OTEL behavior
- `deno-http-server` — auto-instrumentation targets `Deno.serve` and `fetch`

# Key Properties

1. **Zero SDK setup**: No need to call `setGlobalMeterProvider()`, `setGlobalTracerProvider()`, or `setGlobalContextManager()` — Deno handles this automatically.
2. **Environment-driven configuration**: Endpoint (`OTEL_EXPORTER_OTLP_ENDPOINT`), protocol (`OTEL_EXPORTER_OTLP_PROTOCOL`), headers (`OTEL_EXPORTER_OTLP_HEADERS`), service name (`OTEL_SERVICE_NAME`), and resource attributes (`OTEL_RESOURCE_ATTRIBUTES`) are all configured via environment variables.
3. **Console log modes**: `OTEL_DENO_CONSOLE` controls log handling: `capture` (default, both stdout and OTEL), `replace` (OTEL only), or `ignore` (stdout only).
4. **Propagators**: W3C Trace Context and Baggage propagation enabled by default, configurable via `OTEL_PROPAGATORS`.
5. **Metric export interval**: Configurable via `OTEL_METRIC_EXPORT_INTERVAL` (default 60 seconds).
6. **Per-signal endpoint overrides**: `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT`, `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT`, `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT`.

# Construction / Recognition

Enable auto-instrumentation:
```sh
OTEL_DENO=true deno run my_script.ts
```

Create custom traces:
```ts
import { trace } from "npm:@opentelemetry/api@1";
const tracer = trace.getTracer("my-app", "1.0.0");

function myFunction() {
  return tracer.startActiveSpan("myFunction", (span) => {
    try {
      // work
    } catch (error) {
      span.recordException(error);
      span.setStatus({ code: trace.SpanStatusCode.ERROR, message: error.message });
      throw error;
    } finally {
      span.end();
    }
  });
}
```

Create custom metrics:
```ts
import { metrics } from "npm:@opentelemetry/api@1";
const meter = metrics.getMeter("my-app", "1.0.0");
const counter = meter.createCounter("my_counter", { description: "A counter", unit: "1" });
counter.add(1, { color: "red" });
```

# Context & Application

OpenTelemetry support enables production monitoring of Deno applications using standard observability tooling (Grafana, Prometheus, Jaeger, etc.). The automatic instrumentation provides immediate visibility into HTTP request performance without code changes. Custom metrics and traces allow application-specific observability.

# Examples

**Adding route information to server spans** (from `runtime/fundamentals/open_telemetry.md`):
```ts
import { trace } from "npm:@opentelemetry/api@1";

Deno.serve(async (req) => {
  const span = trace.getActiveSpan();
  if (BOOK_ROUTE.test(req.url)) {
    span.setAttribute("http.route", "/book/:id");
    span.updateName(`${req.method} /book/:id`);
    // handle route
  }
});
```

**Quick start with LGTM stack** (from `runtime/fundamentals/open_telemetry.md`):
```sh
docker run --name lgtm -p 3000:3000 -p 4317:4317 -p 4318:4318 --rm -ti \
  docker.io/grafana/otel-lgtm:0.8.1
```

# Relationships

- **Related**: `deno-debugging` — OTEL complements debugging for production observability
- **Related**: `deno-http-server` — auto-instrumentation targets `Deno.serve`

# Common Errors

1. **Forgetting `span.end()`**: Spans must be explicitly ended, ideally in a `finally` block.
2. **Not setting error status**: `recordException()` does not automatically set span status to `ERROR`; `setStatus()` must be called separately.
3. **High cardinality attributes**: Metric attributes should have low cardinality (e.g., continent, not exact coordinates) to avoid storage issues.

# Common Confusions

- **`recordException` vs `setStatus`**: Recording an exception attaches the error to the span as an event, but does not mark the span as errored. You must also call `setStatus({ code: SpanStatusCode.ERROR })`.
- **Traces always sampled**: Currently, Deno always samples traces (`parentbased_always_on`); custom samplers are not supported.

# Source Reference

Source: "Deno Documentation", file `runtime/fundamentals/open_telemetry.md`, all sections.

# Verification Notes

All features, environment variables, and limitations are explicitly documented in the source file. Extraction confidence is high.
