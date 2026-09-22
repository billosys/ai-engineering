# Worked recordkeeping decisions

These are hypothetical routing examples, not records of completed experiments.
They show how the guides affect actions in a collection using the default layout.

## A first notebook entry

A researcher suspects a Maxima simplification depends on an unstated positivity
assumption. They create a dated journal entry recording the expression,
assumption, source, and uncertainty. They do not need an experiment folder.
When they decide to examine a bounded set of identities and counterexamples,
they create a derivation experiment linked back to that entry.

## A local coding-model comparison

A lab maintains a local inference setup. Its installation instructions live in
`procedures/`; an experiment comparing linked-file compliance pins the exact
procedure, model configuration, task packet, rubric, and linked code examples.
The first attempt cannot reach the filesystem tool. It ends as `blocked`, with
the transport error retained. A repaired attempt receives a new run ID and
links to the same planned slot. The report distinguishes transport failure
from observed model behavior and retains both attempts in its accounting.

## An Octave analysis is corrected

A script used the wrong unit conversion while aggregating existing runs. The
researcher retains the original raw observations and analysis output, records
the correction, and writes a newly identified analysis output. The revised
report links both outputs and explains which finding changed. If the error
affected acquisition as well, new acquisition attempts receive new run IDs.

## An unexplained CSV is discovered

A CSV already exists in an experiment directory. Its filename suggests a
successful benchmark, but its producer and conditions are unknown. Leave it
in place and record that uncertainty in the journal. Do not score it or move
it into a trusted raw-evidence directory. If a later source trace establishes
its origin, add the inventory identity and record the routing decision.

## A new external dataset arrives

A dataset arrives before its destination is clear. Put permitted material in
the lab inbox, or an external store if large, with an intake receipt retaining
its source, original name, checksum, and access terms. Once classified, update
the receipt with its canonical inventory and destination. Do not silently
delete the receipt after the inbox has been emptied.

## Several labs use one calibration

The originating lab retains the calibration procedure and dataset. Other labs
link to that canonical record and pin its revision in their inputs. A revised
calibration does not retroactively change earlier runs. A lab may share the
same custodian while retaining its own creator and experiment identities.

## A reader contradicts a finding

A reader reconstructs an experiment with a newer numerical library and obtains
a different result. Preserve that execution as a new run, including the changed
dependency. Report the discrepancy without claiming it is an exact replication.
A follow-up can isolate the library version. Link the discrepancy from the
original report so future readers encounter the unresolved evidence.
