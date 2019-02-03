---
title: "Python Package Set-up and Structure"
teaching: 30
exercises: 60
questions:
- "What is the layout of a Python package?"
- "How can I quickly create the structure of a Python package?"
objectives:
- "Explain Python package structure."
- "Use the [CMS CookieCutter] to build a Python package."
keypoints:
- "There is a common way to structure these packages"
---

# Examples of Python package structure
If you look at the GitHub repositories for several large Python packages such as [numpy], [scipy], or [scikit-learn], you will notice a lot of similarities between the directory layouts of these projects.

Having a similar, or "canonical" way to lay out Python packages allows people to more easily understand and contribute to your code.

# Creating a Python package using CookieCutter
To create a skeletal structure for our project, we will use the MolSSI [CMS CookieCutter]. This will not only create our directory layout, but will also set up many tools we will use including testing, continuous integration, documentation, and git. We will discuss what all of these are later in the workshop.

## Obtaining CookieCutter

You should have the CMS CookieCutter installed, according to the directions given in the [setup] portion of this workshop. If you do not, please navigate to [setup] and follow the instructions given there.

## Running CookieCutter

## Reviewing directory contents

## Basic Structure

Let us layout our first module like the following:

```
├── LICENSE                         <- License file
├── README.md                       <- Description of project which GitHub will render
├── docs                            <- Documentation for the project
├── <project>
│   ├── __init__.py                 <- Basic Python Package import file
│   ├── string_util.py              <- Example python file - string utilities
│   ├── my_math.py                     <- Example python file - some math function
│   ├── data                        <- Sample additional data (non-code) which can be packaged
│   │   ├── README.md               <- Always helpful to have README in subdirectories
│   └── tests                       <- Unit test directory with sample tests
│       ├── __init__.py
├── setup.py                        <- Your package's setup file for installing with additional options that can be set
└── .gitignore                      <- Stock helper file telling git what file name patterns to ignore when adding
```

To visualize your project like above you will use "tree"
(linux) if you do not have tree you can get using `sudo apt-get install tree`
The above command is specific to distribution please refer to google for your distribution

## Python local installs

For development work it is often recommended to do a "local" or "developer" install via
`pip install -e .`. This command will insert a link to your new project into your Python
site-packages folder so that it can be found when you are in any directory on your computer.

- Go over where the `site-packages` directory is
- After doing the developer install, show the file that was created

Show a quick python REPL loading the library that was installed

- Load the module, and then `print()` it
- Also show that the docstrings are available via `help()`

Show that importing the module works from anywhere on the system, as long
as you are in the right environment.

Optional dependencies can be installed as well with `pip install -e .[docs,tests]`


{% include links.md %}
[numpy]: https://github.com/numpy/numpy
[scipy]: https://github.com/scipy/scipy
[scikit-learn]: https://github.com/scikit-learn/scikit-learn
[CMS CookieCutter]: https://github.com/MolSSI/cookiecutter-cms
[Install cookiecutter]: https://cookiecutter.readthedocs.io/en/latest/installation.html
