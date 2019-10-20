---
title: "Python Testing"
teaching: 45
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

This episode explains the importance of code testing and demonstrates the possible capabilities.

## Why testing

Software should be tested regularly throughout the development cycle to ensure correct operation. Thorough testing is typically an afterthought, but for larger projects, it is essential for ensuring changes in some parts of the code do not negatively affect other parts.

Software testing is checking the behavior of part of the code (such as a method, class, or a module) by comparing its expected output or behavior with the observed one. We will explain this in more details shortly.


## Unit vs Regression vs Integration testing

There are many types of testing. There are three main levels of testing:

- **Unit tests**: the purpose is to verify that each part of the code is functioning as expected.
Unit testing is done on smaller units (such as single functions or classes) as you work on
your code.
This is helpful for catching errors in uncommonly-used parts of the code. Unit tests can
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
values? This kind of testing can catch problems in previously working code that may
 has been broken by new changes or new features.

It is highly encouraged to have Unit tests that *cover* most of your code. It is
also helpful to have some Integration and System tests.

In this lesson, we are focusing on unit testing, along with regression testing.
Same concepts here can be applied to perform Integration tests across modules.
We will be using Python version 3.5 or above.

## The pytest testing framework

The Python testing framework was chosen to be [pytest](https://pytest.org) for this project.
Other testing frameworks are available (such as unittest and nose tests);
however, the authors believe the combination of easy [parametrization of tests](https://docs.pytest.org/en/latest/parametrize.html),
[fixtures](https://docs.pytest.org/en/latest/fixture.html), and [test marking](https://docs.pytest.org/en/latest/example/markers.html)
make `pytest` particularly suited for computational chemistry.

If you don't have `pytest` installed or it's not updated to version 3, install it using:
~~~
$ pip install -U pytest-cov
~~~
{: .bash}

### Running our first test

When we run `pytest`, it will look for directories and files which start with `test` or `test_`. CookieCutter has already created a test for us. Let's examine this file. In a text editor, open `molss_devops/tests/test_molssi_devops.py`

~~~
"""
Unit and regression test for the molssi_devops package.
"""

# Import package, test suite, and other packages as needed
import molssi_devops
import pytest
import sys

def test_molssi_devops_imported:
    """Sample test, will always pass so long as import statement worked"""
    assert "molssi_devops" in sys.modules
~~~
{: .language-python}

This file begins with `test_`, and contains a single function `test_molssi_devops_imported`. This module will import our package, then checks to see if it has been imported correctly by checking if the package name is in the list of imported modules.

The last line, containing the python keyword `assert`, is called an assertion. Assertions are used to check the behavior of the code during runtime. The `assert` keyword halts code execution instantly if the comparison is False, and does nothing if the comparison is True.

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

molssi_devops/tests/test_molssi_devops.py .                    [100%]

=========================== 1 passed in 0.06 seconds ===========================
~~~
{: .output}

Here, `pytest` has looked through our directory and its subdirectories for anything matching `test*`. It found the `tests` folder, and within that folder, it found the file `test_molssi_devops.py`. It then executed the function `test_molssi_devops_imported` within that module. Since our `assertion` was True, the test passed.

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

molssi_devops/tests/test_molssi_devops.py::test_molssi_devops_imported PASSED [100%]

=========================== 1 passed in 0.06 seconds ===========================
~~~
{: .output}

Now we see that `pytest` dsiplays the test name for us, as well as `PASSED` next to the test name.

## Testing our functions

We will now add tests to test our functions.

Recall that we have two functions. `mean` in `molssi_math`, and `title_case` in `util`. Let's first write some functions for our `mean` function.

Create a new file called `test_molssi_math.py` in the `tests` directory with the following contents.

~~~
"""
Unit and regression test for the molssi_math module.
"""

# Import package, test suite, and other packages as needed
import molssi_devops
import pytest
import sys

def test_mean():
    """Test that mean function calculates what we expect."""
    test_list = [1, 2, 3, 4, 5]
    expected = 3
    calculated =  molssi_devops.mean(test_list)
    assert expected == calculated
~~~
{: .language-python}

We have written one test in this file. It calculates the mean of a test list, and asserts that it is equal to our expected value.

Run this test using `pytest`. In the terminal window, type

~~~
pytest -v
~~~
{: .language-bash}

You should now see the following.

~~~
============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-3.6.4, py-1.5.4, pluggy-0.6.0 -- /Users/jessica/miniconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/jessica/dev/molssi_devops, inifile:
collected 2 items

molssi_devops/tests/test_molssi_devops.py::test_molssi_devops_2019_imported PASSED [ 50%]
molssi_devops/tests/test_molssi_math.py::test_mean PASSED           [100%]

=========================== 2 passed in 0.07 seconds ===========================
~~~
{: .output}

We now see that we have two tests which have been run, and they both passed.

### Failing tests
Let's see what happens when one of the test fails.

In case of test failure, Pytest will show detailed output from doing its own analysis to discover the error by inspecting your objects at runtime. Change the value of the `expected` variable in your test function to `2` and rerun the test.

~~~
$ pytest -v
~~~
{: .language-bash}

~~~
============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-3.6.4, py-1.5.4, pluggy-0.6.0 -- /Users/jessica/miniconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/jessica/dev/molssi_devops, inifile:
collected 2 items

molssi_devops_2019/tests/test_molssi_devops_2019.py::test_molssi_devops_2019_imported PASSED [ 50%]
molssi_devops/tests/test_molssi_math.py::test_mean FAILED    [100%]

=================================== FAILURES ===================================
__________________________________ test_mean ___________________________________

    def test_mean():
        """Test that mean function calculates what we expect."""
        test_list = [1, 2, 3, 4, 5]
        expected = 2
        calculated =  molssi_devops.mean(test_list)
>       assert expected == calculated
E       assert 2 == 3.0

molssi_devops_2019/tests/test_molssi_math.py:19: AssertionError
====================== 1 failed, 1 passed in 0.17 seconds ======================
~~~
{: .output}

Pytest shows a detailed failure report, including the source code around the failing line. The line that failed is marked with `>`.
Next, it shows the values used in the assert comparison at runtime, that is `3.0 == 2`. This runtime analysis is one of the advantages of pytest that help you debug your code.

Change the expected value back to 3 so that your tests pass.

> ## Exercise
> Create a test for your `title_case` function. Use the example string in the docstring for the function. You will need to create a new file in the `tests` folder for this.
>
> In other words, test that the string 'ThIS is a STRinG to BE ConVerTeD.' is correctly converted to 'This Is A String To Be Converted.'
>
> Verify that your test is working by running pytest. You should now see three passing tests.
>> ## Solution
>> First, create a new file in the `tests` directory. We will call our file `test_util.py`.
>>
>> Here is a sample of the contents of `test_util.py` with the specified test written.
>>
>> ~~~
>> """
>> Unit and regression test for the util module.
>> """
>>
>> # Import package, test suite, and other packages as needed
>> import molssi_devops
>> import pytest
>> import sys
>>
>> def test_title_case():
>>     """Test the title case function."""
>>     test_string = 'ThIS is a STRinG to BE ConVerTeD.'
>>     expected = 'This Is A String To Be Converted.'
>>     calculated =  molssi_devops.title_case(test_string)
>>     assert expected == calculated
>> ~~~
>> {: .language-python}
> {: .solution}
{: .challenge}

> ## Test Driven Development - TDD
> Sometimes, tests are written before code is actually written. This is called "Test Driven Development" or TDD. In this case, you would write tests which define the behavior of your code, run the tests to see they pass, then write code to pass each test. TDD is common when developing a library with well-defined interfaces and features.
{: .callout}

### Checking inputs - raising errors

Let's return to the terminal window temporarily to consider behavior of our functions. Currently, our `title_case` function has some unexpected behavior. Consider the following example. In the python command line,

~~~
>>> import molssi_devops as md
>>> test_case = ['this', 'is', 'not', 'a', 'string']
>>> md.title_case(test_case)
~~~
{: .language-python}

~~~
'THISisnotastring'
~~~
{: .output}

Because of the way our function is written, it gives unexpected behavior. Worse, our program does not actually fail. If we were calling this in a script, it would continue without giving an error. Because of this, we want to check the user inputs in our functions.

For the `title_case` function, we will want to check that the user input is type `string`.

Modify your `title_case` function to contain the following after the docstring.

~~~
# Check that input is string
  if not isinstance(sentence, str):
      raise TypeError('Invalid input, type %s - Input must be type string' %(type(sentence)))
~~~
{: .language-python}

In the first line, we are checking that the input `sentence` is a string. If it is not, we are raising a `TypeError`, then giving a custom error message saying that the input must be of type string.

Now, if we try the previous example again, we get the following error

~~~
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jessica/dev/molssi_devops/molssi_devops/util.py", line 31, in title_case
    raise TypeError('Invalid input, type %s - Input must be type string.' %(type(sentence)))
TypeError: Invalid input, type <class 'list'> - Input must be type string.
~~~
{: .output}

### Testing Expected Exceptions

If you expect your code to raise exceptions, you can test this behavior with pytest.
First, you need to import `pytest`. We can test that an exception is properly raised when we input the wrong type to our `title_case` function.

In your `test_util.py` file, add the following.

~~~
def test_type_error():
    test_case = ['this', 'is', 'not', 'a', 'string']

    with pytest.raises(TypeError):
        md.title_case(test_case)
~~~
{: .language-python}

The test will pass if the `title_case` method raises a 'TypeError', otherwise, the test will fail.

What are some thing we might want to check on user input for the `mean` function. If you think for a bit, you may come up with the following responses:

1. Check that input is type `list`
2. Check that input list has length (ie that it is not an empty list)
3. Check that all elements of the input list is numeric.

> ## Exercise
> Modify your mean function to check that inputs meet all three criteria outlined above.
>> ## Solution
>> ~~~
>> def mean(num_list):
>>    """
>>    Computes the mean of a list of numbers.
>>
>>    Parameters
>>    ----------
>>    num_list: list
>>        List to calculate mean of
>>
>>    Returns
>>    -------
>>    list_mean: float
>>    Mean of list of numbers
>>    """
>>
>>     # Check that input is type list
>>    if not isinstance(num_list, list):
>>        raise TypeError('Invalid input %s - must be type list' %(num_list))
>>
>>    # Check that list is not empty
>>    if not num_list:
>>        raise ValueError('Cannot calculate the mean of an empty list.')
>>
>>    try:
>>        list_mean = sum(num_list) / len(num_list)
>>    except TypeError:
>>        raise TypeError('Cannot calculate mean of list - all list elements must be numeric')
>>
>>    return list_mean
>> ~~~
>> {: .language-python}
>>
> {: .solution}
{: .challenge}

We can modify our tests to check that all of the expected exceptions are raised.

Add the following two tests to `test_molssi_math.py`
~~~
def test_mean_type_error():
    test_variable = 'this is a string'

    with pytest.raises(TypeError):
        molssi_devops.mean(test_variable)

def test_zero_length():
    test_list = []

    with pytest.raises(ValueError):
        molssi_devops.mean(test_list)
~~~
{: .language-python}

### More Pytest Features - Pytest Marks

Marks are an easy way to add annotations to your tests. For instance, you can mark some tests to be skipped
by adding the skip decorator to your test method `pytest.mark.skip`.
Add the following code to your `test_molssi_math.py`.

~~~
@pytest.mark.skip
def test_mean_type_error():
    test_variable = 'this is a string'

    with pytest.raises(TypeError):
        molssi_devops.mean(test_variable)
~~~
{: .python}

after running `pytest -v`, pytest will run the other tests, skipping test_mean_type_error.
~~~
============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-3.6.4, py-1.5.4, pluggy-0.6.0 -- /Users/jessica/miniconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/jessica/dev/molssi_devops, inifile:
collected 5 items

molssi_devops/tests/test_molssi_devops_2019.py::test_molssi_devops_imported PASSED [ 20%]
molssi_devops/tests/test_molssi_math.py::test_mean PASSED           [ 40%]
molssi_devops/tests/test_molssi_math.py::test_mean_type_error SKIPPED [ 60%]
molssi_devops/tests/test_molssi_math.py::test_zero_length PASSED    [ 80%]
molssi_devops/tests/test_util.py::test_title_case PASSED            [100%]

===================== 4 passed, 1 skipped in 0.11 seconds ======================
~~~
{: .output}

You can also use your own custom marks and run pytest with some selected tests. Let's mark
this method with the mark `@pytest.mark.my_test`

~~~
@pytest.mark.my_test
def test_zero_length():
    test_list = []

    with pytest.raises(ValueError):
        molssi_devops.mean(test_list)
~~~
{: .python}

You can run `pytest -m "not my_test"` to run all tests that are NOT marked with
`@pytest.mark.my_test`.
Custom marks are a great way to organize tests into groups so you can quickly run subsets of your tests while debugging your code.

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
