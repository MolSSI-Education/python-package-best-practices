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

## Project creation on GitHub

Create the project on GitHub. The students should create it under their own account

- Choose a license. Recommend BSD-3C, but git a quick overview of
  open-source licenses. See https://opensource.org for details.

- Choose the .gitignore for python, and explain why this is a good idea.

- Have GitHub create the README.md

After that, clone the project on the command line.

`git clone github.com:<account>/<project>.git

That is all for git in this section - more will be covered later.


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
(linux) if you do not have tree you can get using 'sudo apt-get install tree'
The above command is specific to distribution please refer to google for your distribution

## Creating the first python files

First, create the overall directory structure

Create the `__init__.py` and `my_math.py`.

In the `my_math.py` file, we are going to create a function that takes the mean/average
of a list.

1. What goes at the top of the file? File documentation
2. Then imports (we don't have any in this example)
3. Then write the function

At the end, the file should resemble the following. Note that
there is no error checking in the function - that will
be discussed later.

~~~
"""
Some miscellaneous math functions

Some example math functions for the MolSSI bootcamp
"""

def mean(num_list):
    """
    Calculates the mean of a list of numbers

    Parameters
    ----------
    num_list: list (int or float)


    Returns
    -------
    ret: int or float
        The mean of the list


    Examples
    --------
    >>> mean([1, 2, 3, 4, 5])
    3.0
    """

    return sum(num_list)/len(num_list)
~~~
{: .python}


Similarly, create the `string_util.py` file. The example function will be called
`title_string` and will transform a string to title case (where every word is
capitalized, but is otherwise lowercase).


~~~
"""
Some miscellaneous string manipulation functions

Some example string functions for the MolSSI bootcamp
"""

def title_string(s):
    """
    Converts a string to title case

    Title case is where the first letter of every word is capitalized,
    and every other character is lowercase.

    Parameters
    ----------
    s: string


    Returns
    -------
    ret: string
        The input string converted to title case


    Examples
    --------
    >>> title_string("this iS a String TO BE converTED")
    This Is A String To Be Converted
    """

    ret = s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] == ' ':
            ret += s[i].upper()
        else:
            ret += s[i].lower()
    return ret
~~~
{: .python}



## Introduction to importing

Go over how importing modules and submodules works. Modify the `__init__.py` file.

~~~
"""
Main project description
"""

from .math import *
from .string_util import *
~~~
{: .python}


## Go over setup.py

This file is mostly boiler plate, but go over which fields should be updated.
Copy example from `https://github.com/MolSSI/EEX/blob/master/setup.py` and modify.

Modifications:
  - Remove versioneer
  - Remove `cmdclass`
  - Change name, version, description, author, author_email, url
  - Remove entries under `install_requires`
  - Can remove version restriction on sphinx

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

Optional dependencies can be installed as well with `pip install -e .[docs,tests]

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

## Sphinx documentation

Documentation for python projects is usually written with Sphinx
(http://www.sphinx-doc.org).  The output of the documentation is
usually HTML, which can be uploaded to services such as ReadTheDocs
(https://readthedocs.org) or Github Pages (https://pages.github.com/).

Documentation can be started by changing to the `docs` directory , 
running `sphinx-quickstart`, and then answering the questions.

After that, have a look a the `conf.py` file and make any other necessary
modifications.

- Add numpydoc to the extensions list
- Change the theme to `sphinx_rtd_theme`

Then, try to build it with `make html`. If successful, you can open
the `_build/index.html` file in your browser.

Modify the the `index.rst` file, putting more information about your project.

One powerful feature of sphinx is the ability to pull out the docstrings
that you put in your code. This is done with the `autodoc` module that you
hopefully included when you ran the quickstart.

Create the file `module_doc.rst`.

~~~
Module Documentation
====================

math - Miscellaneous Math Functions
-----------------------------------

.. automodule:: msfdevops.math
   :members:


string_util - Some string functions
-----------------------------------

.. automodule:: msfdevops.string_util
   :members:

~~~
{: .rst}


Also, add the newly-created file to the table of contents on the main documentation
page (index.rst)

~~~
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   module_doc
~~~
{: .rst}

Rebuild (`make html`), and docstring documenation should show up on the generated HTML page.







{% include links.md %}
