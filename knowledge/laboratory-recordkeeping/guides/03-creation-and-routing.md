# Creation and routing

Start from the nearest README and actual directory contents. This decision
sequence chooses the smallest useful record:

1. **A thought, observation, reading note, or possible question?** Add a dated
   journal entry in the relevant lab. Label speculative material exploratory
   and tentative. It need not become an experiment.
2. **A continuing inquiry or capability with no suitable lab?** Create a lab
   entrypoint and update the collection index. A new topic within a lab does
   not automatically need another lab.
3. **A bounded question with an inspectable method?** Create an experiment.
   Record its kind: exploration, comparison, replication, derivation, or
   commissioning. These labels describe intent, not evidence strength.
4. **Another execution of that method?** Create a new run. A retry is another
   attempt, even when the first failed before producing a measurement.
5. **A changed method?** Preserve an amendment with reason, time, and effective
   run IDs. A new central question or incompatible design normally becomes a
   linked successor experiment. A parameter change already allowed by the
   protocol is another run condition.
6. **Analysis of existing observations?** Put scripts, native calculations,
   and recipes in `analysis/`, pointing to source runs. If it generates new
   experimental observations, give that execution a run record.
7. **A reusable setup or input?** Put it in lab `procedures/` or `resources/`
   once reuse exists. Pin the revision used by each experiment.

Cross-lab work has one canonical home, named in the cooperating lab indexes.
Link shared evidence instead of maintaining divergent copies. Findings that
lead to engineering implementation link to that project's planning records.

## Unexpected files

An unfamiliar file is evidence of an unresolved classification, not permission
to delete, move, or ignore it.

- **Already present:** leave it in place initially. Record its path, discovery
  date, apparent producer, and uncertainty in the nearest journal or intake
  record. Inspect enough to determine whether it is source, raw observation,
  derived output, operational debris, or unknown.
- **Newly received:** place it in a lab's `inbox/` when ownership or purpose is
  unresolved. Create `inbox/README.md` with original name/location, receipt
  date, source, checksum where useful, proposed home, and disposition owner.
- **Resolved:** record the destination and rationale before moving it; retain
  the intake entry as a receipt. Keep the source-to-destination mapping.
- **Still unknown:** retain it with an explicit unresolved status and a next
  action. Do not silently promote it to trusted input.

An inbox is temporary intake, not an unindexed archive. Revisit open entries
when pausing or concluding work. Suspected duplicates require identity and
provenance checks before disposition; a duplicate's arrival context can matter.

Do not create blanket ignore patterns for notebooks, raw data, or logs. Ignore
only identified regenerable or local-only files under the collection's storage
policy. Externally retained evidence still needs an inventory entry.
