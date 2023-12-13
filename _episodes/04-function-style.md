# Python Coding Style

```{admonition} Overview
:class: overview

Questions:

- How can I write Python code that is readable?

Objectives:

- Learn how to raise exceptions.
- Understand how to follow PEP8 style for Python.
- Understand what docstrings are and why they are important.
- Learn to write docstrings in numpy style.
```

:::{admonition} Follow Along with This Lesson
:class: tip

To follow along with this lesson, you should first complete
the 'Using Branches Exercise' in Episode 2 or you can download a pre-made workshop repository that is at the starting 
point.

- [Download the pre-made workshop repository as a zip file](https://github.com/MolSSI-Education/molecool/archive/refs/tags/python-coding-style-start.zip)

Alternatively, download the repository using the command line:

````{tab-set-code} 
```{code-block} shell
git clone https://github.com/MolSSI-Education/molecool.git
git checkout python-coding-style-start

```
````
:::

## Editing a function in our package
Let's look at one of the functions in our package.
Open your `molecool/functions.py` module in a text editor.
The function `open_pdb` reads coordinates and atom symbols from a pdb file.

````{tab-set-code} 

```{code-block} python
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
```
````


If we want to test our function, we require a pdb file.
The workshop materials downloaded during the setup include a set of pdb examples.
These are found in `molssi_beter_practices/starting_material/data/pdb/`.
We want to store these files in our `molecool` directory.
Luckily, `cookiecutter` created a folder designed specifically for that purpose.
The folder is in `molecool/data/`.
This folder can contain any data useful for testing of the basic functionality of our code.
Be mindful that this folder is also downloaded when installing our package,
so do not include data whose size is significant. 

Go ahead and copy the pdb files to a new folder `pdb` inside the data folder.
With the files in our `molecool` folder,
we can access the function when we execute it in the interactive Python interpreter.
Test this by opening the interactive Python interpreter and typing the following.

````{tab-set-code} 

```{code-block} python
>>> import os
>>> from molecool import open_pdb
>>> pdb_file = os.path.join('molecool', 'data', 'pdb', 'water.pdb')
>>> symbols, coords = open_pdb(pdb_file)
>>> symbols
```
````


````{tab-set-code} 

```{code-block} output
['O', 'H', 'H']
```
````


You should get a list of atomic symbols of the water molecule by executing this code.
You can also see the atomic coordinates by executing:
````{tab-set-code} 

```{code-block} python
>>> coords
```
````


You should get a numpy array of atomic coordinates.

````{tab-set-code} 

```{code-block} output
array([[ 9.626,  6.787, 12.673],
       [ 9.626,  8.42 , 12.673],
       [10.203,  7.604, 12.673]])
```
````

### Function Return Type

When we examine our `open_pdb` function, you may notice some inconsistency in the data type of the returned values.
Our function returns both molecules symbols and coordinates.
However, the molecule symbols are returned as a list, while the coordinates are returned as a numpy array.
This is not necessarily a problem, but it is inconsistent.
We should make sure that our function returns the same type of data for each variable.
This will be more clear to both users of our code and developers who are editing our code.
To change both outputs to NumPy arrays, our function can now look like the following:

````{tab-set-code} 

```{code-block} python

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
    sym = np.array(sym)
    return sym, coords

```
````

You can test your function again using the same procedure we applied above,
and now you will see that your function returns two NumPy arrays.

### Raising Exceptions 

Hooray! It seems like this function works!
This should come as no surprise since we are the authors of the function,
and we know its internal structure.
This is not necessarily true for someone editing our code and specially not true
for someone just using our code.
There are instances where unwanted behavior occurs, even though the code executes
(i.e. there are no syntax errors).
In these cases, our code should be able to stop itself to prevent further malfunction.

Take for example the division by zero. If we try to calculate 
````{tab-set-code} 

```{code-block} python
>>> 1/0
```
````


We would get

````{tab-set-code} 

```{code-block} output
ZeroDivisionError: division by zero
```
````

In this example, the code was smart enough to identify the division by zero and halt.
This type of feedback is much more helpful than just throwing an ugly `NaN`.
This is called an *exception* error.
There are several built-in exceptions, such as the "ZeroDivisionError".
You can choose to raise exceptions yourself when you think a function should fail
(instead of the function not failing, or running until it hits some other failure.)

Consider our function `write_xyz`.

````{tab-set-code} 

```{code-block} python
def write_xyz(file_location, symbols, coordinates):
    
    ## Write an xyz file given a file location, symbols, and coordinates.

    num_atoms = len(symbols)
    with open(file_location, 'w+') as f:
        f.write('{}\n'.format(num_atoms))
        f.write('XYZ file\n')
        
        for i in range(num_atoms):
            f.write('{}\t{}\t{}\t{}\n'.format(symbols[i], 
                                              coordinates[i,0], coordinates[i,1], coordinates[i,2]))
```
````


When examining this function, you may see a few opportunities for failure.
For example, a user could supply `symbols` and `coordinates` with different lengths.
If the `coordinates` argument is the longer one, we will not see an error.
The function will simply ignore the last coordinate.
If `symbols` is the longer argument, we will not have enough `coordinates` and an error will occur.
Neither of these is our intended behavior, but would occur without us knowing (some errors are silent)!

Let's try this out. In a python interpreter, try the following:

````{tab-set-code} 

```{code-block} python
>>> import molecool
>>> import numpy as np
>>> test_atoms = ["H", "O"]
>>> test_coords = np.array([[1,0,0],[0,0,0], [0,1,0]])
>>> molecool.write_xyz("test.xyz", test_atoms, test_coords)
```
````

You will see that no error occurs. 
If we open the written XYZ file, the last coordinate point has been discarded.

We probably intend for these variables to have the same number of elements.
When they don't, there's no way to tell what the user wanted,
or if they have accidentally passed us incorrect data.
We should check the length of these and raise an appropriate exception to halt the program if necessary. 

````{tab-set-code} 

```{code-block} python
def write_xyz(file_location, symbols, coordinates):
    
    ## Write an xyz file given a file location, symbols, and coordinates.
    num_atoms = len(symbols)
    
    if num_atoms != len(coordinates):
        raise ValueError(f"write_xyz : the number of symbols ({num_atoms}) and number of coordinates ({len(coordinates)}) must be the same to write xyz file!")
    
    with open(file_location, 'w+') as f:
        f.write('{}\n'.format(num_atoms))
        f.write('XYZ file\n')
        
        for i in range(num_atoms):
            f.write('{}\t{}\t{}\t{}\n'.format(symbols[i], 
                                              coordinates[i,0], coordinates[i,1], coordinates[i,2]))
```
````


As you can see, custom error messages can be quite descriptive of the problem.
Let's try this out with some fake data.
Using the same example as before:

````{tab-set-code} 

```{code-block} python
>>> import molecool
>>> import numpy as np
>>> test_atoms = ["H", "O"]
>>> test_coords = np.array([[1,0,0],[0,0,0], [0,1,0]])
>>> molecool.write_xyz("test.xyz", test_atoms, test_coords)
```
````


````{tab-set-code} 

```{code-block} output
ValueError: write_xyz : the number of symbols (2) and number of coordinates (3) must be the same to write xyz file!
```
````


The built-in exceptions already include errors that are common while programming.
For example, our function requires explicit use of [numpy] arrays.
Nevertheless, a user may be tempted to use a list of length 3 to describe the position of two atoms.
We know that it is not possible to perform arithmetic between full lists.
In this case we might use the exception type `TypeError`.

Other types of common exceptions include undefined variables (`NameError`)
and failed assertions that two numbers are the same (`AssertionError`).
The latter will be particularly useful when we want to automate testing within our package. 

### Coding Style

Our functions are now smarter and will better guide users while using them.
However, our function still might be hard to read and understand for others,
so we might want to consider styling it better.

As a developer, you spend a lot of time thinking about writing your code.
However, code is read much more often than it is written.
Following a style guide will help others (and perhaps you in the future!) to read your code.

For Python, the common convention for code style is called [PEP8].
PEP8 is a document that gives guidelines for best practices in Python coding style.
PEP8 is a recommendation, not a rule.
However, you should follow this convention when possible.

:::{admonition} Python PEP
:class: note
If you spend a lot of time programming in Python, you will see references to PEPs a lot.
PEP stands for "Python Enhancement Proposal".
These are design documents which provide information about features.
PEPs come from the Python community, meaning anyone can author a PEP (however, there is a strict review process).
PEPs are classified into three categories - standards, informational, or process.

You can read more about PEPs in [Python's documentation](https://www.python.org/dev/peps/pep-0001/).
PEP1 outlines what a PEP is and how they work.
:::

PEP8 tells us several things about styling that will make our code easier to read.
Let's consider some of these and how they might change our function.

### Variable names
PEP8 recommends that

> Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.
 
> Function names should be lowercase, with words separated by underscores as necessary to improve readability.

Though not specifically referenced in PEP8,
we also recommend making all variable names descriptive so that
someone reading your code can easily understand what the variable is. 

Consider a few variable we have defined in our function (`c`, `sym`, `c2`, `l`).
Is it clear what these are or mean? We can change them to be more descriptive and readable.

````{tab-set-code} 

```{code-block} python
def open_pdb(file_location):
    with open(file_location) as f:
        data = f.readlines()
    coordinates = []
    symbols = []
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coords = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coords)
    coords = np.array(coordinates)
    symbols = np.array(symbols)
    return symbols, coords
```
````


For this rewrite of the function, we have made the following changes in variable names.

- `f_loc`  ---> `file_location`
- `c` ---> `coordinates`
- `sym` ---> `symbols`
- `l` ---> `line`
- `c2` ---> `atom_coords`

These variable names follow PEP8 convention and are much more descriptive and readable. 

### Indentation

PEP8 indicates that indentation should be 4 spaces per indentation level.
Our code meets these criteria.

### Whitespace

> Always surround these binary operators with a single space on either side: assignment (=), augmented assignment (+=, -= etc.), comparisons (==, <, >, !=, <>, <=, >=, in, not in, is, is not), Booleans (and, or, not).

This means that every time we have an expression assigning a variable, it should be `variable = value` instead of `variable=value`.

You can also use whitespace to separate ideas within a function or code.

> Use blank lines in functions, sparingly, to indicate logical sections.

Using these rules, our function becomes

````{tab-set-code} 

```{code-block} python
def open_pdb(file_location):
    
    with open(file_location) as f:
        data = f.readlines()

    coordinates = []
    symbols = []
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coords = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coords)

    coords = np.array(coordinates)
    symbols = np.array(symbols)

    return symbols, coords
```
````


Now that we've written a new function in our project, we should commit our changes and push to GitHub.

````{tab-set-code} 

```{code-block} shell
git add .
git commit -m "add open_pdb function to molecool"
git push origin main
```
````

### Exercise - Improving the `calculate_distance` function

``````{admonition} Exercise
:class: exercise

Below is the `calculate_distance` function that takes two points in 3D space
and returns the distance between them. Even though it works just fine,
it might hard for others to understand.
Take a couple of minutes to reformat this function in the `molecool/functions.py` module.

````{tab-set-code} 

```{code-block} python
def calculate_distance(rA, rB):
    d=(rA-rB)
    dist=np.linalg.norm(d)
    return dist
```
````
`````{admonition} Solution
:class: solution dropdown

Here is a better formatted version of `calculate_distance`, which is easier to read and understand.

````{tab-set-code} 

```{code-block} python
def calculate_distance(rA, rB):

    dist_vec = (rA - rB)
    distance = np.linalg.norm(dist_vec)

    return distance
```
````
`````
``````

Now we've successfully styled function according to PEP8! However, if we compare what we've written above to the sample function, `canvas`, we notice that ours is a little different.

Keeping your previous Python interpreter open, type the following:

````{tab-set-code}
```{code-block} python
>>> import molecool as mc
>>> help(mc.canvas)
```
````


**Note: Do not use `help(mc.canvas())`, this will actually execute your code (not what we want).**

The code above calls Python's built-in function, `help`.
For our canvas function, it displays the multi-line comment (called a `docstring`), that is written beneath the function definition.

````{tab-set-code} 

```{code-block} output
Help on function canvas in module molecool.functions:

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
```
````


If we try the same thing on our `calculate_distance` function, we don't get a helpful message.

We will want to write a docstring for our new `calculate_distance` function.
This way, it will be clear to new developers who use our code what the function does,
and be accessible to anyone using the function interactively.
Returning to the `functions.py` module file,
edit your `calculate_distance` function to look like the following.

````{tab-set-code} 

```{code-block} python
def calculate_distance(rA, rB):
    """Calculate the distance between two points.

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between the two points.
    
    Examples
    --------
    >>> r1 = np.array([0, 0, 0])
    >>> r2 = np.array([0, 0.1, 0])
    >>> calculate_distance(r1, r2)
    0.1
    """
    dist_vec = (rA - rB)
    distance = np.linalg.norm(dist_vec)
        
    return distance
```
````



### Docstrings
We've now added a multi-line comment (called a `docstring`, short for "documentation string"), to the beginning of our function.
Docstrings **are the first statement after a function or module definition** and are opened and closed with three quotes.
The docstring should explain what the function or module does (and not how it is done).

[PEP257] provides very basic guidelines for docstrings.
There are many ways you could format a docstring (different styles/conventions).
We recommend using [numpy style docstrings],
which we used for the example above and for the `calculate_distance` function.

:::{admonition} The `__doc__` attribute
:class: note

When you add a docstring to a function or module, python automatically adds this to the `__doc__` attribute of the object.

You can also see an object's docstring by typing `object.__doc__` into the Python interpreter.
For example, to see the docstring associated with the canvas function, `molecool.canvas.__doc__` into the Python interpreter (after importing `molecool`, of course.)
:::

#### Sections of a Docstring
Each docstring has a number of sections which are separated by headings.
Headings should be underlined with hyphens (`-----`).
There are many options for sections, we will only cover the most relevant here.
If you would like to see a full list, check out the documentation for [numpy style docstrings].

##### 1. Short summary
A one-line summary that does not use the variable name or the function name.
In our `calculate_distance` function, this corresponds to the following.

````{tab-set-code} 

```{code-block} python
"""
Calculate the distance between two points.
"""
```
````


##### 2. Extended summary
A few sentences giving a detailed description of the function or module.
This section should be used to clarify *functionality*, not to discuss implementation.

We do not have an extended summary in our `calculate_distance` function, since it is relatively straightforward.

##### 3. Parameters
This section contains a description of the function arguments - keywords and expected types.

The parameters for our `calculate_distance` function are shown below.

````{tab-set-code} 

```{code-block} python
"""
Parameters
----------
rA, rB : np.ndarray
    The coordinates of each point.
"""
```
````


Here, you can see that the parameter section begins with the section title ("Parameters"),
followed by a line of hyphens ("----").
On the next line, we have the argument names (`rA, rB`),
then a colon (`:`) followed by the input type of the argument.
This line says that the arguments `rA` and `rB` should be of type `np.ndarray`.
The next line gives a more detailed description of the parameter.
When the input parameters are of different type, or they aren't related to each other,
they should be written on separate lines.

##### 4. Returns
This section is very similar to the `Parameters` section above.
In contrast to the `Parameters` section, each returned value does not have to be named,
but the type of the returned value is required.

For our `calculate_distance` function, our `Returns` section looks like the following.

````{tab-set-code} 

```{code-block} python
"""
Returns
-------
distance : float
    The distance between the two points.
"""
```
````


##### 5. Examples
This is an optional section to show examples of functionality.
This section is meant to illustrate usage.
Though this section is optional, its use is strongly encouraged.

Consider the example we have in our docstring

````{tab-set-code} 

```{code-block} python
"""
Examples
--------
>>> r1 = np.array([0, 0, 0])
>>> r2 = np.array([0, 0.1, 0])
>>> calculate_distance(r1, r2)
0.1
"""
```
````


It is important that your examples in docstrings are working Python.
We will see in the `testing` lesson how we can run automatic tests on our docstrings,
and in the `documentation` lesson, we will see how we can display examples in documentation to our users. 

We have three lines of code for our example. In examples, lines of code begin with `>>>`.
The first two lines define numpy arrays that are used in our `calculate_distance` function.
Note that `r1` and `r2` must be numpy arrays (as indicated by our `Parameters` section),
or our example will not give valid Python code (our function would error if we ran it).
On the last line, you give the output (with no `>>>` in front.)

Now that we've written a function in our project, we should commit our changes and push to GitHub.

````{tab-set-code} 

```{code-block} shell
git add .
git commit -m "edit style of calculate_distance function"
git push origin main
```
````


### Exercise - Docstrings

``````{admonition} Exercise - Docstrings
:class: exercise

Let's add a docstring to our `open_pdb` function including short summary, extended summary, parameters, and returns sections.

Start with the following docstring.
You will need to add the `Parameters` and `Returns` sections and edit the one-line description.
We have filled in an extended summary.
 
````{tab-set-code} 

```{code-block} python
def open_pdb(file_location):
    """One line description here.

    The pdb file must specify the atom elements in the last column, and follow
    the conventions outlined in the PDB format specification.
    
    """
```
````
`````{admonition} Solution
:class: solution dropdown

````{tab-set-code} 

```{code-block} python
def open_pdb(file_location):
     """Open and read coordinates and atom symbols from a pdb file.

     The pdb file must specify the atom elements in the last column, and follow
     the conventions outlined in the PDB format specification.

     Parameters
     ----------
     file_location : str
         The location of the pdb file to read in.

     Returns
     -------
     coords : np.ndarray
         The coordinates of the pdb file.
     symbols : list
         The atomic symbols of the pdb file.

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
```
````
Once you're done make sure to add, commit, and push your changes to GitHub.
``````

### More on Coding Style

If you look at PEP8, you will see that it is quite long.
While you should definitely read it if you spend a lot of time programming in Python,
there are luckily tools which will help us make sure
our code is following PEP8 convention or other styling guidelines.
There are auto-formatting tools such as `yapf` and `Black`,
and static code "linters" such as `pylint` or `flake8`.

Automatic code formatters will parse your python files and format them
according to standards defined by that code formatter.
It is usually a good idea to use a formatter (of your choice) when working on a python project.
In particular, [Black](https://github.com/psf/black) has gained popularity lately. 

We will use [Black](https://github.com/psf/black) in this workshop.
Black is an auto-formatter which is almost entirely non-customizable,
ensuring all of your files will be uniform. 

Install `black` using `pip`. In your terminal, type

````{tab-set-code}
```{code-block} shell
pip install black
```
````

Now we can use `black` on our python files.

````{tab-set-code} 

```{code-block} shell
black molecool/functions.py
```
````


You can see the changes to the `write_xyz` function, for example.
You'll notice that Black also has some rules which are in addition to PEP8 formatting.
For example, strings are all normalized to use double quotes.
Note that `black` does not always follow PEP8. For example,
PEP8 recommends that line lengths be no more than 79 characters.
This is a convention which is often not followed. Black defaults to 88 characters per line instead.
When you are working on a project, the exact style you use may be different.
However, it is important to choose a consistent style.
This will make your code much cleaner and easier to read.

Now that we've changed and formatted some functions in our project,
we should commit our changes and push to GitHub.

````{tab-set-code} 

```{code-block} shell
git add .
git commit -m "run black on molecool"
git push origin master
```
````


There are other tools, such as [pylint](https://www.pylint.org/) and
[flake8](https://flake8.pycqa.org/en/latest/) that are not automatic formatters,
but will check your code for adherence to the PEP8 standard.
Pylint, for example, will find your variables which are not `snake_case`,
functions which do not have `docstrings`, simple stylistic changes, unused variables, etc.
Flake8 is a little less strict in general.
We will try `flake8` out here.
If you would like to try `flake8`, first install it.

````{tab-set-code} 

```{code-block} shell
pip install flake8
```
````


You can run it on our `functions` module.

````{tab-set-code} 

```{code-block} shell
flake8 molecool/functions.py
```
````


Let's examine one of the errors shown by the flake8 command above.

````{tab-set-code} 

```{code-block} output
molecool/functions.py:1:1: F401 'os' imported but unused
```
````


This tells us it is looking at line 1 of `molecool/functions.py` (your line number may vary).
`F401` is an error code which you can look up.
Here, we are importing `os`, but never using it.
We should remove this from our file.

You will also see a second "unused import" error:

````{tab-set-code} 

```{code-block} output
molecool/functions.py:5:1: F401 'mpl_toolkits.mplot3d.Axes3D' imported but unused
```
````


Although it appears this isn't used, this import is actually necessary for our 3D plot.
We can tell `flake8` to ignore this problem by adding a special comment:

````{tab-set-code} 

```{code-block} python
from mpl_toolkits.mplot3d import Axes3D  ## noqa: F401
```
````


You can run `flake8` again to see that the import error is no longer reported.


:::{admonition} Final Repository State
:class: tip

You can see the final state of the repository after this section [here](https://github.com/MolSSI-Education/molecool/tree/ce11656b043846d6600b989eeba6a37ba541ea0c).

You can also download a zip of the repository [here](https://github.com/MolSSI-Education/molecool/archive/refs/tags/python-coding-style-end.zip).

:::



## Key Points

```{admonition} Key Points
:class: key

* Your project should adopt a consistent style so that others can easily read it.

* The style adopted in Python is called PEP8.

* There are autoformatting tools you can use to ensure that your code meets PEP8 standards.

* All functions and modules should be documented with docstrings. 

* Docstrings have a specific format. We recommend the NumPy format for docstrings.

```


[Exceptions]: https://realpython.com/python-exceptions/#the-try-and-except-block-handling-exceptions
[PEP8]: https://www.python.org/dev/peps/pep-0008/
[PEP257]: https://www.python.org/dev/peps/pep-0257/
[YAPF]: https://github.com/google/yapf
[numpy style docstrings]: https://numpydoc.readthedocs.io/en/latest/format.html

