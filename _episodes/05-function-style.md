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
We will now add a new function to our Python package. Create a new folder named `io` under `molecool` directory and add a file named `pdb.py`. Open your `molecool/io/pdb.py` module in a text editor. Currently, it should only have the default `canvas` function written by the CMS CookieCutter.

Let's add another function. We will add a function to open and read coordinates and atom symbols from a pdb file.

~~~
def open_pdb(f_loc):
    with open(f_loc) as f:
        data = f.readlines()
    c = []
    sym = []
    for l in data:
        if 'ATOM' in l[0:6] or 'HETATM' in l[0:6]:
            sym.append(l[76:79].strip())
            c2 = [float(x) for x in l[30:55].split()]
            c.append(c2)
    coords = np.array(c)
    return sym, coords
~~~
{: .language-python}

This function should now be accessible when we execute it in the interactive Python interpreter. Test this by opening the interactive Python interpreter and typing the following

~~~
>>> import os
>>> from molecool.io import open_pdb
>>> pdb_file = os.path.join('molecool', 'data', 'pdb', 'water.pdb')
>>> symbols, coords = open_pdb(pdb_file)
>>> symbols
~~~
{: .language-python}

~~~
array(['O', 'H', 'H'], dtype='<U1')
~~~
{: .output}

You should get a numpy array with atomic sybols of the water molecule from executing this code.
You can also see the atomic coordinates by executing:
~~~
>>> coords
~~~
{: .language-python}

Hooray! We've successfully implemented and are able to use our own custom function! However, if we compare what we've written above to the sample function, `canvas`, we notice that ours is a little different.

Keeping your previous Python interpreter open, type the following:

~~~
help(open_pdb)
~~~

**Note: Do not use `help(open_pdb())`, this will actually execute your code (not what we want).**

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

If we try the same thing on our `open_pdb` function, we don't get a helpful error message.

We will want to write a docstring for our new mean function. This way, it will be clear to new developers who use our code what the function does, and be accessible to any users using the function interactively. Returning, to the `pdb.py` module file, edit your `open_pdb` function to look like the following:

~~~
def open_pdb(file_location):
    """Open and read coordinates and atom symbols from a pdb file.

    The pdb file must specify the atom elements in the last column, and follow
    the conventions outlined in the PDB format specification.

    Parameters
    ----------
    file_location : str
        The location of the xyz file to read in.

    Returns
    -------
    coords : np.ndarray
        The coordinates of the xyz file.
    symbols : list
        The atomic symbols of the xyz file.

    """

    with open(file_location) as f:
        data = f.readlines()

    coordinates = []
    symbols = []

    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())

            coords = [float(x) for x in line[30:55].split()]
            coordinates.append(coords)

    coords = np.array(coordinates)
    symbols = np.array(symbols)

    return symbols, coords
~~~
{: .language-python}


## Docstrings
We've now added a multi-line comment (called a `docstring`, short for "doumentation string"), to the beginning of our function. Docstrings **are the first statment after a function or module definition** and are opened and closed with three quotes.

The docstring should explain what the function or module does (and not how it is done).

> ## The `__doc__` attribute
>
> When you add a docstring to a function or module, python automatically adds this to the `__doc__` attribute of the object.
>
> You can also see an object's docstring by typing `object.__doc__` into the Python interpreter. For example, to see the docstring associated with the canvas function, `molecool.canvas.__doc__` into the Python interpreter (after importing `molecool`, of course.)
{: .callout}

### Sections of a Docstring
There are many ways you could format this docstring (different styles/conventions). We recommend using [numpy style docstrings], and this is what the example above and `open_pdb` funtion are written in.

Each docstring has a number of sections which are separated by headings. Headings should be underlined with hyphens (`-----`). There are many options for sections, we will only cover the most relevant here. If you would like to see a full list, check out the documentation for [numpy style docstrings].

#### 1. Short summary
A one-line summary that does not use the variable name or the function name. In our `open_pdb` function, this corresponds to the following.

~~~
"""
Open and read coordinates and atom symbols from a pdb file.
"""
~~~
{: .language-python}

#### 2. Extended summary
A few sentences giving a detailed description of the function or module. This section should be used to clarify *functionality*, not to discuss implementation.

We do not have an extended summary in our `open_pdb` function, since it is relatively straightforward.

#### 3. Parameters
This section contains a description of the function arguments - keywords and expected types.

The parameters for our `open_pdb` function is shown below:

~~~
Parameters
----------
file_location : str
    The location of the xyz file to read in.
~~~
{: .language-python}

Here, you can see that the parameter section begins with the section title ("Parameters"), followed by a line of hypens ("----"). On the next line, we have the argument name (`file_location`), then a colon followed by the input type of the argument. This line says that the argument `file_location` should be of type `str`. The next line gives a more detailed description of the variable.

#### 4. Returns
This section is very similar to the `Parameters` section above. In contrast to the `Parameters` section, each returned value does not have to be named, but the type of the return value is required.

For our `open_pdb` function, our `Returns` section looks like the following.

~~~
Returns
-------
coords : np.ndarray
    The coordinates of the xyz file.
symbols : list
    The atomic symbols of the xyz file.
~~~
{: .language-python}

#### 5. Examples
This is an optional section to show examples of functionality. This section is meant to illustrate usage. Though this section is optional, its use is strongly encouraged.

Now that we've written a function in our project, we should commit our changes and push to [GitHub].

~~~
$ git add .
$ git commit -m "add open_pdb function to molecool"
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

If you look at PEP8, you will see that it is quite long. While you should definitely read it if you spend a lot of time programming in Python, there are luckily tools which will help us make sure our code is following PEP8 convention. We will use [yapf], an open source formatter for Python files from Google.

Install yapf using pip. In your terminal, type

~~~
$ pip install yapf
~~~
{: .language-bash}

Now we can use yapf on our python files. Just to see the power of yapf, let's mangle one of our functions and use yapf to reformat it.

~~~
def open_pdb(file_location):
            """
    Open and read coordinates and atom symbols from a pdb file.

    The pdb file must specify the atom elements in the last column, and follow
    the conventions outlined in the PDB format specification.

    Parameters
    ----------
    file_location : str
        The location of the xyz file to read in.

    Returns
    -------
    coords : np.ndarray
        The coordinates of the xyz file.
    symbols : list
        The atomic symbols of the xyz file.

            """

            with open(file_location) as f:
                data = f.readlines()

            coordinates = []
            symbols = []

            for line in data:
                if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
                    symbols.append(line[76:79].strip())

                    coords = [float(x) for x in line[30:55].split()]
                    coordinates.append(coords)

            coords = np.array(coordinates)
            symbols = np.array(symbols)

            return symbols, coords
~~~
{: .language-python}

If you save the file and test your function in the command line, you will see that it still works when formated this way. However, it is significantly harder to read in the text editor. We can use yapf to format this automatically. In your terminal, run yapf with the following command -

~~~
$ yapf -i molecool/io/pdb.py
~~~
{: .language-bash}

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
$ git commit -m "run yapf on molecool"
$ git push origin master
~~~
{: .bash}

[PEP8]: https://www.python.org/dev/peps/pep-0008/
[YAPF]: https://github.com/google/yapf
[numpy style docstrings]: https://docs.scipy.org/doc/numpy/docs/howto_document.html#numpydoc-docstring-guide
