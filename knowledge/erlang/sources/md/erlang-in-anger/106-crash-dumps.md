# Reading Crash Dumps

Whenever an Erlang node crashes, it will generate a crash dump[^1].

The format is mostly documented in Erlang’s official documentation[^2], and anyone willing to dig deeper inside of it will likely be able to figure out what data means by looking at that documentation. There will be specific data that is hard to understand without also understanding the part of the VM they refer to, but that might be too complex for this document.

The crash dump is going to be named `erl_crash.dump` and be located wherever the Erlang process was running by default. This behaviour (and the file name) can be overridden by specifying the `ERL_CRASH_DUMP` environment variable[^3].

## General View

Reading the crash dump will be useful to figure out possible reasons for a node to die *a posteriori*. One way to get a quick look at things is to use recon’s `erl_crashdump_analyzer.sh`[^4] and run it on a crash dump:

```text
$ ./recon/script/erl_crashdump_analyzer.sh erl_crash.dump
analyzing erl_crash.dump, generated on:  Thu Apr 17 18:34:53 2014

Slogan: eheap_alloc: Cannot allocate 2733560184 bytes of memory
(of type "old_heap").

Memory:
===
  processes: 2912 Mb
  processes_used: 2912 Mb
  system: 8167 Mb
  atom: 0 Mb
  atom_used: 0 Mb
  binary: 3243 Mb
  code: 11 Mb
  ets: 4755 Mb
  ---
  total: 11079 Mb

Different message queue lengths (5 largest different):
===
      1 5010932
      2 159
      5 158
     49 157
      4 156

Error logger queue length:
===
0

File descriptors open:
===
  UDP:  0
  TCP:  19951
  Files:  2
  ---
  Total:  19953

Number of processes:
===
36496

Processes Heap+Stack memory sizes (words) used in the VM (5 largest
different):
===
      1 284745853
      1 5157867
      1 4298223
      2 196650
     12 121536

Processes OldHeap memory sizes (words) used in the VM (5 largest
different):
===
      3 318187
      9 196650
     14 121536
     64 75113
     15 46422

Process States when crashing (sum):
===
      1 Garbing
     74 Scheduled
  36421 Waiting
```

This data dump won’t point out a problem directly to your face, but will be a good clue as to where to look. For example, the node here ran out of memory and had 11079 Mb out of 15 Gb used (I know this because that’s the max instance size we were using!) This can be a symptom of:

memory fragmentation;

memory leaks in C code or drivers;

lots of memory that got to be garbage-collected before generating the crash dump[^5].

More generally, look for anything surprising for memory there. Correlate it with the number of processes and the size of mailboxes. One may explain the other.

In this particular dump, one process had 5 million messages in its mailbox. That’s telling. Either it doesn’t match on all it can get, or it is getting overloaded. There are also dozens of processes with hundreds of messages queued up — this can point towards overload or contention. It’s hard to have general advice for your generic crash dump, but there still are a few pointers to help figure things out.

## Full Mailboxes

For loaded mailboxes, looking at large counters is the best way to do it. If there is one large mailbox, go investigate the process in the crash dump. Figure out if it’s happening because it’s not matching on some message, or overload. If you have a similar node running, you can log on it and go inspect it. If you find out many mailboxes are loaded, you may want to use recon’s `queue_fun.awk` to figure out what function they’re running at the time of the crash:

```text
$ awk -v threshold=10000 -f queue_fun.awk /path/to/erl_crash.dump 
MESSAGE QUEUE LENGTH: CURRENT FUNCTION
======================================
10641: io:wait_io_mon_reply/2
12646: io:wait_io_mon_reply/2
32991: io:wait_io_mon_reply/2
2183837: io:wait_io_mon_reply/2
730790: io:wait_io_mon_reply/2
80194: io:wait_io_mon_reply/2
...
```

This one will run over the crash dump and output all of the functions scheduled to run for processes with at least 10000 messages in their mailbox. In the case of this run, the script showed that the entire node was locking up waiting on IO for `io:format/2` calls, for example.

## Too Many (or too few) Processes

The process count is mostly useful when you know your node’s usual average count[^6], in order to figure if it’s abnormal or not.

A count that is higher than normal may reveal a specific leak or overload, depending on applications.

If the process count is extremely low compared to usual, see if the node terminated with a slogan like:

```text
Kernel pid terminated (application_controller)
  ({application_terminated, <AppName>, shutdown})
```

In such a case, the issue is that a specific application (`<AppName>`) has reached its maximal restart frequency within its supervisors, and that prompted the node to shut down. Error logs that led to the cascading failure should be combed over to figure things out.

## Too Many Ports

Similarly to the process count, the port count is simple and mostly useful when you know your usual values[^7].

A high count may be the result of overload, Denial of Service attacks, or plain old resource leaks. Looking at the type of port leaked (TCP, UDP, or files) can also help reveal if there was contention on specific resources, or if the code using them is just wrong.

## Can’t Allocate Memory

These are by far the most common types of crashes you are likely to see. There’s so much to cover, that Chapter Memory Leaks is dedicated to understanding them and doing the required debugging on live systems.

In any case, the crash dump will help figure out what the problem was after the fact. The process mailboxes and individual heaps are usually good indicators of issues. If you’re running out of memory without any mailbox being outrageously large, look at the processes heap and stack sizes as returned by the recon script.

In case of large outliers at the top, you know some restricted set of processes may be eating up most of your node’s memory. In case they’re all more or less equal, see if the amount of memory reported sounds like a lot.

If it looks more or less reasonable, head towards the "Memory" section of the dump and check if a type (ETS or Binary, for example) seems to be fairly large. They may point towards resource leaks you hadn’t expected.

## Exercises

### Review Questions

1.  How can you choose where a crash dump will be generated?

2.  What are common avenues to explore if the crash dump shows that the node ran out of memory?

3.  What should you look for if the process count is suspiciously low?

4.  If you find the node died with a process having a lot of memory, what could you do to find out which one it was?

### Hands-On

Using the analysis of a crash dump in Section General View:

1.  What are specific outliers that could point to an issue?

2.  Does it look like repeated errors are the issue? If not, what could it be?

[^1]: If it isn’t killed by the OS for violating ulimits while dumping or didn’t segfault.

[^2]: <http://www.erlang.org/doc/apps/erts/crash_dump.html>

[^3]: Heroku’s Routing and Telemetry teams use the `heroku_crashdumps` app to set the path and name of the crash dumps. It can be added to a project to name the dumps by boot time and put them in a pre-set location

[^4]: <https://github.com/ferd/recon/blob/master/script/erl_crashdump_analyzer.sh>

[^5]: Notably here is reference-counted binary memory, which sits in a global heap, but ends up being garbage-collected before generating the crash dump. The binary memory can therefore be underreported. See Chapter Memory Leaks for more details

[^6]: See subsection Processes for details

[^7]: See subsection Ports for details
