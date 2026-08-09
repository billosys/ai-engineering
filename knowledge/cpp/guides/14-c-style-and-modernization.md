# C-Style Code and Modernization

Load for C interoperability, C-style idioms to contain or replace, legacy modernization, and gradual adoption strategy.

Source: `knowledge/cpp/sources/md/cpp-core-guidelines/CppCoreGuidelines.md`.
The imported source is authoritative; this guide preserves selected upstream sections with headings demoted one level.

## Source Sections

- `s-cpl` — CPL: C-style programming (source lines 19178-19269)
- `s-modernizing` — Appendix B: Modernizing code (source lines 22268-22312)

## Rule Index

- `CPL.1` — Prefer C++ to C (`rcpl-c`, source line 19190)
- `CPL.2` — If you must use C, use the common subset of C and C++, and compile the C code as C++ (`rcpl-subset`, source line 19211)
- `CPL.3` — If you must use C for interfaces, use C++ in the calling code using such interfaces (`rcpl-interface`, source line 19230)

---

## <a name="s-cpl"></a>CPL: C-style programming

C and C++ are closely related languages.
They both originate in "Classic C" from 1978 and have evolved in ISO committees since then.
Many attempts have been made to keep them compatible, but neither is a subset of the other.

C rule summary:

* [CPL.1: Prefer C++ to C](#rcpl-c)
* [CPL.2: If you must use C, use the common subset of C and C++, and compile the C code as C++](#rcpl-subset)
* [CPL.3: If you must use C for interfaces, use C++ in the calling code using such interfaces](#rcpl-interface)

#### <a name="rcpl-c"></a>CPL.1: Prefer C++ to C

###### Reason

C++ provides better type checking and more notational support.
It provides better support for high-level programming and often generates faster code.

###### Example

    char ch = 7;
    void* pv = &ch;
    int* pi = pv;   // not C++
    *pi = 999;      // overwrite sizeof(int) bytes near &ch

The rules for implicit casting to and from `void*` in C are subtle and unenforced.
In particular, this example violates a rule against converting to a type with stricter alignment.

###### Enforcement

Use a C++ compiler.

#### <a name="rcpl-subset"></a>CPL.2: If you must use C, use the common subset of C and C++, and compile the C code as C++

###### Reason

That subset can be compiled with both C and C++ compilers, and when compiled as C++ is better type checked than "pure C."

###### Example

    int* p1 = malloc(10 * sizeof(int));                      // not C++
    int* p2 = static_cast<int*>(malloc(10 * sizeof(int)));   // not C, C-style C++
    int* p3 = new int[10];                                   // not C
    int* p4 = (int*) malloc(10 * sizeof(int));               // both C and C++

###### Enforcement

* Flag if using a build mode that compiles code as C.

  * The C++ compiler will enforce that the code is valid C++ unless you use C extension options.

#### <a name="rcpl-interface"></a>CPL.3: If you must use C for interfaces, use C++ in the calling code using such interfaces

###### Reason

C++ is more expressive than C and offers better support for many types of programming.

###### Example

For example, to use a 3rd party C library or C systems interface, define the low-level interface in the common subset of C and C++ for better type checking.
Whenever possible encapsulate the low-level interface in an interface that follows the C++ guidelines (for better abstraction, memory safety, and resource safety) and use that C++ interface in C++ code.

###### Example

You can call C from C++:

    // in C:
    double sqrt(double);

    // in C++:
    extern "C" double sqrt(double);

    sqrt(2);

###### Example

You can call C++ from C:

    // in C:
    X call_f(struct Y*, int);

    // in C++:
    extern "C" X call_f(Y* p, int i)
    {
        return p->f(i);   // possibly a virtual function call
    }

###### Enforcement

None needed

## <a name="s-modernizing"></a>Appendix B: Modernizing code

Ideally, we follow all rules in all code.
Realistically, we have to deal with a lot of old code:

* application code written before the guidelines were formulated or known
* libraries written to older/different standards
* code written under "unusual" constraints
* code that we just haven't gotten around to modernizing

If we have a million lines of new code, the idea of "just changing it all at once" is typically unrealistic.
Thus, we need a way of gradually modernizing a code base.

Upgrading older code to modern style can be a daunting task.
Often, the old code is both a mess (hard to understand) and working correctly (for the current range of uses).
Typically, the original programmer is not around and the test cases incomplete.
The fact that the code is a mess dramatically increases the effort needed to make any change and the risk of introducing errors.
Often, messy old code runs unnecessarily slowly because it requires outdated compilers and cannot take advantage of modern hardware.
In many cases, automated "modernizer"-style tool support would be required for major upgrade efforts.

The purpose of modernizing code is to simplify adding new functionality, to ease maintenance, and to increase performance (throughput or latency), and to better utilize modern hardware.
Making code "look pretty" or "follow modern style" are not by themselves reasons for change.
There are risks implied by every change and costs (including the cost of lost opportunities) implied by having an outdated code base.
The cost reductions must outweigh the risks.

But how?

There is no one approach to modernizing code.
How best to do it depends on the code, the pressure for updates, the backgrounds of the developers, and the available tool.
Here are some (very general) ideas:

* The ideal is "just upgrade everything." That gives the most benefits for the shortest total time.
  In most circumstances, it is also impossible.
* We could convert a code base module for module, but any rules that affects interfaces (especially ABIs), such as [use `span`](#ss-views), cannot be done on a per-module basis.
* We could convert code "bottom up" starting with the rules we estimate will give the greatest benefits and/or the least trouble in a given code base.
* We could start by focusing on the interfaces, e.g., make sure that no resources are lost and no pointer is misused.
  This would be a set of changes across the whole code base, but would most likely have huge benefits.
  Afterwards, code hidden behind those interfaces can be gradually modernized without affecting other code.

Whichever way you choose, please note that the most advantages come with the highest conformance to the guidelines.
The guidelines are not a random set of unrelated rules where you can randomly pick and choose with an expectation of success.

We would dearly love to hear about experience and about tools used.
Modernization can be much faster, simpler, and safer when supported with analysis tools and even code transformation tools.
