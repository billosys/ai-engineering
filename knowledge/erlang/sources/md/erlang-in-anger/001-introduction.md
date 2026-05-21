# Introduction

## On Running Software

There’s something rather unique in Erlang in how it approaches failure compared to most other programming languages. There’s this common way of thinking where the language, programming environment, and methodology do everything possible to prevent errors. Something going wrong at run-time is something that needs to be prevented, and if it cannot be prevented, then it’s out of scope for whatever solution people have been thinking about.

The program is written once, and after that, it’s off to production, whatever may happen there. If there are errors, new versions will need to be shipped.

Erlang, on the other hand, takes the approach that failures will happen no matter what, whether they’re developer-, operator-, or hardware-related. It is rarely practical or even possible to get rid of all errors in a program or a system.[^1] If you can deal with some errors rather than preventing them at all cost, then most undefined behaviours of a program can go in that "deal with it" approach.

This is where the "Let it Crash"[^2] idea comes from: Because you can now deal with failure, and because the cost of weeding out all of the complex bugs from a system before it hits production is often prohibitive, programmers should only deal with the errors they know how to handle, and leave the rest for another process (a supervisor) or the virtual machine to deal with.

Given that most bugs are transient[^3], simply restarting processes back to a state known to be stable when encountering an error can be a surprisingly good strategy.

Erlang is a programming environment where the approach taken is equivalent to the human body’s immune system, whereas most other languages only care about hygiene to make sure no germ enters the body. Both forms appear extremely important to me. Almost every environment offers varying degrees of hygiene. Nearly no other environment offers the immune system where errors at run time can be dealt with and seen as survivable.

Because the system doesn’t collapse the first time something bad touches it, Erlang/OTP also allows you to be a doctor. You can go in the system, pry it open right there in production, carefully observe everything inside as it runs, and even try to fix it interactively. To continue with the analogy, Erlang allows you to perform extensive tests to diagnose the problem and various degrees of surgery (even very invasive surgery), without the patients needing to sit down or interrupt their daily activities.

This book intends to be a little guide about how to be the Erlang medic in a time of war. It is first and foremost a collection of tips and tricks to help understand where failures come from, and a dictionary of different code snippets and practices that helped developers debug production systems that were built in Erlang.

## Who is this for?

This book is not for beginners. There is a gap left between most tutorials, books, training sessions, and actually being able to operate, diagnose, and debug running systems once they’ve made it to production. There’s a fumbling phase implicit to a programmer’s learning of a new language and environment where they just have to figure how to get out of the guidelines and step into the real world, with the community that goes with it.

This book assumes that the reader is proficient in basic Erlang and the OTP framework. Erlang/OTP features are explained as I see fit — usually when I consider them tricky — and it is expected that a reader who feels confused by usual Erlang/OTP material will have an idea of where to look for explanations if necessary[^4].

What is not necessarily assumed is that the reader knows how to debug Erlang software, dive into an existing code base, diagnose issues, or has an idea of the best practices about deploying Erlang in a production environment[^5].

## How To Read This Book

This book is divided in two parts.

Part Writing Applications focuses on how to write applications. It includes how to dive into a code base (Chapter How to Dive into a Code Base), general tips on writing open source Erlang software (Chapter Building Open Source Erlang Software), and how to plan for overload in your system design (Chapter Planning for Overload).

Part Diagnosing Applictions focuses on being an Erlang medic and concerns existing, living systems. It contains instructions on how to connect to a running node (Chapter Connecting to Remote Nodes), and the basic runtime metrics available (Chapter Runtime Metrics). It also explains how to perform a system autopsy using a crash dump (Chapter Reading Crash Dumps), how to identify and fix memory leaks (Chapter Memory Leaks), and how to find runaway CPU usage (Chapter CPU and Scheduler Hogs). The final chapter contains instructions on how to trace Erlang function calls in production using `recon`[^6] to understand issues before they bring the system down (Chapter Tracing).

Each chapter is followed up by a few optional exercises in the form of questions or hands-on things to try if you feel like making sure you understood everything, or if you want to push things further.

[^1]: life-critical systems are usually excluded from this category

[^2]: Erlang people now seem to favour "let it fail", given it makes people far less nervous.

[^3]: 131 out of 132 bugs are transient bugs (they’re non-deterministic and go away when you look at them, and trying again may solve the problem entirely), according to Jim Gray in [Why Do Computers Stop and What Can Be Done About It?](http://www.hpl.hp.com/techreports/tandem/TR-85.7.html)

[^4]: I do recommend visiting [Learn You Some Erlang](http://learnyousomeerlang.com) or the regular [Erlang Documentation](http://www.erlang.org/erldoc) if a free resource is required

[^5]: Running Erlang in a screen or tmux session is *not* a deployment strategy.

[^6]: <http://ferd.github.io/recon/> — a library used to make the text lighter, and with generally production-safe functions.
