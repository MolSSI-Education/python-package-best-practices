---
title: "Python Testing"
teaching: 30
exercises: 50
questions:
- "How is a Python module tested?"
objectives:
- "Explain the overall structure of testing."
- "Explain the reasons why testing is important."
keypoints:
- "Enumerate the types of testing and the importance of each."
- "Explain pytest features and why pytest was selected."
---

This episode explains the importance of testing and demonstrates the possible
capabilities.

## Why testing

Software should be tested regularly throughout the development cycle to insure
correct operation. Thorough testing is typically an afterthought, but for
larger projects it can be essential for ensuring changes in some parts of the
code do not negatively affect other parts.

Two main types of testing are strongly encouraged:

- Regression tests – given a known input, does the software correctly and
consistently return the correct values?

- Unit tests – Similar to general testing, except testing is done on much
smaller units (such as single functions or classes). This is helpful for
catching errors in uncommonly-used parts of the code which may be skipped in
general testing. Unit tests can be added as new features are added, resulting
in better code coverage.

## Unit vs Regression testing

## Pytest examples

The Python testing framework was chosen to be [pytest](https://pytest.org) for this project. Other testing frameworks are available;
however, the authors believe the combination of easy [parametrization of tests](https://docs.pytest.org/en/latest/parametrize.html),
[fixtures](https://docs.pytest.org/en/latest/fixture.html), and [test marking](https://docs.pytest.org/en/latest/example/markers.html)
make `pytest` particularly suited for computational chemistry.

To get started additional tests can be added to the `project/tests/` folder. Any function starting with `test_*` will automatically be
included in the testing framework. While these can be added in anywhere in your directory structure, it is highly recommended to keep them
contained within the `project/tests/` folder.

Tests can be run with the `py.test -v` command. There are a number of additional command line arguments to [explore](https://docs.pytest.org/en/latest/usage.html).

## Advanced features of pytest (fixtures, parameterize)



{% include links.md %}
