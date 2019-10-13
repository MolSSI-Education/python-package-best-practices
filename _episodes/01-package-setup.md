---
title: "Python Package Set-up and Structure"
teaching: 40
exercises: 5
questions:
- "What is the layout of a Python package?"
- "How can I quickly create the structure of a Python package?"
- "What license should I choose for my project?"
objectives:
- "Explain Python package structure."
- "Use the CMS CookieCutter to build a Python package."
keypoints:
- "There is a common way to structure Python packages"
- "You can use the CMS CookieCutter to quickly create the layout for a Python package"
---

For this workshop, we are going to create a Python package that performs analysis and creates visualizations for molecules. We will start from a Jupyter notebook which has some functions and analysis, which you should download on the [setup]. 

The idea is that we would like to take this Jupyter notebook and convert the functions we have created into a Python package. That way, if anyone (a labmate, for example) would like to use our functions, they can do so by installing the package and importing it into their own scripts.

To start, we will first use a tool called [CookieCutter](https://cookiecutter.readthedocs.io/en/latest/) which will set up a Python package structure and several tools we will use during the workshop.

## Examples of Python package structure
If you look at the GitHub repositories for several large Python packages such as [numpy], [scipy], or [scikit-learn], you will notice a lot of similarities between the directory layouts of these projects.

Having a similar way to lay out Python packages allows people to more easily understand and contribute to your code.

## Creating a Python package using CookieCutter
To create a skeletal structure for our project, we will use the MolSSI [CMS CookieCutter]. The [CMS CookieCutter] is a special cookiecutter created specifically by MolSSI to use the tools and services we recommend in developing a Python project.

CookieCutter will not only create our directory layout, but will also set up many tools we will use including testing, continuous integration, documentation, and git. We will discuss what all of these are later in the workshop.

### Obtaining CookieCutter

You should have the general CookieCutter installed, according to the directions given in the [setup] portion of this workshop. If you do not, please navigate to [setup] and follow the instructions given there.

### Running CookieCutter
To run the [CMS CookieCutter], navigate to the directory where you would like to start your project, and type:

~~~
$ cookiecutter gh:molssi/cookiecutter-cms
~~~
{: .language-bash}

This command runs the cookiecutter software (`cookiecutter` in the command) and tells cookiecutter to look at GitHub (`gh`) n the repository under `molssi/cookiecutter-cms`. This repository contains a template which cookiecutter uses to create your project, once you have provided some 

You will see an interactive prompt which asks questions about your project. Here, the prompt is given first, followed by the default value in square brackets. The first question will be on your project name. You have very cleverly decided to give it the name `molecool` (it's like molecule, but with `cool` instead, because of your cool visualizations - get it?)

Answer the questions according to the following.
If nothing is given after the colon (`:`), hit enter to use the default value.
~~~
project_name [ProjectName]: molecool
repo_name [molecool]:
first_module_name [molecool]: measure
author_name [Your name (or your organization/company/team)]: *YOUR_NAME_HERE*
author_email [Your email (or your organization/company/team)]: *YOUR_EMAIL_ADDRESS_HERE*
description [A short description of the project.]: A Python package for analyzing and visualizing xyz files. For MolSSI Workshop Python Package development workshop.

Select open_source_license:
1 - MIT
2 - BSD-3-Clause
3 - LGPLv3
4 - Not Open Source
Choose from 1, 2, 3, 4 (1, 2, 3, 4) [1]: 2

Select dependency_source:
1 - Prefer conda-forge over the default anaconda channel with pip fallback
2 - Prefer default anaconda channel with pip fallback
3 - Dependencies from pip only (no conda)

Choose from 1, 2, 3 (1, 2, 3) [1]:

Select Include_Windows_continuous_integration:
1 - y
2 - n
Choose from 1, 2 (1, 2) [1]:
~~~

### About these decisions

#### License Choice
Choosing which license to use is often confusing for new developers. The MIT license (option 1) is a very common license and the default on GitHub. It allows for anyone to use, modify, or redistribute your work with no restristions (and also no warranty)

Here, we have chosen the `BSD-3-Clause`. The `BSD-3-Clause` license is an open-source, permissive license (meaning that few requirements are placed on deveopers of derivative works), similar to the MIT license. However, it prohibits others from using the name of the project or its contributors to promote derived products without written consent.

If there is no license in a repository, you should assume that the project is not open source, and you cannot modify or redistribute the software.

For most of your projects, the license you choose will not matter a great deal. However, remember that if you ever want to change a license, you must get permission of all contributors. So, if you ever start a project that becomes popular or has contributors, be sure to decide your license early!

> ## Types of Open-Source Licenses
>
> Open-source licenses can either be 'permissive' or 'copy-left'. Copy-left licenses require that derivative works also be open source. Out of the choices given above, MIT and BSD-3-Clause are permissive, while LGLLv3 is a copy left license.
>
> We recommend that you spend some time reading about licensing. One place to start is this [helpful guide] from the Chodera Lab or the website [choosealicense.com](https://choosealicense.com).  
{: .callout}

#### Dependency Source
TODO - explanation here


### Reviewing directory contents
Now we can examine the project layout the CookieCutter has set up for us. Navigate to the newly created `molssi_devops` directory. You should see the following directory structure.

```
.
├── LICENSE                         <- License file
├── README.md                       <- Description of project which GitHub will render
├── appveyor.yml                    <- AppVeyor config file for Windows testing (if chosen)
├── molecool
│   ├── __init__.py                 <- Basic Python Package import file
│   ├── measure.py              <- Starting package module
│   ├── data                        <- Sample additional data (non-code) which can be packaged
│   │   ├── README.md
│   │   └── look_and_say.dat
│   ├── tests                       <- Unit test directory with sample tests
│   │   ├── __init__.py
│   │   └── test_molecool.py
│   └── _version.py                 <- Automatic version control with Versioneer
├── devtools                        <- Deployment, packaging, and CI helpers directory
│   ├── README.md
│   ├── conda-envs                  <- Environments for testing
│   │   └── test_env.yaml
│   ├── conda-recipe                <- Conda build and deployment skeleton
│   │   ├── bld.bat                 <- Win specific file, not present if Win CI not chosen
│   │   ├── build.sh
│   │   └── meta.yaml
│   ├── scripts
│   │   └── create_conda_env.py     <- OS agnostic Helper script to make conda environments based on simple flags
│   └── travis-ci
│       └── install.sh
├── docs                            <- Documentation template folder with many settings already filled in
│   ├── Makefile
│   ├── README.md                   <- Instructions on how to build the docs
│   ├── _static
│   ├── _templates
│   ├── conf.py
│   ├── index.rst
│   └── make.bat
├── setup.cfg                       <- Near-master config file to make house INI-like settings for Coverage, Flake8, YAPF, etc.
├── setup.py                        <- Your package's setup file for installing with additional options that can be set
├── versioneer.py                   <- Automatic version control with Versioneer
├── .github                         <- GitHub hooks for user contribution and pull request guides
│   ├── CONTRIBUTING.md
│   └── PULL_REQUEST_TEMPLATE.md
├── .codecov.yml                    <- Codecov config to help reduce its verbosity to more reasonable levels
├── .gitignore                      <- Stock helper file telling git what file name patterns to ignore when adding
└── .travis.yml                     <- Travis-CI config file for Linux and OSX testing
```
{: .output}

To visualize your project like above you will use "tree". If you do not have tree you can get using `sudo apt-get install tree` on linux, or `brew install tree` on Mac.

CookieCutter has created a lot of files! We will be working on and focusing in the `molecool` folder initially to develop our functions and tests. The other created directories, `devtools`, and `docs`, are related to package deployment and documentation respectively.

> ## Packages and modules
>
> What 'packages' or 'modules' are in Python may be confusing.
> In general, 'module' refers to a single `.py` file containing Python definitions and statements. It may be imported for use in another module or script. The module name is determined by the file name. A function defined in a module is used (once the module is imported) using the syntax `module_name.function_name()`.
> 'Package' refers to a collection of Python modules.
>
> To read more about Python packages vs. modules, check out [Python's documentation].
{: .callout}

## The `molecool` directory
Navigate inside our package directory. From the directory where you ran CookieCutter,

~~~
$ cd molecool
~~~
{: .language-bash}


### Our first module
Once inside of the `molecool` folder (`molecool/molecool`), examine the files that are there. View the first module (`measure.py`) in a text editor. We see a few things about this file. The top begins with a description of this module. Right now, that is the file name, followed by our short description, then the sentence "Handles the primary functions". We will change this to be more descriptive later. CookieCutter has also created a placeholder function in called `canvas`.  At the start of the `canvas` function, we have a `docstring` (more about this in [documentation]), which describes the function.

We will be moving all of the functions we defined in the jupyter notebook into python modules (`.py` files) like these.

### The `__init__.py` file

A Python package is defined by a special file recognized by the Python interpreter called `__init__.py`. Without an `__init__.py`, we don't have a Python package. This file can be blank in some cases, however, we will use it to define how the user interacts with the functions in our package.

~~~
"""
molecool
A Python package for analyzing and visualizing xyz files. For MolSSI Workshop.
"""

# Add imports here
from .molecool import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
~~~
{: .language-python}

The section we will be concerned with is under `# Add imports here`. This is how we define the way functions from modules are used.

In particular, the line

~~~
from .molecule import *
~~~
{: .language}

goes to the `molecool.py` file, and brings everything that is defined there into the file. When we use our function defined in `molecool.py`, that means we will be able to just say `molecool.canvas()` instead of giving the full path `molecool.molecool.canvas()`. If that's confusing, don't worry too much for now. We will be returning to this file in a few minutes. For now, just note that it exists and makes our directory into a package.

### Python local installs

To develop this package, we will want to something called a developmental install so that we can try out our functions and package as we develop it. 

#### Reviewing `setup.py`
Return to the top directory (`molecool`). One of the files CookieCutter generated is a `setup.py` file. `setup.py` is the build script for [setuptools]. It tells setuptools about your package (such as the name and version) as well as which code files to include. We'll be using this file in the next section.

#### Installing your package
A developer install will allow you to import your package and use it from anywhere on your computer. You will then be able to import your package into scripts in the same way you import `matplotlib` or `numpy`. 

A local install uses the `setup.py` file to install your package by inserting a link to your new project into your Python site-packages folder. To find the location of your site packages folder, you can check your Python path. Open Python (type `python` into your terminal window), and type

~~~
>>> import sys
>>> sys.path
~~~
{: .language-python}

This will give a list of locations python looks for packages when you do an import. One of the locations should end with `python3.7/site_packages`

To do a local install, type

~~~
$ pip install -e .
~~~
{: .language-bash}

Here, the `-e` indicates that we are installing this project in 'editable' mode (i.e. setuptools "develop mode"), while `.` indicates to install from the local directory (you could also specify a path here). Now, if you navigate to your site packages folder, you should see a link to `molecool` (`molecool.egg-link`). The folder has also been added to your path (check `sys.path` again.)

Now, we can use our package from any directory, similar to how we can use other installed packages like `numpy`. Open Python, and type

~~~
>>> import molecool
>>> molecool.canvas()
~~~
{: .language-python}

This should print a quote.

~~~
'The code is but a canvas to our imagination.\n\t- Adapted from Henry David Thoreau'
~~~
{: .output}

This should work from anywhere on your computer.

> ## Exercise
> What happens if we use `conda deactivate` and attempt to execute the code above? What if we switch directories?
>> ## Solution
>> If you are in the project directory, the code will still work. However, it will not work in any other location.
> {: .solution}
{: .challenge}

Optional dependencies can be installed as well with `pip install -e .[docs,tests]`

### Returning to `__init__.py`
We mentioned before that we would use the `__init__.py` file to define some things about how our package behaves. Open the file again and look at the line `from .measure import *`.

Let's break down this line so that we understand what is going on.

`from .molecool` means 'from the molecool.py module'. We use a `.` at the beginning of this module name to indicate that this is a relative import (the module is in the same directory as the `__init__.py` file). The `*` says to import everything that is in the file. For now, that is only the `canvas` function.

Comment this line out and try using your function again. You should get the message

~~~
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'molecool' has no attribute 'canvas'
~~~
{: .output}

If you wanted to specify the module name for calling this function, you could change your `__init__.py`.

~~~
import molecool.measure
~~~
{: .language-python}

Then, when you call the function, you must use `molecool.measure.canvas()`.

We will stick with our `from .measure` command. However, it is generally considered bad practice to use a `*` on imports. 


{% include links.md %}
[Python's documentation]: https://docs.python.org/3/tutorial/modules.html
[setup]: https://molssi-education.github.io/CMS-Python-DevOps/setup.html
[numpy]: https://github.com/numpy/numpy
[scipy]: https://github.com/scipy/scipy
[scikit-learn]: https://github.com/scikit-learn/scikit-learn
[CMS CookieCutter]: https://github.com/MolSSI/cookiecutter-cms
[Install cookiecutter]: https://cookiecutter.readthedocs.io/en/latest/installation.html
[setuptools]: https://packaging.python.org/key_projects/#setuptools
[helpful guide]: https://github.com/choderalab/software-development/blob/master/LICENSING_GUIDELINES.md
