---
title: "Documentation"
teaching: 30
exercises: 40
questions:
- "How can we document out module?"
objectives:
- "Run the lesson checking script and interpret its output correctly."
- "Explain in-code documentation"
- "Explain documentation tools like Read The Docs"
keypoints:
- "Some documentation is better than no documentation"
---

This episode discusses documentation strategies.

Documentation must be provided to allow for use, development, and maintenance
of the code. Documentation is often overlooked by developers since it is
tedious and boring, however good documentation is an extremely good habit to
develop.

The documentation typically involves several components:

 - Build requirements and dependencies (if applicable)
 - How to compile/build/test/install
 - How to use the software (through the API or through inputs)
 - Some examples
 - Another aspect of documentation is code documentation. This is very
important for further development and maintenance, including by yourself in the
future. This typically includes documenting various internal files, functions,
and classes; what pieces of code do; and most importantly, the reasoning behind
some decisions as to why some code was written a particular way.

Documentation should be kept up to date with changes in the code, which is not
an easy task for large, fast-moving codebases. However, slightly out-of-date
documentation is generally preferable to no documentation.

It is recommended that the examples provided within the documentation are
compiled and/or run regularly (if possible, as part of the testing of the
software) to ensure that it does not become neglected and out-of-date,
confusing users.

## In-code documentation

## README documentation

- Ok to document in README for simple modules

## RTD for complex modules

When you want to improve your documentation strategies use RTD

{% include links.md %}
