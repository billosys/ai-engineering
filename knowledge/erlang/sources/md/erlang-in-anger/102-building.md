# Building Open Source Erlang Software

Most Erlang books tend to explain how to build Erlang/OTP applications, but few of them go very much in depth about how to integrate with the Erlang community doing Open Source work. Some of them even avoid the topic on purpose. This chapter dedicates itself to doing a quick tour of the state of affairs in Erlang.

OTP applications are the vast majority of the open source code people will encounter. In fact, many people who would need to build an OTP release would do so as one umbrella OTP application.

If what you’re writing is a stand-alone piece of code that could be used by someone building a product, it’s likely an OTP application. If what you’re building is a product that stands on its own and should be deployed by users as-is (or with a little configuration), what you should be building is an OTP release.[^1]

The main build tools supported are `rebar3` and `erlang.mk`. The former is a build tool and package manager trying to make it easy to develop and release Erlang libraries and systems in a repeatable manner, while the latter is a very fancy makefile that offers a bit less for production and releases but allows more flexibility. In this chapter, I’ll mostly focus on using `rebar3` to build things, given it’s the de-facto standard, is a tool I know well, and that `erlang.mk` applications tend to also be supported by `rebar3` as dependencies (the opposite is also true).

## Project Structure

The structures of OTP applications and of OTP releases are different. An OTP application can be expected to have one top-level supervisor (if any) and possibly a bunch of dependencies that sit below it. An OTP release will usually be composed of multiple OTP applications, which may or may not depend on each other. This will lead to two major ways to lay out applications.

### OTP Applications

For OTP applications, the proper structure is pretty much the same as what was explained in OTP Applications:

```text
_build/
doc/
src/
test/
LICENSE.txt
README.md
rebar.config
rebar.lock
```

What’s new in this one is the `_build/` directory and the `rebar.lock` file, which will be generated automatically by `rebar3`[^2].

This is the directory where `rebar3` places all build artifacts for a project, including local copies of libraries and packages required for it to work. No mainstream Erlang tool installs packages globally[^3], preferring to instead keep everything project-local to avoid inter-project conflicts.

Such dependencies can be specified for `rebar3` by adding a few config lines to `rebar.config`:

```text
{deps, [
  %% Hex.pm Packages
  myapp,
  {myapp,"1.0.0"},
  %% source dependencies 
  {myapp, {git, "git://github.com/user/myapp.git", {ref, "aef728"}}},
  {myapp, {git, "https://github.com/user/myapp.git", {branch, "master"}}},
  {myapp, {hg, "https://othersite.com/user/myapp", {tag, "3.0.0"}}}
 ]}.
```

Dependencies are fetched directly from a `git` (or `hg`) source or as a package from [`hex.pm`](https://hex.pm) in a level-order traversal. They can then be compiled, and specific compile options can be added with the `{erl_opts, List}.` option in the config file[^4].

You can call `rebar3 compile`, which will download all dependencies, and then build them and your app at once.

When making your application’s source code public to the world, distribute it *without* the `_build/` directory. It’s quite possible that other developers’ applications depend on the same applications yours do, and it’s no use shipping them all multiple times. The build system in place (in this case, `rebar3`) should be able to figure out duplicated entries and fetch everything necessary only once.

### OTP Releases

For releases, the structure can a bit different. Releases are collections of applications, and their structures may reflect that.

Instead of having a top-level app alone in `src`, applications can be nested one level deeper in a `apps` or `lib` directory:

```text
_build/
apps/
  - myapp1/
     - src/
  - myapp2/
     - src/
doc/
LICENSE.txt
README.md
rebar.config
rebar.lock
```

This structure lends itself to generating releases where multiple OTP applications under your control under a single code repository. Both `rebar3` and `erlang.mk` rely on the `relx` library to assemble releases. Other tools such as Systool and Reltool have been covered before[^5], and can allow the user plenty of power if they do not like what they would get otherwise.

A `relx` configuration tuple (within `rebar.config`) for the directory structure above would look like:

```text
{relx, [
  {release, {demo, "1.0.0"},
    [myapp1, myapp2, ..., recon]},
     
  {include_erts, false} % will use local Erlang install
]}
```

Calling `rebar3 release` will build a release, to be found in the `_build/default/rel/` directory. Calling `rebar3 tar` will generate a tarball at  
`_build/default/rel/demo/demo-1.0.0.tar.gz`, ready to be deployed.

## Supervisors and start\_link Semantics

In complex production systems, most faults and errors are transient, and retrying an operation is a good way to do things — Jim Gray’s paper[^6] quotes *Mean Times Between Failures* (MTBF) of systems handling transient bugs being better by a factor of 4 when doing this. Still, supervisors aren’t just about restarting.

One very important part of Erlang supervisors and their supervision trees is that *their start phases are synchronous*. Each OTP process has the potential to prevent its siblings and cousins from booting. If the process dies, it’s retried again, and again, until it works, or fails too often.

That’s where people make a very common mistake. There isn’t a backoff or cooldown period before a supervisor restarts a crashed child. When a network-based application tries to set up a connection during its initialization phase and the remote service is down, the application fails to boot after too many fruitless restarts. Then the system may shut down.

Many Erlang developers end up arguing in favor of a supervisor that has a cooldown period. I strongly oppose the sentiment for one simple reason: *it’s all about the guarantees*.

### It’s About the Guarantees

Restarting a process is about bringing it back to a stable, known state. From there, things can be retried. When the initialization isn’t stable, supervision is worth very little. An initialized process should be stable no matter what happens. That way, when its siblings and cousins get started later on, they can be booted fully knowing that the rest of the system that came up before them is healthy.

If you don’t provide that stable state, or if you were to start the entire system asynchronously, you would get very little benefit from this structure that a `try ... catch` in a loop wouldn’t provide.

Supervised processes *provide guarantees* in their initialization phase, *not a best effort*. This means that when you’re writing a client for a database or service, you shouldn’t need a connection to be established as part of the initialization phase unless you’re ready to say it will always be available no matter what happens.

You could force a connection during initialization if you know the database is on the same host and should be booted before your Erlang system, for example. Then a restart should work. In case of something incomprehensible and unexpected that breaks these guarantees, the node will end up crashing, which is desirable: a pre-condition to starting your system hasn’t been met. It’s a system-wide assertion that failed.

If, on the other hand, your database is on a remote host, you should expect the connection to fail. It’s just a reality of distributed systems that things go down.[^7] In this case, the only guarantee you can make in the client process is that your client will be able to handle requests, but not that it will communicate to the database. It could return `{error, not_connected}` on all calls during a net split, for example.

The reconnection to the database can then be done using whatever cooldown or backoff strategy you believe is optimal, without impacting the stability of the system. It can be attempted in the initialization phase as an optimization, but the process should be able to reconnect later on if anything ever disconnects.

If you expect failure to happen on an external service, do not make its presence a guarantee of your system. We’re dealing with the real world here, and failure of external dependencies is always an option.

### Side Effects

Of course, the libraries and processes that call such a client will then error out if they don’t expect to work without a database. That’s an entirely different issue in a different problem space, one that depends on your business rules and what you can or can’t do to a client, but one that is possible to work around. For example, consider a client for a service that stores operational metrics — the code that calls that client could very well ignore the errors without adverse effects to the system as a whole.

The difference in both initialization and supervision approaches is that the client’s callers make the decision about how much failure they can tolerate, not the client itself. That’s a very important distinction when it comes to designing fault-tolerant systems. Yes, supervisors are about restarts, but they should be about restarts to a stable known state.

### Example: Initializing without guaranteeing connections

The following code attempts to guarantee a connection as part of the process’ state:

```text
init(Args) ->
    Opts = parse_args(Args),
    {ok, Port} = connect(Opts),
    {ok, #state{sock=Port, opts=Opts}}.

[...]

handle_info(reconnect, S = #state{sock=undefined, opts=Opts}) ->
    %% try reconnecting in a loop
    case connect(Opts) of
        {ok, New} -> {noreply, S#state{sock=New}};
         _ -> self() ! reconnect, {noreply, S}
    end;
```

Instead, consider rewriting it as:

```text
init(Args) ->
    Opts = parse_args(Args),
    %% you could try connecting here anyway, for a best
    %% effort thing, but be ready to not have a connection.
    self() ! reconnect,
    {ok, #state{sock=undefined, opts=Opts}}.

[...]

handle_info(reconnect, S = #state{sock=undefined, opts=Opts}) ->
    %% try reconnecting in a loop
    case connect(Opts) of
        {ok, New} -> {noreply, S#state{sock=New}};
        _ -> self() ! reconnect, {noreply, S}
    end;
```

You now allow initializations with fewer guarantees: they went from *the connection is available* to *the connection manager is available*.

### In a nutshell

Production systems I have worked with have been a mix of both approaches.

Things like configuration files, access to the file system (say for logging purposes), local resources that can be depended on (opening UDP ports for logs), restoring a stable state from disk or network, and so on, are things I’ll put into requirements of a supervisor and may decide to synchronously load no matter how long it takes (some applications may just end up having over 10 minute boot times in rare cases, but that’s okay because we’re possibly syncing gigabytes that we *need* to work with as a base state if we don’t want to serve incorrect information.)

On the other hand, code that depends on non-local databases and external services will adopt partial startups with quicker supervision tree booting because if the failure is expected to happen often during regular operations,
then there’s no difference between now and later. You have to handle it the same, and for these parts of the system, far less strict guarantees are often the better solution.

### Application Strategies

No matter what, a sequence of failures is not a death sentence for the node. Once a system has been divided into various OTP applications, it becomes possible to choose which applications are vital or not to the node. Each OTP application can be started in 3 ways: temporary, transient, permanent, either by doing it manually in `application:start(Name, Type)`, or in the config file for your release:

`permanent`: if the app terminates, the entire system is taken down, excluding manual termination of the app with `application:stop/1`.

`transient`: if the app terminates for reason `normal`, that’s ok. Any other reason for termination shuts down the entire system.

`temporary`: the application is allowed to stop for any reason. It will be reported, but nothing bad will happen.

It is also possible to start an application as an *included application*, which starts it under your own OTP supervisor with its own strategy to restart it.

## Exercises

### Review Questions

1.  Are Erlang supervision trees started depth-first? breadth-first? Synchronously or asynchronously?

2.  What are the three application strategies? What do they do?

3.  What are the main differences between the directory structure of an app and a release?

4.  When should you use a release?

5.  Give two examples of the type of state that can go in a process’ init function, and two examples of the type of state that shouldn’t go in a process’ init function

### Hands-On

Using the code at <https://github.com/ferd/recon_demo>:

1.  Extract the main application hosted in the release to make it independent, and includable in other projects.

2.  Host the application somewhere (Github, Bitbucket, local server), and build a release with that application as a dependency.

3.  The main application’s workers (`council_member`) starts a server and connects to it in its `init/1` function. Can you make this connection happen outside of the init function’s? Is there a benefit to doing so in this specific case?

[^1]: The details of how to build an OTP application or release is left up to the Erlang introduction book you have at hand.

[^2]: Some people package `rebar3` directly in their application. This was initially done to help people who had never used rebar3 or its predecessors use libraries and projects in a boostrapped manner. Feel free to install rebar3 globally on your system, or keep a local copy if you require a specific version to build your system.

[^3]: Except as a local cache of unbuilt packages.

[^4]: More details on <https://www.rebar3.org/docs/configuration>

[^5]: <http://learnyousomeerlang.com/release-is-the-word>

[^6]: <http://mononcqc.tumblr.com/post/35165909365/why-do-computers-stop>

[^7]: Or latency shoots up enough that it is impossible to tell the difference from failure.
