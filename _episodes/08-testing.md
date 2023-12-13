# Python Testing

````{admonition} Overview
:class: overview

Questions:
- How is a Python module tested?

Objectives:
- Explain the overall structure of testing.
- Explain the reasons why testing is important.
- Understand how to write tests using the pytest framework.
````
:::{admonition} Follow Along with This Lesson
:class: tip

To follow along with this lesson, you can complete the previous lessons,
or you can download a pre-made workshop repository that is at the starting 
point.

- [Download the pre-made workshop repository as a zip file](https://github.com/MolSSI-Education/molecool/archive/refs/tags/python-testing-start.zip)

Alternatively, download the repository using the command line:

````{tab-set-code} 
```{code-block} shell
git clone https://github.com/MolSSI-Education/molecool.git
git checkout python-testing-start
```
````
:::

Until now, we have been writing functions and checking their behavior using an interactive Python interpreter and manually inspecting the output.
While this seems to work, it can be tedious, and prone to error.
In this lesson, we'll discuss how to write tests and run them using the `pytest` testing framework.

Using a testing framework will allow us to easily define tests for all of our functions and modules, and to test these each time we make a change.
This will ensure that our code is behaving the way we expect and that we do not break any features existing in the code by making new changes.

This episode explains the importance of code testing and demonstrates the possible capabilities.

## Why testing

Software should be tested regularly throughout the development cycle to ensure correct operation.
Thorough testing is typically an afterthought, but for larger projects, it is essential to ensure changes in some parts of the code do not negatively affect other parts.

**Software testing is checking the behavior of part of the code (such as a method, class, or module) by comparing its expected output or behavior with the observed one.**
We will explain this in more detail shortly.

## Levels of Testing

There are three main levels of testing:

- **Unit tests**:
The purpose is to verify that each part of the code is functioning as expected.
Unit testing is done on smaller units (such as single functions or classes) as you work on your code.
This is helpful for catching errors in uncommonly-used parts of the code.
Unit tests should be added as new features are added, resulting in better code coverage.
In unit tests, you are testing a part of your code independent of any other factors;
therefore, you should avoid using the file system, databases, network, or any other resources unless you are testing a function directly related to that resource.

- **Integration tests**:
This is a more holistic approach where you test the interface between modules, and how they combine and integrate together.

- **System tests**:
Where you test your system as a whole to check if it meets all the requirements.

Another important type of testing is **Regression tests**.
In Regression tests, the software is checked to ensure that it consistently returns correct values given known inputs.
This kind of testing can catch problems in previously working code that may have been broken by new changes or new features.

It is highly encouraged to have Unit tests that *cover* most of your code.
It is also helpful to have some Integration and System tests.

In this lesson, we are focusing on unit testing.
The same concepts can be utilized to conduct integration tests throughout various modules.

## The pytest testing framework

MolSSI recommends using the [pytest](https://pytest.org) testing framework.
Other testing frameworks are available (such as [unittest](https://docs.python.org/3/library/unittest.html) and [nose tests](https://nose.readthedocs.io/en/latest/));
however, the combination of easy implementation, [parametrization of tests](https://docs.pytest.org/en/latest/parametrize.html),
[fixtures](https://docs.pytest.org/en/latest/fixture.html), and [test marking](https://docs.pytest.org/en/latest/example/markers.html)
make `pytest` an ideal testing framework.

If you don't have `pytest` installed, or it's not updated to version 3, install it using:
````{tab-set-code} 

```{code-block} shell
pip install -U pytest-cov
```
````


## Running our first test

When we run `pytest`, it will look for directories and files which start with `test` or `test_`.
It then looks inside those files and executes any functions that begin with the word `test_`.
This syntax lets pytest know that these functions are tests.
If these functions do not result in an error, `pytest` counts the function as passing.
If an error occurs, the test fails.

CookieCutter has already created a test for us. Let's examine this file.
In a text editor, open `molecool/tests/test_molecool.py`.

````{tab-set-code} 

```{code-block} python
"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import sys

def test_molecool_imported:
    """Sample test, will always pass so long as import statement worked"""
    assert "molecool" in sys.modules
```
````


This file begins with `test_`, and contains a single function `test_molecool`.
This module will import our package, then it checks to see if it has been imported correctly by checking if the package name is in the list of imported modules.

The last line, containing the Python keyword `assert`, is called an assertion.
Assertions are used to check the behavior of the code during runtime.
The `assert` keyword halts code execution instantly if the comparison is `False`, and does nothing if the comparison is `True`.
Remember that pytest counts a test as passing if no error occurs while it is being run.

We can see if this function works by running `pytest` in our terminal.
In the top level of your package, run the following command.

````{tab-set-code} 

```{code-block} shell
pytest
```
````


You should see an output similar to the following.

````{tab-set-code} 

```{code-block} output
============================= test session starts ==============================
platform darwin -- Python 3.11.6, pytest-7.4.2, pluggy-1.3.0
rootdir: /Users/jessica/dev/molecool, inifile:
collected 1 item

molecool/tests/test_molecool.py .                    [100%]

=========================== 1 passed in 0.06 seconds ===========================
```
````


Here, `pytest` has looked through our directory and its subdirectories for anything matching `test*`.
If the `tests` folder exists, the code locates the `test_molecool.py` file within it and executes the `test_molecool_imported` function present within the module.
Since our `assertion` was `True`, our test did not result in an error and the test passed.

We can see the names of the tests `pytest` ran by adding a `-v` tag to the pytest command.

````{tab-set-code} 

```{code-block} shell
pytest -v
```
````


Using the command argument `-v` will result in pytest listing which tests are executed and whether they pass or not.
There are a number of additional command line arguments to [explore](https://docs.pytest.org/en/latest/usage.html).

````{tab-set-code} 

```{code-block} output
============================= test session starts ==============================
platform darwin -- Python 3.11.6, pytest-7.4.2, pluggy-1.3.0 -- /Users/jessica/miniconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/jessica/dev/molecool, inifile:
collected 1 item

molecool/tests/test_molecool.py::test_molecool_imported PASSED [100%]

=========================== 1 passed in 0.06 seconds ===========================
```
````


Now we see that `pytest` displays the test name for us, as well as `PASSED` next to the test name.

### Adding tests to our package

We will now add tests to test our functions.
After dividing our package into modules, we have four modules and one subpackage.
It is considered good practice to also break your tests into different files depending on the module or subpackage.

Create a new file called `test_measure.py` in the `tests` directory with the following contents.

````{tab-set-code} 

```{code-block} python
"""
Unit and regression test for the measure module.
"""

# Import package, test suite, and other packages as needed
import molecool
import numpy as np

def test_calculate_distance():
    """Test that calculate_distance function calculates what we expect."""
    
    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance
```
````


We have written one test in this file.
In our test function `test_calculate_distance`, we have defined two points.
We know that these points should be at a distance of 1 from one another.

Run this test using `pytest`. In the terminal window, type

````{tab-set-code} 

```{code-block} shell
pytest -v
```
````


You should now see an output similar to the following:

````{tab-set-code} 

```{code-block} output
============================================================ test session starts ============================================================
platform darwin -- Python 3.11.6, pytest-7.4.2, pluggy-1.3.0
rootdir: /Users/jessica/lessons/molecool
collected 2 items

molecool/tests/test_molecool.py::test_molecool_imported PASSED [ 50%]
molecool/tests/test_measure.py::test_calculate_distance PASSED           [100%]

=========================== 2 passed in 0.07 seconds ===========================
```
````


Now we can see that two tests have been run and both have passed.
This means that our calculated distance was equal to what we set as the expected distance, and the assertion did not fail.

### Failing tests
Let's see what happens when one of the tests fails.

If a test fails, Pytest will provide detailed output by analyzing the objects at runtime to discover the error. 
To rerun the test, you can change the value of the `expected` variable in your test function to `2`.

````{tab-set-code} 

```{code-block} shell
pytest -v
```
````


````{tab-set-code} 

```{code-block} output
============================================================ test session starts ============================================================
platform darwin -- Python 3.11.6, pytest-7.4.2, pluggy-1.3.0
rootdir: /Users/jessica/lessons/molecool
collected 2 items

molecool/tests/test_molecool.py::test_molecool_imported PASSED [ 50%]
molecool/tests/test_measure.py::test_calculate_distance FAILED           [100%]

=========================== 2 passed in 0.07 seconds ===========================

================================================================== FAILURES ===================================================================
___________________________________________________________ test_calculate_distance ___________________________________________________________

    def test_calculate_distance():
        """Test the calculate_distance function"""
    
        r1 = np.array([0, 0, 0])
        r2 = np.array([0, 1, 0])
    
        expected_distance = 2
    
        calculated_distance = molecool.calculate_distance(r1, r2)
    
>       assert expected_distance == calculated_distance
E       assert 2 == 1.0

molecool/tests/test_measure.py:26: AssertionError
======================================================== 1 failed, 1 passed in 0.56s =========================================================
```
````

Pytest displays a detailed failure report which includes the source code surrounding the line that failed. 
The failed line is marked with `>`. Additionally, it displays the values used in the assert comparison at runtime, such as `2 == 1.0`. 
This runtime analysis is one of the advantages of pytest, which can help you with debugging your code.

``````{admonition} Check Your Understanding
:class: exercise

What happens if you leave your `expected_value` equal to 2, but remove the assertion?

`````{admonition} Solution
:class: solution dropdown

If you remove the word `assert`, you should notice that your test still passes.
This is because the expression is being evaluated as `False`. However, since there was no Assertion, there was no error.

Since there was no error, pytest counted it as a passing test.
The `assert` statement causes an error when it evaluates to False.
It's very important to remember that `pytest` counts a test as failing when some type of exception occurs.
You could also do something like the following to make your test fail:

```python
def test_calculate_distance():
    """Test that calculate distance function calculates what we expect"""

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 2

    calculated_distance = molecool.calculate_distance(r1, r2)

    if expected_distance != calculated_distance:
        raise Exception("My test will fail!")
```

You can see that an `AssertionError` is easier than something like this :)
`````
``````

Change the expected value back to 1 so that your tests pass and make sure you have the `assert` statement.

### Exercise - `calculate_angle` test

``````{admonition} Exericse
:class: exercise

Create a test for the `calculate_angle` function. Use the three points

```python
r1 = np.array([0, 0, -1])
r2 = np.array([0, 0, 0])
r3 = np.array([1, 0, 0])
```

These three points correspond to an angle of 90 degrees.

Verify that your test is working by running pytest.
You should now see three passing tests.

`````{admonition} Solution
:class: solution dropdown

Since `calculate_angle` is in the `measure` module, the tests for this function should go in the same file as `calculate_distance`.
You should define a new function in `test_measure` called `test_calculate_angle`.
```python
def test_calculate_angle():
   """Test the calculate_angle function"""

   r1 = np.array([1, 0, 0])
   r2 = np.array([0, 0, 0])
   r3 = np.array([0, 1, 0])

   expected_value = 90

   calculated_value = molecool.calculate_angle(r1, r2, r3, degrees=True)
   assert expected_value == calculated_value

```
````
``````
Let's also make a test for the `build_bond_list` function.
We start with creating `test_molecule.py`, and then defining the test inside that file.

We must have some coordinates to test.
In our Jupyter Notebook, we were reading this data from an xyz file.
However, remember that for unit tests, we do not want to make our test dependent on any other functions.
Therefore, we will just make up some coordinates in our test.

Next, there are several things we might test about this function.
We could check that we find the correct number of bonds and that those bonds are of the correct length.
You should write at least one test per function, but you may have multiple assertions in the same test.
For example, we could write the following test for `build_bond_list`.

````{tab-set-code} 

```{code-block} python
def test_build_bond_list():

    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4],
    ])

    bonds = molecool.build_bond_list(coordinates)

    assert len(bonds) == 4

    for bond_length in bonds.values():
        assert bond_length == 1.4
```
````


Here, we assert the correct number of bonds and iterate through the dictionary to ensure a 1.4 Angstrom distance for each bond.

## Testing Expected Exceptions

If you expect your code to raise exceptions, you can test this behavior with pytest.
For example in our `calculate_angle` function, our inputs must be numpy arrays, or the function will give an error.

Consider our `build_bond_list` function. We may want to raise a `ValueError` if `min_bond` is set to be less than zero.
We can add a type check to the function so that a more informative message is given to the user.

Add the following to your `build_bond_list` function right below the docstring.

````{tab-set-code} 

```{code-block} python
if min_bond < 0:
        raise ValueError("Invalid minimum bond distance entered! Minimum bond distance must be greater than zero!")
```
````


We can test that this `ValueError` is raised in our testing functions.

In the `test_molecule.py` file, copy and modify your first test to check for this.
Note that you must alter your imports to also `import pytest`.

````{tab-set-code} 

```{code-block} test_molecule.py
import pytest

def test_build_bond_failure():

    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4],
    ])

    with pytest.raises(ValueError):
        bonds = molecool.build_bond_list(coordinates, min_bond=-1)
```
````


The test will pass if the `build_bond_list` method raises a `ValueError`, otherwise, the test will fail.

## Exercise - Test Driven Development

Sometimes, tests are written before writing the code. 
This is called "Test Driven Development" or TDD.
In this case, you would first write tests that define the behavior of your code, then run these tests to see if they pass, and finally write code to pass each of these tests.
TDD is a common approach when developing a library with well-defined interfaces and features.

TDD has another benefit of never having false positives.
If you ensure that your tests first fail and THEN pass, you know that you have written a function that works and that your test is not just passing by default.


``````{admonition} Exercise 1
:class: exercise

For this homework assignment, you are given a function specification and a test.
You should write a function to make the test pass.

Add the following function definition and docstring to `molecule.py`.

````{tab-set-code} 

```{code-block} python
def calculate_molecular_mass(symbols):
    """Calculate the mass of a molecule.
    
    Parameters
    ----------
    symbols : list
        A list of elements.
    
    Returns
    -------
    mass : float
        The mass of the molecule
    """
    pass
```
````

This defines a function, its inputs, and what the function should return.
Next, add  the following test into `test_molecule.py`.

````{tab-set-code}
```{code-block} test_molecule.py
def test_molecular_mass():
    symbols = ['C', 'H', 'H', 'H', 'H']
    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass
```
````

If you run `pytest`, this test should fail.
Your assignment is to write the function to make the tests pass.
You should use the `atomic_weights` data in the `atom_data` module.

`````{admonition} Solution
:class: solution dropdown

Here is a potential solution. 

```python
from .atom_data import atomic_weights


def calculate_molecular_mass(symbols):
    """Calculate the mass of a molecule.
    
    Parameters
    ----------
    symbols : list
        A list of elements.
    
    Returns
    -------
    mass : float
        The mass of the molecule
    """

    mass = 0
    for atom in symbols:
        mass += atomic_weights[atom]
    
    return mass
```

Also, don't forget to add the `calculate_molecular_mass` function to `__init__.py`

````{tab-set-code}
```{code-block} __init__.py
# Add imports here
from .measure import calculate_distance, calculate_angle
from .molecule import build_bond_list, calculate_molecular_mass
from .visualize import draw_molecule, bond_histogram
from .io import open_pdb, open_xyz, write_xyz
```
````
`````
``````

``````{admonition} Exercise 2
:class: exercise

Consider the following function definition inside the `molecule` module.

````{tab-set-code}
```{code-block} molecule.py
import numpy as np

def calculate_center_of_mass(symbols, coordinates):
    """Calculate the center of mass of a molecule.
    
    The center of mass is weighted by each atom's weight.
    
    Parameters
    ----------
    symbols : list
        A list of elements for the molecule
    coordinates : np.ndarray
        The coordinates of the molecule.
    
    Returns
    -------
    center_of_mass: np.ndarray
        The center of mass of the molecule.
    
    Notes
    -----
    The center of mass is calculated with the formula
    
    .. math:: \\vec{R}=\\frac{1}{M} \\sum_{i=1}^{n} m_{i}\\vec{r_{}i}
    
    """
    
    return np.array([])
```
````

Don't forget to add the `calculate_center_of_mass` function to `__init__.py`

````{tab-set-code}
```{code-block} __init__.py
# Add imports here
from .measure import calculate_distance, calculate_angle
from .molecule import build_bond_list, calculate_molecular_mass, calculate_center_of_mass
from .visualize import draw_molecule, bond_histogram
from .io import open_pdb, open_xyz, write_xyz
```
````

And the test for the function above.

````{tab-set-code}
```{code-block} test_molecule.py
def test_center_of_mass():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])

    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1,1,1])

    assert center_of_mass.all() == expected_center.all()
```
````

Notice that this test always passes.
Even if we were to write our function, we would not know it was right.

Fix this test so that it fails.
**Hint** - You will have to compare two arrays (look into numpy functions which compare two arrays.)

`````{admonition} Solution
:class: solution dropdown

The problem with `.all()` is that it does not compare arrays element-wise, it simply evaluates as True if all values in the array are True, or False if not.
The numpy function `array_equal` returns True if two arrays have the same shape and elements.

```python
def test_center_of_mass():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])

    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1,1,1])

    assert np.array_equal(center_of_mass, expected_center)
```

Below is an implementation of the function which meets the specification outlined by the test.

```python
def calculate_center_of_mass(symbols, coordinates):
    """Calculate the center of mass of a molecule.
    
    The center of mass is weighted by each atom's weight.
    
    Parameters
    ----------
    symbols : list
        A list of elements for the molecule
    coordinates : np.ndarray
        The coordinates of the molecule.
    
    Returns
    -------
    center_of_mass: np.ndarray
        The center of mass of the molecule.
    
    Notes
    -----
    The center of mass is calculated with the formula
    
    .. math:: \\vec{R}=\\frac{1}{M} \\sum_{i=1}^{n} m_{i}\\vec{r_{}i}
    
    """
    
    total_mass = calculate_molecular_mass(symbols)
    
    mass_array = np.zeros([len(symbols), 1])
    
    for i in range(len(symbols)):
        mass_array[i] = atomic_weights[symbols[i]]
    
    center_of_mass = sum(coordinates * mass_array) / total_mass
    
    return center_of_mass
```
`````
``````

## Advanced features of pytest

````{admonition} Python Decorators
:class: note

Some of pytest's advanced features make use of decorators.
Decorators are a very powerful tool in programming, which we will not explore in depth here.
You can think of them as functions that act on other functions.
To decorate a particular function, you write the name of the decorator, preceded by `@`, in the line above the `def` statement:
```python
@decorator
def foo():
    pass
```
````

### Pytest Marks
Pytest marks allow you to mark your functions.
There are built-in marks for pytest and you can also define your own marks.
Marks are implemented using decorators.
One of the built-in marks in pytest is `@pytest.mark.skip`.
To use this mark we have to import pytest.
Then modify your `test_calculate_distance` function to use this mark.

````{tab-set-code}
```{code-block} test_measure.py
import pytest

@pytest.mark.skip
def test_calculate_distance():
    """Test that calculate distance function calculates what we expect"""

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance
```
````


When you run your tests, you will see that this test is now skipped:

````{tab-set-code} 

```{code-block} output
molecool/tests/test_measure.py::test_calculate_distance SKIPPED
```
````


You might also use the `pytest.mark.xfail` if you expect a test to fail.

You can also define your own marks.
Let's consider if some of our tests were slow or took a long time.
Maybe we would not want to run these tests every time.
We could add our own mark:

````{tab-set-code} 

```{code-block} test_measure.py
@pytest.mark.slow
def test_calculate_distance():
    """Test that calculate distance function calculates what we expect"""

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance
```
````


We could then run the slow tests only using the `-m` argument on the command line:

````{tab-set-code} 

```{code-block} shell
pytest -v -m "slow"
```
````


Or, you could choose to skip the slow tests:

````{tab-set-code} 

```{code-block} shell
pytest -v -m "not slow"
```
````



### Pytest Fixtures

In your `test_molecule` module, you may have noticed that you kept having to create coordinates and symbols over and over again in each test.
For this particular case, you could use a global variable, but a better approach is to create something called a `pytest fixture`. 

Fixtures are resources that tests can repeatedly request to use.
Fixtures can be used for dependency injection (a way of passing or supplying resources from one object to another) which helps to decouple the code and make it cleaner.

To use fixtures, we need to import `pytest` and use the `@pytest.fixture` decorator.
Fixtures can be defined as methods, where the name of the method is the name of this resource, and the returned data is its value.

````{tab-set-code} 

```{code-block} test_molecule.py
@pytest.fixture
def methane_molecule():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4],
    ])
    
    return symbols, coordinates
```
````


We defined a fixture named `methane_molecule` which has symbols and coordinates.
Now, any test method can request this fixture by adding its name to its input argument.
For example, our `test_molecular_mass` function becomes.

````{tab-set-code} 

```{code-block} test_molecule.py
def test_molecular_mass(methane_molecule):
    symbols, coordinates = methane_molecule
    
    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass
```
````

After filling in your fixture to other tests, your `test_molecule.py` file should look something like this.

````{tab-set-code} 

```{code-block} test_molecule.py
"""
Testing for molecule module
"""

import molecool
import pytest
import sys

import numpy as np
import os

@pytest.fixture
def methane_molecule():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4],
    ])
    
    return symbols, coordinates

def test_build_bond_list(methane_molecule):
    symbols, coordinates = methane_molecule

    bonds = molecool.build_bond_list(coordinates)

    assert len(bonds) == 4

    for atoms, bonds in bonds.items():
        assert bonds == 1.4

def test_molecular_mass(methane_molecule):
    symbols, coordinates = methane_molecule
    
    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass

def test_build_bond_list_failure(methane_molecule):
    symbols, coordinates = methane_molecule
    
    with pytest.raises(ValueError):
        molecool.build_bond_list(coordinates, min_bond=-1)

def test_center_of_mass(methane_molecule):
    symbols, coordinates = methane_molecule

    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1,1,1])
    
    assert np.array_equal(center_of_mass, expected_center)
```
````


#### Fixture Scope

By default, the fixture has the scope of "function".
This means a new object is created for each test function.
For example, consider adding the following test which moves the carbon atom in our methane molecule.

````{tab-set-code} 

```{code-block} test_molecule.py
def test_move_methane(methane_molecule):
    symbols, coordinates = methane_molecule

    coordinates[0] += 5
```
````


Once you run your tests, you will notice that all the tests pass without any errors.

If you have an "expensive" fixture (one that takes a lot of time to generate), you may want to change this so that the fixture is created fewer times.
You can do this by adding the `scope` argument to the fixture.
One scope we might pick is `module`, meaning that a new fixture will be created for each testing module rather than for each testing function.

````{tab-set-code} 

```{code-block} test_molecule.py
@pytest.fixture(scope="module")
def methane_molecule():
    symbols = np.array(['C', 'H', 'H', 'H'])
    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4],
    ])

    return symbols, coordinates
```
````


Notice that when you run your tests now, the `test_build_bond_list` will fail.
This is because the `test_move_methane` moved the carbon atom, and since the scope was set to `module`, the atom remained moved for the subsequent tests. 

The `scope` keyword can be helpful for saving time, however, be aware if you are changing properties of the fixture in other tests!

````{admonition} Using fixtures across different test files
:class: tip

If you realize while implementing your tests that a fixture function needs to be used in multiple test files, you can move it to a conftest.py file,
 and you don't need to import it in the test as it will be automatically discovered by pytest.
 For further information, please refer to [this article](https://www.tutorialspoint.com/pytest/pytest_conftest_py.htm).
Read more about this [here](https://www.tutorialspoint.com/pytest/pytest_conftest_py.htm).
````

### Pytest Parametrize

For some of our functions like `calculate_distance` or `calculate_angle`, we have only tested one measurement so far.
This is not complete, and we may be missing testing edge cases.
You may think of writing another test where you change the values that you can input into the calculation.
This is definitely something you can do, and `pytest` has a feature that makes it easy to run a test with multiple inputs/values - the `parametrize` mark.

````{admonition} Edge and Corner Cases
:class: note

### Edge cases
The situation where the test examines either the beginning or the end of a range, but not the middle, is called an edge case.
In a simple, one-dimensional problem, the two edge cases should always be tested along with at least one internal point.
This ensures that you have good coverage over the range of values.

Anecdotally, testing the edge cases is crucial since this is where errors often arise.
Boundaries exhibit qualitatively distinct behavior, which is why they usually have a dedicated code in the implementation.

### Corner cases
When two or more edge cases are combined, it is called a corner case.
If a function is parametrized by two linear and independent variables, a test at the extreme of both variables is in a corner.
````


The syntax for the `pytest.mark.parametrize` decorator is:

````{tab-set-code} 

```{code-block} python
@pytest.mark.parametrize("variable_name1, variable_name2, ...variable_nameN, expected_answer", [
    (variable_value1, variable_value2, ...variable_valueN, expected_answer_value),
    (variable_value1, variable_value2, ...variable_valueN, expected_answer_value), ...
])
def test_name(variable_name1, variable_name2, ... variable_nameN, expected_answer):
```
````


Where each line in the middle (in parentheses) gives a set of values for the test.
Then, these variables are passed to the test written under the decorator.

For example, for testing our `calculate_angle` function, we might test several angles at one time.

````{tab-set-code} 

```{code-block} test_measure.py
@pytest.mark.parametrize("p1, p2, p3, expected_angle", [
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 45),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60  ),
    (np.array([np.sqrt(3)/2, (1/2), 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 30),
])
def test_calculate_angle_many(p1, p2, p3, expected_angle):

    calculated_angle = molecool.calculate_angle(p1, p2, p3, degrees=True)

    assert expected_angle == pytest.approx(calculated_angle), F'{calculated_angle} {expected_angle}'
```
````


Run these tests, but this time add another special option to pytest `-k` which allows you to specify the name of the test you want to run.

````{tab-set-code} 

```{code-block} shell
pytest -v -k "test_calculate_angle_many"
```
````


````{tab-set-code} 

```{code-block} output
============================================================= test session starts =============================================================
platform darwin -- Python 3.11.6, pytest-7.4.2, pluggy-1.3.0 -- /Users/jessica/miniconda3/envs/molecool/bin/python
cachedir: .pytest_cache
rootdir: /Users/jessica/lessons/molecool
collected 14 items / 11 deselected / 3 selected                                                                                               

molecool/tests/test_measure.py::test_calculate_angle_many[p10-p20-p30-45] PASSED                                                        [ 33%]
molecool/tests/test_measure.py::test_calculate_angle_many[p11-p21-p31-60] PASSED                                                        [ 66%]
molecool/tests/test_measure.py::test_calculate_angle_many[p12-p22-p32-30] PASSED                                                        [100%]

====================================================== 3 passed, 7 deselected in 0.44s =======================================================
```
````


Running this test resulted in three different tests with three different values.

#### Combining multiple parameters

To get all combinations of multiple parametrized arguments you can stack parametrize decorators:

````{tab-set-code} 

```{code-block} python
import pytest
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    pass
```
````


This will run the test with the arguments set to x=0/y=2, x=1/y=2, x=0/y=3, and x=1/y=3 exhausting parameters in the order of the decorators.

### Testing Documentation Examples
As our package changes over time, we want to make sure that the examples in our docstrings still behave as originally written, but checking these by hand can be a real pain.
Luckily, `pytest` has a feature that will look for examples in docstrings and run them as tests.

`pytest` searches the docstrings for the Python shell code, which it executes and compares to the outputs in the docstring.
For example, in the docstring of our function `calculate_distance` we have:

````{tab-set-code} 

```{code-block} python
>>> r1 = np.array([0, 0, 0])
>>> r2 = np.array([0, 0.1, 0])
>>> calculate_distance(r1, r2)
0.1
```
````


`pytest` will find and execute this code (indicated by `>>>`).
If the output is not `0.1`, `pytest` will treat the example test as a failure.

We can test docstrings by adding the option `--doctest-modules`.
If you are in the top level of your project, you will have to also give the name of the project folder (which is `molecool`) after the option.
````{tab-set-code} 

```{code-block} shell
pytest -v --doctest-modules molecool
```
````


````{tab-set-code} 

```{code-block} output
=========================================================================== test session starts ===========================================================================
platform darwin -- Python 3.11.6, pytest-7.4.2, pluggy-1.3.0 -- /Users/jessica/miniconda3/envs/molecool/bin/python
cachedir: .pytest_cache
rootdir: /Users/jessica/lessons/molecool
collected 11 items                                                                                                                                                        

molecool/measure.py::molecool.measure.calculate_distance PASSED                                                                                                     [  9%]
molecool/tests/test_measure.py::test_molecool_imported PASSED                                                                                                       [ 18%]
molecool/tests/test_measure.py::test_calculate_distance PASSED                                                                                                      [ 27%]
molecool/tests/test_measure.py::test_calculate_angle_90 PASSED                                                                                                      [ 36%]
molecool/tests/test_measure.py::test_calculate_angle_many[p10-p20-p30-45] PASSED                                                                                    [ 45%]
molecool/tests/test_measure.py::test_calculate_angle_many[p11-p21-p31-60] PASSED                                                                                    [ 54%]
molecool/tests/test_measure.py::test_calculate_angle_many[p12-p22-p32-30] PASSED                                                                                    [ 63%]
molecool/tests/test_molecule.py::test_build_bond_list_default PASSED                                                                                                [ 72%]
molecool/tests/test_molecule.py::test_molecular_mass PASSED                                                                                                         [ 81%]
molecool/tests/test_molecule.py::test_build_bond_list_failure PASSED                                                                                                [ 90%]
molecool/tests/test_molecule.py::test_center_of_mass PASSED                                                                                                         [100%]

=========================================================================== 11 passed in 0.42s ============================================================================
```
````


The first test run is now a test of the docstring for the `calculate_distance` function.


Change the expected answer to 0.2 in the docstring and re-run the test to get the following error:

````{tab-set-code} 

```{code-block} output
=========================================================================== test session starts ===========================================================================
platform darwin -- Python 3.11.6, pytest-7.4.2, pluggy-1.3.0 -- /Users/jessica/miniconda3/envs/molecool/bin/python
cachedir: .pytest_cache
rootdir: /Users/jessica/lessons/molecool
collected 11 items                                                                                                                                                        

molecool/measure.py::molecool.measure.calculate_distance FAILED                                                                                                     [  9%]
molecool/tests/test_measure.py::test_molecool_imported PASSED                                                                                                       [ 18%]
molecool/tests/test_measure.py::test_calculate_distance PASSED                                                                                                      [ 27%]
molecool/tests/test_measure.py::test_calculate_angle_90 PASSED                                                                                                      [ 36%]
molecool/tests/test_measure.py::test_calculate_angle_many[p10-p20-p30-45] PASSED                                                                                    [ 45%]
molecool/tests/test_measure.py::test_calculate_angle_many[p11-p21-p31-60] PASSED                                                                                    [ 54%]
molecool/tests/test_measure.py::test_calculate_angle_many[p12-p22-p32-30] PASSED                                                                                    [ 63%]
molecool/tests/test_molecule.py::test_build_bond_list_default PASSED                                                                                                [ 72%]
molecool/tests/test_molecule.py::test_molecular_mass PASSED                                                                                                         [ 81%]
molecool/tests/test_molecule.py::test_build_bond_list_failure PASSED                                                                                                [ 90%]
molecool/tests/test_molecule.py::test_center_of_mass PASSED                                                                                                         [100%]

================================================================================ FAILURES =================================================================================
______________________________________________________________ [doctest] molecool.measure.calculate_distance ______________________________________________________________
015     Returns
016     -------
017     distance : float
018         The distance between the two points.
019     
020     Examples
021     --------
022     >>> r1 = np.array([0, 0, 0])
023     >>> r2 = np.array([0, 0.1, 0])
024     >>> calculate_distance(r1, r2)
Expected:
    0.2
Got:
    0.1

/Users/jessica/lessons/molecool/molecool/measure.py:24: DocTestFailure
====================================================================== 1 failed, 10 passed in 0.41s =======================================================================
```
````


## Code Coverage Part I

Now that we have a set of modules and associated tests, we want to see how much of our package is "covered" by our tests.
We'll measure this by counting the lines of our packages that are touched, i.e. used, during our tests.

We already have everything we need for this since we installed `pytest-cov` earlier which includes the coverage tools on top of the `pytest` package.

We can assess our code coverage as follows:

````{tab-set-code} 

```{code-block} shell
pytest --cov=molecool
```
````


````{tab-set-code} 

```{code-block} output
=========================================================================== test session starts ===========================================================================
platform darwin -- Python 3.11.6, pytest-7.4.2, pluggy-1.3.0
rootdir: /Users/jessica/lessons/molecool
plugins: cov-2.8.1
collected 10 items                                                                                                                                                        

molecool/tests/test_measure.py ......                                                                                                                               [ 60%]
molecool/tests/test_molecule.py ....                                                                                                                                [100%]

---------- coverage: platform darwin, Python 3.11.6-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
molecool/__init__.py          9      0   100%
molecool/atom_data.py         2      0   100%
molecool/io/__init__.py       2      0   100%
molecool/io/pdb.py           14     12    14%
molecool/io/xyz.py           14     11    21%
molecool/measure.py          12      1    92%
molecool/molecule.py         28      1    96%
molecool/visualize.py        33     28    15%
---------------------------------------------
TOTAL                       114     53    54%


=========================================================================== 10 passed in 0.70s ============================================================================
```
````


The output shows how many statements (i.e. not comments) are in a file, how many weren't executed during testing, and the percentage of statements that were.

To improve our coverage, we also want to see exactly which lines we missed and we can determine this using the `.coverage` file produced by `pytest`.
Unfortunately, this strategy becomes impractical when we are working with anything larger than our test package because the `.coverage` file becomes too convoluted to read.
We will need more tools to help us determine how to improve our tests and that will be the subject of Code Coverage Part II, which we will cover later in the workshop.

```{admonition} Do we need to get 100% coverage?
:class: attention

Short answer: __no__.
Code coverage is a useful tool to assess how comprehensive are our set of tests, and in general the higher our code coverage the better.
__However__, trying to achieve 100% coverage on packages any larger than this sample package is a bit unrealistic and would require more time than that last bit of coverage is worth.
```

:::{admonition} Final Repository State
:class: tip

You can see the final state of the repository after this section [here](https://github.com/MolSSI-Education/molecool/tree/7025c726eee958f0ad6b302e9f1118a7a9cadb36).

You can also download a zip of the repository [here](https://github.com/MolSSI-Education/molecool/archive/refs/tags/python-testing-end.zip).

:::


## Key Points
````{admonition} Key Points
:class: key

- A good set of tests covers individual functions/features __and__ behavior of the software as a whole.
- It's better to write tests during development so you can check your progress along the way.
````
