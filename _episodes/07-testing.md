---
title: "Python Testing"
teaching: 60
exercises: 10
questions:
- "How is a Python module tested?"
objectives:
- "Explain the overall structure of testing."
- "Explain the reasons why testing is important."
- "Understand how to write tests using the pytest framework."
keypoints:
- "A good set of tests covers individual functions/features __and__ behavior of the software as a whole."
- "It's better to write tests during development so you can check your progress along the way. The longer you wait to start the harder it is."
- "Try to test as much of your package as you can, but don't go overboard, most packages don't have 100% test coverage."
---

Until now, we have been writing functions and checking their behavior using an interactive Python interpreter and manually inspecting the output. While this seems to work, it can be tedious, and prone to error. In this lesson, we'll discuss how to write tests and run them using the `pytest` testing framework.

Using a testing framework will allow us to easily define tests for all of our functions and modules, and to test these each time we make a change. This will ensure that our code is behaving the way we expect, and that we do not break any features existing in the code by making new changes.

This episode explains the importance of code testing and demonstrates the possible capabilities.

## Why testing

Software should be tested regularly throughout the development cycle to ensure correct operation. Thorough testing is typically an afterthought, but for larger projects, it is essential for ensuring changes in some parts of the code do not negatively affect other parts.

**Software testing is checking the behavior of part of the code (such as a method, class, or a module) by comparing its expected output or behavior with the observed one.** We will explain this in more detail shortly.

## Unit vs Regression vs Integration testing

There are three main levels of testing:

- **Unit tests**: the purpose is to verify that each part of the code is functioning as expected.
Unit testing is done on smaller units (such as single functions or classes) as you work on
your code.
This is helpful for catching errors in uncommonly-used parts of the code. Unit tests should
be added as new features are added, resulting in better code coverage.
In unit tests, you are testing a part of your code independent of any other factors;
therefore, you should avoid using the file system, databases, network, or any other
resources unless you are testing a function directly related to that resource.

- **Integration tests**: this is a more holistic approach where you test the interface
between modules, and how they combine and integrate together.

- **System tests**: where you test your system as a whole to check if meets all the
requirements.

Another important type of testing is **Regression tests**. In Regression tests,
given a known input, does the software correctly and consistently return the correct
values? This kind of testing can catch problems in previously working code that may has been broken by new changes or new features.

It is highly encouraged to have Unit tests that *cover* most of your code. It is
also helpful to have some Integration and System tests.

In this lesson, we are focusing on unit testing.
Same concepts here can be applied to perform Integration tests across modules.

## The pytest testing framework

MolSSI recommends using the [pytest](https://pytest.org) testing framework.
Other testing frameworks are available (such as unittest and nose tests);
however, the combination of easy implementation, [parametrization of tests](https://docs.pytest.org/en/latest/parametrize.html),
[fixtures](https://docs.pytest.org/en/latest/fixture.html), and [test marking](https://docs.pytest.org/en/latest/example/markers.html)
make `pytest` an ideal testing framework.

If you don't have `pytest` installed or it's not updated to version 3, install it using:
~~~
$ pip install -U pytest-cov
~~~
{: .bash}

### Running our first test

When we run `pytest`, it will look for directories and files which start with `test` or `test_`. It then looks inside of those files and executes and functions that begin with the word `test_`. This syntax lets pytest know that these functions are tests. If these functions do not result in an error, `pytest` counts the function as passing. If an error occurs, the test fails.

CookieCutter has already created a test for us. Let's examine this file. In a text editor, open `molecool/tests/test_molecool.py`.

~~~
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
~~~
{: .language-python}

This file begins with `test_`, and contains a single function `test_molecool`. This module will import our package, then checks to see if it has been imported correctly by checking if the package name is in the list of imported modules.

The last line, containing the python keyword `assert`, is called an assertion. Assertions are used to check the behavior of the code during runtime. The `assert` keyword halts code execution instantly if the comparison is `False`, and does nothing if the comparison is `True`. Remember that pytest counts a test as passing if no error occurs while it is being run.

We can see if this function works by running `pytest` in our terminal. In the top level of your package, run the following command.

~~~
$ pytest
~~~
{: .language-bash}

You should see an output similar to the following.

~~~
============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-3.6.4, py-1.5.4, pluggy-0.6.0
rootdir: /Users/jessica/dev/molssi_devops, inifile:
collected 1 item

molecool/tests/test_molecool.py .                    [100%]

=========================== 1 passed in 0.06 seconds ===========================
~~~
{: .output}

Here, `pytest` has looked through our directory and its subdirectories for anything matching `test*`. It found the `tests` folder, and within that folder, it found the file `test_functions.py`. It then executed the function `test_molecool_imported` within that module. Since our `assertion` was `True`, the test passed.

We can see the names of the tests `pytest` ran by adding a `-v` tag to the pytest command.

~~~
$ pytest -v
~~~
{: .language-bash}

Using the command argument ` -v` will result in pytest, listing which tests are executed and whether they pass or not. There are a number of
additional command line arguments to [explore](https://docs.pytest.org/en/latest/usage.html).

~~~
============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-3.6.4, py-1.5.4, pluggy-0.6.0 -- /Users/jessica/miniconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/jessica/dev/molssi_devops, inifile:
collected 1 item

molecool/tests/test_molecool.py::test_molecool_imported PASSED [100%]

=========================== 1 passed in 0.06 seconds ===========================
~~~
{: .output}

Now we see that `pytest` dsiplays the test name for us, as well as `PASSED` next to the test name.

## Testing our functions

We will now add tests to test our functions. After dividing our package into modules, we have four modules and one subpackage. It is considered good practices to also break your tests into different files depending on the module or subpackage.

Create a new file called `test_measure.py` in the `tests` directory with the following contents.

~~~
"""
Unit and regression test for the measure module.
"""

# Import package, test suite, and other packages as needed
import molssi_devops
import pytest
import sys

def test_calculate_distance():
    """Test that calculate_distance function calculates what we expect."""
    
    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance
~~~
{: .language-python}

We have written one test in this file. In our test function `test_calculate_distance`, we defined two points. We know that these points should be a distance of 1 from one another.

Run this test using `pytest`. In the terminal window, type

~~~
pytest -v
~~~
{: .language-bash}

You should now see an output similar to the following

~~~
============================================================ test session starts ============================================================
platform darwin -- Python 3.7.3, pytest-5.2.1, py-1.8.0, pluggy-0.13.0
rootdir: /Users/jessica/lessons/molecool
collected 2 items

molssi_devops/tests/test_molecool.py::test_molecool_imported PASSED [ 50%]
molssi_devops/tests/test_measure.py::test_calculate_distance PASSED           [100%]

=========================== 2 passed in 0.07 seconds ===========================
~~~
{: .output}

We now see that we have two tests which have been run, and they both passed. This means that our calculated distance was equal to what we set as the expected distance, and the assertion did not fail.

### Failing tests
Let's see what happens when one of the test fails.

In case of test failure, Pytest will show detailed output from doing its own analysis to discover the error by inspecting your objects at runtime. Change the value of the `expected` variable in your test function to `2` and rerun the test.

~~~
$ pytest -v
~~~
{: .language-bash}

~~~
============================================================ test session starts ============================================================
platform darwin -- Python 3.7.3, pytest-5.2.1, py-1.8.0, pluggy-0.13.0
rootdir: /Users/jessica/lessons/molecool
collected 2 items

molssi_devops/tests/test_molecool.py::test_molecool_imported PASSED [ 50%]
molssi_devops/tests/test_measure.py::test_calculate_distance FAILED           [100%]

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
~~~
{: .output}

Pytest shows a detailed failure report, including the source code around the failing line. The line that failed is marked with `>`.
Next, it shows the values used in the assert comparison at runtime, that is `2 == 1.0`. This runtime analysis is one of the advantages of pytest that help you debug your code.

> ## Check Your Understanding
> What happens if you leave your `expected_value` equal to 2, but remove the assertion? Change your assertion line to the following
> ~~~
> expected_distance == calculated_distance
> ~~~
> {: .language-python}
>  
>  -
>> ## Answer
>> If you remove the word `assert`, you should notice that your test still passes. This is because the expression evaluated to `False`, but since there was no Assertion, there was no error. Since there was no error, the pytest counted it as a passing test. The `assert` statement causes an error when it evaluates to False.
> {: .solution}
{: .challenge}

Change the expected value back to 1 so that your tests pass and make sure you have the `assert` statement so that your test passes.

> ## Exercise
> Create a test for the `calculate_angle ` function. Use the three points
> ~~~
> r1 = np.array([0, 0, -1])
> r2 = np.array([0, 1, 0])
> r3 = np.array([1, 0, 0])
> ~~~
> {: .language-python}
>
> These three points correspond to an angle of 90 degrees.
> 
> Verify that your test is working by running pytest. You should now see three passing tests.
>> ## Solution
>> Since `calculate_angle` is in the `measure` module, the tests for this function should go in the same file as `calculate_distance`. You should define a new function in `test_measure` called `test_calculate_angle`
>>
>> ~~~
>> def test_calculate_angle():
>>    """Test the calculate_angle function"""
>> 
>>    r1 = np.array([1, 0, 0])
>>    r2 = np.array([0, 0, 0])
>>    r3 = np.array([0, 1, 0])
>> 
>>    expected_value = 90
>> 
>>    calculated_value = molecool.calculate_angle(r1, r2, r3, degrees=True)
>>    assert expected_value == calculated_value
>> ~~~
>> {: .language-python}
> {: .solution}
{: .challenge}

Let's also make a test for the `build_bond_list` function. We start with defining the test.

~~~
def test_build_bond_list():
~~~
{: .language-python}

Next we must have some coordinates to test. In our Jupyter Notebook, we were reading this data from an xyz file. However, remember that for unit tests, we do not want to make our test dependent on any other functions. Therefore, we will just make up some coordinates in our test.

Next, there are several things we might test about this function. We could check that we find the correct number of bonds, and that those bonds are the correct length. You should write at least one test per function, but you may have multiple assertions in the same test. For example, we could write the following test for `build_bond_list`.

~~~
def test_build_bond_list():

    coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])

    bonds = molecool.build_bond_list(coordinates)

    assert len(bonds) == 3

    for atoms, bonds in bonds.items():
        assert bonds == 1.4
~~~
{: .language-python}

Here, we are asserting that the correct number of bonds were found, and next we are iterating through the dictionary to ensure that a distance of 1.4 angstrom was calculated for each bond.

### Testing Expected Exceptions

If you expect your code to raise exceptions, you can test this behavior with pytest.
You need to import `pytest` in your testing modules in order to do this.  We can test that an exception is properly raised when we input the wrong type to our `title_case` function.

In our `build_bond_list` function, we have added a check on the input that ensures that the coordinates array is not empty. If an empty array or list is passed, a `ValueError` is raised. Using pytest, we can test this behavior

In the `test_molecule.py` file, add the following.

~~~
def test_type_error():
    test_case = [[]

    with pytest.raises(ValueError):
        molecool.build_bond_list(test_case)
~~~
{: .language-python}

The test will pass if the `build_bond_list` method raises a 'TypeError', otherwise, the test will fail.


## Test Driven Development - TDD - Homework Assignment

Sometimes, tests are written before code is actually written. This is called "Test Driven Development" or TDD. In this case, you would write tests which define the behavior of your code, run the tests to see they pass, then write code to pass each test. TDD is common when developing a library with well-defined interfaces and features.

TDD has another benefit of never having false positives. If you ensure that your tests first fail THEN pass, you know that you have really written a function that works and that your test is not just passing by default.

> ## Exercise (Homework Assignment #1)
> For this homework assignment, you are given a function specification and a test. You should write a function to make the test pass.
>
> Add the following function definition and docstring to `molecule.py`.
>
> ~~~
> def calculate_molecular_mass(symbols):
>    """Calculate the mass of a molecule.
>    
>    Parameters
>    ----------
>    symbols : list
>        A list of elements.
>    
>    Returns
>    -------
>    mass : float
>        The mass of the molecule
>    """
>    pass
> ~~~
> {: .language-python}
>
> This defines a function, inputs, and what the function should return.
> Next, add  the following test into `test_molecule.py`.
> ~~~
> def test_molecular_mass(test_molecule):
>     symbols = ['C', 'H', 'H', 'H', 'H']
>     
>     calculated_mass = molecool.calculate_molecular_mass(symbols)
> 
>     actual_mass = molecool.atom_data.atom_weights['C'] + molecool.atom_data.atom_weights['H'] +\
>          molecool.atom_data.atom_weights['H'] + molecool.atom_data.atom_weights['H']
> ~~~
> {: .language-python}
>
> If you run `pytest`, this test should fail. Your assignment is to write the function to make the tests pass. You should use the `atomic_weights` data in the `atom_data` module.
>> ## Solution
>> Here is a potential solution. 
>> ~~~
>> def calculate_molecular_mass(symbols):
>>     """Calculate the mass of a molecule.
>>     
>>     Parameters
>>     ----------
>>     symbols : list
>>         A list of elements.
>>     
>>     Returns
>>     -------
>>     mass : float
>>         The mass of the molecule
>>     """
>> 
>>     mass = 0
>>     for atom in symbols:
>>         mass += atom_weights[atom]
>>     
>>     return mass
>> ~~~
>> {: .language-python}
> {: .solution}
{: .challenge}

> ## Exercise - (Homework Assignment #2)
> Consider the following function definition and the test written.
> def calculate_center_of_mass(symbols, coordinates):
> ~~~
>    """Calculate the center of mass of a molecule.
>    
>    The center of mass is weighted by each atom's weight.
>    
>    Parameters
>    ----------
>    symbols : list
>        A list of elements for the molecule
>    coordinates : np.ndarray
>        The coordinates of the molecule.
>    
>    Returns
>    -------
>    center_of_mass: np.ndarray
>        The center of mass of the molecule.
>
>    Notes
>    -----
>    The center of mass is calculated with the formula
>    
>    .. math:: \\vec{R}=\\frac{1}{M} \\sum_{i=1}^{n} m_{i}\\vec{r_{}i}
>    
>    """
>
>    return np.array([])
> ~~~
> {: .language-python}
> 
> and the test
> ~~~
> def test_center_of_mass():
>     symbols = np.array(['C', 'H', 'H', 'H', 'H'])
>     coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])
> 
>     center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)
> 
>     expected_center = np.array([1,1,1])
> 
>     assert center_of_mass.all() == expected_center.all()
> ~~~
> {: .language-python}
>
> Notice that this test always passes. Even if we were to write our function, we would not know it was right.
> 
> Fix this test so that it fails. **Hint** - You will have to compare two arrays (look into the function `numpy.array_equal`)
>> ## Solution - Fixing the test
>> The problem with `.all()` is that it does not compare arrays element-wise, it simply evaluates as True if all values in the array are True, or False if not. The numpy function `array_equal` returns True if two arrays have the same shape and elements.
>>
>> ~~~
>> def test_center_of_mass(test_molecule):
>>     symbols = np.array(['C', 'H', 'H', 'H', 'H'])
>>     coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])
>> 
>>     center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)
>> 
>>     expected_center = np.array([1,1,1])
>> 
>>     assert np.array_equal(center_of_mass, expected_center)
>> ~~~
>> {: .language-python}
> {: .solution}
>
> Below is an implementation of the function which meets the specification outlined by the test.
>
>> ## Function Implementation
>> ~~~
>> def calculate_center_of_mass(symbols, coordinates):
>>    """Calculate the center of mass of a molecule.
>>    
>>    The center of mass is weighted by each atom's weight.
>>    
>>    Parameters
>>    ----------
>>    symbols : list
>>        A list of elements for the molecule
>>    coordinates : np.ndarray
>>        The coordinates of the molecule.
>>    
>>    Returns
>>    -------
>>    center_of_mass: np.ndarray
>>        The center of mass of the molecule.
>>
>>    Notes
>>    -----
>>    The center of mass is calculated with the formula
>>    
>>    .. math:: \\vec{R}=\\frac{1}{M} \\sum_{i=1}^{n} m_{i}\\vec{r_{}i}
>>    
>>    """
>>
>>    total_mass = calculate_molecular_mass(symbols)
>>    
>>    mass_array = np.zeros([len(symbols), 1])
>>    
>>    for i in range(len(symbols)):
>>        mass_array[i] = atom_weights[symbols[i]]
>>    
>>    center_of_mass = sum(coordinates * mass_array) / total_mass
>>    
>>    return center_of_mass
>> ~~~
>> {: .language-python}
> {: .solution}
{: .challenge}



## Edge and Corner Cases

### Edge cases
The situation where the test examines either the beginning or the end of a range, but not the middle, is called an edge case.
In a simple, one-dimensional problem, the two edge cases should always be tested along with at least one internal point.
This ensures that you have good coverage over the range of values.

Anecdotally, it is important to test edges cases because this is where errors tend to arise. Qualitatively different behavior happens at boundaries. As such, they tend to have special code dedicated to them in the implementation.

### Corner cases
When two or more edge cases are combined, it is called a corner case. If a function is parametrized by two linear and independent variables, a test that is at the extreme of both variables is in a corner.

## Advanced features of pytest (fixtures, parameterize)

### Pytest Fixtures

Fixtures are resources that tests can repeatedly request to use. Fixtures can be used for dependency injection (a way of passing or supplying resources from one object to another) which help decouple the code and make it cleaner.

To use fixtures, we need to import `pytest`. Fixtures can be defined as methods, where the name of the method is the name of this resource, and
the returned data is its value. For this example:

~~~
@pytest.fixture
def num_list_3():
    return [1, 2, 3, 4, 5]
~~~
{: .python}

we defined a fixture named `num_list_3` which will have the value `[1, 2, 3, 4, 5]`. Now, any test
method can request this fixture by adding its name to its input argument as follows.

~~~
def test_mean(num_list_3):
    assert mean(num_list_3) == 3.0
~~~
{: .python}

Fixtures can be reused by other tests too. Also, test methods can request multiple fixtures.


### Pytest Parametrize

The built-in `pytest.mark.parametrize` decorator enables parametrization of arguments for a test function.
Here is a typical example of a test function that implements checking that a certain input leads to an expected output.

~~~
import pytest
import numpy as np

@pytest.mark.parametrize("num_list, expected_mean" , [
    ([1, 2, 3, 4, 5], 3),
    ([0, 2, 4, 6], 3),
    ([1, 2, 3, 4], 2.5),
    (list(range(1, 1000000)), 1000000/2.0)
])

def test_many(num_list, expected_mean):
    # assert mean(num_list) == expected_mean
    assert np.isclose(mean(num_list), expected_mean, 1e-6)
~~~
{: .python}

Here, the @parametrize decorator defines four different (test_input, expected) tuples
so that the `test_many` function will run four times using them in turn.
Here, we used the `numpy` method `isclose` to compare float values within the range `1e-6`.

To get all combinations of multiple parametrized arguments you can stack parametrize decorators:

~~~
import pytest
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    pass
~~~
{: .python}

This will run the test with the arguments set to x=0/y=2, x=1/y=2, x=0/y=3,
and x=1/y=3 exhausting parameters in the order of the decorators.



### Testing Documentation Examples
As our package changes over time, we want to make sure that the examples in our docstrings still behave as originally written, but checking these by hand can be a real pain.
Luckily, `pytest` has a feature that will look for examples in docstrings and run them as tests.

`pytest` searches the docstrings for the Python shell code, which it executes and compares to the outputs in the docstring.
For example, in the docstring of our function `title_case` we have:

~~~
>>> title_case('ThIS is a STRinG to BE ConVerTeD.')
'This Is A String To Be Converted.'
~~~
{: .language-python}

`pytest` will find and execute `title_case('ThIS is a STRinG to BE ConVerTeD.')`.
If the output is not `'This Is A String To Be Converted.'`, `pytest` will treat the test as a failure.

From the main `molssi_devops` directory, we can test the examples in the docstrings of `util.py`:

~~~
$ pytest -v --doctest-modules molssi_devops/util.py
~~~
{: .language-bash}

~~~
================================================= test session starts ==================================================
platform darwin -- Python 3.6.7, pytest-4.4.1, py-1.8.0, pluggy-0.9.0 -- /Users/jets/miniconda3/envs/omp_mpi/bin/python
cachedir: .pytest_cache
rootdir: /Users/jets/Google Drive/research/MolSSI/CU_Boulder_Workshop/molssi_devops
plugins: cov-2.6.1
collected 1 item                                                                                                       

molssi_devops/util.py::molssi_devops.util.title_case PASSED                                                      [100%]

=============================================== 1 passed in 0.10 seconds ===============================================
~~~
{: .output}

If we change the example in the `title_case` docstring to:

~~~
>>> title_case('ThIS is a STRinG to BE ConVerTeD.')
'This Is A String To Be Converted'
~~~
{: .language-python}

and re-run the test we get the following error:

~~~
================================================= test session starts ==================================================
platform darwin -- Python 3.6.7, pytest-4.4.1, py-1.8.0, pluggy-0.9.0 -- /Users/jets/miniconda3/envs/omp_mpi/bin/python
cachedir: .pytest_cache
rootdir: /Users/jets/Google Drive/research/MolSSI/CU_Boulder_Workshop/molssi_devops
plugins: cov-2.6.1
collected 1 item                                                                                                       

molssi_devops/util.py::molssi_devops.util.title_case FAILED                                                      [100%]

======================================================= FAILURES =======================================================
_______________________________________ [doctest] molssi_devops.util.title_case ________________________________________
010     String to be converted to title case
011
012   Returns
013   -------
014   ret: str
015     String converted to title case.
016
017   Example
018   -------
019   >>> title_case('ThIS is a STRinG to BE ConVerTeD.')
Expected:
    'This Is A String To Be Converted'
Got:
    'This Is A String To Be Converted.'

/Users/jets/Google Drive/research/MolSSI/CU_Boulder_Workshop/molssi_devops/molssi_devops/util.py:19: DocTestFailure
=============================================== 1 failed in 0.06 seconds ==============================================
~~~
{: .output}

We can test multiple docstring examples at once and can even test the dosctring examples at the same time as our unit tests with:

~~~
pytest -v --doctest-modules molssi_devops
~~~
{: .language-bash}

~~~
================================================= test session starts =================================================
platform darwin -- Python 3.6.7, pytest-4.4.1, py-1.8.0, pluggy-0.9.0 -- /Users/jets/miniconda3/envs/omp_mpi/bin/python
cachedir: .pytest_cache
rootdir: /Users/jets/Google Drive/research/MolSSI/CU_Boulder_Workshop/molssi_devops
plugins: cov-2.6.1
collected 12 items                                                                                                    

molssi_devops/molssi_math.py::molssi_devops.molssi_math.mean PASSED                                             [  8%]
molssi_devops/util.py::molssi_devops.util.title_case PASSED                                                     [ 16%]
molssi_devops/tests/test_molssi_devops.py::test_molssi_devops_imported PASSED                                   [ 25%]
molssi_devops/tests/test_molssi_math.py::test_many[num_list0-3] PASSED                                          [ 33%]
molssi_devops/tests/test_molssi_math.py::test_many[num_list1-3] PASSED                                          [ 41%]
molssi_devops/tests/test_molssi_math.py::test_many[num_list2-2.5] PASSED                                        [ 50%]
molssi_devops/tests/test_molssi_math.py::test_many[num_list3-500000.0] PASSED                                   [ 58%]
molssi_devops/tests/test_molssi_math.py::test_mean PASSED                                                       [ 66%]
molssi_devops/tests/test_molssi_math.py::test_mean_type_error PASSED                                            [ 75%]
molssi_devops/tests/test_molssi_math.py::test_zero_length PASSED                                                [ 83%]
molssi_devops/tests/test_util.py::test_type_error PASSED                                                        [ 91%]
molssi_devops/tests/test_util.py::test_title_case PASSED                                                        [100%]

============================================== 12 passed in 0.25 seconds ==============================================
~~~
{: .output}

### Code Coverage Pt. 1

Now that we have a set of modules and associated tests, we want to see how much of our package is "covered" by our tests.
We'll measure this by counting the lines of our packages that are touched, i.e. used, during our tests.

We already have everything we need for this since we installed `pytest-cov` earlier which includes the coverage tools on top of the `pytest` package.

We can assess our code coverage as follows:

~~~
pytest --cov=molssi_devops
~~~
{: .language-bash}

~~~
================================================= test session starts =================================================
platform darwin -- Python 3.6.7, pytest-4.4.1, py-1.8.0, pluggy-0.9.0
rootdir: /Users/jets/Google Drive/research/MolSSI/CU_Boulder_Workshop/molssi_devops
plugins: cov-2.6.1
collected 10 items                                                                                                    

molssi_devops/tests/test_molssi_devops.py .                                                                     [ 10%]
molssi_devops/tests/test_molssi_math.py .......                                                                 [ 80%]
molssi_devops/tests/test_util.py ..                                                                             [100%]

---------- coverage: platform darwin, python 3.6.7-final-0 -----------
Name                           Stmts   Miss  Cover
--------------------------------------------------
molssi_devops/__init__.py          7      0   100%
molssi_devops/molssi_math.py      17      7    59%
molssi_devops/util.py              9      0   100%
--------------------------------------------------
TOTAL                             33      7    79%


============================================== 10 passed in 0.36 seconds ==============================================
~~~
{: .output}

The output shows how many statements (i.e. not comments) are in a file, how many weren't executed during testing, and the percentage of statements that were.
For the example above, we have perfect coverage of `util.py`, but not `molssi_math.py`.

To improve our coverage, we also want to see exactly which lines we missed and we can determine this using the `.coverage` file produced by `pytest`.
Unfortunately, this strategy becomes impractical when we are working with anything larger than our test package because the `.coverage` file becomes too convoluted to read.
We will need more tools to help us determine how to improve out tests and that will be the subject of Code Coverage pt. 2, which we will cover in Episode 6.

> ## Do we need to get 100% coverage?
>
> Short answer: __no__.
> Code coverage is a useful tool to assess how comprehensive our set of tests are and in general the higher our code coverage the better.
> __However__, trying to achieve 100% coverage on packages any larger than this sample package is a bit unrealistic and would require more time than that last bit of coverage is worth.
>
{: .callout}
