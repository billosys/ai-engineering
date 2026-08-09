# Project Structure and Tooling

Load for source files, headers, namespaces, build/tool support, profiles, enforcement, suppression, and codebase organization.

Source: `knowledge/cpp/sources/md/cpp-core-guidelines/CppCoreGuidelines.md`.
The imported source is authoritative; this guide preserves selected upstream sections with headings demoted one level.

## Source Sections

- `s-source` — SF: Source files (source lines 19270-19820)
- `s-profile` — Pro: Profiles (source lines 21171-21324)
- `s-tools` — Appendix D: Supporting tools (source lines 22886-22898)

## Rule Index

- `SF.1` — Use a `.cpp` suffix for code files and `.h` for interface files if your project doesn't already follow another convention (`rs-file-suffix`, source line 19295)
- `SF.2` — A header file must not contain object definitions or non-inline function definitions (`rs-inline`, source line 19299)
- `SF.3` — Use header files for all declarations used in multiple source files (`rs-declaration-header`, source line 19340)
- `SF.4` — Include header files before other declarations in a file (`rs-include-order`, source line 19362)
- `SF.5` — A `.cpp` file must include the header file(s) that defines its interface (`rs-consistency`, source line 19408)
- `SF.6` — Use `using namespace` directives for transition, for foundation libraries (such as `std`), or within a local scope (only) (`rs-using`, source line 19449)
- `SF.7` — Don't write `using namespace` at global scope in a header file (`rs-using-directive`, source line 19500)
- `SF.8` — Use `#include` guards for all header files (`rs-guards`, source line 19532)
- `SF.9` — Avoid cyclic dependencies among source files (`rs-cycles`, source line 19561)
- `SF.10` — Avoid dependencies on implicitly `#include`d names (`rs-implicit`, source line 19589)
- `SF.11` — Header files should be self-contained (`rs-contained`, source line 19659)
- `SF.12` — Prefer the quoted form of `#include` for files relative to the including file and the angle bracket form everywhere else (`rs-incform`, source line 19684)
- `SF.13` — Use portable header identifiers in `#include` statements (`rs-portable-header-id`, source line 19713)
- `SF.20` — Use `namespace`s to express logical structure (`rs-namespace`, source line 19741)
- `SF.21` — Don't use an unnamed (anonymous) namespace in a header (`rs-unnamed`, source line 19755)
- `SF.22` — Use an unnamed (anonymous) namespace for all internal/non-exported entities (`rs-unnamed2`, source line 19788)

---

## <a name="s-source"></a>SF: Source files

Distinguish between declarations (used as interfaces) and definitions (used as implementations).
Use header files to represent interfaces and to emphasize logical structure.

Source file rule summary:

* [SF.1: Use a `.cpp` suffix for code files and `.h` for interface files if your project doesn't already follow another convention](#rs-file-suffix)
* [SF.2: A header file must not contain object definitions or non-inline function definitions](#rs-inline)
* [SF.3: Use header files for all declarations used in multiple source files](#rs-declaration-header)
* [SF.4: Include header files before other declarations in a file](#rs-include-order)
* [SF.5: A `.cpp` file must include the header file(s) that defines its interface](#rs-consistency)
* [SF.6: Use `using namespace` directives for transition, for foundation libraries (such as `std`), or within a local scope (only)](#rs-using)
* [SF.7: Don't write `using namespace` at global scope in a header file](#rs-using-directive)
* [SF.8: Use `#include` guards for all header files](#rs-guards)
* [SF.9: Avoid cyclic dependencies among source files](#rs-cycles)
* [SF.10: Avoid dependencies on implicitly `#include`d names](#rs-implicit)
* [SF.11: Header files should be self-contained](#rs-contained)
* [SF.12: Prefer the quoted form of `#include` for files relative to the including file and the angle bracket form everywhere else](#rs-incform)
* [SF.13: Use portable header identifiers in `#include` statements](#rs-portable-header-id)

* [SF.20: Use `namespace`s to express logical structure](#rs-namespace)
* [SF.21: Don't use an unnamed (anonymous) namespace in a header](#rs-unnamed)
* [SF.22: Use an unnamed (anonymous) namespace for all internal/non-exported entities](#rs-unnamed2)

#### <a name="rs-file-suffix"></a>SF.1: Use a `.cpp` suffix for code files and `.h` for interface files if your project doesn't already follow another convention

See [NL.27](#rl-file-suffix)

#### <a name="rs-inline"></a>SF.2: A header file must not contain object definitions or non-inline function definitions

###### Reason

Including entities subject to the one-definition rule leads to linkage errors.

###### Example

    // file.h:
    namespace Foo {
        int x = 7;
        int xx() { return x+x; }
    }

    // file1.cpp:
    #include <file.h>
    // ... more ...

     // file2.cpp:
    #include <file.h>
    // ... more ...

Linking `file1.cpp` and `file2.cpp` will give two linker errors.

**Alternative formulation**: A header file must contain only:

* `#include`s of other header files (possibly with include guards)
* templates
* class definitions
* function declarations
* `extern` declarations
* `inline` function definitions
* `constexpr` definitions
* `const` definitions
* `using` alias definitions
* ???

###### Enforcement

Check the positive list above.

#### <a name="rs-declaration-header"></a>SF.3: Use header files for all declarations used in multiple source files

###### Reason

Maintainability. Readability.

###### Example, bad

    // bar.cpp:
    void bar() { cout << "bar\n"; }

    // foo.cpp:
    extern void bar();
    void foo() { bar(); }

A maintainer of `bar` cannot find all declarations of `bar` if its type needs changing.
The user of `bar` cannot know if the interface used is complete and correct. At best, error messages come (late) from the linker.

###### Enforcement

* Flag declarations of entities in other source files not placed in a `.h`.

#### <a name="rs-include-order"></a>SF.4: Include header files before other declarations in a file

###### Reason

Minimize context dependencies and increase readability.

###### Example

    #include <vector>
    #include <algorithm>
    #include <string>

    // ... my code here ...

###### Example, bad

    #include <vector>

    // ... my code here ...

    #include <algorithm>
    #include <string>

###### Note

This applies to both `.h` and `.cpp` files.

###### Note

There is an argument for insulating code from declarations and macros in header files by `#including` headers *after* the code we want to protect
(as in the example labeled "bad").
However

* that only works for one file (at one level): Use that technique in a header included with other headers and the vulnerability reappears.
* a namespace (an "implementation namespace") can protect against many context dependencies.
* full protection and flexibility require modules.

**See also**:

* [Working Draft, Extensions to C++ for Modules](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/n4592.pdf)
* [Modules, Componentization, and Transition](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0141r0.pdf)

###### Enforcement

Easy.

#### <a name="rs-consistency"></a>SF.5: A `.cpp` file must include the header file(s) that defines its interface

###### Reason

This enables the compiler to do an early consistency check.

###### Example, bad

    // foo.h:
    void foo(int);
    int bar(long);
    int foobar(int);

    // foo.cpp:
    void foo(int) { /* ... */ }
    int bar(double) { /* ... */ }
    double foobar(int);

The errors will not be caught until link time for a program calling `bar` or `foobar`.

###### Example

    // foo.h:
    void foo(int);
    int bar(long);
    int foobar(int);

    // foo.cpp:
    #include "foo.h"

    void foo(int) { /* ... */ }
    int bar(double) { /* ... */ }
    double foobar(int);   // error: wrong return type

The return-type error for `foobar` is now caught immediately when `foo.cpp` is compiled.
The argument-type error for `bar` cannot be caught until link time because of the possibility of overloading, but systematic use of `.h` files increases the likelihood that it is caught earlier by the programmer.

###### Enforcement

???

#### <a name="rs-using"></a>SF.6: Use `using namespace` directives for transition, for foundation libraries (such as `std`), or within a local scope (only)

###### Reason

 `using namespace` can lead to name clashes, so it should be used sparingly.
 However, it is not always possible to qualify every name from a namespace in user code (e.g., during transition)
 and sometimes a namespace is so fundamental and prevalent in a code base, that consistent qualification would be verbose and distracting.

###### Example

    #include <string>
    #include <vector>
    #include <iostream>
    #include <memory>
    #include <algorithm>

    using namespace std;

    // ...

Here (obviously), the standard library is used pervasively and apparently no other library is used, so requiring `std::` everywhere
could be distracting.

###### Example

The use of `using namespace std;` leaves the programmer open to a name clash with a name from the standard library

    #include <cmath>
    using namespace std;

    int g(int x)
    {
        int sqrt = 7;
        // ...
        return sqrt(x); // error
    }

However, this is not particularly likely to lead to a resolution that is not an error and
people who use `using namespace std` are supposed to know about `std` and about this risk.

###### Note

A `.cpp` file is a form of local scope.
There is little difference in the opportunities for name clashes in an N-line `.cpp` containing a `using namespace X`,
an N-line function containing a `using namespace X`,
and M functions each containing a `using namespace X` with N lines of code in total.

###### Note

[Don't write `using namespace` at global scope in a header file](#rs-using-directive).

#### <a name="rs-using-directive"></a>SF.7: Don't write `using namespace` at global scope in a header file

###### Reason

Doing so takes away an `#include`r's ability to effectively disambiguate and to use alternatives. It also makes `#include`d headers order-dependent as they might have different meaning when included in different orders.

###### Example

    // bad.h
    #include <iostream>
    using namespace std; // bad

    // user.cpp
    #include "bad.h"

    bool copy(/*... some parameters ...*/);    // some function that happens to be named copy

    int main()
    {
        copy(/*...*/);    // now overloads local ::copy and std::copy, could be ambiguous
    }

###### Note

An exception is `using namespace std::literals;`. This is necessary to use string literals
in header files and given [the rules](https://eel.is/c++draft/over.literal) - users are required
to name their own UDLs `operator""_x` - they will not collide with the standard library.

###### Enforcement

Flag `using namespace` at global scope in a header file.

#### <a name="rs-guards"></a>SF.8: Use `#include` guards for all header files

###### Reason

To avoid files being `#include`d several times.

In order to avoid include guard collisions, do not just name the guard after the filename.
Be sure to also include a key and good differentiator, such as the name of library or component
the header file is part of.

###### Example

    // file foobar.h:
    #ifndef LIBRARY_FOOBAR_H
    #define LIBRARY_FOOBAR_H
    // ... declarations ...
    #endif // LIBRARY_FOOBAR_H

###### Enforcement

Flag `.h` files without `#include` guards.

###### Note

Some implementations offer vendor extensions like `#pragma once` as alternative to include guards.
It is not standard and it is not portable.  It injects the hosting machine's filesystem semantics
into your program, in addition to locking you down to a vendor.
Our recommendation is to write in ISO C++: See [rule P.2](#rp-cplusplus).

#### <a name="rs-cycles"></a>SF.9: Avoid cyclic dependencies among source files

###### Reason

Cycles complicate comprehension and slow down compilation. They also
complicate conversion to use language-supported modules (when they become
available).

###### Note

Eliminate cycles; don't just break them with `#include` guards.

###### Example, bad

    // file1.h:
    #include "file2.h"

    // file2.h:
    #include "file3.h"

    // file3.h:
    #include "file1.h"

###### Enforcement

Flag all cycles.


#### <a name="rs-implicit"></a>SF.10: Avoid dependencies on implicitly `#include`d names

###### Reason

Avoid surprises.
Avoid having to change `#include`s if an `#include`d header changes.
Avoid accidentally becoming dependent on implementation details and logically separate entities included in a header.

###### Example, bad

    #include <iostream>
    using namespace std;

    void use()
    {
        string s;
        cin >> s;               // fine
        getline(cin, s);        // error: getline() not defined
        if (s == "surprise") {  // error == not defined
            // ...
        }
    }

`<iostream>` exposes the definition of `std::string` ("why?" makes for a fun trivia question),
but it is not required to do so by transitively including the entire `<string>` header,
resulting in the popular beginner question "why doesn't `getline(cin,s);` work?"
or even an occasional "`string`s cannot be compared with `==`").

The solution is to explicitly `#include <string>`:

###### Example, good

    #include <iostream>
    #include <string>
    using namespace std;

    void use()
    {
        string s;
        cin >> s;               // fine
        getline(cin, s);        // fine
        if (s == "surprise") {  // fine
            // ...
        }
    }

###### Note

Some headers exist exactly to collect a set of consistent declarations from a variety of headers.
For example:

    // basic_std_lib.h:

    #include <string>
    #include <map>
    #include <iostream>
    #include <random>
    #include <vector>

a user can now get that set of declarations with a single `#include`

    #include "basic_std_lib.h"

This rule against implicit inclusion is not meant to prevent such deliberate aggregation.

###### Enforcement

Enforcement would require some knowledge about what in a header is meant to be "exported" to users and what is there to enable implementation.
No really good solution is possible until we have modules.

#### <a name="rs-contained"></a>SF.11: Header files should be self-contained

###### Reason

Usability, headers should be simple to use and work when included on their own.
Headers should encapsulate the functionality they provide.
Avoid clients of a header having to manage that header's dependencies.

###### Example

    #include "helpers.h"
    // helpers.h depends on std::string and includes <string>

###### Note

Failing to follow this results in difficult to diagnose errors for clients of a header.

###### Note

A header should include all its dependencies. Be careful about using relative paths because C++ implementations diverge on their meaning.

###### Enforcement

A test should verify that the header file itself compiles or that a cpp file which only includes the header file compiles.

#### <a name="rs-incform"></a>SF.12: Prefer the quoted form of `#include` for files relative to the including file and the angle bracket form everywhere else

###### Reason

The [standard](https://eel.is/c++draft/cpp.include) provides flexibility for compilers to implement
the two forms of `#include` selected using the angle (`<>`) or quoted (`""`) syntax. Vendors take
advantage of this and use different search algorithms and methods for specifying the include path.

Nevertheless, the guidance is to use the quoted form for including files that exist at a relative path to the file containing the `#include` statement (from within the same component or project) and to use the angle bracket form everywhere else, where possible. This encourages being clear about the locality of the file relative to files that include it, or scenarios where the different search algorithm is required. It makes it easy to understand at a glance whether a header is being included from a local relative file versus a standard library header or a header from the alternate search path (e.g. a header from another library or a common set of includes).

###### Example

    // foo.cpp:
    #include <string>                // From the standard library, requires the <> form
    #include <some_library/common.h> // A file that is not locally relative, included from another library; use the <> form
    #include "foo.h"                 // A file locally relative to foo.cpp in the same project, use the "" form
    #include "util/util.h"           // A file locally relative to foo.cpp in the same project, use the "" form
    #include <component_b/bar.h>     // A file in the same project located via a search path, use the <> form

###### Note

Failing to follow this results in difficult to diagnose errors due to picking up the wrong file by incorrectly specifying the scope when it is included. For example, in a typical case where the `#include ""` search algorithm might search for a file existing at a local relative path first, then using this form to refer to a file that is not locally relative could mean that if a file ever comes into existence at the local relative path (e.g. the including file is moved to a new location), it will now be found ahead of the previous include file and the set of includes will have been changed in an unexpected way.

Library creators should put their headers in a folder and have clients include those files using the relative path `#include <some_library/common.h>`

###### Enforcement

A test should identify whether headers referenced via `""` could be referenced with `<>`.

#### <a name="rs-portable-header-id"></a>SF.13: Use portable header identifiers in `#include` statements

###### Reason

The [standard](https://eel.is/c++draft/cpp.include) does not specify how compilers uniquely locate headers from an identifier in an `#include` directive, nor does it specify what constitutes uniqueness. For example, whether the implementation considers the identifiers to be case-sensitive, or whether the identifiers are file system paths to a header file, and if so, how a hierarchical file system path is delimited.

To maximize the portability of `#include` directives across compilers, guidance is to:

* use case-sensitivity for the header identifier, matching how the header is defined by the standard, specification, implementation, or file that provides the header.
* when the header identifier is a hierarchical file path, use forward-slash `/` to delimit path components as this is the most widely-accepted path-delimiting character.

###### Example

    // good examples
    #include <vector>
    #include <string>
    #include "util/util.h"

    // bad examples
    #include <VECTOR>        // bad: the standard library defines a header identified as <vector>, not <VECTOR>
    #include <String>        // bad: the standard library defines a header identified as <string>, not <String>
    #include "Util/Util.H"   // bad: the header file exists on the file system as "util/util.h"
    #include "util\util.h"   // bad: may not work if the implementation interprets `\u` as an escape sequence, or where '\' is not a valid path separator

###### Enforcement

It is only possible to enforce on implementations where header identifiers are case-sensitive and which only support `/` as a file path delimiter.

#### <a name="rs-namespace"></a>SF.20: Use `namespace`s to express logical structure

###### Reason

 ???

###### Example

    ???

###### Enforcement

???

#### <a name="rs-unnamed"></a>SF.21: Don't use an unnamed (anonymous) namespace in a header

###### Reason

It is almost always a bug to mention an unnamed namespace in a header file.

###### Example

    // file foo.h:
    namespace
    {
        const double x = 1.234;  // bad

        double foo(double y)     // bad
        {
            return y + x;
        }
    }

    namespace Foo
    {
        const double x = 1.234; // good

        inline double foo(double y)        // good
        {
            return y + x;
        }
    }

###### Enforcement

* Flag any use of an anonymous namespace in a header file.

#### <a name="rs-unnamed2"></a>SF.22: Use an unnamed (anonymous) namespace for all internal/non-exported entities

###### Reason

Nothing external can depend on an entity in a nested unnamed namespace.
Consider putting every definition in an implementation source file in an unnamed namespace unless that is defining an "external/exported" entity.

###### Example; bad

    static int f();
    int g();
    static bool h();
    int k();

###### Example; good

    namespace {
        int f();
        bool h();
    }
    int g();
    int k();

###### Example

An API class and its members can't live in an unnamed namespace; but any "helper" class or function that is defined in an implementation source file should be at an unnamed namespace scope.

    ???

###### Enforcement

* ???

## <a name="s-profile"></a>Pro: Profiles

Ideally, we would follow all of the guidelines.
That would give the cleanest, most regular, least error-prone, and often the fastest code.
Unfortunately, that is usually impossible because we have to fit our code into large code bases and use existing libraries.
Often, such code has been written over decades and does not follow these guidelines.
We must aim for [gradual adoption](#s-modernizing).

Whatever strategy for gradual adoption we adopt, we need to be able to apply sets of related guidelines to address some set
of problems first and leave the rest until later.
A similar idea of "related guidelines" becomes important when some, but not all, guidelines are considered relevant to a code base
or if a set of specialized guidelines is to be applied for a specialized application area.
We call such a set of related guidelines a "profile".
We aim for such a set of guidelines to be coherent so that they together help us reach a specific goal, such as "absence of range errors"
or "static type safety."
Each profile is designed to eliminate a class of errors.
Enforcement of "random" rules in isolation is more likely to be disruptive to a code base than delivering a definite improvement.

A "profile" is a set of deterministic and portably enforceable subset of rules (i.e., restrictions) that are designed to achieve a specific guarantee.
"Deterministic" means they require only local analysis and could be implemented in a compiler (though they don't need to be).
"Portably enforceable" means they are like language rules, so programmers can count on different enforcement tools giving the same answer for the same code.

Code written to be warning-free using such a language profile is considered to conform to the profile.
Conforming code is considered to be safe by construction with regard to the safety properties targeted by that profile.
Conforming code will not be the root cause of errors for that property,
although such errors might be introduced into a program by other code, libraries or the external environment.
A profile might also introduce additional library types to ease conformance and encourage correct code.

Profiles summary:

* [Pro.type: Type safety](#ss-type)
* [Pro.bounds: Bounds safety](#ss-bounds)
* [Pro.lifetime: Lifetime safety](#ss-lifetime)

In the future, we expect to define many more profiles and add more checks to existing profiles.
Candidates include:

* narrowing arithmetic promotions/conversions (likely part of a separate safe-arithmetic profile)
* arithmetic cast from negative floating point to unsigned integral type (ditto)
* selected undefined behavior: Start with Gabriel Dos Reis's UB list developed for the WG21 study group
* selected unspecified behavior: Addressing portability concerns.
* `const` violations: Mostly done by compilers already, but we can catch inappropriate casting and underuse of `const`.

Enabling a profile is implementation defined; typically, it is set in the analysis tool used.

To suppress enforcement of a profile check, place a `suppress` annotation on a language contract. For example:

    [[suppress("bounds")]] char* raw_find(char* p, int n, char x)    // find x in p[0]..p[n - 1]
    {
        // ...
    }

Now `raw_find()` can scramble memory to its heart's content.
Obviously, suppression should be very rare.

### <a name="ss-type"></a>Pro.safety: Type-safety profile

This profile makes it easier to construct code that uses types correctly and avoids inadvertent type punning.
It does so by focusing on removing the primary sources of type violations, including unsafe uses of casts and unions.

For the purposes of this section,
type-safety is defined to be the property that a variable is not used in a way that doesn't obey the rules for the type of its definition.
Memory accessed as a type `T` should not be valid memory that actually contains an object of an unrelated type `U`.
Note that the safety is intended to be complete when combined also with [Bounds safety](#ss-bounds) and [Lifetime safety](#ss-lifetime).

An implementation of this profile shall recognize the following patterns in source code as non-conforming and issue a diagnostic.

Type safety profile summary:

* <a name="pro-type-avoidcasts"></a>Type.1: [Avoid casts](#res-casts):

  1. <a name="pro-type-reinterpretcast"></a>Don't use `reinterpret_cast`; A strict version of [Avoid casts](#res-casts) and [prefer named casts](#res-casts-named).
  2. <a name="pro-type-arithmeticcast"></a>Don't use `static_cast` for arithmetic types; A strict version of [Avoid casts](#res-casts) and [prefer named casts](#res-casts-named).
  3. <a name="pro-type-identitycast"></a>Don't cast between pointer types where the source type and the target type are the same; A strict version of [Avoid casts](#res-casts).
  4. <a name="pro-type-implicitpointercast"></a>Don't cast between pointer types when the conversion could be implicit; A strict version of [Avoid casts](#res-casts).
* <a name="pro-type-downcast"></a>Type.2: Don't use `static_cast` to downcast:
[Use `dynamic_cast` instead](#rh-dynamic_cast).
* <a name="pro-type-constcast"></a>Type.3: Don't use `const_cast` to cast away `const` (i.e., at all):
[Don't cast away const](#res-casts-const).
* <a name="pro-type-cstylecast"></a>Type.4: Don't use C-style `(T)expression` or functional `T(expression)` casts:
Prefer [construction](#res-construct) or [named casts](#res-casts-named) or `T{expression}`.
* <a name="pro-type-init"></a>Type.5: Don't use a variable before it has been initialized:
[always initialize](#res-always).
* <a name="pro-type-memberinit"></a>Type.6: Always initialize a data member:
[always initialize](#res-always),
possibly using [default constructors](#rc-default0) or
[default member initializers](#rc-in-class-initializer).
* <a name="pro-type-union"></a>Type.7: Avoid naked union:
[Use `variant` instead](#ru-naked).
* <a name="pro-type-varargs"></a>Type.8: Avoid varargs:
[Don't use `va_arg` arguments](#f-varargs).

###### Impact

With the type-safety profile you can trust that every operation is applied to a valid object.
An exception can be thrown to indicate errors that cannot be detected statically (at compile time).
Note that this type-safety can be complete only if we also have [Bounds safety](#ss-bounds) and [Lifetime safety](#ss-lifetime).
Without those guarantees, a region of memory could be accessed independent of which object, objects, or parts of objects are stored in it.


### <a name="ss-bounds"></a>Pro.bounds: Bounds safety profile

This profile makes it easier to construct code that operates within the bounds of allocated blocks of memory.
It does so by focusing on removing the primary sources of bounds violations: pointer arithmetic and array indexing.
One of the core features of this profile is to restrict pointers to only refer to single objects, not arrays.

We define bounds-safety to be the property that a program does not use an object to access memory outside of the range that was allocated for it.
Bounds safety is intended to be complete only when combined with [Type safety](#ss-type) and [Lifetime safety](#ss-lifetime),
which cover other unsafe operations that allow bounds violations.

Bounds safety profile summary:

* <a name="pro-bounds-arithmetic"></a>Bounds.1: Don't use pointer arithmetic. Use `span` instead:
[Pass pointers to single objects (only)](#ri-array) and [Keep pointer arithmetic simple](#res-ptr).
* <a name="pro-bounds-arrayindex"></a>Bounds.2: Only index into arrays using constant expressions:
[Pass pointers to single objects (only)](#ri-array) and [Keep pointer arithmetic simple](#res-ptr).
* <a name="pro-bounds-decay"></a>Bounds.3: No array-to-pointer decay:
[Pass pointers to single objects (only)](#ri-array) and [Keep pointer arithmetic simple](#res-ptr).
* <a name="pro-bounds-stdlib"></a>Bounds.4: Don't use standard-library functions and types that are not bounds-checked:
[Use the standard library in a type-safe manner](#rsl-bounds).

###### Impact

Bounds safety implies that access to an object - notably arrays - does not access beyond the object's memory allocation.
This eliminates a large class of insidious and hard-to-find errors, including the (in)famous "buffer overflow" errors.
This closes security loopholes as well as a prominent source of memory corruption (when writing out of bounds).
Even if an out-of-bounds access is "just a read", it can lead to invariant violations (when the accessed isn't of the assumed type)
and "mysterious values."


### <a name="ss-lifetime"></a>Pro.lifetime: Lifetime safety profile

Accessing through a pointer that doesn't point to anything is a major source of errors,
and very hard to avoid in many traditional C or C++ styles of programming.
For example, a pointer might be uninitialized, the `nullptr`, point beyond the range of an array, or to a deleted object.

[See the current design specification here.](https://github.com/isocpp/CppCoreGuidelines/blob/master/docs/Lifetime.pdf)

Lifetime safety profile summary:

* <a name="pro-lifetime-invalid-deref"></a>Lifetime.1: Don't dereference a possibly invalid pointer:
[detect or avoid](#res-deref).

###### Impact

Once completely enforced through a combination of style rules, static analysis, and library support, this profile

* eliminates one of the major sources of nasty errors in C++
* eliminates a major source of potential security violations
* improves performance by eliminating redundant "paranoia" checks
* increases confidence in correctness of code
* avoids undefined behavior by enforcing a key C++ language rule

## <a name="s-tools"></a>Appendix D: Supporting tools

This section contains a list of tools that directly support adoption of the C++ Core Guidelines. This list is not intended to be an exhaustive list of tools
that are helpful in writing good C++ code. If a tool is designed specifically to support and links to the C++ Core Guidelines it is a candidate for inclusion.

#### <a name="St-clangtidy"></a>Tools: [Clang-tidy](https://clang.llvm.org/extra/clang-tidy/checks/list.html)

Clang-tidy has a set of rules that specifically enforce the C++ Core Guidelines. These rules are named in the pattern `cppcoreguidelines-*`.

#### <a name="St-cppcorecheck"></a>Tools: [CppCoreCheck](https://docs.microsoft.com/en-us/visualstudio/code-quality/using-the-cpp-core-guidelines-checkers)

The Microsoft compiler's C++ code analysis contains a set of rules specifically aimed at enforcement of the C++ Core Guidelines.
