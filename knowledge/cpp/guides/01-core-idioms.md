# Core C++ Idioms

Load for any C++ task to ground design in modern C++, type safety, simplicity, immutability, naming, and guideline enforcement.

Source: `knowledge/cpp/sources/md/cpp-core-guidelines/CppCoreGuidelines.md`.
The imported source is authoritative; this guide preserves selected upstream sections with headings demoted one level.

## Source Sections

- `s-abstract` — Abstract (source lines 185-223)
- `s-introduction` — In: Introduction (source lines 224-460)
- `s-philosophy` — P: Philosophy (source lines 461-1214)
- `s-naming` — NL: Naming and layout suggestions (source lines 21473-22163)

## Rule Index

- `In.0` — Don't panic! (`r0`, source line 251)
- `P.1` — Express ideas directly in code (`rp-direct`, source line 485)
- `P.2` — Write in ISO Standard C++ (`rp-cplusplus`, source line 566)
- `P.3` — Express intent (`rp-what`, source line 598)
- `P.4` — Ideally, a program should be statically type safe (`rp-typesafe`, source line 664)
- `P.5` — Prefer compile-time checking to run-time checking (`rp-compile-time`, source line 694)
- `P.6` — What cannot be checked at compile time should be checkable at run time (`rp-run-time`, source line 738)
- `P.7` — Catch run-time errors early (`rp-early`, source line 846)
- `P.8` — Don't leak any resources (`rp-leak`, source line 963)
- `P.9` — Don't waste time or space (`rp-waste`, source line 1016)
- `P.10` — Prefer immutable data to mutable data (`rp-mutable`, source line 1092)
- `P.11` — Encapsulate messy constructs, rather than spreading through the code (`rp-library`, source line 1103)
- `P.12` — Use supporting tools as appropriate (`rp-tools`, source line 1153)
- `P.13` — Use support libraries as appropriate (`rp-lib`, source line 1182)
- `NL.1` — Don't say in comments what can be clearly stated in code (`rl-comments`, source line 21518)
- `NL.2` — State intent in comments (`rl-comments-intent`, source line 21534)
- `NL.3` — Keep comments crisp (`rl-comments-crisp`, source line 21553)
- `NL.4` — Maintain a consistent indentation style (`rl-indent`, source line 21570)
- `NL.5` — Avoid encoding type information in names (`rl-name-type`, source line 21596)
- `NL.7` — Make the length of a name roughly proportional to the length of its scope (`rl-name-length`, source line 21670)
- `NL.8` — Use a consistent naming style (`rl-name`, source line 21692)
- `NL.9` — Use `ALL_CAPS` for macro names only (`rl-all-caps`, source line 21743)
- `NL.10` — Prefer `underscore_style` names (`rl-camel`, source line 21768)
- `NL.11` — Make literals readable (`rl-literals`, source line 21796)
- `NL.15` — Use spaces sparingly (`rl-space`, source line 21828)
- `NL.16` — Use a conventional class member declaration order (`rl-order`, source line 21863)
- `NL.17` — Use K&R-derived layout (`rl-knr`, source line 21925)
- `NL.18` — Use C++-style declarator layout (`rl-ptr`, source line 21996)
- `NL.19` — Avoid names that are easily misread (`rl-misread`, source line 22019)
- `NL.20` — Don't place two statements on the same line (`rl-stmt`, source line 22038)
- `NL.21` — Declare one name (only) per declaration (`rl-dcl`, source line 22054)
- `NL.25` — Don't use `void` as an argument type (`rl-void`, source line 22066)
- `NL.26` — Use conventional `const` notation (`rl-const`, source line 22088)
- `NL.27` — Use a `.cpp` suffix for code files and `.h` for interface files (`rl-file-suffix`, source line 22117)

---

## <a name="s-abstract"></a>Abstract

This document is a set of guidelines for using C++ well.
The aim of this document is to help people to use modern C++ effectively.
By "modern C++" we mean effective use of the ISO C++ standard (currently C++20, but almost all of our recommendations also apply to C++17, C++14 and C++11).
In other words, what would you like your code to look like in 5 years' time, given that you can start now? In 10 years' time?

The guidelines are focused on relatively high-level issues, such as interfaces, resource management, memory management, and concurrency.
Such rules affect application architecture and library design.
Following the rules will lead to code that is statically type safe, has no resource leaks, and catches many more programming logic errors than is common in code today.
And it will run fast -- you can afford to do things right.

We are less concerned with low-level issues, such as naming conventions and indentation style.
However, no topic that can help a programmer is out of bounds.

Our initial set of rules emphasizes safety (of various forms) and simplicity.
They might very well be too strict.
We expect to have to introduce more exceptions to better accommodate real-world needs.
We also need more rules.

You will find some of the rules contrary to your expectations or even contrary to your experience.
If we haven't suggested you change your coding style in any way, we have failed!
Please try to verify or disprove rules!
In particular, we'd really like to have some of our rules backed up with measurements or better examples.

You will find some of the rules obvious or even trivial.
Please remember that one purpose of a guideline is to help someone who is less experienced or coming from a different background or language to get up to speed.

Many of the rules are designed to be supported by an analysis tool.
Violations of rules will be flagged with references (or links) to the relevant rule.
We do not expect you to memorize all the rules before trying to write code.
One way of thinking about these guidelines is as a specification for tools that happens to be readable by humans.

The rules are meant for gradual introduction into a code base.
We plan to build tools for that and hope others will too.

Comments and suggestions for improvements are most welcome.
We plan to modify and extend this document as our understanding improves and the language and the set of available libraries improve.

## <a name="s-introduction"></a>In: Introduction

This is a set of core guidelines for modern C++ (currently C++20 and C++17) taking likely future enhancements and ISO Technical Specifications (TSs) into account.
The aim is to help C++ programmers to write simpler, more efficient, more maintainable code.

Introduction summary:

* [In.target: Target readership](#ss-readers)
* [In.aims: Aims](#ss-aims)
* [In.not: Non-aims](#ss-non)
* [In.force: Enforcement](#ss-force)
* [In.struct: The structure of this document](#ss-struct)
* [In.sec: Major sections](#ss-sec)

### <a name="ss-readers"></a>In.target: Target readership

All C++ programmers. This includes [programmers who might consider C](#s-cpl).

### <a name="ss-aims"></a>In.aims: Aims

The purpose of this document is to help developers to adopt modern C++ (currently C++20 and C++17) and to achieve a more uniform style across code bases.

We do not suffer the delusion that every one of these rules can be effectively applied to every code base. Upgrading old systems is hard. However, we do believe that a program that uses a rule is less error-prone and more maintainable than one that does not. Often, rules also lead to faster/easier initial development.
As far as we can tell, these rules lead to code that performs as well or better than older, more conventional techniques; they are meant to follow the zero-overhead principle ("what you don't use, you don't pay for" or "when you use an abstraction mechanism appropriately, you get at least as good performance as if you had handcoded using lower-level language constructs").
Consider these rules ideals for new code, opportunities to exploit when working on older code, and try to approximate these ideals as closely as feasible.
Remember:

#### <a name="r0"></a>In.0: Don't panic!

Take the time to understand the implications of a guideline rule on your program.

These guidelines are designed according to the "subset of superset" principle ([Stroustrup05](#Stroustrup05)).
They do not simply define a subset of C++ to be used (for reliability, safety, performance, or whatever).
Instead, they strongly recommend the use of a few simple "extensions" ([library components](#gsl-guidelines-support-library))
that make the use of the most error-prone features of C++ redundant, so that they can be banned (in our set of rules).

The rules emphasize static type safety and resource safety.
For that reason, they emphasize possibilities for range checking, for avoiding dereferencing `nullptr`, for avoiding dangling pointers, and the systematic use of exceptions (via RAII).
Partly to achieve that and partly to minimize obscure code as a source of errors, the rules also emphasize simplicity and the hiding of necessary complexity behind well-specified interfaces.

Many of the rules are prescriptive.
We are uncomfortable with rules that simply state "don't do that!" without offering an alternative.
One consequence of that is that some rules can be supported only by heuristics, rather than precise and mechanically verifiable checks.
Other rules articulate general principles. For these more general rules, more detailed and specific rules provide partial checking.

These guidelines address the core of C++ and its use.
We expect that most large organizations, specific application areas, and even large projects will need further rules, possibly further restrictions, and further library support.
For example, hard-real-time programmers typically can't use free store (dynamic memory) freely and will be restricted in their choice of libraries.
We encourage the development of such more specific rules as addenda to these core guidelines.
Build your ideal small foundation library and use that, rather than lowering your level of programming to glorified assembly code.

The rules are designed to allow [gradual adoption](#s-modernizing).

Some rules aim to increase various forms of safety while others aim to reduce the likelihood of accidents, many do both.
The guidelines aimed at preventing accidents often ban perfectly legal C++.
However, when there are two ways of expressing an idea and one has shown itself a common source of errors and the other has not, we try to guide programmers towards the latter.

### <a name="ss-non"></a>In.not: Non-aims

The rules are not intended to be minimal or orthogonal.
In particular, general rules can be simple, but unenforceable.
Also, it is often hard to understand the implications of a general rule.
More specialized rules are often easier to understand and to enforce, but without general rules, they would just be a long list of special cases.
We provide rules aimed at helping novices as well as rules supporting expert use.
Some rules can be completely enforced, but others are based on heuristics.

These rules are not meant to be read serially, like a book.
You can browse through them using the links.
However, their main intended use is to be targets for tools.
That is, a tool looks for violations and the tool returns links to violated rules.
The rules then provide reasons, examples of potential consequences of the violation, and suggested remedies.

These guidelines are not intended to be a substitute for a tutorial treatment of C++.
If you need a tutorial for some given level of experience, see [the references](#s-references).

This is not a guide on how to convert old C++ code to more modern code.
It is meant to articulate ideas for new code in a concrete fashion.
However, see [the modernization section](#s-modernizing) for some possible approaches to modernizing/rejuvenating/upgrading.
Importantly, the rules support gradual adoption: It is typically infeasible to completely convert a large code base all at once.

These guidelines are not meant to be complete or exact in every language-technical detail.
For the final word on language definition issues, including every exception to general rules and every feature, see the ISO C++ standard.

The rules are not intended to force you to write in an impoverished subset of C++.
They are *emphatically* not meant to define a, say, Java-like subset of C++.
They are not meant to define a single "one true C++" language.
We value expressiveness and uncompromised performance.

The rules are not value-neutral.
They are meant to make code simpler and more correct/safer than most existing C++ code, without loss of performance.
They are meant to inhibit perfectly valid C++ code that correlates with errors, spurious complexity, and poor performance.

The rules are not precise to the point where a person (or machine) can follow them without thinking.
The enforcement parts try to be that, but we would rather leave a rule or a definition a bit vague
and open to interpretation than specify something precisely and wrong.
Sometimes, precision comes only with time and experience.
Design is not (yet) a form of Math.

The rules are not perfect.
A rule can do harm by prohibiting something that is useful in a given situation.
A rule can do harm by failing to prohibit something that enables a serious error in a given situation.
A rule can do a lot of harm by being vague, ambiguous, unenforceable, or by enabling every solution to a problem.
It is impossible to completely meet the "do no harm" criteria.
Instead, our aim is the less ambitious: "Do the most good for most programmers";
if you cannot live with a rule, object to it, ignore it, but don't water it down until it becomes meaningless.
Also, suggest an improvement.

### <a name="ss-force"></a>In.force: Enforcement

Rules with no enforcement are unmanageable for large code bases.
Enforcement of all rules is possible only for a small weak set of rules or for a specific user community.

* But we want lots of rules, and we want rules that everybody can use.
* But different people have different needs.
* But people don't like to read lots of rules.
* But people can't remember many rules.

So, we need subsetting to meet a variety of needs.

* But arbitrary subsetting leads to chaos.

We want guidelines that help a lot of people, make code more uniform, and strongly encourage people to modernize their code.
We want to encourage best practices, rather than leave all to individual choices and management pressures.
The ideal is to use all rules; that gives the greatest benefits.

This adds up to quite a few dilemmas.
We try to resolve those using tools.
Each rule has an **Enforcement** section listing ideas for enforcement.
Enforcement might be done by code review, by static analysis, by compiler, or by run-time checks.
Wherever possible, we prefer "mechanical" checking (humans are slow, inaccurate, and bore easily) and static checking.
Run-time checks are suggested only rarely where no alternative exists; we do not want to introduce "distributed bloat".
Where appropriate, we label a rule (in the **Enforcement** sections) with the name of groups of related rules (called "profiles").
A rule can be part of several profiles, or none.
For a start, we have a few profiles corresponding to common needs (desires, ideals):

* **type**: No type violations (reinterpreting a `T` as a `U` through casts, unions, or varargs)
* **bounds**: No bounds violations (accessing beyond the range of an array)
* **lifetime**: No leaks (failing to `delete` or multiple `delete`) and no access to invalid objects (dereferencing `nullptr`, using a dangling reference).

The profiles are intended to be used by tools, but also serve as an aid to the human reader.
We do not limit our comment in the **Enforcement** sections to things we know how to enforce; some comments are mere wishes that might inspire some tool builder.

Tools that implement these rules shall respect the following syntax to explicitly suppress a rule:

    [[gsl::suppress("tag")]]

and optionally with a message (following usual C++11 standard attribute syntax):

    [[gsl::suppress("tag", justification: "message")]]

where

* `"tag"` is a string literal with the anchor name of the item where the Enforcement rule appears (e.g., for [C.134](#rh-public) it is "rh-public"), the
name of a profile group-of-rules ("type", "bounds", or "lifetime"),
or a specific rule in a profile ([type.4](#pro-type-cstylecast), or [bounds.2](#pro-bounds-arrayindex)). Any text that is not one of those should be rejected.

* `"message"` is a string literal

### <a name="ss-struct"></a>In.struct: The structure of this document

Each rule (guideline, suggestion) can have several parts:

* The rule itself -- e.g., **no naked `new`**
* A rule reference number -- e.g., **C.7** (the 7th rule related to classes).
  Since the major sections are not inherently ordered, we use letters as the first part of a rule reference "number".
  We leave gaps in the numbering to minimize "disruption" when we add or remove rules.
* **Reason**s (rationales) -- because programmers find it hard to follow rules they don't understand
* **Example**s -- because rules are hard to understand in the abstract; can be positive or negative
* **Alternative**s -- for "don't do this" rules
* **Exception**s -- we prefer simple general rules. However, many rules apply widely, but not universally, so exceptions must be listed
* **Enforcement** -- ideas about how the rule might be checked "mechanically"
* **See also**s -- references to related rules and/or further discussion (in this document or elsewhere)
* **Note**s (comments) -- something that needs saying that doesn't fit the other classifications
* **Discussion** -- references to more extensive rationale and/or examples placed outside the main lists of rules

Some rules are hard to check mechanically, but they all meet the minimal criteria that an expert programmer can spot many violations without too much trouble.
We hope that "mechanical" tools will improve with time to approximate what such an expert programmer notices.
Also, we assume that the rules will be refined over time to make them more precise and checkable.

A rule is aimed at being simple, rather than carefully phrased to mention every alternative and special case.
Such information is found in the **Alternative** paragraphs and the [Discussion](#s-discussion) sections.
If you don't understand a rule or disagree with it, please visit its **Discussion**.
If you feel that a discussion is missing or incomplete, enter an [Issue](https://github.com/isocpp/CppCoreGuidelines/issues)
explaining your concerns and possibly a corresponding PR.

Examples are written to illustrate rules.

* Examples are not intended to be production quality or to cover all tutorial dimensions.
For example, many examples are language-technical and use names like `f`, `base`, and `x`.
* We try to ensure that "good" examples follow the Core Guidelines.
* Comments are often illustrating rules where they would be unnecessary and/or distracting in "real code."
* We assume knowledge of the standard library. For example, we use plain `vector` rather than `std::vector`.

This is not a language manual.
It is meant to be helpful, rather than complete, fully accurate on technical details, or a guide to existing code.
Recommended information sources can be found in [the references](#s-references).

### <a name="ss-sec"></a>In.sec: Major sections

* [In: Introduction](#s-introduction)
* [P: Philosophy](#s-philosophy)
* [I: Interfaces](#s-interfaces)
* [F: Functions](#s-functions)
* [C: Classes and class hierarchies](#s-class)
* [Enum: Enumerations](#s-enum)
* [R: Resource management](#s-resource)
* [ES: Expressions and statements](#s-expr)
* [Per: Performance](#s-performance)
* [CP: Concurrency and parallelism](#s-concurrency)
* [E: Error handling](#s-errors)
* [Con: Constants and immutability](#s-const)
* [T: Templates and generic programming](#s-templates)
* [CPL: C-style programming](#s-cpl)
* [SF: Source files](#s-source)
* [SL: The Standard Library](#sl-the-standard-library)

Supporting sections:

* [A: Architectural ideas](#s-a)
* [NR: Non-Rules and myths](#s-not)
* [RF: References](#s-references)
* [Pro: Profiles](#s-profile)
* [GSL: Guidelines support library](#gsl-guidelines-support-library)
* [NL: Naming and layout suggestions](#s-naming)
* [FAQ: Answers to frequently asked questions](#s-faq)
* [Appendix A: Libraries](#s-libraries)
* [Appendix B: Modernizing code](#s-modernizing)
* [Appendix C: Discussion](#s-discussion)
* [Appendix D: Supporting tools](#s-tools)
* [Glossary](#s-glossary)
* [To-do: Unclassified proto-rules](#s-unclassified)

These sections are not orthogonal.

Each section (e.g., "P" for "Philosophy") and each subsection (e.g., "C.hier" for "Class Hierarchies (OOP)") have an abbreviation for ease of searching and reference.
The main section abbreviations are also used in rule numbers (e.g., "C.11" for "Make concrete types regular").

## <a name="s-philosophy"></a>P: Philosophy

The rules in this section are very general.

Philosophy rules summary:

* [P.1: Express ideas directly in code](#rp-direct)
* [P.2: Write in ISO Standard C++](#rp-cplusplus)
* [P.3: Express intent](#rp-what)
* [P.4: Ideally, a program should be statically type safe](#rp-typesafe)
* [P.5: Prefer compile-time checking to run-time checking](#rp-compile-time)
* [P.6: What cannot be checked at compile time should be checkable at run time](#rp-run-time)
* [P.7: Catch run-time errors early](#rp-early)
* [P.8: Don't leak any resources](#rp-leak)
* [P.9: Don't waste time or space](#rp-waste)
* [P.10: Prefer immutable data to mutable data](#rp-mutable)
* [P.11: Encapsulate messy constructs, rather than spreading through the code](#rp-library)
* [P.12: Use supporting tools as appropriate](#rp-tools)
* [P.13: Use support libraries as appropriate](#rp-lib)

Philosophical rules are generally not mechanically checkable.
However, individual rules reflecting these philosophical themes are.
Without a philosophical basis, the more concrete/specific/checkable rules lack rationale.

#### <a name="rp-direct"></a>P.1: Express ideas directly in code

###### Reason

Compilers don't read comments (or design documents) and neither do many programmers (consistently).
What is expressed in code has defined semantics and can (in principle) be checked by compilers and other tools.

###### Example

    class Date {
    public:
        Month month() const;  // do
        int month();          // don't
        // ...
    };

The first declaration of `month` is explicit about returning a `Month` and about not modifying the state of the `Date` object.
The second version leaves the reader guessing and opens more possibilities for uncaught bugs.

###### Example, bad

This loop is a restricted form of `std::find`:

    void f(vector<string>& v)
    {
        string val;
        cin >> val;
        // ...
        int index = -1;                    // bad, plus should use gsl::index
        for (int i = 0; i < v.size(); ++i) {
            if (v[i] == val) {
                index = i;
                break;
            }
        }
        // ...
    }

###### Example, good

A much clearer expression of intent would be:

    void f(vector<string>& v)
    {
        string val;
        cin >> val;
        // ...
        auto p = find(begin(v), end(v), val);  // better
        // ...
    }

A well-designed library expresses intent (what is to be done, rather than just how something is being done) far better than direct use of language features.

A C++ programmer should know the basics of the standard library, and use it where appropriate.
Any programmer should know the basics of the foundation libraries of the project being worked on, and use them appropriately.
Any programmer using these guidelines should know the [guidelines support library](#gsl-guidelines-support-library), and use it appropriately.

###### Example

    change_speed(double s);   // bad: what does s signify?
    // ...
    change_speed(2.3);

A better approach is to be explicit about the meaning of the double (new speed or delta on old speed?) and the unit used:

    change_speed(Speed s);    // better: the meaning of s is specified
    // ...
    change_speed(2.3);        // error: no unit
    change_speed(23_m / 10s);  // meters per second

We could have accepted a plain (unit-less) `double` as a delta, but that would have been error-prone.
If we wanted both absolute speed and deltas, we would have defined a `Delta` type.

###### Enforcement

Very hard in general.

* use `const` consistently (check if member functions modify their object; check if functions modify arguments passed by pointer or reference)
* flag uses of casts (casts neuter the type system)
* detect code that mimics the standard library (hard)

#### <a name="rp-cplusplus"></a>P.2: Write in ISO Standard C++

###### Reason

This is a set of guidelines for writing ISO Standard C++.

###### Note

There are environments where extensions are necessary, e.g., to access system resources.
In such cases, localize the use of necessary extensions and control their use with non-core Coding Guidelines.  If possible, build interfaces that encapsulate the extensions so they can be turned off or compiled away on systems that do not support those extensions.

Extensions often do not have rigorously defined semantics.  Even extensions that
are common and implemented by multiple compilers might have slightly different
behaviors and edge case behavior as a direct result of *not* having a rigorous
standard definition.  With sufficient use of any such extension, expected
portability will be impacted.

###### Note

Using valid ISO C++ does not guarantee portability (let alone correctness).
Avoid dependence on undefined behavior (e.g., [undefined order of evaluation](#res-order))
and be aware of constructs with implementation defined meaning (e.g., `sizeof(int)`).

###### Note

There are environments where restrictions on use of standard C++ language or library features are necessary, e.g., to avoid dynamic memory allocation as required by aircraft control software standards.
In such cases, control their (dis)use with an extension of these Coding Guidelines customized to the specific environment.

###### Enforcement

Use an up-to-date C++ compiler (currently C++20 or C++17) with a set of options that do not accept extensions.

#### <a name="rp-what"></a>P.3: Express intent

###### Reason

Unless the intent of some code is stated (e.g., in names or comments), it is impossible to tell whether the code does what it is supposed to do.

###### Example

    gsl::index i = 0;
    while (i < v.size()) {
        // ... do something with v[i] ...
    }

The intent of "just" looping over the elements of `v` is not expressed here. The implementation detail of an index is exposed (so that it might be misused), and `i` outlives the scope of the loop, which might or might not be intended. The reader cannot know from just this section of code.

Better:

    for (const auto& x : v) { /* do something with the value of x */ }

Now, there is no explicit mention of the iteration mechanism, and the loop operates on a reference to `const` elements so that accidental modification cannot happen. If modification is desired, say so:

    for (auto& x : v) { /* modify x */ }

For more details about for-statements, see [ES.71](#res-for-range).
Sometimes better still, use a named algorithm. This example uses the `for_each` from the Ranges TS because it directly expresses the intent:

    for_each(v, [](int x) { /* do something with the value of x */ });
    for_each(par, v, [](int x) { /* do something with the value of x */ });

The last variant makes it clear that we are not interested in the order in which the elements of `v` are handled.

A programmer should be familiar with

* [The guidelines support library](#gsl-guidelines-support-library)
* [The ISO C++ Standard Library](#sl-the-standard-library)
* Whatever foundation libraries are used for the current project(s)

###### Note

Alternative formulation: Say what should be done, rather than just how it should be done.

###### Note

Some language constructs express intent better than others.

###### Example

If two `int`s are meant to be the coordinates of a 2D point, say so:

    draw_line(int, int, int, int);  // obscure: (x1,y1,x2,y2)? (x,y,h,w)? ...?
                                    // need to look up documentation to know

    draw_line(Point, Point);        // clearer

###### Enforcement

Look for common patterns for which there are better alternatives

* simple `for` loops vs. range-`for` loops
* `f(T*, int)` interfaces vs. `f(span<T>)` interfaces
* loop variables in too large a scope
* naked `new` and `delete`
* functions with many parameters of built-in types

There is a huge scope for cleverness and semi-automated program transformation.

#### <a name="rp-typesafe"></a>P.4: Ideally, a program should be statically type safe

###### Reason

Ideally, a program would be completely statically (compile-time) type safe.
Unfortunately, that is not possible. Problem areas:

* unions
* casts
* array decay
* range errors
* narrowing conversions

###### Note

These areas are sources of serious problems (e.g., crashes and security violations).
We try to provide alternative techniques.

###### Enforcement

We can ban, restrain, or detect the individual problem categories separately, as required and feasible for individual programs.
Always suggest an alternative.
For example:

* unions -- use `variant` (in C++17)
* casts -- minimize their use; templates can help
* array decay -- use `span` (from the GSL)
* range errors -- use `span`
* narrowing conversions -- minimize their use and use `narrow` or `narrow_cast` (from the GSL) where they are necessary

#### <a name="rp-compile-time"></a>P.5: Prefer compile-time checking to run-time checking

###### Reason

Code clarity and performance.
You don't need to write error handlers for errors caught at compile time.

###### Example

    // Int is an alias used for integers
    int bits = 0;         // don't: avoidable code
    for (Int i = 1; i; i <<= 1)
        ++bits;
    if (bits < 32)
        cerr << "Int too small\n";

This example fails to achieve what it is trying to achieve (because overflow is undefined) and should be replaced with a simple `static_assert`:

    // Int is an alias used for integers
    static_assert(sizeof(Int) >= 4);    // do: compile-time check

Or better still just use the type system and replace `Int` with `int32_t`.

###### Example

    void read(int* p, int n);   // read max n integers into *p

    int a[100];
    read(a, 1000);    // bad, off the end

better

    void read(span<int> r); // read into the range of integers r

    int a[100];
    read(a);        // better: let the compiler figure out the number of elements

**Alternative formulation**: Don't postpone to run time what can be done well at compile time.

###### Enforcement

* Look for pointer arguments.
* Look for run-time checks for range violations.

#### <a name="rp-run-time"></a>P.6: What cannot be checked at compile time should be checkable at run time

###### Reason

Leaving hard-to-detect errors in a program is asking for crashes and bad results.

###### Note

Ideally, we catch all errors (that are not errors in the programmer's logic) at either compile time or run time. It is impossible to catch all errors at compile time and often not affordable to catch all remaining errors at run time. However, we should endeavor to write programs that in principle can be checked, given sufficient resources (analysis programs, run-time checks, machine resources, time).

###### Example, bad

    // separately compiled, possibly dynamically loaded
    extern void f(int* p);

    void g(int n)
    {
        // bad: the number of elements is not passed to f()
        f(new int[n]);
    }

Here, a crucial bit of information (the number of elements) has been so thoroughly "obscured" that static analysis is probably rendered infeasible and dynamic checking can be very difficult when `f()` is part of an ABI so that we cannot "instrument" that pointer. We could embed helpful information into the free store, but that requires global changes to a system and maybe to the compiler. What we have here is a design that makes error detection very hard.

###### Example, bad

We can of course pass the number of elements along with the pointer:

    // separately compiled, possibly dynamically loaded
    extern void f2(int* p, int n);

    void g2(int n)
    {
        // bad: the wrong number of elements can be passed to f2()
        f2(new int[n], n);
    }

Passing the number of elements as an argument is better (and far more common) than just passing the pointer and relying on some (unstated) convention for knowing or discovering the number of elements. However (as shown), a simple typo can introduce a serious error. The connection between the two arguments of `f2()` is conventional, rather than explicit.

Also, it is implicit that `f2()` is supposed to `delete` its argument (or did the caller make a second mistake?).

###### Example, bad

The standard library resource management pointers fail to pass the size when they point to an object:

    // separately compiled, possibly dynamically loaded
    // NB: this assumes the calling code is ABI-compatible, using a
    // compatible C++ compiler and the same stdlib implementation
    extern void f3(unique_ptr<int[]>, int n);

    void g3(int n)
    {
        f3(make_unique<int[]>(n), m);    // bad: pass ownership and size separately
    }

###### Example

We need to pass the pointer and the number of elements as an integral object:

    extern void f4(vector<int>&);   // separately compiled, possibly dynamically loaded
    extern void f4(span<int>);      // separately compiled, possibly dynamically loaded
                                    // NB: this assumes the calling code is ABI-compatible, using a
                                    // compatible C++ compiler and the same stdlib implementation

    void g3(int n)
    {
        vector<int> v(n);
        f4(v);                     // pass a reference, retain ownership
        f4(span<int>{v});          // pass a view, retain ownership
    }

This design carries the number of elements along as an integral part of an object, so that errors are unlikely and dynamic (run-time) checking is always feasible, if not always affordable.

###### Example

How do we transfer both ownership and all information needed for validating use?

    vector<int> f5(int n)    // OK: move
    {
        vector<int> v(n);
        // ... initialize v ...
        return v;
    }

    unique_ptr<int[]> f6(int n)    // bad: loses n
    {
        auto p = make_unique<int[]>(n);
        // ... initialize *p ...
        return p;
    }

    owner<int*> f7(int n)    // bad: loses n and we might forget to delete
    {
        owner<int*> p = new int[n];
        // ... initialize *p ...
        return p;
    }

###### Example

* ???
* show how possible checks are avoided by interfaces that pass polymorphic base classes around, when they actually know what they need?
  Or strings as "free-style" options

###### Enforcement

* Flag (pointer, count)-style interfaces (this will flag a lot of examples that can't be fixed for compatibility reasons)
* ???

#### <a name="rp-early"></a>P.7: Catch run-time errors early

###### Reason

Avoid "mysterious" crashes.
Avoid errors leading to (possibly unrecognized) wrong results.

###### Example

    void increment1(int* p, int n)    // bad: error-prone
    {
        for (int i = 0; i < n; ++i) ++p[i];
    }

    void use1(int m)
    {
        const int n = 10;
        int a[n] = {};
        // ...
        increment1(a, m);   // maybe typo, maybe m <= n is supposed
                            // but assume that m == 20
        // ...
    }

Here we made a small error in `use1` that will lead to corrupted data or a crash.
The (pointer, count)-style interface leaves `increment1()` with no realistic way of defending itself against out-of-range errors.
If we could check subscripts for out of range access, then the error would not be discovered until `p[10]` was accessed.
We could check earlier and improve the code:

    void increment2(span<int> p)
    {
        for (int& x : p) ++x;
    }

    void use2(int m)
    {
        const int n = 10;
        int a[n] = {};
        // ...
        increment2({a, m});    // maybe typo, maybe m <= n is supposed
        // ...
    }

Now, `m <= n` can be checked at the point of call (early) rather than later.
If all we had was a typo so that we meant to use `n` as the bound, the code could be further simplified (eliminating the possibility of an error):

    void use3(int m)
    {
        const int n = 10;
        int a[n] = {};
        // ...
        increment2(a);   // the number of elements of a need not be repeated
        // ...
    }

###### Example, bad

Don't repeatedly check the same value. Don't pass structured data as strings:

    Date read_date(istream& is);    // read date from istream

    Date extract_date(const string& s);    // extract date from string

    void user1(const string& date)    // manipulate date
    {
        auto d = extract_date(date);
        // ...
    }

    void user2()
    {
        Date d = read_date(cin);
        // ...
        user1(d.to_string());
        // ...
    }

The date is validated twice (by the `Date` constructor) and passed as a character string (unstructured data).

###### Example

Excess checking can be costly.
There are cases where checking early is inefficient because you might never need the value, or might only need part of the value that is more easily checked than the whole.  Similarly, don't add validity checks that change the asymptotic behavior of your interface (e.g., don't add a `O(n)` check to an interface with an average complexity of `O(1)`).

    class Jet {    // Physics says: e * e < x * x + y * y + z * z
        float x;
        float y;
        float z;
        float e;
    public:
        Jet(float x, float y, float z, float e)
            :x(x), y(y), z(z), e(e)
        {
            // Should I check here that the values are physically meaningful?
        }

        float m() const
        {
            // Should I handle the degenerate case here?
            return sqrt(x * x + y * y + z * z - e * e);
        }

        ???
    };

The physical law for a jet (`e * e < x * x + y * y + z * z`) is not an invariant because of the possibility for measurement errors.

???

###### Enforcement

* Look at pointers and arrays: Do range-checking early and not repeatedly
* Look at conversions: Eliminate or mark narrowing conversions
* Look for unchecked values coming from input
* Look for structured data (objects of classes with invariants) being converted into strings
* ???

#### <a name="rp-leak"></a>P.8: Don't leak any resources

###### Reason

Even a slow growth in resources will, over time, exhaust the availability of those resources.
This is particularly important for long-running programs, but is an essential piece of responsible programming behavior.

###### Example, bad

    void f(const char* name)
    {
        FILE* input = fopen(name, "r");
        // ...
        if (something) return;   // bad: if something == true, a file handle is leaked
        // ...
        fclose(input);
    }

Prefer [RAII](#rr-raii):

    void f(const char* name)
    {
        ifstream input {name};
        // ...
        if (something) return;   // OK: no leak
        // ...
    }

**See also**: [The resource management section](#s-resource)

###### Note

A leak is colloquially "anything that isn't cleaned up."
The more important classification is "anything that can no longer be cleaned up."
For example, allocating an object on the heap and then losing the last pointer that points to that allocation.
This rule should not be taken as requiring that allocations within long-lived objects must be returned during program shutdown.
For example, relying on system guaranteed cleanup such as file closing and memory deallocation upon process shutdown can simplify code.
However, relying on abstractions that implicitly clean up can be as simple, and often safer.

###### Note

Enforcing [the lifetime safety profile](#ss-lifetime) eliminates leaks.
When combined with resource safety provided by [RAII](#rr-raii), it eliminates the need for "garbage collection" (by generating no garbage).
Combine this with enforcement of [the type and bounds profiles](#ss-force) and you get complete type- and resource-safety, guaranteed by tools.

###### Enforcement

* Look at pointers: Classify them into non-owners (the default) and owners.
  Where feasible, replace owners with standard-library resource handles (as in the example above).
  Alternatively, mark an owner as such using `owner` from [the GSL](#gsl-guidelines-support-library).
* Look for naked `new` and `delete`
* Look for known resource allocating functions returning raw pointers (such as `fopen`, `malloc`, and `strdup`)

#### <a name="rp-waste"></a>P.9: Don't waste time or space

###### Reason

This is C++.

###### Note

Time and space that you spend well to achieve a goal (e.g., speed of development, resource safety, or simplification of testing) is not wasted.
"Another benefit of striving for efficiency is that the process forces you to understand the problem in more depth." - Alex Stepanov

###### Example, bad

    struct X {
        char ch;
        int i;
        string s;
        char ch2;

        X& operator=(const X& a);
        X(const X&);
    };

    X waste(const char* p)
    {
        if (!p) throw Nullptr_error{};
        int n = strlen(p);
        auto buf = new char[n];
        if (!buf) throw Allocation_error{};
        for (int i = 0; i < n; ++i) buf[i] = p[i];
        // ... manipulate buffer ...
        X x;
        x.ch = 'a';
        x.s = string(n);    // give x.s space for *p
        for (gsl::index i = 0; i < x.s.size(); ++i) x.s[i] = buf[i];  // copy buf into x.s
        delete[] buf;
        return x;
    }

    void driver()
    {
        X x = waste("Typical argument");
        // ...
    }

Yes, this is a caricature, but we have seen every individual mistake in production code, and worse.
Note that the layout of `X` guarantees that at least 6 bytes (and most likely more) are wasted.
The spurious definition of copy operations disables move semantics so that the return operation is slow
(please note that the Return Value Optimization, RVO, is not guaranteed here).
The use of `new` and `delete` for `buf` is redundant; if we really needed a local string, we should use a local `string`.
There are several more performance bugs and gratuitous complication.

###### Example, bad

    void lower(zstring s)
    {
        for (int i = 0; i < strlen(s); ++i) s[i] = tolower(s[i]);
    }

This is actually an example from production code.
We can see that in our condition we have `i < strlen(s)`. This expression will be evaluated on every iteration of the loop, which means that `strlen` must walk through string every loop to discover its length. While the string contents are changing, it's assumed that `tolower` will not affect the length of the string, so it's better to cache the length outside the loop and not incur that cost each iteration.

###### Note

An individual example of waste is rarely significant, and where it is significant, it is typically easily eliminated by an expert.
However, waste spread liberally across a code base can easily be significant and experts are not always as available as we would like.
The aim of this rule (and the more specific rules that support it) is to eliminate most waste related to the use of C++ before it happens.
After that, we can look at waste related to algorithms and requirements, but that is beyond the scope of these guidelines.

###### Enforcement

Many more specific rules aim at the overall goals of simplicity and elimination of gratuitous waste.

* Flag an unused return value from a user-defined non-defaulted postfix `operator++` or `operator--` function. Prefer using the prefix form instead. (Note: "User-defined non-defaulted" is intended to reduce noise. Review this enforcement if it's still too noisy in practice.)


#### <a name="rp-mutable"></a>P.10: Prefer immutable data to mutable data

###### Reason

It is easier to reason about constants than about variables.
Something immutable cannot change unexpectedly.
Sometimes immutability enables better optimization.
You can't have a data race on a constant.

See [Con: Constants and immutability](#s-const)

#### <a name="rp-library"></a>P.11: Encapsulate messy constructs, rather than spreading through the code

###### Reason

Messy code is more likely to hide bugs and harder to write.
A good interface is easier and safer to use.
Messy, low-level code breeds more such code.

###### Example

    int sz = 100;
    int* p = (int*) malloc(sizeof(int) * sz);
    int count = 0;
    // ...
    for (;;) {
        // ... read an int into x, exit loop if end of file is reached ...
        // ... check that x is valid ...
        if (count == sz)
            p = (int*) realloc(p, sizeof(int) * sz * 2);
        p[count++] = x;
        // ...
    }

This is low-level, verbose, and error-prone.
For example, we "forgot" to test for memory exhaustion and assign new value to `sz`.
Instead, we could use `vector`:

    vector<int> v;
    v.reserve(100);
    // ...
    for (int x; cin >> x; ) {
        // ... check that x is valid ...
        v.push_back(x);
    }

###### Note

The standards library and the GSL are examples of this philosophy.
For example, instead of messing with the arrays, unions, cast, tricky lifetime issues, `gsl::owner`, etc.,
that are needed to implement key abstractions, such as `vector`, `span`, `lock_guard`, and `future`, we use the libraries
designed and implemented by people with more time and expertise than we usually have.
Similarly, we can and should design and implement more specialized libraries, rather than leaving the users (often ourselves)
with the challenge of repeatedly getting low-level code well.
This is a variant of the [subset of superset principle](#r0) that underlies these guidelines.

###### Enforcement

* Look for "messy code" such as complex pointer manipulation and casting outside the implementation of abstractions.


#### <a name="rp-tools"></a>P.12: Use supporting tools as appropriate

###### Reason

There are many things that are done better "by machine".
Computers don't tire or get bored by repetitive tasks.
We typically have better things to do than repeatedly do routine tasks.

###### Example

Run a static analyzer to verify that your code follows the guidelines you want it to follow.

###### Note

See

* [Static analysis tools](https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis)
* [Concurrency tools](#rconc-tools)
* [Testing tools](https://github.com/isocpp/CppCoreGuidelines/tree/master)

There are many other kinds of tools, such as source code repositories, build tools, etc.,
but those are beyond the scope of these guidelines.

###### Note

Be careful not to become dependent on over-elaborate or over-specialized tool chains.
Those can make your otherwise portable code non-portable.


#### <a name="rp-lib"></a>P.13: Use support libraries as appropriate

###### Reason

Using a well-designed, well-documented, and well-supported library saves time and effort;
its quality and documentation are likely to be greater than what you could do
if the majority of your time must be spent on an implementation.
The cost (time, effort, money, etc.) of a library can be shared over many users.
A widely used library is more likely to be kept up-to-date and ported to new systems than an individual application.
Knowledge of a widely-used library can save time on other/future projects.
So, if a suitable library exists for your application domain, use it.

###### Example

    std::sort(begin(v), end(v), std::greater<>());

Unless you are an expert in sorting algorithms and have plenty of time,
this is more likely to be correct and to run faster than anything you write for a specific application.
You need a reason not to use the standard library (or whatever foundational libraries your application uses) rather than a reason to use it.

###### Note

By default use

* The [ISO C++ Standard Library](#sl-the-standard-library)
* The [Guidelines Support Library](#gsl-guidelines-support-library)

###### Note

If no well-designed, well-documented, and well-supported library exists for an important domain,
maybe you should design and implement it, and then use it.

## <a name="s-naming"></a>NL: Naming and layout suggestions

Consistent naming and layout are helpful.
If for no other reason because it minimizes "my style is better than your style" arguments.
However, there are many, many, different styles around and people are passionate about them (pro and con).
Also, most real-world projects include code from many sources, so standardizing on a single style for all code is often impossible.
After many requests for guidance from users, we present a set of rules that you might use if you have no better ideas, but the real aim is consistency, rather than any particular rule set.
IDEs and tools can help (as well as hinder).

Naming and layout rules:

* [NL.1: Don't say in comments what can be clearly stated in code](#rl-comments)
* [NL.2: State intent in comments](#rl-comments-intent)
* [NL.3: Keep comments crisp](#rl-comments-crisp)
* [NL.4: Maintain a consistent indentation style](#rl-indent)
* [NL.5: Avoid encoding type information in names](#rl-name-type)
* [NL.7: Make the length of a name roughly proportional to the length of its scope](#rl-name-length)
* [NL.8: Use a consistent naming style](#rl-name)
* [NL.9: Use `ALL_CAPS` for macro names only](#rl-all-caps)
* [NL.10: Prefer `underscore_style` names](#rl-camel)
* [NL.11: Make literals readable](#rl-literals)
* [NL.15: Use spaces sparingly](#rl-space)
* [NL.16: Use a conventional class member declaration order](#rl-order)
* [NL.17: Use K&R-derived layout](#rl-knr)
* [NL.18: Use C++-style declarator layout](#rl-ptr)
* [NL.19: Avoid names that are easily misread](#rl-misread)
* [NL.20: Don't place two statements on the same line](#rl-stmt)
* [NL.21: Declare one name (only) per declaration](#rl-dcl)
* [NL.25: Don't use `void` as an argument type](#rl-void)
* [NL.26: Use conventional `const` notation](#rl-const)
* [NL.27: Use a `.cpp` suffix for code files and `.h` for interface files](#rl-file-suffix)

Most of these rules are aesthetic and programmers hold strong opinions.
IDEs also tend to have defaults and a range of alternatives.
These rules are suggested defaults to follow unless you have reasons not to.

We have had comments to the effect that naming and layout are so personal and/or arbitrary that we should not try to "legislate" them.
We are not "legislating" (see the previous paragraph).
However, we have had many requests for a set of naming and layout conventions to use when there are no external constraints.

More specific and detailed rules are easier to enforce.

These rules bear a strong resemblance to the recommendations in the [PPP Style Guide](https://www.stroustrup.com/Programming/PPP-style.pdf)
written in support of Stroustrup's [Programming: Principles and Practice using C++](https://www.stroustrup.com/programming.html).

#### <a name="rl-comments"></a>NL.1: Don't say in comments what can be clearly stated in code

###### Reason

Compilers do not read comments.
Comments are less precise than code.
Comments are not updated as consistently as code.

###### Example, bad

    auto x = m * v1 + vv;   // multiply m with v1 and add the result to vv

###### Enforcement

Build an AI program that interprets colloquial English text and see if what is said could be better expressed in C++.

#### <a name="rl-comments-intent"></a>NL.2: State intent in comments

###### Reason

Code says what is done, not what is supposed to be done. Often intent can be stated more clearly and concisely than the implementation.

###### Example

    void stable_sort(Sortable& c)
        // sort c in the order determined by <, keep equal elements (as defined by ==) in
        // their original relative order
    {
        // ... quite a few lines of non-trivial code ...
    }

###### Note

If the comment and the code disagree, both are likely to be wrong.

#### <a name="rl-comments-crisp"></a>NL.3: Keep comments crisp

###### Reason

Verbosity slows down understanding and makes the code harder to read by spreading it around in the source file.

###### Note

Use intelligible English.
I might be fluent in Danish, but most programmers are not; the maintainers of my code might not be.
Avoid SMS lingo and watch your grammar, punctuation, and capitalization.
Aim for professionalism, not "cool."

###### Enforcement

not possible.

#### <a name="rl-indent"></a>NL.4: Maintain a consistent indentation style

###### Reason

Readability. Avoidance of "silly mistakes."

###### Example, bad

    int i;
    for (i = 0; i < max; ++i); // bug waiting to happen
    if (i == j)
        return i;

###### Note

Always indenting the statement after `if (...)`, `for (...)`, and `while (...)` is usually a good idea:

    if (i < 0) error("negative argument");

    if (i < 0)
        error("negative argument");

###### Enforcement

Use a tool.

#### <a name="rl-name-type"></a>NL.5: Avoid encoding type information in names

###### Rationale

If names reflect types rather than functionality, it becomes hard to change the types used to provide that functionality.
Also, if the type of a variable is changed, code using it will have to be modified.
Minimize unintentional conversions.

###### Example, bad

    void print_int(int i);
    void print_string(const char*);

    print_int(1);          // repetitive, manual type matching
    print_string("xyzzy"); // repetitive, manual type matching

###### Example, good

    void print(int i);
    void print(string_view);    // also works on any string-like sequence

    print(1);              // clear, automatic type matching
    print("xyzzy");        // clear, automatic type matching

###### Note

Names with types encoded are either verbose or cryptic.

    printS  // print a std::string
    prints  // print a C-style string
    printi  // print an int

Requiring techniques like Hungarian notation to encode a type has been used in untyped languages, but is generally unnecessary and actively harmful in a strongly statically-typed language like C++, because the annotations get out of date (the warts are just like comments and rot just like them) and they interfere with good use of the language (use the same name and overload resolution instead).

###### Note

Some styles use very general (not type-specific) prefixes to denote the general use of a variable.

    auto p = new User();
    auto p = make_unique<User>();
    // note: "p" is not being used to say "raw pointer to type User,"
    //       just generally to say "this is an indirection"

    auto cntHits = calc_total_of_hits(/*...*/);
    // note: "cnt" is not being used to encode a type,
    //       just generally to say "this is a count of something"

This is not harmful and does not fall under this guideline because it does not encode type information.

###### Note

Some styles distinguish members from local variable, and/or from global variable.

    struct S {
        int m_;
        S(int m) : m_{abs(m)} { }
    };

This is not harmful and does not fall under this guideline because it does not encode type information.

###### Note

Like C++, some styles distinguish types from non-types.
For example, by capitalizing type names, but not the names of functions and variables.

    typename<typename T>
    class HashTable {   // maps string to T
        // ...
    };

    HashTable<int> index;

This is not harmful and does not fall under this guideline because it does not encode type information.

#### <a name="rl-name-length"></a>NL.7: Make the length of a name roughly proportional to the length of its scope

**Rationale**: The larger the scope the greater the chance of confusion and of an unintended name clash.

###### Example

    double sqrt(double x);   // return the square root of x; x must be non-negative

    int length(const char* p);  // return the number of characters in a zero-terminated C-style string

    int length_of_string(const char zero_terminated_array_of_char[])    // bad: verbose

    int g;      // bad: global variable with a cryptic name

    int open;   // bad: global variable with a short, popular name

The use of `p` for pointer and `x` for a floating-point variable is conventional and non-confusing in a restricted scope.

###### Enforcement

???

#### <a name="rl-name"></a>NL.8: Use a consistent naming style

**Rationale**: Consistency in naming and naming style increases readability.

###### Note

There are many styles and when you use multiple libraries, you can't follow all their different conventions.
Choose a "house style", but leave "imported" libraries with their original style.

###### Example

ISO Standard, use lower case only and digits, separate words with underscores:

* `int`
* `vector`
* `my_map`

Avoid identifier names that contain double underscores `__` or that start with an underscore followed by a capital letter (e.g., `_Throws`).
Such identifiers are reserved for the C++ implementation.

###### Example

[Stroustrup](https://www.stroustrup.com/Programming/PPP-style.pdf):
ISO Standard, but with upper case used for your own types and concepts:

* `int`
* `vector`
* `My_map`

###### Example

CamelCase: capitalize each word in a multi-word identifier:

* `int`
* `vector`
* `MyMap`
* `myMap`

Some conventions capitalize the first letter, some don't.

###### Note

Try to be consistent in your use of acronyms and lengths of identifiers:

    int mtbf {12};
    int mean_time_between_failures {12}; // make up your mind

###### Enforcement

Would be possible except for the use of libraries with varying conventions.

#### <a name="rl-all-caps"></a>NL.9: Use `ALL_CAPS` for macro names only

###### Reason

To avoid confusing macros with names that obey scope and type rules.

###### Example

    void f()
    {
        const int SIZE{1000};  // Bad, use 'size' instead
        int v[SIZE];
    }

###### Note

In particular, this avoids confusing macros with non-macro symbolic constants (see also [Enum.5: Don't use `ALL_CAPS` for enumerators](#renum-caps))

    enum bad { BAD, WORSE, HORRIBLE }; // BAD

###### Enforcement

* Flag macros with lower-case letters
* Flag `ALL_CAPS` non-macro names

#### <a name="rl-camel"></a>NL.10: Prefer `underscore_style` names

###### Reason

The use of underscores to separate parts of a name is the original C and C++ style and used in the C++ Standard Library.

###### Note

This rule is a default to use only if you have a choice.
Often, you don't have a choice and must follow an established style for [consistency](#rl-name).
The need for consistency beats personal taste.

This is a recommendation for [when you have no constraints or better ideas](#s-naming).
This rule was added after many requests for guidance.

###### Example

[Stroustrup](https://www.stroustrup.com/Programming/PPP-style.pdf):
ISO Standard, but with upper case used for your own types and concepts:

* `int`
* `vector`
* `My_map`

###### Enforcement

Impossible.

#### <a name="rl-literals"></a>NL.11: Make literals readable

###### Reason

Readability.

###### Example

Use digit separators to avoid long strings of digits

    auto c = 299'792'458; // m/s2
    auto q2 = 0b0000'1111'0000'0000;
    auto ss_number = 123'456'7890;

###### Example

Use literal suffixes where clarification is needed

    auto hello = "Hello!"s; // a std::string
    auto world = "world";   // a C-style string
    auto interval = 100ms;  // using <chrono>

###### Note

Literals should not be sprinkled all over the code as ["magic constants"](#res-magic),
but it is still a good idea to make them readable where they are defined.
It is easy to make a typo in a long string of integers.

###### Enforcement

Flag long digit sequences. The trouble is to define "long"; maybe 7.

#### <a name="rl-space"></a>NL.15: Use spaces sparingly

###### Reason

Too much space makes the text larger and distracts.

###### Example, bad

    #include < map >

    int main(int argc, char * argv [ ])
    {
        // ...
    }

###### Example

    #include <map>

    int main(int argc, char* argv[])
    {
        // ...
    }

###### Note

Some IDEs have their own opinions and add distracting space.

This is a recommendation for [when you have no constraints or better ideas](#s-naming).
This rule was added after many requests for guidance.

###### Note

We value well-placed whitespace as a significant help for readability. Just don't overdo it.

#### <a name="rl-order"></a>NL.16: Use a conventional class member declaration order

###### Reason

A conventional order of members improves readability.

When declaring a class use the following order

* types: classes, enums, and aliases (`using`)
* constructors, assignments, destructor
* functions
* data

Use the `public` before `protected` before `private` order.

This is a recommendation for [when you have no constraints or better ideas](#s-naming).
This rule was added after many requests for guidance.

###### Example

    class X {
    public:
        // interface
    protected:
        // unchecked function for use by derived class implementations
    private:
        // implementation details
    };

###### Example

Sometimes, the default order of members conflicts with a desire to separate the public interface from implementation details.
In such cases, private types and functions can be placed with private data.

    class X {
    public:
        // interface
    protected:
        // unchecked function for use by derived class implementations
    private:
        // implementation details (types, functions, and data)
    };

###### Example, bad

Avoid multiple blocks of declarations of one access (e.g., `public`) dispersed among blocks of declarations with different access (e.g. `private`).

    class X {   // bad
    public:
        void f();
    public:
        int g();
        // ...
    };

The use of macros to declare groups of members often leads to violation of any ordering rules.
However, using macros obscures what is being expressed anyway.

###### Enforcement

Flag departures from the suggested order. There will be a lot of old code that doesn't follow this rule.

#### <a name="rl-knr"></a>NL.17: Use K&R-derived layout

###### Reason

This is the original C and C++ layout. It preserves vertical space well. It distinguishes different language constructs (such as functions and classes) well.

###### Note

In the context of C++, this style is often called "Stroustrup".

This is a recommendation for [when you have no constraints or better ideas](#s-naming).
This rule was added after many requests for guidance.

###### Example

    struct Cable {
        int x;
        // ...
    };

    double foo(int x)
    {
        if (0 < x) {
            // ...
        }

        switch (x) {
        case 0:
            // ...
            break;
        case amazing:
            // ...
            break;
        default:
            // ...
            break;
        }

        if (0 < x)
            ++x;

        if (x < 0)
            something();
        else
            something_else();

        return some_value;
    }

Note the space between `if` and `(`

###### Note

Use separate lines for each statement, the branches of an `if`, and the body of a `for`.

###### Note

The `{` for a `class` and a `struct` is *not* on a separate line, but the `{` for a function is.

###### Note

Capitalize the names of your user-defined types to distinguish them from standards-library types.

###### Note

Do not capitalize function names.

###### Enforcement

If you want enforcement, use an IDE to reformat.

#### <a name="rl-ptr"></a>NL.18: Use C++-style declarator layout

###### Reason

The C-style layout emphasizes use in expressions and grammar, whereas the C++-style emphasizes types.
The use in expressions argument doesn't hold for references.

###### Example

    T& operator[](size_t);   // OK
    T &operator[](size_t);   // just strange
    T & operator[](size_t);   // undecided

###### Note

This is a recommendation for [when you have no constraints or better ideas](#s-naming).
This rule was added after many requests for guidance.

###### Enforcement

Impossible in the face of history.


#### <a name="rl-misread"></a>NL.19: Avoid names that are easily misread

###### Reason

Readability.
Not everyone has screens and printers that make it easy to distinguish all characters.
We easily confuse similarly spelled and slightly misspelled words.

###### Example

    int oO01lL = 6; // bad

    int splunk = 7;
    int splonk = 8; // bad: splunk and splonk are easily confused

###### Enforcement

???

#### <a name="rl-stmt"></a>NL.20: Don't place two statements on the same line

###### Reason

Readability.
It is really easy to overlook a statement when there is more on a line.

###### Example

    int x = 7; char* p = 29;    // don't
    int x = 7; f(x);  ++x;      // don't

###### Enforcement

Easy.

#### <a name="rl-dcl"></a>NL.21: Declare one name (only) per declaration

###### Reason

Readability.
Minimizing confusion with the declarator syntax.

###### Note

For details, see [ES.10](#res-name-one).


#### <a name="rl-void"></a>NL.25: Don't use `void` as an argument type

###### Reason

It's verbose and only needed where C compatibility matters.

###### Example

    void f(void);   // bad

    void g();       // better

###### Note

Even Dennis Ritchie deemed `void f(void)` an abomination.
You can make an argument for that abomination in C when function prototypes were rare so that banning:

    int f();
    f(1, 2, "weird but valid C89");   // hope that f() is defined int f(a, b, c) char* c; { /* ... */ }

would have caused major problems, but not in the 21st century and in C++.

#### <a name="rl-const"></a>NL.26: Use conventional `const` notation

###### Reason

Conventional notation is more familiar to more programmers.
Consistency in large code bases.

###### Example

    const int x = 7;    // OK
    int const y = 9;    // bad

    const int *const p = nullptr;   // OK, constant pointer to constant int
    int const *const p = nullptr;   // bad, constant pointer to constant int

###### Note

We are well aware that you could claim the "bad" examples are more logical than the ones marked "OK",
but they also confuse more people, especially novices relying on teaching material using the far more common, conventional OK style.

As ever, remember that the aim of these naming and layout rules is consistency and that aesthetics vary immensely.

This is a recommendation for [when you have no constraints or better ideas](#s-naming).
This rule was added after many requests for guidance.

###### Enforcement

Flag `const` used as a suffix for a type.

#### <a name="rl-file-suffix"></a>NL.27: Use a `.cpp` suffix for code files and `.h` for interface files

###### Reason

It's a longstanding convention.
But consistency is more important, so if your project uses something else, follow that.

###### Note

This convention reflects a common use pattern:
Headers are more often shared with C to compile as both C++ and C, which typically uses `.h`,
and it's easier to name all headers `.h` instead of having different extensions for just those headers that are intended to be shared with C.
On the other hand, implementation files are rarely shared with C and so should typically be distinguished from `.c` files,
so it's normally best to name all C++ implementation files something else (such as `.cpp`).

The specific names `.h` and `.cpp` are not required (just recommended as a default) and other names are in widespread use.
Examples are `.hh`, `.C`, and `.cxx`. Use such names equivalently.
In this document, we refer to `.h` and `.cpp` as a shorthand for header and implementation files,
even though the actual extension might be different.

Your IDE (if you use one) might have strong opinions about suffixes.

###### Example

    // foo.h:
    extern int a;   // a declaration
    extern void foo();

    // foo.cpp:
    int a;   // a definition
    void foo() { ++a; }

`foo.h` provides the interface to `foo.cpp`. Global variables are best avoided.

###### Example, bad

    // foo.h:
    int a;   // a definition
    void foo() { ++a; }

`#include <foo.h>` twice in a program and you get a linker error for two one-definition-rule violations.

###### Enforcement

* Flag non-conventional file names.
* Check that `.h` and `.cpp` (and equivalents) follow the rules below.
