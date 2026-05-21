# Runtime Metrics

One of the best selling points of the Erlang VM for production use is how transparent it can be for all kinds of introspection, debugging, profiling, and analysis at run time.

The advantage of having these runtime metrics accessible programmatically is that building tools relying on them is easy, and building automation for some tasks or watchdogs is equally simple[^1]. Then, in times of need, it’s also possible to bypass the tools and go direct to the VM for information.

A practical approach to growing a system and keeping it healthy in production is to make sure all angles are observable: in the large, and in the small. There’s no generic recipe to tell in advance what is going to be normal or not. You want to keep a lot of data and to look at it from time to time to form an idea about what your system looks like under normal circumstances. The day something goes awry, you will have all these angles you’ve grown to know, and it will be simpler to find what is off and needs fixing.

For this chapter (and most of those that follow), most of the concepts or features to be shown are accessible through code in the standard library, part of the regular OTP distribution.

However, these features aren’t all in one place, and can make it too easy to shoot yourself in the foot within a production system. They also tend to be closer to building blocks than usable tools.

Therefore, to make the text lighter and to be more usable, common operations have been regrouped in the `recon`[^2] library, and are generally production-safe.

## Global View

For a view of the VM in the large, it’s useful to track statistics and metrics general to the VM, regardless of the code running on it. Moreover, you should aim for a solution that allows long-term views of each metric — some problems show up as a very long accumulation over weeks that couldn’t be detected over small time windows.

Good examples for issues exposed by a long-term view include memory or process leaks, but also could be regular or irregular spikes in activities relative to the time of the day or week, which can often require having months of data to be sure about it.

For these cases, using existing Erlang metrics applications is useful. Common options are:

`folsom`[^3] to store metrics in memory within the VM, whether global or app-specific..

`vmstats`[^4] and `statsderl`[^5], sending node metrics over to graphite through `statsd`[^6].

`exometer`[^7], a fancy-pants metrics system that can integrate with `folsom` (among other things), and a variety of back-ends (graphite, collectd, `statsd`, Riak, SNMP, etc.). It’s the newest player in town

`ehmon`[^8] for output done directly to standard output, to be grabbed later through specific agents, splunk, and so on.

custom hand-rolled solutions, generally using ETS tables and processes periodically dumping the data.[^9]

or if you have nothing and are in trouble, a function printing stuff in a loop in a shell[^10].

It is generally a good idea to explore them a bit, pick one, and get a persistence layer that will let you look through your metrics over time.

### Memory

The memory reported by the Erlang VM in most tools will be a variant of what is reported by `erlang:memory()`:

```erlang-repl
1> erlang:memory().
[{total,13772400},
 {processes,4390232},
 {processes_used,4390112},
 {system,9382168},
 {atom,194289},
 {atom_used,173419},
 {binary,979264},
 {code,4026603},
 {ets,305920}]
```

This requires some explaining.

First of all, all the values returned are in bytes, and they represent memory *allocated* (memory actively used by the Erlang VM, not the memory set aside by the operating system for the Erlang VM). It will sooner or later look much smaller than what the operating system reports.

The `total` field contains the sum of the memory used for `processes` and `system` (which is incomplete, unless the VM is instrumented!). `processes` is the memory used by Erlang processes, their stacks and heaps. `system` is the rest: memory used by ETS tables, atoms in the VM, refc binaries[^11], and some of the hidden data I mentioned was missing.

If you want the total amount of memory owned by the virtual machine, as in the amount that will trip system limits (`ulimit`), this value is more difficult to get from within the VM. If you want the data without calling `top` or `htop`, you have to dig down into the VM’s memory allocators to find things out.[^12]

Fortunately, recon has the function `recon_alloc:memory/1` to figure it out, where the argument is:

`used` reports the memory that is actively used for allocated Erlang data;

`allocated` reports the memory that is reserved by the VM. It includes the memory used, but also the memory yet-to-be-used but still given by the OS. This is the amount you want if you’re dealing with `ulimit` and OS-reported values.

`unused` reports the amount of memory reserved by the VM that is not being allocated. Equivalent to `allocated - used`.

`usage` returns a percentage (0.0 .. 1.0) of used over allocated memory ratios.

There are additional options available, but you’ll likely only need them when investigating memory leaks in chapter Memory Leaks

### CPU

Unfortunately for Erlang developers, CPU is very hard to profile. There are a few reasons for this:

The VM does a lot of work unrelated to processes when it comes to scheduling — high scheduling work and high amounts of work done by the Erlang processes are hard to characterize.

The VM internally uses a model based on *reductions*, which represent an arbitrary number of work actions. Every function call, including BIFs, will increment a process reduction counter. After a given number of reductions, the process gets descheduled.

To avoid going to sleep when work is low, the threads that control the Erlang schedulers will do busy looping. This ensures the lowest latency possible for sudden load spikes. The VM flag `+sbwt none|very_short|short|medium|long|very_long` can be used to change this value.

These factors combine to make it fairly hard to find a good absolute measure of how busy your CPU is actually running Erlang code. It will be common for Erlang nodes in production to do a moderate amount of work and use a lot of CPU, but to actually fit a lot of work in the remaining place when the workload gets higher.

The most accurate representation for this data is the scheduler wall time. It’s an optional metric that needs to be turned on by hand on a node, and polled at regular intervals. It will reveal the time percentage a scheduler has been running processes and normal Erlang code, NIFs, BIFs, garbage collection, and so on, versus the amount of time it has spent idling or trying to schedule processes.

The value here represents *scheduler utilization* rather than CPU utilization. The higher the ratio, the higher the workload.

While the basic usage is explained in the Erlang/OTP reference manual[^13], the value can be obtained by calling recon:

```erlang-repl
1> recon:scheduler_usage(1000).
[{1,0.9919596133421669},
 {2,0.9369579039389054},
 {3,1.9294092120138725e-5},
 {4,1.2087551402238991e-5}]
```

The function `recon:scheduler_usage(N)` will poll for `N` milliseconds (here, 1 second) and output the value of each scheduler. In this case, the VM has two very loaded schedulers (at 99.2% and 93.7% repectively), and two mostly unused ones at far below 1%. Yet, a tool like `htop` would report something closer to this for each core:

```text
[|||||||||||||||||||||||||     70.4%]
[|||||||                       20.6%]
[|||||||||||||||||||||||||||||100.0%]
[||||||||||||||||              40.2%]
```

The result being that there is a decent chunk of CPU usage that would be mostly free for scheduling actual Erlang work (assuming the schedulers are busy waiting more than trying to select tasks to run), but is being reported as busy by the OS.

Another interesting behaviour possible is that the scheduler usage may show a higher rate (1.0) than what the OS will report. Schedulers waiting for os resources are considered utilized as they cannot handle more work. If the OS itself is holding up on non-CPU tasks it is still possible for Erlang’s schedulers not to be able to do more work and report a full ratio.

These behaviours may especially be important to consider when doing capacity planning, and can be better indicators of headroom than looking at CPU usage or load.

### Processes

Trying to get a global view of processes is helpful when trying to assess how much work is being done in the VM in terms of *tasks*. A general good practice in Erlang is to use processes for truly concurrent activities — on web servers, you will usually get one process per request or connection, and on stateful systems, you may add one process per-user — and therefore the number of processes on a node can be used as a metric for load.

Most tools mentioned in section Global View will track them in one way or another, but if the process count needs to be done manually, calling the following expression is enough:

```erlang-repl
1> length(processes()).
56535
```

Tracking this value over time can be extremely helpful to try and characterize load or detect process leaks, along with other metrics you may have around.

### Ports

In a manner similar to processes, *Ports* should be considered. Ports are a datatype that encompasses all kinds of connections and sockets opened to the outside world: TCP sockets, UDP sockets, SCTP sockets, file descriptors, and so on.

There is a general function (again, similar to processes) to count them: `length(erlang:ports())`. However, this function merges in all types of ports into a single entity. Instead, one can use `recon` to get them sorted by type:

```erlang-repl
1> recon:port_types().
[{"tcp_inet",21480},
 {"efile",2},
 {"udp_inet",2},
 {"0/1",1},
 {"2/2",1},
 {"inet_gethost 4 ",1}]
```

This list contains the types and the count for each type of port. The type name is a string and is defined by the Erlang VM itself.

All the `*_inet` ports are usually sockets, where the prefix is the protocol used (TCP, UDP, SCTP). The `efile` type is for files, while `"0/1"` and `"2/2"` are file descriptors for standard I/O channels (*stdin* and *stdout*) and standard error channels (*stderr*), respectively.

Most other types will be given names of the driver they’re talking to, and will be examples of *port programs*[^14] or *port drivers*[^15].

Again, tracking these can be useful to assess load or usage of a system, detect leaks, and so on.

## Digging In

Whenever some ’in the large’ view (or logging, maybe) has pointed you towards a potential cause for an issue you’re having, it starts being interesting to dig around with a purpose. Is a process in a weird state? Maybe it needs tracing[^16]! Tracing is great whenever you have a specific function call or input or output to watch for, but often, before getting there, a lot more digging is required.

Outside of memory leaks, which often need their own specific techniques and are discussed in Chapter Memory Leaks, the most common tasks are related to processes, and ports (file descriptors and sockets).

### Processes

By all means, processes are an important part of a running Erlang system. And because they’re so central to everything that goes on, there’s a lot to want to know about them. Fortunately, the VM makes a lot of information available, some of which is safe to use, and some of which is unsafe to use in production (because they can return data sets large enough that the amount of memory copied to the shell process and used to print it can kill the node).

All the values can be obtained by calling `process_info(Pid, Key)` or `process_info(Pid, [Keys])`[^17]. Here are the commonly used keys[^18]:

`dictionary`  
returns all the entries in the process dictionary[^19]. Generally safe to use, because people shouldn’t be storing gigabytes of arbitrary data in there.

`group_leader`  
the group leader of a process defines where IO (files, output of `io:format/1-3`) goes.[^20]

`registered_name`  
if the process has a name (as registered with `erlang:register/2`), it is given here.

`status`  
the nature of the process as seen by the scheduler. The possible values are:

<!-- -->

`links`  
will show a list of all the links a process has towards other processes and also ports (sockets, file descriptors). Generally safe to call, but to be used with care on large supervisors that may return thousands and thousands of entries.

`monitored_by`  
gives a list of processes that are monitoring the current process (through the use of `erlang:monitor/2`).

`monitors`  
kind of the opposite of `monitored_by`; it gives a list of all the processes being monitored by the one polled here.

`trap_exit`  
has the value `true` if the process is trapping exits, `false` otherwise.

<!-- -->

`current_function`  
displays the current running function, as a tuple of the form `{Mod, Fun, Arity}`.

`current_location`  
displays the current location within a module, as a tuple of the form `{Mod, Fun, Arity, [{File, FileName}, {line, Num}]}`.

`current_stacktrace`  
more verbose form of the preceding option; displays the current stacktrace as a list of ’current locations’.

`initial_call`  
shows the function that the process was running when spawned, of the form `{Mod, Fun, Arity}`. This may help identify what the process was spawned as, rather than what it’s running right now.

<!-- -->

`binary`  
Displays the all the references to refc binaries[^21] along with their size. Can be unsafe to use if a process has a lot of them allocated.

`garbage_collection`  
contains information regarding garbage collection in the process. The content is documented as ’subject to change’ and should be treated as such. The information tends to contains entries such as the number of garbage collections the process has went through, options for full-sweep garbage collections, and heap sizes.

`heap_size`  
A typical Erlang process contains an ’old’ heap and a ’new’ heap, and goes through generational garbage collection. This entry shows the process’ heap size for the newest generation, and it usually includes the stack size. The value returned is in *words*.

`memory`  
Returns, in *bytes*, the size of the process, including the call stack, the heaps, and internal structures used by the VM that are part of a process.

`message_queue_len`  
Tells you how many messages are waiting in the mailbox of a process.

`messages`  
Returns all of the messages in a process’ mailbox. This attribute is *extremely* dangerous to request in production because mailboxes can hold millions of messages if you’re debugging a process that managed to get locked up. *Always* call for the `message_queue_len` first to make sure it’s safe to use.

`total_heap_size`  
Similar to `heap_size`, but also contains all other fragments of the heap, including the old one. The value returned is in *words*.

<!-- -->

`reductions`  
The Erlang VM does scheduling based on *reductions*, an arbitrary unit of work that allows rather portable implementations of scheduling (time-based scheduling is usually hard to make work efficiently on as many OSes as Erlang runs on). The higher the reductions, the more work, in terms of CPU and function calls, a process is doing.

Fortunately, for all the common ones that are also safe, recon contains the `recon:info/1` function to help:

```erlang-repl
1> recon:info("<0.12.0>").
[{meta,[{registered_name,rex},
        {dictionary,[{'$ancestors',[kernel_sup,<0.10.0>]},
                     {'$initial_call',{rpc,init,1}}]},
        {group_leader,<0.9.0>},
        {status,waiting}]},
 {signals,[{links,[<0.11.0>]},
           {monitors,[]},
           {monitored_by,[]},
           {trap_exit,true}]},
 {location,[{initial_call,{proc_lib,init_p,5}},
            {current_stacktrace,[{gen_server,loop,6,
                                  [{file,"gen_server.erl"},{line,358}]},
                                 {proc_lib,init_p_do_apply,3,
                                  [{file,"proc_lib.erl"},{line,239}]}]}]},
 {memory_used,[{memory,2808},
               {message_queue_len,0},
               {heap_size,233},
               {total_heap_size,233},
               {garbage_collection,[{min_bin_vheap_size,46422},
                                    {min_heap_size,233},
                                    {fullsweep_after,65535},
                                    {minor_gcs,0}]}]},
 {work,[{reductions,35}]}]
```

For the sake of convenience, `recon:info/1` will accept any pid-like first argument and handle it: literal pids, strings (`"<0.12.0>"`), registered atoms, global names (`{global, Atom}`), names registered with a third-party registry (e.g. with `gproc`: `{via, gproc, Name}`), or tuples (`{0,12,0}`). The process just needs to be local to the node you’re debugging.

If only a category of information is wanted, the category can be used directly:

```erlang-repl
2> recon:info(self(), work).
{work,[{reductions,11035}]}
```

or can be used in exactly the same way as `process_info/2`:

```erlang-repl
3> recon:info(self(), [memory, status]).
[{memory,10600},{status,running}]
```

This latter form can be used to fetch unsafe information.

With all this data, it’s possible to find out all we need to debug a system. The challenge then is often to figure out, between this per-process data, and the global one, which process(es) should be targeted.

When looking for high memory usage, for example it’s interesting to be able to list all of a node’s processes and find the top `N` consumers. Using the attributes above and the `recon:proc_count(Attribute, N)` function, we can get these results:

```erlang-repl
4> recon:proc_count(memory, 3).
[{<0.26.0>,831448,
  [{current_function,{group,server_loop,3}},
   {initial_call,{group,server,3}}]},
 {<0.25.0>,372440,
  [user,
   {current_function,{group,server_loop,3}},
   {initial_call,{group,server,3}}]},
 {<0.20.0>,372312,
  [code_server,
   {current_function,{code_server,loop,1}},
   {initial_call,{erlang,apply,2}}]}]
```

Any of the attributes mentioned earlier can work, and for nodes with long-lived processes that can cause problems, it’s a fairly useful function.

There is however a problem when most processes are short-lived, usually too short to inspect through other tools, or when a moving window is what we need (for example, what processes are busy accumulating memory or running code *right now*).

For this use case, Recon has the `recon:proc_window(Attribute, Num, Milliseconds)` function.

It is important to see this function as a snapshot over a sliding window. A program’s timeline during sampling might look like this:

```text
--w---- [Sample1] ---x-------------y----- [Sample2] ---z--->
```

The function will take two samples at an interval defined by `Milliseconds`.

Some processes will live between `w` and die at `x`, some between `y` and `z`, and some between `x` and `y`. These samples will not be too significant as they’re incomplete.

If the majority of your processes run between a time interval `x` to `y` (in absolute terms), you should make sure that your sampling time is smaller than this so that for many processes, their lifetime spans the equivalent of `w` and `z`. Not doing this can skew the results: long-lived processes that have 10 times the time to accumulate data (say reductions) will look like huge consumers when they’re not one.[^22]

The function, once running gives results like follows:

```erlang-repl
5> recon:proc_window(reductions, 3, 500).
[{<0.46.0>,51728,
  [{current_function,{queue,in,2}},
   {initial_call,{erlang,apply,2}}]},
 {<0.49.0>,5728,
  [{current_function,{dict,new,0}},
   {initial_call,{erlang,apply,2}}]},
 {<0.43.0>,650,
  [{current_function,{timer,sleep,1}},
   {initial_call,{erlang,apply,2}}]}]
```

With these two functions, it becomes possible to hone in on a specific process that is causing issues or misbehaving.

### OTP Processes

When processes in question are OTP processes (most of the processes in a production system should definitely be OTP processes), you instantly win more tools to inspect them.

In general the `sys` module[^23] is what you want to look into. Read the documentation on it and you’ll discover why it’s so useful. It contains the following features for any OTP process:

logging of all messages and state transitions, both to the shell or to a file, or even in an internal buffer to be queried;

statistics (reductions, message counts, time, and so on);

fetching the status of a process (metadata including the state);

fetching the state of a process (as in the `#state{}` record);

replacing that state

custom debugging functions to be used as callbacks

It also provides functionality to suspend or resume process execution.

I won’t go into a lot of details about these functions, but be aware that they exist.

### Ports

Similarly to processes, Erlang ports allow a lot of introspection. The info can be accessed by calling `erlang:port_info(Port, Key)`, and more info is available through the `inet` module. Most of it has been regrouped by the `recon:port_info/1-2` functions, which work using a somewhat similar interface to their process-related counterparts.

`id`  
internal index of a port. Of no particular use except to differentiate ports.

`name`  
type of the port — with names such as `"tcp_inet"`, `"udp_inet"`, or `"efile"`, for example.

`os_pid`  
if the port is not an inet socket, but rather represents an external process or program, this value contains the os pid related to the said external program.

<!-- -->

`connected`  
Each port has a controlling process in charge of it, and this process’ pid is the `connected` one.

`links`  
ports can be linked with processes, much like other processes can be. The list of linked processes is contained here. Unless the process has been owned by or manually linked to a lot of processes, this should be safe to use.

`monitors`  
ports that represent external programs can have these programs end up monitoring Erlang processes. These processes are listed here.

<!-- -->

`input`  
the number of bytes read from the port.

`output`  
the number of bytes written to the port.

<!-- -->

`memory`  
this is the memory (in bytes) allocated by the runtime system for the port. This number tends to be small-ish and excludes space allocated by the port itself.

`queue_size`  
Port programs have a specific queue, called the driver queue[^24]. This return the size of this queue, in bytes.

<!-- -->

Inet Ports  
Returns inet-specific data, including statistics[^25], the local address and port number for the socket (`sockname`), and the inet options used[^26]

Others  
currently no other form than inet ports are supported in recon, and an empty list is returned.

The list can be obtained as follows:

```erlang-repl
1> recon:port_info("#Port<0.818>").
[{meta,[{id,6544},{name,"tcp_inet"},{os_pid,undefined}]},
 {signals,[{connected,<0.56.0>},
           {links,[<0.56.0>]},
           {monitors,[]}]},
 {io,[{input,0},{output,0}]},
 {memory_used,[{memory,40},{queue_size,0}]},
 {type,[{statistics,[{recv_oct,0},
                     {recv_cnt,0},
                     {recv_max,0},
                     {recv_avg,0},
                     {recv_dvi,...},
                     {...}|...]},
        {peername,{{50,19,218,110},80}},
        {sockname,{{97,107,140,172},39337}},
        {options,[{active,true},
                  {broadcast,false},
                  {buffer,1460},
                  {delay_send,...},
                  {...}|...]}]}]
```

On top of this, functions to find out specific problematic ports exist the way they do for processes. The gotcha is that so far, recon only supports them for inet ports and with restricted attributes: the number of octets (bytes) sent, received, or both (`send_oct`, `recv_oct`, `oct`, respectively), or the number of packets sent, received, or both (`send_cnt`, `recv_cnt`, `cnt`, respectively).

So for the cumulative total, which can help find out who is slowly but surely eating up all your bandwidth:

```erlang-repl
2> recon:inet_count(oct, 3).
[{#Port<0.6821166>,15828716661,
  [{recv_oct,15828716661},{send_oct,0}]},
 {#Port<0.6757848>,15762095249,
  [{recv_oct,15762095249},{send_oct,0}]},
 {#Port<0.6718690>,15630954707,
  [{recv_oct,15630954707},{send_oct,0}]}]
```

Which suggest some ports are doing only input and eating lots of bytes. You can then use `recon:port_info("#Port<0.6821166>")` to dig in and find who owns that socket, and what is going on with it.

Or in any other case, we can look at what is sending the most data within any time window[^27] with the `recon:inet_window(Attribute, Count, Milliseconds)` function:

```erlang-repl
3> recon:inet_window(send_oct, 3, 5000).
[{#Port<0.11976746>,2986216,[{send_oct,4421857688}]},
 {#Port<0.11704865>,1881957,[{send_oct,1476456967}]},
 {#Port<0.12518151>,1214051,[{send_oct,600070031}]}]
```

For this one, the value in the middle of the tuple is what `send_oct` was worth (or any chosen attribute for each call) during the specific time interval chosen (5 seconds here).

There is still some manual work involved into properly linking a misbehaving port to a process (and then possibly to a specific user or customer), but all the tools are in place.

## Exercises

### Review Questions

1.  What kind of values are reported for Erlang’s memory?

2.  What’s a valuable process-related metric for a global view?

3.  What’s a port, and how should it be monitored globally?

4.  Why can’t you trust `top` or `htop` for CPU usage with Erlang systems? What’s the alternative?

5.  Name two types of signal-related information available for processes

6.  How can you find what code a specific process is running?

7.  What are the different kinds of memory information available for a specific process?

8.  How can you know if a process is doing a lot of work?

9.  Name a few of the values that are dangerous to fetch when inspecting processes in a production system.

10. What are some features provided to OTP processes through the sys module?

11. What kind of values are available when inspecting inet ports?

12. How can you find the type of a port (Files, TCP, UDP)?

### Open-ended Questions

1.  Why do you want a long time window available on global metrics?

2.  Which would be more appropriate between `recon:proc_count/2` and `recon:proc_window/3` to find issues with:

3.  How can you find information about who is the supervisor of a given process?

4.  When should you use `recon:inet_count/2`? `recon:inet_window/3`?

5.  What could explain the difference in memory reported by the operating system and the memory functions in Erlang?

6.  Why is it that Erlang can sometimes look very busy even when it isn’t?

7.  How can you find what proportion of processes on a node are ready to run, but can’t be scheduled right away?

### Hands-On

Using the code at <https://github.com/ferd/recon_demo>:

1.  What’s the system memory?

2.  Is the node using a lot of CPU resources?

3.  Is any process mailbox overflowing?

4.  Which chatty process (`council_member`) takes the most memory?

5.  Which chatty process is eating the most CPU?

6.  Which chatty process is consuming the most bandwidth?

7.  Which chatty process sends the most messages over TCP? The least?

8.  Can you find out if a specific process tends to hold multiple connections or file descriptors open at the same time on a node?

9.  Can you find out which function is being called by the most processes at once on the node right now?

[^1]: Making sure your automated processes don’t run away and go overboard with whatever corrective actions they take is more complex

[^2]: <http://ferd.github.io/recon/>

[^3]: <https://github.com/boundary/folsom>

[^4]: <https://github.com/ferd/vmstats>

[^5]: <https://github.com/lpgauth/statsderl>

[^6]: <https://github.com/etsy/statsd/>

[^7]: <https://github.com/Feuerlabs/exometer>

[^8]: <https://github.com/heroku/ehmon>

[^9]: Common patterns may fit the `ectr` application, at <https://github.com/heroku/ectr>

[^10]: The `recon` application has the function `recon:node_stats_print/2` to do this if you’re in a pinch

[^11]: See Section Binaries

[^12]: See Section Erlang’s Memory Model

[^13]: <http://www.erlang.org/doc/man/erlang.html#statistics_scheduler_wall_time>

[^14]: <http://www.erlang.org/doc/tutorial/c_port.html>

[^15]: <http://www.erlang.org/doc/tutorial/c_portdriver.html>

[^16]: See Chapter Tracing

[^17]: In cases where processes contain sensitive information, data can be forced to be kept private by calling `process_flag(sensitive, true)`

[^18]: For *all* options, look at <http://www.erlang.org/doc/man/erlang.html#process_info-2>

[^19]: See <http://www.erlang.org/course/advanced.html#dict> and <http://ferd.ca/on-the-use-of-the-process-dictionary-in-erlang.html>

[^20]: See <http://learnyousomeerlang.com/building-otp-applications#the-application-behaviour> and <http://erlang.org/doc/apps/stdlib/io_protocol.html> for more details.

[^21]: See Section Binaries

[^22]: Warning: this function depends on data gathered at two snapshots, and then building a dictionary with entries to differentiate them. This can take a heavy toll on memory when you have many tens of thousands of processes, and a little bit of time.

[^23]: <http://www.erlang.org/doc/man/sys.html>

[^24]: The driver queue is available to queue output from the emulator to the driver (data from the driver to the emulator is queued by the emulator in normal Erlang message queues). This can be useful if the driver has to wait for slow devices etc, and wants to yield back to the emulator.

[^25]: <http://www.erlang.org/doc/man/inet.html#getstat-1>

[^26]: <http://www.erlang.org/doc/man/inet.html#setopts-2>

[^27]: See the explanations for the `recon:proc_window/3` in the preceding subsection
