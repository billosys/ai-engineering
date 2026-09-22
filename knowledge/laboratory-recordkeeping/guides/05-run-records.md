# Run records

A run is one execution attempt under a specified method. Its record starts
before execution and ends with an explicit outcome, even when no usable
measurement was produced.

## Prepare

Use the [run template](../templates/run-record.md). Record:

- full run identity, responsible person/session, condition and planned slot;
- exact protocol and task-packet revisions, including linked examples;
- input inventory, code revision and any uncommitted patch or snapshot;
- hardware, OS, tools, dependencies, configuration, environment variables that
  affect behavior, and external services or models, without secret values;
- commands, working directory, limits, random seed where applicable, and the
  output destinations.

Use a commit plus relevant file paths when the tree is clean. A branch name
alone is mutable. For uncommitted inputs, retain the actual bytes or patch with
an inventory and checksums; writing “dirty tree” is not enough to reconstruct it.
For hosted services, retain reported identities and note what cannot be pinned.

Read required linked material before dependent execution. Missing required
inputs block the affected step; record that fact rather than filling the gap
from remembered versions. In file-following evaluations, distinguish successful
transport, returned contents, contract understanding, and resulting behavior.

## Execute and finish

Record start/end times with offsets, actual commands and exits, observations,
errors, interruptions, and deviations as they occur. Preserve the original
outputs before reducing or scoring them. Keep logs and measurements in `raw/`;
put cleaned, scored, or transformed outputs in `derived/` with their recipes.

Use these run states: `prepared`, `running`, `completed`, `failed`, `blocked`,
`aborted`, `not-run`. `Completed` means execution ended as intended, not that
the hypothesis was supported. Record the scientific outcome separately.
Recover a stale `running` record by documenting what is known about its end;
do not invent a successful completion.

The run index lists all planned slots and actual attempts. Record retries as
new IDs linked to their predecessor and the same planned slot where applicable.
Retain excluded attempts with reasons. Reports distinguish planned samples,
execution attempts, usable measurements, exclusions, and missing evidence;
changing denominators silently can make failed attempts disappear.

## Freeze and revisit

After completion, preserve the capture. Corrections are dated annotations;
reanalysis gets a new output identity. Re-execution always gets a new run ID
and states whether it repeats the original conditions or intentionally changes
them. Pin shared procedures and inputs per run so later improvements do not
rewrite what an earlier attempt actually used.
