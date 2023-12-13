# Type Hinting in Python

````{admonition} Overview
:class: overview

Questions:

- What is type hinting?
- What does type hinting do for my software?

Objectives:

- Learn about type hinting in Python.
- Learn the syntax to utilize type hinting in Python.

````
:::{admonition} Follow Along with This Lesson
:class: tip

To follow along with this lesson, you can complete the previous lessons,
or you can download a pre-made workshop repository that is at the starting 
point.

- [Download the pre-made workshop repository as a zip file](https://github.com/MolSSI-Education/molecool/archive/refs/tags/python-type-hinting-start.zip)

Alternatively, download the repository using the command line:

````{tab-set-code} 
```{code-block} shell
git clone https://github.com/MolSSI-Education/molecool.git
git checkout python-type-hinting-start
```
:::

Python does not inherently require or enforce the *types* of variables in code.
Python instead works under a principle called `Duck Typing`.
Duck Typing is derived from the phrase, "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."
Similarily, if the value assigned to a variable can be used when an integer is called for, the code largely is unconcerned if the variable is an integer or another type.

Though Duck Typing allows for flexibility in the use of variables, and similarily functions which take and return values of arbitrary type, a number of issues can arise.

Consider the `calculate_distance` function from `measure.py`:

````{tab-set-code}

```{code-block} measure.py
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

    dist_vec = rA - rB
    distance = np.linalg.norm(dist_vec)

    return distance
```
````

What are the types of the inputs for this function?
The docstring currently specifies that the parameters `rA` and `rB` are both `np.ndarray`.
The code does not explicitly type the variables, however there is implicit typing, which is where duck typing comes into play.
Consider the operations that are applied to the variables `rA` and `rB`.
First, `rB` is subtracted from `rA`.
Any types that do not support the `-` operation will cause an error.
As an example, try running the function with two lists.

````{tab-set-code}
```{code-block} python
>>> calculate_distance([1,2,3], [2,3,4])
```
````

Python will throw an exception.

````{tab-set-code}
```{code-block} output
TypeError: unsupported operand type(s) for -: 'list' and 'list'
```
````

This `TypeError` seems like an appropriate exception, but it would be nice if we could do more to anticipate this error and catch it before run time.

If the function is provided with a type that is usable, it will run successfully, even if it is being used in a way we did not anticipate.

```python
calculate_distance(2, 1)
```

Though the function is designed to work on two `np.ndarray` variables,
Python's Duck Typing will allow the code to _try_ to execute with arguments of any type.
Since (as the author) we _know_ that the code will not behave as expected if the user provides inappropriate arguments,
we should do more to help make sure the code is used and behaves as expected.

## Type Hinting
Type hinting a function, and in fact any variable, can improve how easy it is to understand the needs and behaviors of a function.
It is important to note that type hints will not be enforced by Python.
The benefits of type hinting are to support error checking at development time to help avoid errors at run time.
Python makes it easy to specify a type hint for any variable.
We can specify a type with or without providing a default value.

````{tab-set-code}
```{code-block} python
my_integer: int

my_float: float = 0.3

list_of_ints: list[int]
```
````

Type hints can include any type available where the code is written, including
 * Simple types available in all Python code: int, float, str, bool, list
 * User defined types
 * Imported types

Note that (since Python 3.9) the built-in container types support subscripting syntax.
Above, we want to specify that `list_of_ints` is not a
[Generic](https://docs.python.org/3/library/typing.html#generics) `list`,
but specifically a `list` with `int` elements.

This syntax is only relevant to static type checking.
At run time, `list[int]` is identically the same type as `list`.

### Function Type Hinting

The same syntax can be used to specify function inputs.
We can add type hints to a function to specify what types the function works on.

````{tab-set-code}
```{code-block} python
def my_function(var1: int, var2: float):
    ...
```
````

Each variable can be assigned its own type.

`my_function` expects two variables, `var1` and `var2`, which should be an `int` and a `float` respectively.

The syntax for type hinting a function output is a bit different.
We follow the function declaration with an `->` and then the type before the `:`.

````{tab-set-code}
```{code-block} python
def my_function(var1: int, var2: float) -> float:
    ...
```
````
Lets apply type hinting to the `calculate_distance` function.

## Exercise - Adding type annotations to `calculate_distance`

``````{admonition} Exercise
:class: exercise 

Add type hints to the `calculate_distance` function.
Hint: our docstring specifies what types we should be using for the parameters and the output of the function.

`````{admonition} Solution
:class: solution dropdown

````{tab-set-code}
```{code-block} python
def calculate_distance(rA: np.ndarray, rB: np.ndarray) -> float:
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
    dist_vec = rA - rB
    distance = np.linalg.norm(dist_vec)
    return distance
```
````
`````
``````

## Static Type Checking

After adding the type hint annotations, you may already notice that your IDE
warns you if you try to write `calculate_distance([0, 0, 0], [0, 0.1, 0])`
(with lists instead of numpy arrays) before you even try to run the command.
If you are using Visual Studio Code and you do not have type hinting warnings,
see the "Type Checking in VS Code" section below.

You and your users can avoid a lot of bugs during development by enabling static
type checking in your editor or with a standalone tool.

- Static type checking (mypy, pyright)
- Type checking through ide (pylance, atom)

## Type Checking in VS Code

Enabling type checking through your IDE is a simple step to benefit from type hinting in python.
Pylance is an optional dependency of the Python extension for VS Code, which means it is likely already installed and just needs to be activated.

To activate Pylance, click the gear icon in the bottom left corner of VS Code and then select the "Settings" option.
In the search box at the top, type: `type checking mode`.
You should see an option labeled `Python > Analysis: Type Checking Mode` with a dropdown box underneath.
Click the dropdown box and select `basic`.
VS Code should now perform static type checking on your code.
Try and pass a set of integers into the function and you should now see a red underline under each of the integers informing you that the types are incompatible.

## More

For more complex or flexible typing, note that the abstract base classes in
[collections.abc](https://docs.python.org/3/library/collections.abc.html) can be used as `Generic` types.
The [typing](https://docs.python.org/3/library/typing.html) library includes a number of other useful types.
 * `typing.Union` specifies a set of different types that can be assigned to a variable. `Union[int, float]` indicates that either an `int` or a `float` is acceptable.
 * `typing.SupportsFloat` matches any value that is convertible to `float`.
 * `collections.abc.Iterable` matches any object that can be iterated over.
   It is a Generic class. The return value of a function annotated `-> list[int]`
   can be used in a function argument annotated `arg: Iterable[SupportsFloat]`

More information on Python's typing package can be found in the [Python documentation](https://docs.python.org/3/library/typing.html).

:::{admonition} Final Repository State
:class: tip

You can see the final state of the repository after this section [here](https://github.com/MolSSI-Education/molecool/tree/cc3e3267215f8e773caa42d4dfc3b4d64646568e).

You can also download a zip of the repository [here](https://github.com/MolSSI-Education/molecool/archive/refs/tags/python-type-hinting-end.zip).

:::

## Key Points

```{admonition} Key Points
:class: key

- Type hinting improves the readability of your code by annotating the data types of variables.
- Type hinting is used by IDEs to help discover problems before runtime.

```
