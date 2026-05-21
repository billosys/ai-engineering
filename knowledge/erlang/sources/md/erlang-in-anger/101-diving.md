# How to Dive into a Code Base

"Read the source" is one of the most annoying things to be told, but dealing with Erlang programmers, you’ll have to do it often. Either the documentation for a library will be incomplete, outdated, or just not there. In other cases, Erlang programmers are a bit similar to Lispers in that they will tend to write libraries that will solve their problems and not really test or try them in other circumstances, leaving it to you to extend or fix issues that arise in new contexts.

It’s thus pretty much guaranteed you’ll have to go dive in some code base you know nothing about, either because you inherited it at work, or because you need to fix it or understand it to be able to move forward with your own system. This is in fact true of most languages whenever the project you work on is not one you designed yourself.

There are three main types of Erlang code bases you’ll encounter in the wild: raw Erlang code bases, OTP applications, and OTP releases. In this chapter, we’ll look at each of these and try to provide helpful tips on navigating them.

## Raw Erlang

If you encounter a raw Erlang code base, you’re pretty much on your own. These rarely follow any specific standard, and you have to dive in the old way to figure out whatever happens in there.

This means hoping for a `README.md` file or something similar that can point to an entry point in the application, and going from there, or hoping for some contact information that can be used to ask questions to the author(s) of the library.

Fortunately, you should rarely encounter raw Erlang in the wild, and they are often beginner projects, or awesome projects that were once built by Erlang beginners and now need a serious rewrite. In general, the advent of tools such as `rebar3` and its earlier incarnations[^1] made it so most people use OTP Applications.

## OTP Applications

Figuring out OTP applications is usually rather simple. They usually all share a directory structure that looks like:

```text
doc/
ebin/
src/
test/
LICENSE.txt
README.md
rebar.config
```

There might be slight differences, but the general structure will be the same.

Each OTP application should contain an *app file*, either `ebin/<AppName>.app` or more often, `src/<AppName>.app.src`[^2]. There are two main varieties of app files:

```erlang
{application, useragent, [
  {description, "Identify browsers & OSes from useragent strings"},
  {vsn, "0.1.2"},
  {registered, []},
  {applications, [kernel, stdlib]},
  {modules, [useragent]}
]}.
```

And:

```erlang
{application, dispcount, [
  {description, "A dispatching library for resources and task "
                "limiting based on shared counters"},
  {vsn, "1.0.0"},
  {applications, [kernel, stdlib]},
  {registered, []},
  {mod, {dispcount, []}},
  {modules, [dispcount, dispcount_serv, dispcount_sup,
             dispcount_supersup, dispcount_watcher, watchers_sup]}
]}.
```

This first case is called a *library application*, while the second case is a regular *application*.

### Library Applications

Library applications will usually have modules named `appname_something`, and one module named `appname`. This will usually be the interface module that’s central to the library and contains a quick way into most of the functionality provided.

By looking at the source of the module, you can figure out how it works with little effort: If the module adheres to any given behaviour (`gen_server`, `gen_fsm`, etc.), you’re most likely expected to start a process under one of your own supervisors and call it that way. If no behaviour is included, then you probably have a functional, stateless library on your hands. For this case, the module’s exported functions should give you a quick way to understand its purpose.

### Regular Applications

For a regular OTP application, there are two potential modules that act as the entry point:

`appname`

`appname_app`

The first file should be similar in use to what we had in a library application (an entry point), while the second one will implement the `application` behaviour, and will represent the top of the application’s process hierarchy. In some cases the first file will play both roles at once.

If you plan on simply adding the application as a dependency to your own app, then look inside `appname` for details and information. If you need to maintain and/or fix the application, go for `appname_app` instead.

The application will start a top-level supervisor and return its *pid*. This top-level supervisor will then contain the specifications of all the child processes it will start on its own[^3].

The higher a process resides in the tree, the more likely it is to be vital to the survival of the application. You can also estimate how important a process is by the order it is started (all children in the supervision tree are started in order, depth-first). If a process is started later in the supervision tree, it probably depends on processes that were started earlier.

Moreover, worker processes that depend on each other within the same application (say, a process that buffers socket communications and relays them to a finite-state machine in charge of understanding the protocol) are likely to be regrouped under the same supervisor and to fail together when something goes wrong. This is a deliberate choice, as it is usually simpler to start from a blank slate, restarting both processes, rather than trying to figure out how to recuperate when one or the other loses or corrupts its state.

The supervisor restart strategy reflects the relationship between processes under a supervisor:

`one_for_one` and `simple_one_for_one` are used for processes that are not dependent upon each other directly, although their failures will collectively be counted towards total application shutdown[^4].

`rest_for_one` will be used to represent processes that depend on each other in a linear manner.

`one_for_all` is used for processes that entirely depend on each other.

This structure means it is easiest to navigate OTP applications in a top-down manner by exploring supervision subtrees.

For each worker process supervised, the behaviour it implements will give a good clue about its purpose:

a `gen_server` holds resources and tends to follow client/server patterns (or more generally, request/response patterns)

a `gen_fsm` will deal with a sequence of events or inputs and react depending on them, as a Finite State Machine. It will often be used to implement protocols.

a `gen_event` will act as an event hub for callbacks, or as a way to deal with notifications of some sort.

All of these modules will contain the same kind of structure: exported functions that represent the user-facing interface, exported functions for the callback module, and private functions, usually in that order.

Based on their supervision relationship and the typical role of each behaviour, looking at the interface to be used by other modules and the behaviours implemented should reveal a lot of information about the program you’re diving into.

### Dependencies

All applications have dependencies[^5], and these dependencies will have their own dependencies. OTP applications usually share no state between them, so it’s possible to know what bits of code depend on what other bits of code by looking at the app file only, assuming the developer wrote them in a mostly correct manner. Figure Dependencies shows a diagram that can be generated from looking at app files to help understand the structure of OTP applications.

![Dependency graph of riak\_cs, Basho’s open source cloud library.
The graph ignores dependencies on common applications like kernel and stdlib. Ovals are applications, rectangles are library applications.](assets/app-deps-riak-cs.png)

Using such a hierarchy and looking at each application’s short description might be helpful to draw a rough, general map of where everything is located. To generate a similar diagram, find `recon`’s script directory and call `escript script/app_deps.erl`[^6]. Similar hierarchies can be found using the `observer`[^7] application, but for individual supervision trees. Put together, you may get an easy way to find out what does what in the code base.

## OTP Releases

OTP releases are not a lot harder to understand than most OTP applications you’ll encounter in the wild. A release is a set of OTP applications packaged in a production-ready manner so it boots and shuts down without needing to manually call `application:start/2` for any app. Compiled releases may contain their own copy of the Erlang virtual machine with more or less libraries than the default distribution, and can be ready to run standalone. Of course there’s a bit more to releases than that, but generally, the same discovery process used for individual OTP applications will be applicable here.

You’ll usually have a file named `relx.config` or a `relx` tuple in a `rebar.config` file, which will state which top-level applications are part of the release and some options regarding their packaging. Relx-based releases can be understood by reading the project’s wiki[^8], or their documentation on the documentation sites of `rebar3`[^9] or `erlang.mk`[^10].

Other systems may depend on the configuration files used by `systools` or `reltool`, which will state all applications part of the release and a few[^11] options regarding their packaging. To understand them, I recommend [reading existing documentation on them](http://learnyousomeerlang.com/release-is-the-word).

## Exercises

### Review Questions

1.  How do you know if a code base is an application? A release?

2.  What differentiates an application from a library application?

3.  What can be said of processes under a `one_for_all` scheme for supervision?

4.  Why would someone use a `gen_fsm` behaviour over a `gen_server`?

### Hands-On

Download the code at <https://github.com/ferd/recon_demo>. This will be used as a test bed for exercises throughout the book. Given you are not familiar with the code base yet, let’s see if you can use the tips and tricks mentioned in this chapter to get an understanding of it.

1.  Is this application meant to be used as a library? A standalone system?

2.  What does it do?

3.  Does it have any dependencies? What are they?

4.  The app’s `README` mentions being non-deterministic. Can you prove if this is true? How?

5.  Can you express the dependency chain of applications in there? Generate a diagram of them?

6.  Can you add more processes to the main application than those described in the `README`?

[^1]: <https://www.rebar3.org> — a build tool briefly introduced in Chapter Building Open Source Erlang Software

[^2]: A build system generates the final file that goes in `ebin`. Note that in these cases, many `src/<AppName>.app.src` files do not specify modules and let the build system take care of it.

[^3]: In some cases, the supervisor specifies no children: they will either be started dynamically by some function of the API or in a start phase of the application, or the supervisor is only there to allow OTP environment variables (in the `env` tuple of the app file) to be loaded.

[^4]: Some developers will use `one_for_one` supervisors when `rest_for_one` is more appropriate. They require strict ordering to boot correctly, but forget about said order when restarting or if a predecessor dies.

[^5]: At the very least on the `kernel` and `stdlib` applications

[^6]: This script depends on graphviz

[^7]: <http://www.erlang.org/doc/apps/observer/observer_ug.html>

[^8]: <https://github.com/erlware/relx/wiki>

[^9]: <https://www.rebar3.org/docs/releases>

[^10]: <http://erlang.mk/guide/relx.html>

[^11]: A lot
