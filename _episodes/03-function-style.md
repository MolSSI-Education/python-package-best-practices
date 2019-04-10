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

This function should now be accessible when we execute it in the interactive Python interpreter. Test this by opening the interactive Python interpreter and typing the following

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

**Note: Do not use `help(md.canvas())`, this will actually execute your code (not what we want).**

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

If we try the same thing on our `mean` function, we don't get a helpful error message.

We will want to write a docstring for our new mean function. This way, it will be clear to new developers who use our code what the function does, and be accessible to any users using the function interactively. Returning, to the `molssi_math.py` module file, edit your `mean` function to look like the following:

~~~
def mean(num_list):
    """
    Calculate the mean/average of a list of numbers.

    Parameters
    ----------
    num_list : list
        The list to take the average of

    Returns
    -------
    mean_list: float
        The mean of the list

    Examples
    --------
    >>> mean([1, 2, 3, 4, 5])
    3.0
    """

    mean_list = sum(num_list)/len(num_list)

    return mean_list
~~~
{: .language-python}


## Docstrings
We've now added a multi-line comment (called a `docstring`, short for "doumentation string"), to the beginning of our function. Docstrings **are the first statment after a function or module definition** and are opened and closed with three quotes.

The docstring should explain what the function or module does (and not how it is done).

> ## The `__doc__` attribute
>
> When you add a docstring to a function or module, python automatically adds this to the `__doc__` attribute of the object.
>
> You can also see an object's docstring by typing `object.__doc__` into the Python interpreter. For example, to see the docstring associated with the canvas function, `molssi_devops.canvas.__doc__` into the Python interpreter (after importing `molssi_devops`, of course.)
{: .callout}

### Sections of a Docstring
There are many ways you could format this docstring (different styles/conventions). We recommend using [numpy style docstrings], and this is what the example above and `mean` funtion are written in.

Each docstring has a number of sections which are separated by headings. Headings should be underlined with hyphens (`-----`). There are many options for sections, we will only cover the most relevant here. If you would like to see a full list, check out the documentation for [numpy style docstrings].

#### 1. Short summary
A one-line summary that does not use the variable name or the function name. In our `mean` function, this corresponds to the following.

~~~
"""
Calculate the mean/average of a list of numbers.
"""
~~~
{: .language-python}

#### 2. Extended summary
A few sentences giving a detailed description of the function or module. This section should be used to clarify *functionality*, not to discuss implementation.  

We do not have an extended summary in our `mean` function, since it is relatively straightforward.

#### 3. Parameters
This section contains a description of the function arguments - keywords and expected types.

The parameters for our `mean` function is shown below:

~~~
Parameters
----------
num_list : list
    The list to take the average of.
~~~
{: .language-python}

Here, you can see that the parameter section begins with the section title ("Parameters"), followed by a line of hypens ("----"). On the next line, we have the argument name (`num_list`), then a colon followed by the input type of the argument. This line says that the argument `num_list` should be of type list. The next line gives a more detailed description of the variable.

#### 4. Returns
This section is very similar to the `Parameters` section above. In contrast to the `Parameters` section, each returned value does not have to be named, but the type of the return value is required.

For our `mean` function, our `Returns` section looks like the following.

~~~
Returns
-------
mean_list: float
    The mean of the list
~~~
{: .language-python}

#### 5. Examples
This is an optional section to show examples of functionality. This section is meant to illustrate usage. Though this section is optional, its use is strongly encouraged.

Now that we've written a function in our project, we should commit our changes and push to [GitHub].

~~~
$ git add .
$ git commit -m "add mean function to molssi_math"
$ git push origin master
~~~
{: .bash}

## Coding Style

As a developer, you spend a lot of time thinking about writing your code. However, code is read much more often than it is written. Following a style guide will help others (and perhaps you in the future!) to read your code.

 For Python, the common convention for code style is called [PEP8]. PEP8 is a document that gives guidelines for best practices in Python coding style. PEP8 is a recommendation, not rule. However, you should follow this convention when possible.

 > ## Python PEP
 >
 > If you spend a lot of time programming in Python, you will see references to PEPs a lot. PEP stands for "Python Enhancement Proposal". These are design documents which provide information about features. PEPs come from the Python community, meaning anyone can author a PEP (however, there is a strict review process). PEPs are classified into three categories - standards, informational, or process.
 >
 > You can read more about PEPs in [Python's documentation](https://www.python.org/dev/peps/pep-0001/). PEP1 outlines what a PEP is and how they work.
 {: .callout}

If you look at PEP8, you will see that it is quite long. While you should definitely read it if you spend a lot of time programming in Python, there are luckily tools which will help us make sure our code is following PEP8 convention. We will you [yapf], an open source formatter for Python files from Google.

Install yapf using pip. In your terminal, type

~~~
$ pip install yapf
~~~

Now we can use yapf on our python files. Just to see the power of yapf, let's mangle one of our functions and use yapf to reformat it.

~~~
def mean(num_list):
            """
    Calculate the mean/average of a list of numbers.

    Parameters
    -----------
    num_list : list
        The list to take the average of

    Returns
    --------
    mean_list: float
        The mean of the list

    Examples
    ---------
    >>> mean([1, 2, 3, 4, 5])
    3.0
            """

            mean_list = (sum(num_list    )               /
            len(num_list))

            return mean_list
~~~
{: .language-python}

If you save the file and test your function in the command line, you will see that it still works when formated this way. However, it is significantly harder to read in the text editor. We can use yapf to format this automatically. In your terminal, run yapf with the following command -

~~~
$ yapf -i molssi_devops/molssi_math.py
~~~

Here, the `-i` flag indicates to do this "in-place", this means your file will be overwritten with yapf's changes. If you examine the file after running yapf, you should see that it is returned to an easily readable format.

> ## yapf settings
>
> CookieCutter created some settings for yapf for us when we ran it. In the file `setup.cfg` in the top level directory.
>
> ~~~
>[yapf]
>COLUMN_LIMIT = 119
>INDENT_WIDTH = 4
>USE_TABS = False
> ~~~
> This section overwrites some default parameters for yapf. You can change this to your preferences.
{: .callout}

Commit these Changes

Now that we've written a function in our project, we should commit our changes and push to [GitHub].

~~~
$ git add .
$ git commit -m "run yapf on molssi_math"
$ git push origin master
~~~
{: .bash}

[PEP8]: https://www.python.org/dev/peps/pep-0008/
[YAPF]: https://github.com/google/yapf
[numpy style docstrings]: https://docs.scipy.org/doc/numpy/docs/howto_document.html#numpydoc-docstring-guide
