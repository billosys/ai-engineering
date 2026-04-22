# Observability: Logging, Metrics, and Traces

Observability is a production concern: once a Rust binary is deployed, you need to know what it is doing, how fast, and why it is failing. The Rust ecosystem has settled on a small set of de-facto standards: `tracing` for application logging and spans, `log` as a lightweight facade for libraries, `metrics` for numeric counters/histograms/gauges, and `opentelemetry` for distributed traces exported across services. This guide covers how to wire those crates together, what to log at which level, how to avoid leaking secrets, and how to keep instrumentation cheap enough to leave on in production.


## LO-01: Never Ship `println!` or `eprintln!` as Production Logs

**Strength**: MUST

**Summary**: Use a structured logging framework (`tracing` for applications, `log` for libraries). `println!`/`eprintln!` are for CLI output and ad-hoc debugging only.

```rust
// ❌ BAD: print-debugging leaked into production code
pub fn process(req: &Request) -> Result<Response, Error> {
    println!("processing request {:?}", req);       // unstructured, unfilterable
    eprintln!("warning: cache miss");               // stderr but still unstructured
    let resp = handle(req)?;
    println!("done");
    Ok(resp)
}

// ✅ GOOD: structured events with levels and fields
use tracing::{debug, info, warn};

pub fn process(req: &Request) -> Result<Response, Error> {
    debug!(request_id = %req.id, "processing request");
    let resp = handle(req).inspect_err(|e| warn!(error = %e, "handle failed"))?;
    info!(request_id = %req.id, status = resp.status, "request complete");
    Ok(resp)
}
```

**Rationale**: `println!` locks stdout, blocks on a mutex, has no level/filter/destination control, can't be redirected to JSON for a log aggregator, and can't be turned off without editing code. Structured logging gives you levels, filtering, formatting layers, and machine-parseable output — all of which are required for operating a service.

**See also**: LO-02, LO-04

---

## LO-02: Use `tracing` as the De-Facto Standard for Applications

**Strength**: SHOULD

**Summary**: For binaries and services, prefer `tracing` + `tracing-subscriber`. It is async-aware, supports spans as well as events, and has a mature layer/subscriber ecosystem.

```rust
// Cargo.toml
// [dependencies]
// tracing = "0.1"
// tracing-subscriber = { version = "0.3", features = ["env-filter", "json"] }

use tracing::{info, instrument};
use tracing_subscriber::{EnvFilter, fmt};

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(EnvFilter::from_default_env())
        .with_target(true)
        .init();

    info!(version = env!("CARGO_PKG_VERSION"), "service starting");
    run();
}

#[instrument]
fn run() {
    info!("ready");
}
```

**Rationale**: `tracing` is the async-aware successor to `log`: it models *spans* (units of work with duration) and *events* (point-in-time logs), propagates context across `.await` points, and integrates with OpenTelemetry, `metrics`, Sentry, and virtually every tokio-ecosystem crate. A binary that instruments with `tracing` keeps its options open — swapping the subscriber changes destination and format without touching call sites.

**See also**: LO-03, LO-05, LO-07

---

## LO-03: Use `log` as a Facade for Libraries

**Strength**: SHOULD

**Summary**: Library crates should depend on `log` (or emit `tracing` events that are compatible with the `log` facade via `tracing-log`), not pin consumers to a specific runtime.

```rust
// ✅ GOOD: a library emits through the log facade
// Cargo.toml of mylib:
// [dependencies]
// log = "0.4"

use log::{debug, warn};

pub fn parse(input: &str) -> Result<Ast, ParseError> {
    debug!("parsing {} bytes", input.len());
    // ... if something questionable ...
    warn!("deprecated syntax at line {}", 42);
    Ok(Ast::default())
}

// The application binary chooses the implementation:
// - env_logger, simplelog, fern         (classic log subscribers)
// - tracing-subscriber + tracing-log    (if the app uses tracing)

// ❌ BAD: a library that pulls in tracing-subscriber or env_logger directly
// forces every consumer to use that runtime / format.
```

**Rationale**: `log` is a lightweight, long-stable facade (`log::info!`, `log::warn!`, etc.) with no runtime dependencies. A library that uses `log` works whether the binary ultimately ships `env_logger`, `tracing-subscriber`, `slog`, or a custom aggregator. Libraries that hardcode a subscriber force their choice on every consumer. If you want spans, use `tracing` in the library too — `tracing`'s events implement the `log` facade via the `log` feature, so libraries can publish spans without forcing a subscriber.

**See also**: LO-02, LO-17

---

## LO-04: Distinguish Spans from Events

**Strength**: SHOULD

**Summary**: Spans represent a unit of work with duration and a lifecycle. Events are point-in-time logs. Use spans for "what is happening right now"; use events for "something just happened".

```rust
use tracing::{info, info_span, Instrument};

// ✅ Event: point-in-time log line
info!(user_id = 42, "login succeeded");

// ✅ Span: the entire request is a unit of work
async fn handle_request(req: Request) -> Response {
    let span = info_span!("handle_request", request_id = %req.id, route = req.route);
    async move {
        info!("validating");          // event, emitted inside the span
        validate(&req).await;
        info!("dispatching");
        dispatch(&req).await
    }
    .instrument(span)
    .await
}
```

**Rationale**: Spans give you duration, structure, and context propagation — every event emitted inside a span inherits the span's fields and parentage. This is what lets a log aggregator (or OpenTelemetry trace viewer) show a request as a tree of nested operations with timings. Events alone are flat; spans make the structure visible.

**See also**: LO-05, LO-13

---

## LO-05: Instrument Async Functions with `#[instrument]`

**Strength**: SHOULD

**Summary**: Annotate async functions with `#[tracing::instrument]` so every entry creates a span that survives `.await` suspension and propagates context through the task.

```rust
use tracing::instrument;

// ✅ GOOD: auto-span with all function arguments recorded
#[instrument]
async fn fetch_user(user_id: u64) -> Result<User, DbError> {
    let user = db::query_user(user_id).await?;
    Ok(user)
}

// ✅ Skip large or sensitive arguments
#[instrument(skip(db, password), fields(user_id = %creds.user_id))]
async fn authenticate(db: &Db, creds: Credentials, password: SecretString)
    -> Result<Session, AuthError>
{
    // `db` and `password` are not recorded; `user_id` is recorded explicitly.
    db.verify(&creds, &password).await
}

// ✅ Skip all args and explicitly list what to record
#[instrument(skip_all, fields(req_id = %req.id))]
async fn serve(req: Request) -> Response { /* ... */ Response::default() }
```

**Rationale**: Manually creating a span and calling `.instrument(span)` on the future is error-prone; `#[instrument]` does it correctly for every call. Async tasks may suspend on one thread and resume on another, and without an explicit span a `tracing::info!` inside an `.await` chain would lose its parent. `skip` / `skip_all` are essential: large arguments clutter logs and sensitive arguments (passwords, tokens) must not be recorded by default.

**See also**: LO-02, LO-04, LO-08

---

## LO-06: Use Levels with Intent — Don't Overuse `INFO`

**Strength**: SHOULD

**Summary**: `ERROR` is for failed operations a human must investigate. `WARN` is for recoverable anomalies. `INFO` is for lifecycle events, one or two per request at most. `DEBUG` and `TRACE` are for developers, typically off in production.

```rust
use tracing::{debug, error, info, trace, warn};

// ERROR: the operation failed and a person may need to act
error!(error = %e, user_id = %id, "payment processing failed");

// WARN: anomaly, recovered, worth noticing over time
warn!(retries = 3, "retrying database connection");

// INFO: significant lifecycle — startup, shutdown, request completed
info!(port = 8080, "server listening");

// DEBUG: developer-oriented, internal state; off in production
debug!(cache_hit = true, key = %k, "cache lookup");

// TRACE: very fine-grained; usually for diagnosing a specific bug
trace!(byte_offset = 1024, "parsed header");
```

```rust
// ❌ BAD: everything at INFO — logs become useless noise
info!("entering function foo");
info!("about to call bar");
info!("returned from bar");
info!("about to return");
```

**Rationale**: Levels are a filter, not decoration. If every line is `INFO`, a production log is unsearchable and alerting on `ERROR` becomes impossible. A good heuristic: `INFO` fires once per meaningful lifecycle boundary (service start, request complete), `WARN` fires when an invariant was almost violated, `ERROR` fires when an operation failed visibly to the caller.

**See also**: LO-07, LO-13

---

## LO-07: Record Data as Structured Fields, Not String Interpolation

**Strength**: MUST

**Summary**: Pass values as named fields (`user_id = %id`), not interpolated into the message string. Fields are queryable and cheap; interpolated strings are opaque and allocate.

```rust
// ❌ BAD: interpolated — the aggregator can't filter by user_id
tracing::info!("user {} logged in from {}", user.id, user.ip);

// ✅ GOOD: structured fields — `user_id` and `ip` are indexable
tracing::info!(user_id = %user.id, ip = %user.ip, "user logged in");

// `%` uses Display; `?` uses Debug; bare name = Copy-able types
tracing::info!(
    user_id = %user.id,       // Display
    config = ?config,         // Debug
    attempts = 3,             // Copy
    "login completed"
);
```

**Rationale**: A log aggregator (Datadog, Loki, Elasticsearch, CloudWatch) can filter, group, and chart on structured fields — it can't meaningfully do that on a free-text message. Field syntax also defers formatting (the `Display` / `Debug` impl only runs if the event is actually emitted at the current level), which matters for hot-path events. Keep the message template descriptive of *what happened* and put *data* in fields.

**See also**: LO-06, LO-14, M-LOG-STRUCTURED

---

## LO-08: Redact Secrets in Logs

**Strength**: MUST

**Summary**: Never emit passwords, API keys, tokens, PII, or session cookies as log fields. Wrap secret-bearing types in a newtype with a custom `Debug`/`Display` that renders `<redacted>`.

```rust
use std::fmt::{self, Debug, Display, Formatter};

// ✅ Newtype whose Debug/Display never reveal the value
#[derive(Clone)]
pub struct SecretString(String);

impl SecretString {
    pub fn new(s: String) -> Self { Self(s) }
    pub fn expose(&self) -> &str { &self.0 }    // explicit opt-in to read
}

impl Debug for SecretString {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        f.write_str("SecretString(<redacted>)")
    }
}
impl Display for SecretString {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        f.write_str("<redacted>")
    }
}

// ✅ Safe by construction — tracing will print <redacted>
let password = SecretString::new("hunter2".into());
tracing::info!(user = "alice", password = %password, "login attempt");
// → "login attempt" user=alice password=<redacted>

// ❌ BAD: logs the secret verbatim
// tracing::info!(user = "alice", password = "hunter2", "login attempt");
```

```rust
// Empty field that is recorded later — also useful for redaction
use tracing::field::Empty;
let span = tracing::info_span!("auth", user = Empty);
span.record("user", &tracing::field::display(&user.id));
// Only the id is recorded, not the whole credential object.
```

**Rationale**: Production logs flow through aggregators, backups, and (sometimes) third-party vendors. A single `tracing::info!(password = %p, ...)` can leak credentials irreversibly. Make redaction the default at the type level so human error at the call site is impossible. Unit-test that `format!("{:?}", secret)` never contains the cleartext. Consider the `secrecy` crate for a production-grade version of this pattern.

**See also**: TD-12 (Debug redaction), LO-05 (`skip` in instrument), `secrecy` crate

---

## LO-09: Use `metrics` for Numeric Time Series

**Strength**: SHOULD

**Summary**: Logs are for events; metrics are for aggregated numbers over time. Use the `metrics` facade for counters, histograms, and gauges, and export to Prometheus/OTLP.

```rust
// Cargo.toml
// [dependencies]
// metrics = "0.23"
// metrics-exporter-prometheus = "0.15"

use metrics::{counter, gauge, histogram};
use metrics_exporter_prometheus::PrometheusBuilder;

fn init_metrics() {
    PrometheusBuilder::new()
        .with_http_listener(([0, 0, 0, 0], 9090))
        .install()
        .expect("failed to install Prometheus recorder");
}

async fn handle_request(req: Request) -> Response {
    counter!("http_requests_total", "route" => req.route.clone()).increment(1);
    let start = std::time::Instant::now();

    let resp = dispatch(req).await;

    histogram!("http_request_duration_seconds", "route" => resp.route.clone())
        .record(start.elapsed().as_secs_f64());
    gauge!("http_in_flight").decrement(1.0);
    resp
}
```

**Rationale**: Log storage costs scale with volume; metric storage scales with cardinality of labels. Counting every request in a metric is free; logging every request is expensive. Use metrics for anything you want to chart, alert on, or aggregate (QPS, latency percentiles, queue depths); use logs for anything you want to *read* after the fact.

**See also**: LO-10, LO-13, LO-15

---

## LO-10: Counters, Histograms, Gauges — Pick the Right Primitive

**Strength**: SHOULD

**Summary**: Counters only increase (requests served, errors emitted). Histograms record distributions (latency, payload size). Gauges go up and down (in-flight requests, connection pool size, queue depth).

```rust
use metrics::{counter, gauge, histogram};

// ✅ Counter — monotonic event count
counter!("jobs_completed_total", "kind" => "email").increment(1);

// ✅ Histogram — distribution of observed values
histogram!("job_duration_seconds", "kind" => "email")
    .record(elapsed.as_secs_f64());

// ✅ Gauge — current value, up and down
gauge!("workers_active").increment(1.0);
do_work();
gauge!("workers_active").decrement(1.0);

// ❌ BAD: using a gauge where a counter belongs
// gauge!("requests_total").increment(1.0);
// Gauges can be reset or decremented; `rate()` over a gauge is meaningless.
```

**Rationale**: Prometheus and OTLP treat these as distinct kinds. A counter lets you compute `rate()` and sum across instances; a gauge cannot. Histograms let you compute percentiles (`p99`, `p50`) at query time; a plain counter of latency sums cannot. Picking the wrong primitive silently produces wrong dashboards.

**See also**: LO-09, LO-15

---

## LO-11: Integrate OpenTelemetry for Distributed Tracing

**Strength**: CONSIDER

**Summary**: For multi-service systems, export `tracing` spans to an OTLP collector via `opentelemetry-otlp` + `tracing-opentelemetry`. Propagate trace context across HTTP/gRPC boundaries.

```rust
// Cargo.toml
// [dependencies]
// opentelemetry = "0.24"
// opentelemetry-otlp = { version = "0.17", features = ["tonic"] }
// opentelemetry_sdk = { version = "0.24", features = ["rt-tokio"] }
// tracing = "0.1"
// tracing-subscriber = "0.3"
// tracing-opentelemetry = "0.25"

use opentelemetry::global;
use opentelemetry_otlp::WithExportConfig;
use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt, EnvFilter};

fn init_tracing() -> anyhow::Result<()> {
    let tracer = opentelemetry_otlp::new_pipeline()
        .tracing()
        .with_exporter(opentelemetry_otlp::new_exporter().tonic().with_endpoint("http://otel-collector:4317"))
        .install_batch(opentelemetry_sdk::runtime::Tokio)?;

    let otel_layer = tracing_opentelemetry::layer().with_tracer(tracer);

    tracing_subscriber::registry()
        .with(EnvFilter::from_default_env())
        .with(tracing_subscriber::fmt::layer())
        .with(otel_layer)
        .init();
    Ok(())
}

// On shutdown
fn shutdown_tracing() { global::shutdown_tracer_provider(); }
```

```rust
// ✅ Propagate context across HTTP calls
use opentelemetry::propagation::{Injector, TextMapPropagator};
use tracing::Span;
use tracing_opentelemetry::OpenTelemetrySpanExt;

fn inject_traceparent(req: &mut http::Request<()>) {
    let cx = Span::current().context();
    let propagator = opentelemetry_sdk::propagation::TraceContextPropagator::new();
    let mut injector = HeaderInjector(req.headers_mut());
    propagator.inject_context(&cx, &mut injector);
}
```

**Rationale**: In a single service, local spans are enough. In a microservice architecture, a request may traverse ten services and a trace has to be reassembled across them — that requires a shared trace ID, propagated via `traceparent` headers (W3C Trace Context). OpenTelemetry is the ecosystem-standard protocol; the OTLP exporter ships spans to any compatible collector (Jaeger, Tempo, Datadog, Honeycomb, New Relic). Use this when you have more than one service in the trace.

**See also**: LO-05, LO-13, LO-15

---

## LO-12: Install a Panic Hook to Capture Crashes

**Strength**: SHOULD

**Summary**: Register `std::panic::set_hook` at startup to log panics as structured events (and optionally forward them to Sentry or another crash reporter).

```rust
use std::panic;
use tracing::error;

fn install_panic_hook() {
    let default = panic::take_hook();
    panic::set_hook(Box::new(move |info| {
        let location = info.location()
            .map(|l| format!("{}:{}:{}", l.file(), l.line(), l.column()))
            .unwrap_or_else(|| "<unknown>".into());

        let payload = info.payload();
        let message = payload.downcast_ref::<&str>().map(|s| *s)
            .or_else(|| payload.downcast_ref::<String>().map(String::as_str))
            .unwrap_or("<non-string panic>");

        error!(
            location = %location,
            message = %message,
            backtrace = %std::backtrace::Backtrace::capture(),
            "panic"
        );
        default(info);     // preserve the default behaviour (print + abort)
    }));
}
```

```rust
// Sentry integration — one line replaces the custom hook
// let _guard = sentry::init(("https://dsn@sentry.io/1", sentry::ClientOptions {
//     release: sentry::release_name!(),
//     ..Default::default()
// }));
// `sentry` installs a panic hook that uploads the crash automatically.
```

**Rationale**: Without a panic hook, a panic prints to stderr and is lost — no trace, no log aggregator entry, no crash report. With a hook, panics become first-class events you can alert on. Call `install_panic_hook()` before starting the runtime. If you also use `std::panic::catch_unwind` at task boundaries (common in executors), the hook still fires before the unwind is caught.

**See also**: LO-16, error-handling guide (EH)

---

## LO-13: Use `RUST_LOG` and `EnvFilter` for Per-Module Verbosity

**Strength**: MUST

**Summary**: Read the log level from the `RUST_LOG` environment variable via `tracing_subscriber::EnvFilter`. Support per-module filters so operators can dial up debug on one module without drowning in logs.

```rust
use tracing_subscriber::EnvFilter;

fn init() {
    // Default: INFO everywhere, unless RUST_LOG overrides.
    let filter = EnvFilter::try_from_default_env()
        .unwrap_or_else(|_| EnvFilter::new("info"));

    tracing_subscriber::fmt()
        .with_env_filter(filter)
        .init();
}

// Example RUST_LOG values:
//   RUST_LOG=info                        # everything at INFO
//   RUST_LOG=debug                       # everything at DEBUG
//   RUST_LOG=info,myapp::db=debug        # global INFO, myapp::db at DEBUG
//   RUST_LOG=warn,myapp=trace            # quiet, but trace one crate
//   RUST_LOG=hyper=warn,myapp=debug      # tame noisy deps
```

**Rationale**: `RUST_LOG` is the convention every Rust operator already knows. Per-module syntax lets you trace a single subsystem in production without flooding disk. Hardcoding the filter in code means a redeploy for every log-level change — do not do that. Pair with a signal handler or admin endpoint if you need runtime reload (`tracing_subscriber::reload`).

**See also**: LO-02, LO-06

---

## LO-14: Propagate Request IDs Through Spans

**Strength**: SHOULD

**Summary**: For web services, assign a request ID at the edge (accept the client's if present, otherwise generate one), attach it to the root span, and include it in every outbound call.

```rust
use tracing::{info_span, Instrument};
use uuid::Uuid;

pub async fn serve(req: http::Request<Body>) -> http::Response<Body> {
    let request_id = req.headers()
        .get("x-request-id")
        .and_then(|v| v.to_str().ok())
        .map(String::from)
        .unwrap_or_else(|| Uuid::new_v4().to_string());

    let span = info_span!(
        "request",
        request_id = %request_id,
        method = %req.method(),
        path = %req.uri().path(),
    );

    async move {
        let mut resp = handle(req).await;
        resp.headers_mut().insert("x-request-id", request_id.parse().unwrap());
        resp
    }
    .instrument(span)
    .await
}
```

**Rationale**: Every event emitted inside the span inherits `request_id`, which means you can grep logs for a single request across every module and every async task. Echoing the ID back in `x-request-id` lets the client report it to you. Combined with OpenTelemetry's `traceparent`, the request ID is the human-readable key to a distributed trace.

**See also**: LO-04, LO-11

---

## LO-15: The Three Pillars Complement Each Other

**Strength**: CONSIDER

**Summary**: Logs answer "what happened?". Metrics answer "how much / how fast?". Traces answer "where did the time go?". Don't pick one — use each for what it's best at.

```rust
// ✅ The same request touches all three
async fn handle(req: Request) -> Response {
    // 1. Metric: count every request (cheap, aggregable)
    metrics::counter!("requests_total", "route" => req.route.clone()).increment(1);
    let start = std::time::Instant::now();

    // 2. Trace + log: a span for the unit of work, event for the interesting bit
    let span = tracing::info_span!("handle", request_id = %req.id);
    let resp = async {
        tracing::info!(path = %req.path, "dispatching");
        let r = dispatch(req).await;
        if r.status >= 500 { tracing::error!(status = r.status, "server error"); }
        r
    }
    .instrument(span)
    .await;

    // 3. Metric: record latency as a histogram (percentiles at query time)
    metrics::histogram!("request_duration_seconds")
        .record(start.elapsed().as_secs_f64());
    resp
}
```

**Rationale**: Each pillar has a different storage profile. Metrics are cheap at any cardinality below a few thousand label combinations; logs are cheap for individual events but expensive in volume; traces are expensive per span but uniquely show causality and timing across services. Using all three produces a system that is cheap to monitor, debuggable after the fact, and analyzable across service boundaries.

**See also**: LO-09, LO-11, LO-13

---

## LO-16: Use `field::Empty` + `record()` to Avoid Paying for Expensive Fields

**Strength**: CONSIDER

**Summary**: `tracing` is near-zero-cost for disabled levels. For enabled events, avoid computing expensive field values in hot paths — reserve the field with `Empty` and fill it in only if needed.

```rust
use tracing::{info_span, field::Empty, Span};

// ✅ Reserve the field, fill it only when we know the value
let span = info_span!("query", rows = Empty, duration_ms = Empty);
let _guard = span.enter();

let start = std::time::Instant::now();
let rows = run_query().await;

// Recording is cheap; computing `rows.len()` is too, but imagine
// an expensive `serialize_plan()` call here instead:
Span::current().record("rows", rows.len());
Span::current().record("duration_ms", start.elapsed().as_millis() as u64);
```

```rust
// ❌ BAD: expensive Debug format runs on every call, level permitting
// tracing::info!(plan = ?explain_plan(&query), "executed");
//
// ✅ BETTER: guard with enabled! if the value is costly
if tracing::enabled!(tracing::Level::DEBUG) {
    tracing::debug!(plan = ?explain_plan(&query), "executed");
}
```

**Rationale**: `tracing`'s per-callsite registration means a disabled event costs roughly one atomic load and a branch. The expensive part is evaluating field expressions — `format!`, `serde_json::to_string`, `Debug` impls with deep structure. `field::Empty` lets you declare the field schema up front without paying for the value until it's known; `tracing::enabled!` lets you short-circuit before computing a costly field.

**See also**: LO-05, LO-07

---

## LO-17: Sample Traces Under Load

**Strength**: CONSIDER

**Summary**: Collecting 100% of traces at high QPS is usually infeasible — both expensive and noisy. Sample: keep a fixed fraction, keep all errors, and keep the slow tail.

```rust
use opentelemetry_sdk::trace::{Sampler, Config};

// ✅ Keep 10% of traces, plus always keep error spans
let config = Config::default()
    .with_sampler(Sampler::ParentBased(Box::new(
        Sampler::TraceIdRatioBased(0.1),
    )));
```

```rust
// Tail-based sampling (done at the OTLP collector, not in the app):
//   - always keep traces with status = error
//   - always keep traces with duration > p99
//   - otherwise keep 1%
// Configure this in the collector's `tail_sampling_processor`, not in the Rust app.
```

**Rationale**: A high-QPS service producing one span per request at a dozen nested operations each will generate millions of spans per minute. Most are unremarkable, and most trace backends charge per span. Head-based sampling (`TraceIdRatioBased`) is cheap and easy; tail-based sampling (at the collector) is smarter because it can keep the *interesting* traces (errors, slow outliers). Logs and metrics fill the gap for unsampled requests.

**See also**: LO-09, LO-11

---

## LO-18: Instrument Errors at the Boundary, Not at Every Layer

**Strength**: SHOULD

**Summary**: Don't log the same error at every layer it passes through. Log at the boundary where a decision is made (request failed, retry exhausted, background task gave up); propagate with `?` in between.

```rust
// ❌ BAD: the same error is logged three times
async fn inner() -> Result<(), Error> {
    let r = io::read().await;
    if let Err(ref e) = r { tracing::error!(%e, "inner io failed"); }
    r
}
async fn middle() -> Result<(), Error> {
    let r = inner().await;
    if let Err(ref e) = r { tracing::error!(%e, "middle failed"); }
    r
}
async fn outer() -> Result<(), Error> {
    let r = middle().await;
    if let Err(ref e) = r { tracing::error!(%e, "outer failed"); }
    r
}

// ✅ GOOD: propagate with `?`; log once at the boundary with full context
async fn inner() -> Result<(), Error> { io::read().await }
async fn middle() -> Result<(), Error> { inner().await }

#[tracing::instrument]
async fn outer(request_id: u64) -> Result<(), Error> {
    middle().await.inspect_err(|e| {
        tracing::error!(error = %e, error_chain = ?e, "request failed");
    })
}
```

**Rationale**: Duplicate logs at every layer make it impossible to count failures and obscure the real cause with noise. Use `?` for propagation, log at the point where the error is handled or returned to a human-meaningful boundary, and attach a structured `error_chain` / `%e` / `?e` field so the full causal chain survives in one entry.

**See also**: LO-06, error-handling guide (EH)

---

## Starter Template: Wiring a Typical Application

A realistic `main.rs` combining EnvFilter, pretty (dev) vs JSON (prod) output, and a panic hook:

```rust
use std::panic;
use tracing::error;
use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt, EnvFilter, fmt};

fn main() -> anyhow::Result<()> {
    init_tracing();
    install_panic_hook();

    tracing::info!(
        version = env!("CARGO_PKG_VERSION"),
        "service starting"
    );

    let rt = tokio::runtime::Runtime::new()?;
    rt.block_on(async {
        run().await
    })?;
    Ok(())
}

fn init_tracing() {
    let filter = EnvFilter::try_from_default_env()
        .unwrap_or_else(|_| EnvFilter::new("info"));

    let registry = tracing_subscriber::registry().with(filter);

    // Toggle format by env: JSON in prod, pretty in dev.
    if std::env::var("LOG_FORMAT").as_deref() == Ok("json") {
        registry.with(fmt::layer().json().with_current_span(true)).init();
    } else {
        registry.with(fmt::layer().pretty()).init();
    }
}

fn install_panic_hook() {
    let default = panic::take_hook();
    panic::set_hook(Box::new(move |info| {
        let location = info.location()
            .map(|l| format!("{}:{}", l.file(), l.line()))
            .unwrap_or_default();
        let message = info.payload().downcast_ref::<&str>().copied()
            .or_else(|| info.payload().downcast_ref::<String>().map(String::as_str))
            .unwrap_or("<non-string panic>");
        error!(location = %location, message = %message, "panic");
        default(info);
    }));
}

async fn run() -> anyhow::Result<()> {
    tracing::info!("ready");
    Ok(())
}
```

For services that export metrics and traces, add:

```rust
// Metrics endpoint on :9090/metrics
metrics_exporter_prometheus::PrometheusBuilder::new()
    .with_http_listener(([0, 0, 0, 0], 9090))
    .install()?;

// OTLP trace export (see LO-11 for the full wiring)
```


## Summary Table

| Pattern | Strength | Key Principle |
|---------|----------|---------------|
| LO-01 No `println!` in production | MUST | Use a structured logger |
| LO-02 `tracing` for applications | SHOULD | Async-aware, span-aware, layerable |
| LO-03 `log` facade for libraries | SHOULD | Don't pin consumers to a runtime |
| LO-04 Spans vs events | SHOULD | Spans = work with duration; events = point-in-time |
| LO-05 `#[instrument]` on async fns | SHOULD | Use `skip` for large/secret args |
| LO-06 Levels have meaning | SHOULD | `INFO` = lifecycle, not every line |
| LO-07 Structured fields, not interpolation | MUST | Fields are queryable; strings are opaque |
| LO-08 Redact secrets | MUST | Wrap in a newtype; test the redaction |
| LO-09 `metrics` for numeric time series | SHOULD | Counters/histograms/gauges, not logs |
| LO-10 Pick the right metric primitive | SHOULD | Counter ≠ gauge ≠ histogram |
| LO-11 OpenTelemetry for distributed tracing | CONSIDER | OTLP + W3C Trace Context propagation |
| LO-12 Panic hook for crashes | SHOULD | `std::panic::set_hook` or Sentry |
| LO-13 `RUST_LOG` + `EnvFilter` | MUST | Operator-tunable verbosity without redeploy |
| LO-14 Request IDs in spans | SHOULD | One key to trace a request end-to-end |
| LO-15 Three pillars complement | CONSIDER | Logs + metrics + traces, each for what it does best |
| LO-16 `field::Empty` for expensive fields | CONSIDER | Declare the field, fill it only when known |
| LO-17 Sample traces under load | CONSIDER | Head sampling cheap; tail sampling smart |
| LO-18 Log errors at the boundary | SHOULD | Propagate with `?`; log once with context |


## Related Guidelines

- **Error Handling**: See `03-error-handling.md` for error type design; log-at-the-boundary pairs with `?` propagation.
- **Type Design**: See `05-type-design.md` — TD-12 (`Debug` redaction) is the type-level companion to LO-08.
- **Concurrency and Async**: See `07-concurrency-async.md` — `#[instrument]` and span propagation across `.await` matter most in async code.
- **Performance**: See `08-performance.md` — LO-16 and LO-17 address the cost of observability on hot paths.
- **Anti-Patterns**: See `11-anti-patterns.md` for the counterparts (print-debugging, logging secrets, panicking without a hook).


## External References

- [`tracing` documentation](https://docs.rs/tracing) and [`tracing-subscriber`](https://docs.rs/tracing-subscriber)
- [`log` crate](https://docs.rs/log) — the facade standard
- [`metrics` crate](https://docs.rs/metrics) and [`metrics-exporter-prometheus`](https://docs.rs/metrics-exporter-prometheus)
- [OpenTelemetry Rust](https://opentelemetry.io/docs/languages/rust/) — [`opentelemetry`](https://docs.rs/opentelemetry), [`opentelemetry-otlp`](https://docs.rs/opentelemetry-otlp), [`tracing-opentelemetry`](https://docs.rs/tracing-opentelemetry)
- [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/) — standard attribute names for HTTP, DB, files, errors
- [W3C Trace Context](https://www.w3.org/TR/trace-context/) — the `traceparent` / `tracestate` header standard
- [`sentry` crate](https://docs.rs/sentry) — panic hook + crash reporting integration
- [`secrecy` crate](https://docs.rs/secrecy) — production-grade `SecretString` / `SecretBox`
- [Message Templates Specification](https://messagetemplates.org/)
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- Pragmatic Rust Guidelines: M-LOG-STRUCTURED (structured events, message templates, OTel conventions, redaction)
