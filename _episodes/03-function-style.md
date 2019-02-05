---
title: "Python Coding Style"
teaching: 90
exercises: 120
questions:
- "?"
objectives:
- ""
keypoints:
- ""
---

## Style Guides

Code style is important so that new developers can quickly read and understand
new code. While code style is typically quite personal, languages often have at
least a few dominant coding styles which are familiar to most programmers in
that language. Automatic formatting can enforce a particular coding style, and
are often configurable for each project.

- [Python Style Guide](https://www.python.org/dev/peps/pep-0008/)
- Python: [YAPF](https://github.com/google/yapf) (enforces [PEP8](https://www.python.org/dev/peps/pep-0008/))

Install yapf via pip. Mangle one of the python files, and then show that `yapf` correctly fixes it.

## Create the setup.cfg

Create a `setup.cfg` file in the root directory containing the following:

~~~
[yapf]
COLUMN_LIMIT = 119
INDENT_WIDTH = 4
USE_TABS = False
~~~

This file will be used by yapf, allowing you to override some default options.
