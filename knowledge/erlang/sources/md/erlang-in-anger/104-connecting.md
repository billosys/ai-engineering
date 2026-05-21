# Connecting to Remote Nodes

Interacting with a running server program is traditionally done in one of two ways. One is to do it through an interactive shell kept available by using a `screen` or `tmux` session that runs in the background and letting someone connect to it. The other is to program management functions or comprehensive configuration files that can be dynamically reloaded.

The interactive session approach is usually okay for software that runs in a strict Read-Eval-Print-Loop (REPL). The programmed management and configuration approach requires careful planning in whatever tasks you think you’ll need to do, and hopefully getting it right. Pretty much all systems can try that approach, so I’ll skip it given I’m somewhat more interested in the cases where stuff is already bad and no function exists for it.

Erlang uses something closer to an "interactor" than a REPL. Basically, a regular Erlang virtual machine does not need a REPL, and will happily run byte code and stick with that, no shell needed. However, because of how it works with concurrency and multiprocessing, and good support for distribution, it is possible to have in-software REPLs that run as arbitrary Erlang processes.

This means that, unlike a single screen session with a single shell, it’s possible to have as many Erlang shells connected and interacting with one virtual machine as you want at a time[^1].

Most common usages will depend on a cookie being present on the two nodes you want to connect together[^2], but there are ways to do it that do not include it. Most usages will also require the use of named nodes, and all of them will require *a priori* measures to make sure you can contact the node.

## Job Control Mode

The Job Control Mode (JCL mode) is the menu you get when you press `^G` in the Erlang shell. From that menu, there is an option allowing you to connect to a remote shell:

```erlang-repl
(somenode@ferdmbp.local)1>
User switch command
 --> h
  c [nn]            - connect to job
  i [nn]            - interrupt job
  k [nn]            - kill job
  j                 - list all jobs
  s [shell]         - start local shell
  r [node [shell]]  - start remote shell
  q                 - quit erlang
  ? | h             - this message
 --> r 'server@ferdmbp.local'
 --> c
Eshell Vx.x.x  (abort with ^G)
(server@ferdmbp.local)1>
```

When that happens, the local shell runs all the line editing and job management locally, but the evaluation is actually done remotely. All output coming from said remote evaluation will be forwarded to the local shell.

To quit the shell, go back in the JCL mode with `^G`. This job management is, as I said, done locally, and it is thus safe to quit with `^G q`:

```erlang-repl
(server@ferdmbp.local)1>
User switch command
 --> q
```

You may choose to start the initial shell in hidden mode (with the argument `-hidden`) to avoid connecting to an entire cluster automatically.

## Remsh

There’s a mechanism entirely similar to the one available through the JCL mode, although invoked in a different manner. The entire JCL mode sequence can by bypassed by starting the shell as follows for long names:

```text
erl -name local@domain.name -remsh remote@domain.name
```

And as follows for short names:

```text
erl -sname local@domain -remsh remote@domain
```

All other Erlang arguments (such as `-hidden` and `-setcookie $COOKIE`) are also valid. The underlying mechanisms are the same as when using JCL mode, but the initial shell is started remotely instead of locally (JCL is still local). `^G` remains the safest way to exit the remote shell.

## SSH Daemon

Erlang/OTP comes shipped with an SSH implementation that can both act as a server and a client. Part of it is a demo application providing a remote shell working in Erlang.

To get this to work, you usually need to have your keys to have access to SSH stuff remotely in place already, but for quick test purposes, you can get things working by doing:

```erlang-repl
$ mkdir /tmp/ssh
$ ssh-keygen -t rsa -f /tmp/ssh/ssh_host_rsa_key
$ ssh-keygen -t rsa1 -f /tmp/ssh/ssh_host_key
$ ssh-keygen -t dsa -f /tmp/ssh/ssh_host_dsa_key
$ erl
1> application:ensure_all_started(ssh).
{ok,[crypto,asn1,public_key,ssh]}
2> ssh:daemon(8989, [{system_dir, "/tmp/ssh"},
2>                   {user_dir, "/home/ferd/.ssh"}]).
{ok,<0.52.0>}
```

I’ve only set a few options here, namely `system_dir`, which is where the host files are, and `user_dir`, which contains SSH configuration files. There are plenty of other options available to allow for specific passwords, customize handling of public keys, and so on[^3].

To connect to the daemon, any SSH client will do:

```erlang-repl
$ ssh -p 8989 ferd@127.0.0.1
Eshell Vx.x.x  (abort with ^G)
1>
```

And with this you can interact with an Erlang installation without having it installed on the current machine. Just disconnecting from the SSH session (closing the terminal) will be enough to leave. *Do not run* functions such as `q()` or `init:stop()`, which will terminate the remote host.[^4]

If you have trouble connecting, you can add the `-oLogLevel=DEBUG` option to `ssh` to get debug output.

## Named Pipes

A little known way to connect with an Erlang node that requires no explicit distribution is through named pipes. This can be done by starting Erlang with `run_erl`, which wraps Erlang in a named pipe[^5]:

```erlang-repl
$ run_erl /tmp/erl_pipe /tmp/log_dir "erl"
```

The first argument is the name of the file that will act as the named pipe. The second one is where logs will be saved[^6].

To connect to the node, you use the `to_erl` program:

```erlang-repl
$ to_erl /tmp/erl_pipe
Attaching to /tmp/erl_pipe (^D to exit)

1>
```

And the shell is connected. Closing stdio (with `^D`) will disconnect from the shell while leaving it running.

## Exercises

### Review Questions

1.  What are the 4 ways to connect to a remote node?

2.  Can you connect to a node that wasn’t given a name?

3.  What’s the command to go into the Job Control Mode (JCL)?

4.  Which method(s) of connecting to a remote shell should you avoid for a system that outputs a lot of data to standard output?

5.  What instances of remote connections shouldn’t be disconnected using `^G`?

6.  What command(s) should never be used to disconnect from a session?

7.  Can all of the methods mentioned support having multiple users connected onto the same Erlang node without issue?

[^1]: More details on the mechanisms at <http://ferd.ca/repl-a-bit-more-and-less-than-that.html>

[^2]: More details at <http://learnyousomeerlang.com/distribunomicon#cookies> or <http://www.erlang.org/doc/reference_manual/distributed.html#id83619>

[^3]: Complete instructions with all options to get this set up are available at <http://www.erlang.org/doc/man/ssh.html#daemon-3>.

[^4]: This is true for all methods of interacting with a remote Erlang node.

[^5]: `"erl"` is the command being run. Additional arguments can be added after it. For example `"erl +K true"` will turn kernel polling on.

[^6]: Using this method ends up calling fsync for each piece of output, which may give quite a performance hit if a lot of IO is taking place over standard output
