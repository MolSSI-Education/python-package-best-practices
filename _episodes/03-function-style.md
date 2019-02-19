---
title: "Python Coding Style"
teaching: 30
exercises: 15
questions:
- "How can I write python code that is readable?"
objectives:
- "Understand how to follow PEP8 style for Python."
- "Understand what docstrings are and their importance."
- "Learn to write docstrings in numpy style"
keypoints:
- "Your code should adhere to standards outlined in PEP8 so that it easily readable by others."
- "All functions and modules should be documented with docstrings."
---

# Adding a function to our package
We will now add a new function to our Python package. Open your `molssi_math.py` module in a text editor. Currently, it should only have the default `canvas` function written by the CMS CookieCutter.

Let's add another function. We will add a function to calculate the mean of a list.

~~~
def mean(num_list):
    mean_list = sum(num_list)/len(num_list)
    return mean_list
~~~
{: .language-python}

This function should now be accessible when we execute it in the interactive Python interpreter. Let's test this. Open the interactive Python interpreter and type the following

~~~
>>> import molssi_devops as md
>>> md.mean([1, 2, 3, 4, 5])
~~~
{: .language-python}

~~~
3.0
~~~
{: .output}

You should get a value of 3.0 from executing this code.

Hooray! We've successfully implemented and are able to use our own custom function! However, if we compare what we've written above to the sample function, `canvas`, we notice that ours is a little different.

Keeping your previous Python interpreter open, type the following:

~~~
help(md.canvas)
~~~

**Note: Do not use `help(md.canvas())`, this will actually execute your code, and that is not what you want.**

The code above calls Python's built-in function, `help`. For our canvas function, it displays the multi-line comment (called a `docstring`), that is written beneath the function definition.

~~~
Help on function canvas in module molssi_devops.molssi_math:

canvas(with_attribution=True)
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
~~~
{: .output}

We will want to write one of these for our new mean function. This way, it will be clear to new developers who use our code what the function does, and be accessible to any users using the function interactively. Returning, to the `molssi_math.py` module, edit your `mean` function to look like the following:

~~~
def mean(num_list):
    """
    Calculate the mean/average of a list of numbers

    Parameters
    ------------------
    num_list : list
        The list to take the average of
    Returns
    -------------------
    mean_list: float
        The mean of the list
    Examples
    --------------------
    >>> mean([1, 2, 3, 4, 5])
    3.0
    """

    mean_list = sum(num_list)/len(num_list)

    return mean_list
~~~
{: .language-python}


## docstrings
We've now added a multi-line comment (called a `docstring`), to our function. Docstrings occur right after a function definition, and are opened and closed with three quotes

# Coding Style
Code style is important so that new developers can quickly read, understand, and contribute to
code. While code style is typically quite personal, languages often have at
least a few dominant coding styles which are familiar to most programmers in
that language.  

For Python, the common convention for code style is called [PEP8]. PEP8 is a document that gives guidelines for best practices in Python coding style.

> ## Python PEP
>
> If you spend a lot of time programming in Python, you will see references to PEPs a lot. PEP stands for "Python Enhancement Proposal". These are design documents which provide information about features. PEPs come from the Python community, meaning anyone can author a PEP (however, there is a strict review process). PEPs are classified into three categories - standards, informational, or process.
>
> You can read more about PEPs in [Python's documentation](https://www.python.org/dev/peps/pep-0001/). PEP1 outlines what a PEP is and how they work.
{: .callout}

## Style Guides

As a developer, you spend a lot of time thinking about writing your code. However, code is read much more often than it is written. Following a style guide will help others (and perhaps you in the future!) to read your code.

PEP8 is a recommendation, not rule. However, you should follow this convention when possible.


- Python Style Guide [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Python: [YAPF] (enforces [PEP8])

Install yapf via pip. Mangle one of the python files, and then show that `yapf` correctly fixes it.

Automatic formatting can enforce a particular coding style, and
are often configurable for each project.

## Create the setup.cfg

Create a `setup.cfg` file in the root directory containing the following:

~~~
[yapf]
COLUMN_LIMIT = 119
INDENT_WIDTH = 4
USE_TABS = False
~~~

This file will be used by yapf, allowing you to override some default options.

[PEP8]: https://www.python.org/dev/peps/pep-0008/
[YAPF]: https://github.com/google/yapf
