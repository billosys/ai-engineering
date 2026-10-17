# Independent audit specimens

Exact source copies from the fresh reviewer’s scratch workspace, retained by the
primary context so the meaningful independent checks in final-audit.md can be
reconstructed. These are evidence, not shipped skill files or a runtime dependency.

From this directory, `fennel boundaries.fnl`, `fennel macrodebug.fnl`, and
`fennel --to-be-closed native-protocol.fnl` exercise the named witnesses. The
small implementation exercise runs with `fennel test.fnl` from `app/`; its
vendored settings module must remain in the relative location shown here.
Consult final-audit.md for compile/AOT commands, initial failed assumptions,
expected results and coverage limits. Original temporary compiled outputs were
not copied; regenerate them with the documented toolchain.
