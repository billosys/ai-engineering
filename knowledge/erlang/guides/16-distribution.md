# Distribution

How to reason about and build distributed Erlang systems: transparent node connectivity and its limits, the network fallacies, designing for partitions and the CAP trade-off, the cookie as a weak secret (and securing the transport), cluster-wide naming, cross-node messaging semantics, and node redundancy. The single-node concurrency primitives are in `06-processes-and-concurrency.md`; the fault-tolerance design these build on is in `09-fault-tolerance.md`.

Target environment: **Erlang/OTP 27+**. Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Grounded in: Designing for Scalability with Erlang/OTP (Distributed Architectures, CAP), the Erlang Reference Manual (Distributed Erlang), *Erlang in Anger*, and Learn You Some Erlang (Distribunomicon).

---

## DIST-01: Distributed Erlang Is Transparent — but Not Always the Right Tool

**Strength**: CONSIDER

**Summary**: Nodes communicate transparently (a remote `Pid` works like a local one), which is ideal for small, trusted, single-datacenter clusters — and a poor fit for multi-DC, untrusted, or massive-scale systems.

```erlang
%% Bad - assume distributed Erlang scales unchanged to a huge, multi-datacenter, public deployment

%% Good - use it where it shines (small trusted cluster), with eyes open about the limits
{ok, Pid} = rpc:call('worker@hostB', my_mod, start, [Args]),   %% remote call, transparent
Pid ! {work, Job}.                                             %% send across nodes like local
%% for multi-DC / untrusted / very-large scale, layer a different transport on top
```

**Rationale**: Distributed Erlang "lets nodes communicate transparently… works out of the box but is not always the right tool" — it suits smaller clusters in one datacenter, less so when multi-DC, security, availability, and massive scalability matter (Designing for Scalability). Location transparency is a huge productivity win within its sweet spot; pushing it past that (full mesh over the open internet) invites the problems the rest of this chapter covers.

**See also**: DIST-07, DIST-13

---

## DIST-02: Don't Trust the Network — Remember the Fallacies

**Strength**: SHOULD

**Summary**: Design as if the network is unreliable, because it is; the "network is reliable" assumption is the first fallacy of distributed computing.

```erlang
%% Bad - fire a cross-node message and assume it arrives and is acted upon
'other@host' ! {commit, Tx}.   %% no ack, no timeout, no retry: silent loss under a blip

%% Good - require acknowledgement with a timeout; treat no-reply as failure
Ref = make_ref(),
{server, 'other@host'} ! {commit, Tx, self(), Ref},
receive {ack, Ref} -> ok after 5000 -> {error, no_ack} end.
```

**Rationale**: The fallacies of distributed computing — starting with "the network is reliable" — are "just as relevant to the systems we design today" (Designing for Scalability). Network issues "occur when you least expect them," so any cross-node interaction needs explicit acknowledgement, timeouts, and a failure path. Code that assumes delivery breaks the first time a link blips.

**See also**: DIST-03, DIST-10, `09-fault-tolerance.md` (FT-14)

---

## DIST-03: Design for Partitions — You Can't Tell Slow from Dead

**Strength**: SHOULD

**Summary**: A partition makes a remote node indistinguishable from a slow one; design for it instead of assuming a clean up/down signal.

```erlang
%% Bad - treat a monitor 'DOWN' (or a missed tick) as "the node is gone forever" and act irreversibly
{nodedown, N} -> delete_all_data_owned_by(N).   %% but N may just be partitioned, and will return

%% Good - treat unreachability as temporary; reconcile on reconnect, avoid irreversible action
{nodedown, N} -> mark_unreachable(N), schedule_reconcile(N);
{nodeup, N}   -> reconcile_with(N).
```

**Rationale**: "It is impossible to differentiate between a node crash and a slow node" (Designing for Scalability) — a partition delays or drops messages, so `nodedown` may mean "crashed" or merely "temporarily unreachable." Taking an irreversible action (deleting data, electing a sole leader) on that ambiguous signal causes split-brain damage when the node returns. Design reconciliation, not assumption.

**See also**: DIST-02, DIST-04, DIST-12

---

## DIST-04: Make the CAP Trade-off Explicitly

**Strength**: CONSIDER

**Summary**: Under a partition you can have consistency or availability, not both; choose deliberately per subsystem rather than by accident.

```erlang
%% Bad - assume you get consistency AND availability during a partition (you cannot)

%% Good - pick a side for each operation, consciously
%% CP: refuse writes without a quorum (consistent, not available during partition)
write(K, V) -> case quorum_reachable() of true -> replicate(K, V); false -> {error, no_quorum} end.
%% AP: accept writes on either side, reconcile later (available, eventually consistent)
write_ap(K, V) -> local_write(K, V), enqueue_anti_entropy(K).
```

**Rationale**: "In any distributed system it is impossible to fully provide consistency, availability, and partition tolerance at all times" (CAP theorem; Designing for Scalability). Since partitions *will* happen (DIST-03), the real choice is C-vs-A under partition. Decide explicitly — a quorum/CP design rejects writes when isolated; an AP design accepts them and reconciles — rather than discovering your accidental choice during an outage.

**See also**: DIST-03, DIST-14

---

## DIST-05: The Cookie Is Not Security — Don't Expose Distribution to Untrusted Networks

**Strength**: MUST

**Summary**: A connected node can run arbitrary code on its peers; the cookie is a weak shared secret, so never expose Erlang distribution to an untrusted network, and use TLS for the distribution transport.

```erlang
%% Bad - a publicly-reachable node with a guessable/shared cookie: remote code execution for anyone
%% erl -name n@public-ip -setcookie monster   (epmd 4369 + dist ports open to the internet)

%% Good - distribution only on a trusted network, TLS-encrypted, firewalled
%% vm.args: -proto_dist inet_tls -ssl_dist_optfile /etc/my/dist_ssl.conf
%% epmd and dist ports reachable only from trusted hosts; strong, secret cookie
```

**Rationale**: Any node that completes the distribution handshake can spawn processes and call any function on its peers — full remote code execution — and the cookie is only a plaintext shared atom, trivially sniffed or guessed. Exposing distribution (epmd on 4369 plus the dynamic dist ports) to an untrusted network is a critical vulnerability. Keep distribution on a private network, firewall the ports, encrypt with `inet_tls`, and treat the cookie as a secret, not a control.

**See also**: DIST-06, `14-production-ops.md` (OPS-02)

---

## DIST-06: Use Named Nodes and Understand How They Connect

**Strength**: SHOULD

**Summary**: Run named nodes (`-name`/`-sname`), know that `epmd` maps names to ports, and that connections form on first reference.

```erlang
%% Bad - rely on default/unnamed nodes and "magic" connectivity you can't reason about

%% Good - named nodes with a known discovery mechanism
%% $ erl -name myapp@10.0.0.5 -setcookie SECRET
1> net_adm:ping('worker@10.0.0.6').   %% epmd resolves the name; a connection is established
pong
2> nodes().                            %% see the cluster you're connected to
```

**Rationale**: Each host runs `epmd` (the port mapper) which tells callers which TCP port a named node listens on; referring to a remote node (a `ping`, a send, an `rpc`) triggers the connection. Using long names (`-name`, FQDN/IP) and a known discovery path makes cluster membership something you can reason about and operate, rather than relying on implicit defaults.

**See also**: DIST-05, DIST-07

---

## DIST-07: Distributed Erlang Is a Transitive Full Mesh — Use Hidden Nodes to Limit It

**Strength**: CONSIDER

**Summary**: By default every node connects to every other (and connections are transitive); use hidden nodes (or `-connect_all false`) when you don't want a full mesh.

```erlang
%% Bad - join a 50-node mesh with a tool/debug node, forcing N^2 connections you don't need

%% Good - connect as a hidden node so you don't trigger the transitive full-mesh join
%% $ erl -name tool@host -setcookie SECRET -hidden
%% (or -connect_all false to manage connections explicitly)
```

**Rationale**: Distributed Erlang forms a fully-connected network: if A connects to B and B to C, A and C also connect (transitive). That is fine for small clusters but becomes `O(n²)` connections and chatter at scale, and a transient tool node can perturb the whole mesh. A `-hidden` node connects only where told and isn't propagated, which is the right mode for observers, tools, and bridges.

**See also**: DIST-01, DIST-06

---

## DIST-08: Register Cluster-Wide Names with `global` or `pg`, Not Local `register`

**Strength**: CONSIDER

**Summary**: A local registered name is node-local; to address a process cluster-wide use `global` (unique names) or `pg` (process groups).

```erlang
%% Bad - local registration isn't visible on other nodes
register(coordinator, Pid).
{coordinator, 'other@host'} ! Msg.   %% fragile: assumes the name exists there too

%% Good - cluster-wide registration
global:register_name(coordinator, Pid),
global:send(coordinator, Msg).        %% resolves cluster-wide
%% or pg for a group of equivalent workers:
pg:join(workers, self()),
[P ! Msg || P <- pg:get_members(workers)].
```

**Rationale**: `register/2` names are local to one node (PC-11), so addressing a remote registered name assumes it exists and is correct there. `global` provides cluster-unique names with conflict resolution; `pg` (the modern process-groups module) maintains replicated group membership across the cluster. Both are partition-aware to a degree — understand their behaviour under split (DIST-03) before relying on them.

**See also**: DIST-03, `06-processes-and-concurrency.md` (PC-11)

---

## DIST-09: Tune `net_tick_time` for Your Failure-Detection Needs

**Strength**: CONSIDER

**Summary**: The distribution heartbeat (`net_tick_time`) sets how quickly a dead node is detected; tune it consciously, the same on every node.

```erlang
%% Bad - leave the default tick and be surprised by ~60s detection latency (or set it per-node, mismatched)

%% Good - set net_tick_time consistently across the cluster for your latency/false-positive balance
%% vm.args: -kernel net_ticktime 15
%% lower => faster detection, more false positives under load; higher => slower, more tolerant
```

**Rationale**: Nodes exchange periodic ticks; if several are missed the connection is declared down. The default (~60s) is conservative — too slow for some failover needs; lowering it detects failures faster but raises false positives when a node is merely busy or GC-pausing (DIST-03). It must match across nodes. Choose the value for your tolerance, and remember a missed tick is "unreachable," not "dead."

**See also**: DIST-03, `14-production-ops.md` (OPS-10)

---

## DIST-10: Cross-Node Sends Copy and Can Fail or Reorder

**Strength**: SHOULD

**Summary**: A message to a remote process is serialized and copied over the wire; it can be lost under partition, and ordering guarantees are weaker than locally.

```erlang
%% Bad - send a huge term to a remote pid in a hot path and assume in-order, guaranteed delivery
RemotePid ! {data, HugeTerm}.

%% Good - keep cross-node messages small, acknowledge them, and don't rely on global ordering
RemotePid ! {data_ref, locator(HugeTerm), self(), Ref},
receive {ack, Ref} -> ok after Timeout -> retry end.
```

**Rationale**: Inter-node messaging serializes the term (term_to_binary) and ships it, so large messages are expensive (PF-13/PC-15) and consume the distribution link. Delivery is best-effort: under a partition the message can be lost, and the pairwise-FIFO guarantee (PC-14) holds only while the connection stays up. Keep cross-node messages small, idempotent (DIST-11), and acknowledged.

**See also**: DIST-02, DIST-11, `06-processes-and-concurrency.md` (PC-14, PC-15)

---

## DIST-11: Make Cross-Node Operations Idempotent and Retryable

**Strength**: SHOULD

**Summary**: Because a cross-node request may be lost (or its reply lost), design operations so a retry is safe.

```erlang
%% Bad - retry a non-idempotent remote operation after a timeout: it may apply twice
case rpc:call(N, bank, debit, [Acct, Amt]) of
    {badrpc, _} -> rpc:call(N, bank, debit, [Acct, Amt]);   %% double debit on lost-reply
    Ok -> Ok
end.

%% Good - tag the operation so the remote side recognises a duplicate
rpc:call(N, bank, debit, [Acct, Amt, ReqId]).   %% remote: dedupe on ReqId, safe to retry
```

**Rationale**: A timeout on a remote call is ambiguous — the request may have been lost, or executed with the reply lost (DIST-03). Retrying a non-idempotent operation risks applying it twice. Idempotent operations (a unique request id the receiver deduplicates) make at-least-once delivery safe, which is the practical foundation for reliable cross-node work (FT-14).

**See also**: DIST-10, `09-fault-tolerance.md` (FT-14)

---

## DIST-12: Use Distributed Application Failover/Takeover for Node Redundancy

**Strength**: CONSIDER

**Summary**: To survive a node failure, configure an application to fail over to a standby node (and take over when the primary returns) via the kernel `distributed` configuration.

```erlang
%% Bad - a critical application runs on one node only; that node dies and the service is gone

%% Good - a distributed application with an ordered list of nodes (sys.config)
{kernel, [{distributed, [{my_app, 5000, ['a@host', 'b@host']}]},
          {sync_nodes_mandatory, ['b@host']},
          {sync_nodes_timeout, 30000}]}.
%% my_app runs on a@host; if it dies, it starts on b@host after 5s; takeover on a@host's return
```

**Rationale**: Single-node supervision (chapters 08/09) recovers process and subtree failures, but not the loss of a whole node — that needs redundancy across nodes (FT-15). OTP distributed applications give built-in failover (start elsewhere when the primary dies) and takeover (move back when it returns), coordinated through the kernel `distributed`/`sync_nodes` configuration. Mind the partition caveats (DIST-03) — failover on a partition can produce two primaries.

**See also**: DIST-03, `09-fault-tolerance.md` (FT-15), `08-supervision-and-applications.md` (SUP-16)

---

## DIST-13: Reach for a Different Transport at Large or Untrusted Scale

**Strength**: CONSIDER

**Summary**: For very large clusters, multi-datacenter, or untrusted boundaries, layer an explicit transport/topology (partitioned groups, a message broker, HTTP/gRPC) instead of one flat distributed-Erlang mesh.

```erlang
%% Bad - force a 200-node, multi-region system into a single full-mesh distributed-Erlang cluster

%% Good - bound the mesh and bridge across boundaries explicitly
%% - partition into smaller fully-connected groups (e.g. partisan / s_groups / sd_erlang ideas)
%% - cross datacenters and trust boundaries with an explicit protocol (broker, HTTP, gRPC)
%% - keep distributed Erlang for the trusted, intra-DC core
```

**Rationale**: The transitive full mesh (DIST-07) and the security model (DIST-05) both break down at large scale and across trust boundaries. Approaches that bound connectivity into smaller groups, and explicit messaging across datacenters/boundaries, scale and secure better than one flat mesh. Use distributed Erlang for the trusted core it's good at, and a deliberate transport for the rest.

**See also**: DIST-01, DIST-05, DIST-07

---

## DIST-14: Use Distributed Mnesia Knowingly — Mind Replication and Partitions

**Strength**: CONSIDER

**Summary**: Mnesia gives transactional, replicated, in-VM storage across nodes, but its behaviour under network partition (and the cost of replication) must be understood before you rely on it.

```erlang
%% Bad - assume replicated Mnesia "just works" through a partition with no reconciliation plan

%% Good - choose table storage/replication deliberately, and decide partition behaviour
%% ram_copies / disc_copies on chosen nodes; transactions for consistency;
%% on a partition Mnesia can split-brain -> plan reconciliation / majority, or use dirty ops knowingly
mnesia:transaction(fun() -> mnesia:write(Record) end).   %% consistent within a connected partition
```

**Rationale**: Mnesia integrates with distributed Erlang for replicated tables and transactions, but it inherits the CAP trade-off (DIST-04): a network partition can leave replicas divergent (split-brain), and reconciliation is the application's problem. Choose storage types and replication consciously, use transactions where you need consistency (and understand that dirty operations skip it), and have a partition-recovery plan. For purely local, non-persistent data, ETS is faster (PF-12).

**See also**: DIST-04, `10-performance.md` (PF-12)

---

## DIST-15: Secure and Operate the Distribution Transport

**Strength**: SHOULD

**Summary**: In production, encrypt distribution with TLS, lock down `epmd` and the dist ports, and treat the cluster network as infrastructure to monitor.

```erlang
%% Bad - plaintext distribution on a shared network, epmd open, ports unrestricted

%% Good - TLS-encrypted distribution, restricted ports, monitored connectivity
%% vm.args: -proto_dist inet_tls -ssl_dist_optfile /etc/my/dist.conf
%%          -kernel inet_dist_listen_min 9100 inet_dist_listen_max 9105
%% firewall epmd (4369) and 9100-9105 to trusted hosts; monitor nodedown/nodeup events
```

**Rationale**: Distribution is a privileged channel (DIST-05), so production deployments encrypt it (`inet_tls`), pin the dist port range (so firewalls can restrict it), and limit `epmd` exposure. Operationally, subscribe to `nodeup`/`nodedown` (`net_kernel:monitor_nodes/1`) and trend connectivity so partitions and flapping links are visible (OPS-13) rather than silent.

**See also**: DIST-05, `14-production-ops.md` (OPS-13)

---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| DIST-01 Transparent, with limits | CONSIDER | Great intra-DC; not for multi-DC/untrusted/huge |
| DIST-02 Don't trust the network | SHOULD | Ack + timeout + failure path on every cross-node call |
| DIST-03 Design for partitions | SHOULD | Slow vs dead is indistinguishable |
| DIST-04 CAP trade-off | CONSIDER | Choose C-vs-A per subsystem, explicitly |
| DIST-05 Cookie ≠ security | MUST | Never expose distribution to untrusted networks |
| DIST-06 Named nodes + epmd | SHOULD | Know how nodes resolve and connect |
| DIST-07 Transitive full mesh | CONSIDER | Hidden nodes to avoid the `O(n²)` mesh |
| DIST-08 `global`/`pg` naming | CONSIDER | Cluster-wide names, not local `register` |
| DIST-09 `net_tick_time` | CONSIDER | Tune failure-detection latency, cluster-wide |
| DIST-10 Cross-node sends copy | SHOULD | Small, acked, no global ordering |
| DIST-11 Idempotent + retryable | SHOULD | Timeout is ambiguous; dedupe on a request id |
| DIST-12 Failover/takeover | CONSIDER | Node-level redundancy via `distributed` config |
| DIST-13 Other transports at scale | CONSIDER | Bound the mesh; explicit cross-boundary protocol |
| DIST-14 Distributed Mnesia | CONSIDER | Replication + partition behaviour is yours to plan |
| DIST-15 Secure the transport | SHOULD | TLS dist, locked ports, monitored connectivity |

## Related Guidelines

- **Processes & concurrency**: See `06-processes-and-concurrency.md` — local naming (PC-11), message copy/ordering (PC-14/PC-15) generalise across nodes.
- **Fault tolerance**: See `09-fault-tolerance.md` — idempotence (FT-14) and removing single points of failure (FT-15) are the cross-node forms of DIST-11/DIST-12.
- **Supervision & applications**: See `08-supervision-and-applications.md` (SUP-16) for application start types behind failover.
- **Performance**: See `10-performance.md` (PF-12, PF-13) for ETS-vs-Mnesia and message-copy cost.
- **Production ops**: See `14-production-ops.md` — securing/monitoring distribution (OPS-13) and the remote-shell precondition (OPS-02).

## External References

- [Erlang Reference Manual — Distributed Erlang](https://www.erlang.org/doc/system/distributed.html)
- [Erlang/OTP — Using TLS for Erlang Distribution](https://www.erlang.org/doc/apps/ssl/ssl_distribution.html)
- *Designing for Scalability with Erlang/OTP* (Cesarini & Vinoski) — Distributed Architectures; CAP theorem (pp. 382–418)
- *Learn You Some Erlang* — Distribunomicon; Distributed OTP Applications
- *Erlang in Anger* (Fred Hébert) — connecting to and operating remote nodes
