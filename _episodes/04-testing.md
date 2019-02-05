---
title: "Python Testing"
teaching: 30
exercises: 50
questions:
- "How is a Python module tested?"
objectives:
- "Explain the overall structure of testing."
- "Explain the reasons why testing is important."
keypoints:
- "Enumerate the types of testing and the importance of each."
- "Explain pytest features and why pytest was selected."
---

This episode explains the importance of code testing and demonstrates the possible
capabilities.

## Why testing

Software should be tested regularly throughout the development cycle to ensure
correct operation. Thorough testing is typically an afterthought, but for
larger projects, it is essential for ensuring changes in some parts of the
code do not negatively affect other parts. Sometimes, testing is done before the code is
actually written, which is called Test-Driven Development (TDD). TDD is common when
developing a library with well-defined interfaces and features.

Software testing is checking the behavior of part of the code (such as a method,
class, or a module) by comparing its expected output or behavior with the
 observed one. We will explain this in more details shortly.

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

## Pytest examples

The Python testing framework was chosen to be [pytest](https://pytest.org) for this project.
Other testing frameworks are available (such as unittest and nose tests);
however, the authors believe the combination of easy [parametrization of tests](https://docs.pytest.org/en/latest/parametrize.html),
[fixtures](https://docs.pytest.org/en/latest/fixture.html), and [test marking](https://docs.pytest.org/en/latest/example/markers.html)
make `pytest` particularly suited for computational chemistry.

To get started additional tests can be added to the `project/tests/` folder.
Any function starting with `test_*` will automatically be
included in the testing framework. While these can be added in anywhere
 in your directory structure, it is highly recommended to keep them
contained within the `project/tests/` folder.


### Start by a simple pytest file

If you don't have `pytest` installed or it's not updated to version 3, install it using:
~~~
$ pip install -U pytest
~~~
{: .bash}

First, we will create a simple file to test. Create a `list_util.py` file that contains
a simple method to calculate the mean of a list of numbers.

~~~
# content of list_util.py

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

    try:
        return sum(num_list)/len(num_list)
    except TypeError as err:
        msg = 'Input must be a list of int or float'
        raise TypeError(err.__str__() + '\n' + msg)
    except ZeroDivisionError as err:
        raise ZeroDivisionError(err)

~~~
{: .python}

The method raises a `TypeError` exception if the list is not numeric, or a `ZeroDivisionError`
if the list is empty.

Now, create a test file, `test_list_util.py`, that has a method to test our mean function.

~~~
# content of test_list_util.py
from list_util import mean

def test_mean():
    num_list = [1, 2, 3, 4, 5]
    observed = mean(num_list)
    expected = 3
    assert observed == expected, 'My test failed'
~~~
{: .python}


The last line, containing the python keyword `assert`, is called an assertion.  
They are used to check the behavior of the code during runtime.
The `assert` keyword halt code execution instantly if the comparison is false, and does
nothing if the comparison is true.

The following are some examples of assertions that you can test directly on a python console.

~~~
>>> x = y = 0
>>> assert x
>>> assert x == 1
>>> assert x != 2
>>> assert not x
>>> assert 3 < x < 5 and y < 5
>>> s = 'The universe is expanding.'
>>> assert 'universe' in s
~~~
{: .python}


Once these tests are written in a file called `test_list_util.py`, the command `pytest` can be
called from the directory containing the tests (note that you will have to use
`py.test` for older versions of the pytest package):

~~~
$ pytest -v
~~~
{: .bash}
~~~
tests/test_mean.py::test_mean PASSED                                                 [100%]

================================ 1 passed in 0.05 seconds =================================

~~~
{: .output}


Using the command argument ` -v` will result in pytest, listing which tests are executed and
whether they pass or not. There are a number of
additional command line arguments to [explore](https://docs.pytest.org/en/latest/usage.html).

As we write more code, we would write more tests.
Each passing test is a small, satisfying reward for having written quality scientific software.

Key Points:
The pytest command collects and runs tests starting with Test or test_.

  * . means the test passed
  * F means the test failed or erred
  * x is a known failure
  * s is a purposefully skipped test


### Failing tests

In case of test failure, Pytest will show detailed output
from doing its own analysis to discover the error by inspecting your objects at runtime.
Optionally, the assert can be followed by a message that will be shown when the test has failed,
but this will stop pytest inspection of the error. So it is better not to provide this error
messsage unless you know you will be providing more information.
The following is an example of a test that will fail
(since the mean of [1, 2, 3, 4, 5] is 3.0, not 2.0).

~~~
def test_mean():
    assert mean([1, 2, 3, 4, 5]) == 2
~~~
{: .python}

~~~
tests/test_list_util.py::test_mean FAILED                                         [100%]

==================================== FAILURES ==========================================
_____________________________________ test_mean ________________________________________

    def test_mean():
>       assert mean([1, 2, 3, 4, 5]) == 2
E       assert 3.0 == 2
E        +  where 3.0 = mean([1, 2, 3, 4, 5])

tests/test_mean.py:4: AssertionError
========================= 1 failed in 0.09 seconds ====================================
~~~
{: .output}

Pytest shows a detailed failure report, including the source code around the failing line.
The line that failed is marked with `>`.
Next, it shows the values used in the assert comparison at runtime, that is `3.0 == 2`.
This runtime analysis is one of the advantages of pytest that help you debug your code.

### Expected Exception

If you expect your code to raise exceptions, you can test this behavior with pytest.
First, you need to import `pytest`. And back to our mean method, it should raise an exception
if the list is not numeric. We can test this by the following:

~~~
import pytest

def test_mean_wrong_type():
    str_list = ['a', 'b', 'c']
    with pytest.raises(TypeError):
        mean(str_list)
~~~
{: .python}

The test will pass if the `mean` method raises a 'TypeError', otherwise, the test will fail.

### Marks

Marks are an easy way to add annotations to your tests. For instance,
you can mark some tests to be skipped
by adding the skip decorator to your test method `pytest.mark.skip`.
Add the following code to your `test_list_util.py`.

~~~
@pytest.mark.skip
def test_mean_ints():
    num_list = [1, 2, 3, 4, 5]
    assert num_list == 3.0
~~~
{: .python}

after running `pytest -v`, pytest will run the other tests, skipping test_mean_ints.
~~~
collected 3 items                                                                                                                

tests/test_mean.py::test_mean PASSED                                               [ 33%]
tests/test_mean.py::test_type_error PASSED                                         [ 66%]
tests/test_mean.py::test_mean_ints SKIPPED                                         [100%]

======================= 2 passed, 1 skipped in 0.05 seconds ============================
~~~
{: .output}

You can also use your own custom marks and run pytest with some selected tests. Let's mark
this method with the mark `@pytest.mark.my_easy_tests`

~~~
@pytest.mark.my_easy_tests
def test_mean_small():
    num_list = [1, 2]
    assert mean(num_list) == 1.5
~~~
{: .python}

You can run `pytest -m 'not my_easy_tests` to run all tests that are NOT marked with
`@pytest.mark.my_easy_tests`.


## Edge and Corner Cases

### Edge cases
The situation where the test examines either the beginning or the
end of a range, but not the middle, is called an edge case.
In a simple, one-dimensional problem, the two edge cases should
always be tested along with at least one internal point.
This ensures that you have good coverage over the range of values.

Anecdotally, it is important to test edges cases because this is where errors tend to arise.
Qualitatively different behavior happens at boundaries. As such, they tend to have special code
 dedicated to them in the implementation.


### Corner cases
When two or more edge cases are combined, it is called a corner case.
If a function is parametrized by two linear and independent variables,
a test that is at the extreme of both variables is in a corner.


## Advanced features of pytest (fixtures, parameterize)

### Pytest Fixtures

Fixtures are resources that tests can repeatedly request to use.
Fixtures can be used for dependency injection
(a way of passing or supplying resources from one object to another)
which help decouple the code and make it cleaner.

To use fixtures, we need to import `pytest`. Fixtures can be defined as methods,
where the name of the method is the name of this resource, and
the returned data is its value. For this example:

~~~
@pytest.fixture
def num_list_3():
    return [1, 2, 3, 4, 5]
~~~
{: .python}

we defined a fixture named `num_list_3` which will have the value `[1, 2, 3, 4, 5]`. Now, any test
method can request this fixture by adding its name to its input argument as follows:

~~~
def test_mean_ints(num_list_3):
    assert mean(num_list_3) == 3.0
~~~
{: .python}

Fixtures can be reused by other tests too. Also, test methods can request multiple fixtures.


### Pytest Parametrize

The builtin `pytest.mark.parametrize` decorator enables parametrization of arguments for a test function.
Here is a typical example of a test function that implements checking that a certain input leads to an expected output:

~~~
import pytest
import numpy as np

@pytest.mark.parametrize("num_list, expected_mean" , [
    ([1, 2, 3, 4, 5], 3),
    ([0, 2, 4, 6], 3),
    ([1, 2, 3, 4], 2.5),
    (range(1, 1000000), 1000000/2.0)
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
