# Supervision and Applications

How to structure an Erlang system for recovery and deployment: supervision-tree shape, restart strategies and types, child specifications, the `application` behaviour and its resource file, configuration via the application environment, and packaging as a release. The fault-tolerance *reasoning* behind supervision lives in `09-fault-tolerance.md`; the behaviours that sit as children live in `07-otp-behaviours.md`; the rebar3/umbrella/Hex build layout lives in `12-project-structure.md`.

Target environment: **Erlang/OTP 27+**. Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Grounded in: the OTP Design Principles (Supervisor, Applications, Releases), Designing for Scalability with Erlang/OTP, Programming Erlang, and Learn You Some Erlang.

---

## SUP-01: Structure the System as a Supervision Tree

**Strength**: SHOULD

**Summary**: Organise long-lived processes into a supervision tree rooted in an application, rather than spawning them ad hoc from business code.

```erlang
%% Bad - spawn workers ad hoc; nothing restarts them, there is no defined shutdown order
start() ->
    spawn(fun worker:loop/0),
    spawn(fun other:loop/0).

%% Good - a supervision tree: declared children, restart policy, ordered startup/shutdown
init([]) ->
    Children = [#{id => worker, start => {worker, start_link, []}},
                #{id => other,  start => {other,  start_link, []}}],
    {ok, {#{strategy => one_for_one}, Children}}.
```

**Rationale**: A supervision tree gives every process a defined lifecycle — who starts it, who restarts it, and in what order it shuts down. Ad-hoc `spawn` from application code produces orphan processes with none of that: a crash is permanent and shutdown is undefined. The tree is the backbone the rest of OTP (applications, releases) builds on.

**See also**: SUP-02, SUP-05, `09-fault-tolerance.md`

---

## SUP-02: Keep Supervisors Thin — No Business Logic

**Strength**: SHOULD

**Summary**: A supervisor's job is to start, restart, and stop children. Keep computation and state out of the supervisor module so a bug there can't take the subtree down.

```erlang
%% Bad - real work inside the supervisor; a fault here kills the whole subtree it should be protecting
init(Args) ->
    Data = compute_a_lot(Args),
    {ok, {#{strategy => one_for_one}, child_specs(Data)}}.

%% Good - the supervisor only wires children together; logic lives in workers
init([]) ->
    {ok, {#{strategy => one_for_one}, [worker_spec()]}}.
```

**Rationale**: The supervisor is part of the error kernel (FT-05): it must be simple enough to be trivially correct, because if it crashes, everything under it goes too. Push initialization work and state into the worker children, which are the things designed to crash and be restarted.

**See also**: SUP-01, SUP-10, `09-fault-tolerance.md`

---

## SUP-03: Define Children with the Map Child Specification

**Strength**: SHOULD

**Summary**: Specify children with the map form; `id` and `start` are mandatory, the rest have sensible defaults.

```erlang
%% Bad - the legacy positional tuple child spec: opaque, easy to mis-order
{worker, {worker, start_link, []}, permanent, 5000, worker, [worker]}.

%% Good - the map child spec: mandatory id + start, explicit named keys
#{id => worker,
  start => {worker, start_link, []},
  restart => permanent,            %% default
  shutdown => 5000,                %% default for workers
  type => worker}.                 %% default
```

**Rationale**: The child spec is a map with mandatory `id` and `start` (an `{M,F,A}` resulting in a `*_link` start), plus optional `restart`, `shutdown`, `type`, `significant`, and `modules` (OTP Design Principles, "Child Specification"). The map form is self-documenting and order-independent, unlike the legacy 6-tuple.

**See also**: SUP-04, SUP-07

---

## SUP-04: Match the Restart Type to the Work

**Strength**: SHOULD

**Summary**: `permanent` is always restarted, `transient` only after an abnormal exit, `temporary` is never restarted. Pick per child.

```erlang
%% Bad - permanent for a one-shot job: it finishes, exits 'normal', and is restarted forever
#{id => import, start => {import, run, []}, restart => permanent}.

%% Good - restart type matches the child's nature
#{id => db,      start => {db, start_link, []},      restart => permanent},  %% must always run
#{id => import,  start => {import, run, []},          restart => transient},  %% one-shot; redo only on crash
#{id => session, start => {session, start_link, []},  restart => temporary}.  %% disposable; never redo
```

**Rationale**: `permanent` children are restarted whenever they terminate (the right default for services); `transient` children are restarted only on abnormal termination (good for run-to-completion jobs that shouldn't be re-run on success); `temporary` children are never restarted (disposable, dynamically-created work). A `permanent` one-shot task loops forever once it succeeds.

**See also**: SUP-03, SUP-08

---

## SUP-05: Choose the Restart Strategy by How Children Depend on Each Other

**Strength**: SHOULD

**Summary**: `one_for_one` for independent children, `one_for_all` for shared-fate children, `rest_for_one` when later children depend on earlier ones.

```erlang
%% Bad - one_for_one when the cache depends on the db: db restarts alone, cache keeps a stale pid
{ok, {#{strategy => one_for_one}, [db_spec(), cache_spec()]}}.

%% Good - rest_for_one: restarting db also restarts everything started after it
{ok, {#{strategy => rest_for_one}, [db_spec(), cache_spec()]}}.
```

**Rationale**: The strategy decides the *scope* of a restart (OTP Design Principles, "Restart Strategy"): `one_for_one` restarts only the failed child; `one_for_all` restarts all children (use when they share state/fate); `rest_for_one` restarts the failed child and everything started after it (use for an ordered dependency chain). Match it to the real dependencies, or restarts leave siblings talking to dead pids.

**See also**: SUP-04, SUP-06

---

## SUP-06: Set Restart Intensity and Period Intentionally

**Strength**: SHOULD

**Summary**: Configure `intensity`/`period` so a child that crash-loops trips the limit and escalates to the parent, instead of spinning forever.

```erlang
%% Bad - intensity so high a crash-looping child never trips the limit; the real fault never escalates
{ok, {#{strategy => one_for_one, intensity => 1000000, period => 1}, Children}}.

%% Good - sane limits (defaults are intensity=1, period=5); a persistent fault escalates upward
{ok, {#{strategy => one_for_one, intensity => 5, period => 10}, Children}}.
```

**Rationale**: If more than `intensity` restarts happen within `period` seconds, the supervisor terminates with `shutdown` and the failure escalates to *its* supervisor (OTP Design Principles, "Supervisor Flags"; defaults `intensity => 1`, `period => 5`). That escalation is how a fault a local restart can't fix gets a chance to be fixed higher up — see FT-13. Disable it with an enormous intensity and the system crash-loops silently.

**See also**: SUP-05, `09-fault-tolerance.md` (FT-13)

---

## SUP-07: Set `shutdown` Correctly — Graceful Workers, `infinity` Supervisors

**Strength**: SHOULD

**Summary**: Give workers a graceful shutdown timeout (so `terminate` can run); use `infinity` for child supervisors; reserve `brutal_kill` for processes with nothing to clean up.

```erlang
%% Bad - brutal_kill a worker that holds resources: terminate never runs, buffers/sockets leak
#{id => writer, start => {writer, start_link, []}, shutdown => brutal_kill}.

%% Good - graceful timeout for workers; infinity for sub-supervisors so their trees drain
#{id => writer,  start => {writer, start_link, []},  shutdown => 5000,     type => worker},
#{id => sub_sup, start => {sub_sup, start_link, []}, shutdown => infinity, type => supervisor}.
```

**Rationale**: On shutdown the supervisor sends `exit(Child, shutdown)` and waits up to the `shutdown` time before `brutal_kill` (default `5000` ms for workers, `infinity` for supervisors). A worker that traps exits uses that window to run `terminate/2` and release resources (BEH-10). `brutal_kill` skips `terminate` entirely, and a finite timeout on a supervisor can sever its subtree mid-shutdown.

**See also**: SUP-03, `07-otp-behaviours.md` (BEH-10)

---

## SUP-08: Supervise Dynamic, Identical Children with `simple_one_for_one`

**Strength**: SHOULD

**Summary**: For many identical, dynamically-created children, use a `simple_one_for_one` supervisor and create them with `supervisor:start_child/2` — don't track them yourself.

```erlang
%% Bad - keep a hand-maintained list of dynamic workers and spawn them yourself
handle_cast({new, Job}, S) ->
    Pid = spawn(fun() -> work(Job) end),
    {noreply, [Pid | S]}.

%% Good - a simple_one_for_one supervisor of identical children, started on demand
init([]) ->
    Child = #{id => job, start => {job, start_link, []}, restart => temporary},
    {ok, {#{strategy => simple_one_for_one}, [Child]}}.
%% elsewhere: {ok, _Pid} = supervisor:start_child(job_sup, [Job]).
```

**Rationale**: `simple_one_for_one` is built for a single child spec instantiated many times at runtime — connection handlers, per-session workers — with the supervisor tracking and restarting them for you. Hand-rolling a process registry re-implements supervision badly (no restart policy, no shutdown discipline, leaks on crash).

**See also**: SUP-04, `09-fault-tolerance.md`

---

## SUP-09: Children Must `start_link`, and `init` Must Establish Guarantees

**Strength**: MUST

**Summary**: A child's start function must link to the supervisor (`*_link`) so termination is detected, and its `init` must reach a stable state quickly.

```erlang
%% Bad - start (not start_link): the supervisor isn't linked and never learns the child died
start_link() -> gen_server:start(?MODULE, [], []).

%% Good - start_link so the supervisor is linked; init returns a stable state fast (see FT-12)
start_link() -> gen_server:start_link({local, ?MODULE}, ?MODULE, [], []).
init([]) -> {ok, #state{}}.
```

**Rationale**: Supervision works through links: the supervisor must be linked to each child to receive its exit signal, which is why `start` MFAs must call a `*_start_link` function. And because startup is synchronous and ordered, a child's `init` must provide guarantees, not best effort (FT-12, BEH-09) — a slow or flaky `init` stalls or fails the whole tree's boot.

**See also**: SUP-07, `07-otp-behaviours.md` (BEH-09), `09-fault-tolerance.md` (FT-12)

---

## SUP-10: Shape the Tree Around the Error Kernel

**Strength**: CONSIDER

**Summary**: Isolate risky, restart-prone work under its own sub-supervisor so its failures don't disturb the critical, must-stay-up part of the tree.

```erlang
%% Bad - one flat supervisor: critical state and a flaky worker share a restart fate
{ok, {#{strategy => one_for_one}, [critical_state_spec(), flaky_worker_spec()]}}.

%% Good - separate sub-trees: the kernel and the risky workers restart independently
{ok, {#{strategy => one_for_one},
      [#{id => kernel_sup,  start => {kernel_sup,  start_link, []}, type => supervisor},
       #{id => workers_sup, start => {workers_sup, start_link, []}, type => supervisor}]}}.
```

**Rationale**: Tree shape encodes failure isolation. Grouping the must-be-correct core (FT-05) with churny workers under one supervisor means a worker restart storm (and any escalation) can ripple into the kernel. Give risky subsystems their own sub-supervisor so their `intensity` escalations stay local.

**See also**: SUP-02, SUP-06, `09-fault-tolerance.md` (FT-05)

---

## SUP-11: Package Functionality as an OTP Application

**Strength**: SHOULD

**Summary**: Wrap a unit of functionality as an OTP application — a callback module plus an `.app` resource file — so it can be started, stopped, and reused as a unit.

```erlang
%% Bad - a bag of modules on the code path: can't be started/stopped as a unit, no deps, no release

%% Good - an OTP application: an .app resource file naming the callback module, modules, and deps
%% my_app.app:
{application, my_app,
 [{description, "My app"},
  {vsn, "1.0.0"},
  {modules, [my_app_app, my_app_sup, worker]},
  {registered, [my_app_sup]},
  {applications, [kernel, stdlib]},
  {mod, {my_app_app, []}}]}.
```

**Rationale**: An application "can be started and stopped as a unit, and reused in other systems" (OTP Design Principles). The `.app` file declares the version, modules, dependencies, and (for active applications) the callback module via `{mod, ...}`. This is the unit releases and dependency resolution operate on.

**See also**: SUP-12, SUP-13, `12-project-structure.md`

---

## SUP-12: The Application Callback Returns the Top Supervisor

**Strength**: SHOULD

**Summary**: Implement the `application` behaviour: `start/2` starts and returns the top supervisor's pid; `stop/1` does any global cleanup.

```erlang
%% Bad - start/2 starts the tree but discards the pid; OTP can't manage the application's lifecycle
start(_Type, _Args) -> my_app_sup:start_link(), ok.

%% Good - return {ok, Pid} of the top supervisor; OTP links and tracks it
-behaviour(application).
-export([start/2, stop/1]).
start(_Type, _Args) -> my_app_sup:start_link().   %% returns {ok, Pid}
stop(_State) -> ok.
```

**Rationale**: The application controller links to the pid returned by `start/2` (the application's top supervisor), and uses that link to detect failure and to stop the application. Returning `ok` instead of `{ok, Pid}` breaks that contract — the controller has nothing to monitor. `stop/1` runs after the tree is down, for cleanup the supervision tree didn't cover.

**See also**: SUP-11, SUP-16

---

## SUP-13: Declare Dependencies in the `.app` File; Start with `ensure_all_started`

**Strength**: SHOULD

**Summary**: List the applications you depend on in `{applications, [...]}` and boot with `application:ensure_all_started/1`, instead of starting dependencies by hand.

```erlang
%% Bad - start dependencies manually in the right order, and hope you got it right
start() -> application:start(my_app).   %% crashes if ranch/mnesia aren't already up

%% Good - declare deps; ensure_all_started boots the whole graph in dependency order
%% in my_app.app: {applications, [kernel, stdlib, ranch, mnesia]}
application:ensure_all_started(my_app).
```

**Rationale**: `{applications, ...}` declares the start-order graph; `application:start/1` requires every dependency already started (and errors otherwise), while `ensure_all_started/1` walks the declared graph and starts each app in order. Declaring dependencies makes start order data, not hand-maintained procedure.

**See also**: SUP-11, SUP-18

---

## SUP-14: Read Configuration from the Application Environment

**Strength**: SHOULD

**Summary**: Get tunables from the application environment (with `application:get_env/3` and a default), set via `sys.config` — don't hardcode them.

```erlang
%% Bad - hardcode configuration in source; changing it means a recompile
port() -> 8080.

%% Good - read from the application environment with a default
port() -> application:get_env(my_app, port, 8080).
%% sys.config: [{my_app, [{port, 8080}]}].
```

**Rationale**: The application environment is OTP's configuration mechanism: defaults in the `.app` file's `{env, ...}`, overridden per deployment by `sys.config` (and `-my_app key val` flags). `application:get_env/3` with a default keeps modules decoupled from where the value comes from. Hardcoding forces recompilation and prevents per-environment configuration.

**See also**: SUP-11, `12-project-structure.md`

---

## SUP-15: Distinguish Library Applications from Active Applications

**Strength**: CONSIDER

**Summary**: An application with a supervision tree is *active* and declares `{mod, ...}`; a pure library has no tree and omits `{mod, ...}`.

```erlang
%% Bad - a pure library declares a callback module and a supervisor it has nothing to put in
{application, my_lib, [{mod, {my_lib_app, []}}, {modules, [my_lib]}, ...]}.

%% Good - a library application omits {mod, ...}: no callback, no supervision tree to start
{application, my_lib,
 [{description, "helpers"}, {vsn, "1.0.0"},
  {modules, [my_lib]}, {applications, [kernel, stdlib]}]}.
```

**Rationale**: A *library application* (e.g. `stdlib`) only provides code — it has no processes to supervise, so it has no callback module and "starting" it just loads it. Declaring `{mod, ...}` on a library forces an empty supervisor and an `application` callback that exist for no reason. Reserve the active-application machinery for code that actually runs processes.

**See also**: SUP-11, SUP-12

---

## SUP-16: Use Application Start Types to Control Node Fate

**Strength**: CONSIDER

**Summary**: Start an application `permanent`, `transient`, or `temporary` according to whether its termination should bring the node down.

```erlang
%% Bad - a critical app started temporary: if it dies, the node runs on, silently degraded
application:start(my_app, temporary).

%% Good - start an app whose failure must stop the node as permanent
application:start(my_app, permanent).
%% permanent: app termination stops the node; transient: only abnormal stop does; temporary: neither
```

**Rationale**: The start type sets what happens when the application terminates: a `permanent` application stopping terminates the whole node (the right choice for an indispensable subsystem); `transient` stops the node only on an abnormal exit; `temporary` never does. Choosing `temporary` for a critical app turns its death into silent degradation instead of a clean, supervised node restart.

**See also**: SUP-12, `09-fault-tolerance.md`

---

## SUP-17: Ship the System as a Release

**Strength**: SHOULD

**Summary**: Package the running system as an OTP release — a `.rel` file plus tooling (`systools`/`relx`) — producing a self-contained, bootable bundle, not loose `.beam` files.

```erlang
%% Bad - deploy by copying .beam files onto a host and starting erl by hand
%% (no bundled ERTS, no boot script, no version pinning, no sys.config)

%% Good - a release: a .rel naming exact app versions + ERTS, built into a bootable target system
%% my_app.rel:
{release, {"my_app_release", "1.0.0"}, {erts, "14.0"},
 [{kernel, "9.0"}, {stdlib, "5.0"}, {sasl, "4.2"}, {my_app, "1.0.0"}]}.
%% then: bin/my_app_release start   (bundled ERTS + boot script + config)
```

**Rationale**: A release pins exact application and ERTS versions, generates a boot script, and bundles everything needed to start the system reproducibly on a target host (OTP Design Principles, "Releases"). It is also the unit of upgrade: `release_handler` applies the `relup`/`appup` instructions (see `module-dependencies` and `changing-a-supervisor`) for live upgrades. Loose `.beam` deployment has none of these guarantees.

**See also**: SUP-11, SUP-18, `12-project-structure.md`

---

## SUP-18: Coordinate Cross-Application Startup with Included Apps and Start Phases

**Strength**: CONSIDER

**Summary**: When applications must come up in a coordinated sequence, include one in another and use start phases, rather than racing independent flat applications.

```erlang
%% Bad - two apps that must initialise in lock-step are left as independent flat applications
%% (app_b's tree may come up before app_a finished its first phase)

%% Good - include app_b in app_a and sequence with start phases
%% app_a.app: {included_applications, [app_b]}, {start_phases, [{init, []}, {go, []}]}
-behaviour(application).
start_phase(init, _Type, _Args) -> prepare(), ok;
start_phase(go,   _Type, _Args) -> connect(), ok.
```

**Rationale**: An included application is loaded with its parent but its tree is started by the parent's top supervisor, and "the main reason to use included applications over a flat structure is to coordinate start phases" (Designing for Scalability, pp. 221–222). Start phases give you ordered initialisation hooks across the combined tree — the supported way to express cross-app startup ordering beyond simple dependency edges.

**See also**: SUP-13, SUP-17

---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| SUP-01 Supervision tree | SHOULD | Every process has a defined lifecycle |
| SUP-02 Thin supervisors | SHOULD | No business logic in the supervisor |
| SUP-03 Map child spec | SHOULD | `id` + `start` mandatory; map over tuple |
| SUP-04 Restart type | SHOULD | permanent / transient / temporary per child |
| SUP-05 Restart strategy | SHOULD | one_for_one / one_for_all / rest_for_one by dependency |
| SUP-06 Intensity/period | SHOULD | Let crash-loops escalate, don't disable the limit |
| SUP-07 Shutdown spec | SHOULD | Graceful workers; `infinity` supervisors; avoid brutal_kill |
| SUP-08 simple_one_for_one | SHOULD | Dynamic identical children via `start_child` |
| SUP-09 start_link + init | MUST | Link children; `init` must guarantee a stable state |
| SUP-10 Tree around error kernel | CONSIDER | Isolate risky work under its own sub-supervisor |
| SUP-11 OTP application | SHOULD | Callback module + `.app` file; startable unit |
| SUP-12 Application callback | SHOULD | `start/2` returns the top supervisor pid |
| SUP-13 Declare deps | SHOULD | `{applications, ...}` + `ensure_all_started` |
| SUP-14 Env config | SHOULD | `get_env` + `sys.config`, not hardcoded |
| SUP-15 Library vs active | CONSIDER | Library apps omit `{mod, ...}` |
| SUP-16 Start types | CONSIDER | permanent/transient/temporary controls node fate |
| SUP-17 Releases | SHOULD | Self-contained, version-pinned, bootable bundle |
| SUP-18 Included apps / phases | CONSIDER | Coordinate cross-app startup ordering |

## Related Guidelines

- **OTP behaviours**: See `07-otp-behaviours.md` — supervised children are `gen_server`/`gen_statem`/`gen_event`; SUP-07/SUP-09 tie to BEH-09/BEH-10.
- **Fault tolerance**: See `09-fault-tolerance.md` — supervision is the mechanism behind let-it-crash; SUP-06 is FT-13, SUP-09 is FT-12, SUP-10 is FT-05.
- **Project structure**: See `12-project-structure.md` for rebar3 layout, umbrella projects, and Hex packaging of the applications defined here.
- **Production ops**: See `14-production-ops.md` for navigating and observing live supervision trees, and diagnosing restart storms.
- **Release upgrades**: The `appup`/`relup` mechanics referenced by SUP-17 are detailed via `changing-a-supervisor` and `module-dependencies`.

## External References

- [OTP Design Principles — Supervisor Behaviour](https://www.erlang.org/doc/system/sup_princ.html)
- [OTP Design Principles — Applications](https://www.erlang.org/doc/system/applications.html)
- [OTP Design Principles — Releases](https://www.erlang.org/doc/system/release_structure.html)
- *Designing for Scalability with Erlang/OTP* (Cesarini & Vinoski) — included applications and start phases (pp. 215, 221–222)
- *Programming Erlang* (Joe Armstrong) — supervision trees, applications
- *Learn You Some Erlang* — Supervisors, Building an OTP Application
