---
title: "Python Module Structure"
teaching: 30
exercises: 60
questions:
- "What is the layout of a Python module?"
objectives:
- "Explain Python module structure"
- "Build a small module with a single function"
keypoints:
- "There is a common way to structure these modules"
- "Several pieces of code are what is known as 'boilerplate'"
---

This episode describes the structure of a Python module and the differentiantion
between a Python module and a set of Python scripts.

## Basic Structure
Let us layout our first module like the following:


├── LICENSE                         <- License file
├── README.md                       <- Description of project which GitHub will render
├── module
│   ├── __init__.py                 <- Basic Python Package import file
│   ├── first_module.py             <- Starting packge module
│   ├── data                        <- Sample additional data (non-code) which can be packaged
│   │   ├── README.md
│   │   └── look_and_say.dat
│   └── tests                       <- Unit test directory with sample tests
│       ├── __init__.py
│       └── test1.py
├── setup.py                        <- Your package's setup file for installing with additional options that can be set
└── .gitignore                      <- Stock helper file telling git what file name patterns to ignore when adding 

## Python local installs
For development work it is often recommended to do a "local" python install via
`pip install -e .`. This command will insert your new project into your Python
site-packages folder so that it can be found in any directory on your computer.


## Style Guides

Code style is important so that new developers can quickly read and understand
new code. While code style is typically quite personal, languages often have at
least a few dominant coding styles which are familiar to most programmers in
that language. Automatic formatting can enforce a particular coding style, and
are often configurable for each project.

- [Python Style Guide](https://www.python.org/dev/peps/pep-0008/)
- Python: [YAPF](https://github.com/google/yapf) (enforces [PEP8](https://www.python.org/dev/peps/pep-0008/))

{% include links.md %}
