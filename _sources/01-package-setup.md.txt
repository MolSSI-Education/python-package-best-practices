# Python Package Set-Up


```{admonition} Overview
:class: overview

Questions:

* What is the layout of a Python package?
* How can I quickly create the structure of a Python package?
* What license should I choose for my project?

Objectives:

- Explain Python package structure.
- Use the CMS CookieCutter to build a Python package.

```

For this workshop,
we are going to create a Python package that performs analysis and creates visualizations for molecules.
We will start with a Jupyter Notebook that has some functions and analysis.
(You should have downloaded the Jupyter Notebook during setup ([Set Up](setup.md)). 

The idea is that we would like to take this Jupyter Notebook
and convert the functions we have created into a Python package.
That way, if anyone (a lab-mate, for example) would like to use our functions,
they can do so by installing the package and importing it into their own scripts.

To start, we will first use a tool called [CookieCutter](https://cookiecutter.readthedocs.io/en/latest/),
which will set up a Python package structure and several tools we will use during the workshop.

## Examples of Python package structure
If you look at the GitHub repositories for several large Python packages such as [numpy](https://github.com/numpy/numpy), [scipy]( https://github.com/scipy/scipy), or [scikit-learn](https://github.com/scikit-learn/scikit-learn), you will notice a lot of similarities between the directory layouts of these projects.

Having a similar way to lay out Python packages allows people to more easily understand and contribute to your code.

## Creating a Python package using CookieCutter
To create a skeletal structure for our project, we will use the MolSSI Computational Molecular Science (CMS) CookieCutter.
The [CMS CookieCutter](https://github.com/MolSSI/cookiecutter-cms) is a special cookiecutter created specifically by MolSSI to use the tools and services we recommend in developing a Python project.

CookieCutter will not only create our directory layout, but will also set up many tools we will use including testing, continuous integration, documentation, and version control using git.
We will discuss what all of these are later in the workshop.

### Obtaining CookieCutter

You should have the general CookieCutter installed, according to the directions given in the setup ([Set Up](setup.md)) portion of this workshop.
If you do not, please navigate to setup ([Set Up](setup.md)) and follow the instructions given there.

### Running CookieCutter
Navigate to the `molssi_best_practices` directory created during setup ([Set Up](setup.md)).
(CookieCutter will generate the new project in a subdirectory.)
Run the [CMS CookieCutter](https://github.com/MolSSI/cookiecutter-cms) to start your project:

````{tab-set-code} 

```{code-block} shell
 cookiecutter gh:molssi/cookiecutter-cms
```
````

This command runs the cookiecutter software (`cookiecutter` in the command)
and tells cookiecutter to look at GitHub (`gh`) in the repository under `molssi/cookiecutter-cms`.
This repository contains a template that cookiecutter uses to create your project,
once you have provided some starting information.


:::{admonition} Cookiecutter Template Location
:class: tip

When we use the command `cookiecutter gh:molssi/cookiecutter-cms`, 
we are using the Cookiecutter tool and telling it to use the GitHub repository `https://github.com/molssi/cookiecutter-cms` as a template.

The `gh` is for GitHub, and the `molssi/cookiecutter-cms` is the repository name.

You could point to any location where there is a Cookiecutter template,
including files on your local file system or other online repositories.

:::


You will see an interactive prompt that asks questions about your project.
Here, the prompt appears first, followed by the default value in square brackets.
The first question will be on your project name.
You have very cleverly decided to give it the name `molecool`
(it's like molecule, but with `cool` instead, because of your cool visualizations - get it?)

Answer the questions according to the following.
If nothing is given after the colon (`:`), hit enter to use the default value.

````{tab-set-code} 

```{code-block} shell
project_name [ProjectName]: molecool
repo_name [molecool]:
first_module_name [molecool]: functions
author_name [Your name (or your organization/company/team)]: *YOUR_NAME_HERE*
author_email [Your email (or your organization/company/team)]: *YOUR_EMAIL_ADDRESS_HERE*
description [A short description of the project (less than one line).]: A Python package for analyzing and visualizing xyz files.

Select open_source_license:
1 - MIT
2 - BSD-3-Clause
3 - LGPLv3
4 - Not Open Source
Choose from 1, 2, 3, 4 (1, 2, 3, 4) [1]: 2

Select dependency_source:
1 - Prefer conda-forge with pip fallback
2 - Prefer default anaconda channel with pip fallback
3 - Dependencies from pip only (no conda)

Choose from 1, 2, 3 (1, 2, 3) [1]:

Select include_ReadTheDocs:
1 - y
2 - n
Choose from 1, 2 (1, 2) [1]:
```

````

### Explanation of CookieCutter Questions

The first two questions are for the project and repository name.
The project name is the name of the project, while the repo name is the name of the folder that CookieCutter will create. Usually, you will leave these two to be the same thing.
The `repo_name` is the name that you will use to import the package you eventually create, and because of that has some rules.
The `repo_name` must be a valid Python module name and cannot contain spaces.

The next choice is about the first module name.
Modules are the `.py` files that contain Python code.
The default for this is the `repo_name`, but we will change this to avoid confusion (the module `molecool.py` in a folder named `molecool` in a folder named `molecool`??).
For now, we'll just name our first module `functions`, and this is where we will put all of our starting functions.

Another thing that CookieCutter checks for is your email address.
Be sure to provide a valid email address to `cookiecutter`.
(It must have an `@` symbol followed by a domain name, or `cookiecutter` will fail.)
Note that your email address is not recorded or kept by the CookieCutter software, itself.
`cookiecutter` inserts your email address into generated files so that people using your software will have contact information for you. 

#### License Choice
Choosing which license to use is often confusing for new developers.
The MIT license (option 1) is a very common license and the default on GitHub.
It allows anyone to use, modify, or redistribute your work with no restrictions (and also no warranty).

Here, we have chosen the `BSD-3-Clause`.
The `BSD-3-Clause` license is an open-source, permissive license (meaning that few requirements are placed on developers of derivative works), similar to the MIT license.
However, it adds a copyright notice with your name and requires redistributors of the code to keep the notice.
It also prohibits others from using the name of the project or its contributors to promote derived products without written consent.

You can see more detailed information on each license at [choosealicense.com](https://choosealicense.com) or by clicking the links below:
1. [MIT License](https://choosealicense.com/licenses/mit/)
1. [BSD-3-Clause](https://choosealicense.com/licenses/bsd-3-clause/)
1. [LGPLv3](https://choosealicense.com/licenses/gpl-3.0/)
1. Not Open Source - In this case, the cookiecutter will not generate a license.
   You can add a custom license, or choose to not add a license.
   If there is no license in a repository, you should assume that the project is **not** open source, and [you cannot modify or redistribute the software](https://choosealicense.com/no-permission/).

For most of your projects, it is likely that the license you choose won't matter a great deal.
However, remember that if you ever want to change a license, you may have to get permission of all contributors.
So, if you ever start a project that becomes popular or has contributors, be sure to decide your license early!

```{admonition} Types of Open-Source Licenses
:class: info

 Open-source licenses can either be 'permissive' or 'copy-left'.
 Copy-left licenses require that derivative works also be open source.
 Out of the choices given above, MIT and BSD-3-Clause are permissive, while LGPLv3 is a copyleft license.

 We recommend that you spend some time reading about licensing.
 One place to start is this [helpful guide]( https://github.com/choderalab/software-development/blob/master/LICENSING_GUIDELINES.md) from the Chodera Lab or the website [choosealicense.com](https://choosealicense.com).  
```

#### Dependency Source
This determines some things in the setup for what will be used to install dependencies for testing.
This mostly has consequences for the section on [Continuous Integration](../08-CI/index.html).
We have chosen to install dependencies from Anaconda with pip fallback.
Don't worry too much about this choice for now.

#### Support for ReadTheDocs
This option is to choose whether you would like files associated with the documentation hosting service 
[ReadTheDocs](https://readthedocs.org/).
Choose "yes" for this workshop.

### Reviewing directory contents
Now we can examine the project layout CookieCutter has set up for us.
Navigate to the newly created `molecool` directory.

````{tab-set-code} 

```{code-block} shell   
cd molecool
```
````

You should see the following directory structure.

```
.
├── CODE_OF_CONDUCT.md              <- Code of Conduct for developers and users
├── LICENSE                         <- License file
├── MANIFEST.in                     <- Packaging information for pip
├── README.md                       <- Description of the project which GitHub will render
├── molecool                        <- Basic Python Package import file
│   ├── __init__.py                 <- Basic Python Package import file
│   ├── functions.py                <- Starting package module
│   ├── data                        <- Sample additional data (non-code) which can be packaged. Just an example, delete in production
│   │   ├── README.md
│   │   └── look_and_say.dat
│   └── tests                       <- Unit test directory with sample tests
│       ├── __init__.py
│       └── test_molecool.py
├── devtools                        <- Deployment, packaging, and CI helpers directory
│   ├── README.md
│   ├── conda-envs                  <- Conda environments for testing
│   │   └── test_env.yaml
│   └── scripts
│       └── create_conda_env.py     <- OS agnostic Helper script to make conda environments based on simple flags
├── docs                            <- Documentation template folder with many settings already filled in
│   ├── Makefile
│   ├── README.md                   <- Instructions on how to build the docs
│   ├── _static
│   │   └── README.md
│   ├── _templates
│   │   └── README.md
│   ├── api.rst
│   ├── conf.py
│   ├── getting_started.rst
│   ├── index.rst
│   ├── make.bat
│   └── requirements.yaml           <- Documentation building specific requirements. Usually a smaller set than the main program
├── pyproject.toml                  <- Generic Python build system configuration (PEP-517).
├── readthedocs.yml
├── setup.cfg                       <- Near-master config file to make house INI-like settings for Coverage, Flake8, YAPF, etc.
├── setup.py                        <- Your package's setup file for installation with additional options that can be set
├── .codecov.yml                    <- Codecov config to help reduce its verbosity to more reasonable levels
├── .github                         <- GitHub hooks for user contribution, pull request guides, and GitHub Actions CI
│   ├── CONTRIBUTING.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows
│       └── CI.yaml
├── .gitignore                      <- Stock helper file telling git what file name patterns to ignore when adding files
└── .lgtm.yml
```
```{admonition} Visualizing the Directory Structure
:class: note

To visualize your project like above you will use `tree`.
If you do not have `tree`, you can get it using `sudo apt-get install tree` on Linux,
or `brew install tree` on Mac.
Note: `tree` will not show you the helpful labels after `<-` (those were added by us).
```

CookieCutter has created a lot of files!

If you have set up VSCode as your text editor as described in the setup ([Set Up](setup.md)), you can open a VSCode project that contains the newly created `molecool` directory by typing

````{tab-set-code} 

```{code-block} shell
code .
```
````
This will open a new VSCode window with your current directory (`.`) the `molecool` directory as the root directory.

The files that Cookiecutter has created for us can be thought of as three sections.
In the top level of our project, we have a folder for tools related to development (`devtools`),
documentation (`docs`) and to the package itself (`molecool`).
We will first be working in the `molecool` folder to build our package, and adding more things later.

```
...
├── molecool
│   ├── __init__.py                 <- Basic Python Package import file
│   ├── functions.py                <- Starting package module
│   ├── data                        <- Sample additional data (non-code) which can be packaged
│   │   ├── README.md
│   │   └── look_and_say.dat
│   ├── tests                       <- Unit test directory with sample tests
│   │   ├── __init__.py
│   │   └── test_functions.py
```

This the only folder we actually have to work with to build our package.
The other folders relate to "best practices",
which do not technically have to be used in order for your package to be working (but you should do them,
and we will talk about them later).
You could build this directory structure by hand, but we have just used `cookiecutter` to set it up for us.
This directory will contain all of our Python code for our project,
as well as sample data (in the `data` folder), and tests (in the `tests` folder.)

```{admonition} Packages and modules
:class: info

What 'packages' or 'modules' are in Python may be confusing.
In general, 'module' refers to a single `.py` file containing Python definitions and statements.
It may be imported for use in another module or script.
The module name is determined by the file name.
A function defined in a module is used (once the module is imported) using the syntax `module_name.function_name()`.

'Package' refers to a collection of Python modules.
The package may also have an `__init__.py` file.
To read more about Python packages vs. modules, check out [Python's documentation](https://docs.python.org/3/tutorial/modules.html).

```

## The `molecool` directory
We will first examine some files in the `molecool` directory.
This is the directory that contains our package code.

### The `__init__.py` file

The `__init__.py` file is a special file recognized by the Python interpreter which makes a directory into a package.
This file can be blank in some cases, however, we will use it to define how the user interacts with the functions in our package.

Contents of `molecool/molecool/__init__.py`:
````{tab-set-code} 

```{code-block} python
"""A Python package for analyzing and visualizing xyz files."""

# Add imports here
from .functions import *

from ._version import __version__
```
````


The very first section of this file contains a string opened and closed with three quotations.
This is a [docstring](https://www.python.org/dev/peps/pep-0257/), and has a short description of the file.

The section we will be concerned with is under `# Add imports here`.
This is how we define the way functions from modules are used.

In particular, the line

````{tab-set-code} 

```{code-block} python
from .functions import *
```
````


goes to the `functions.py` file, and brings everything that is defined there into the file.
When we use our function defined in `functions.py`,
that means we will be able to just say `molecool.canvas()` instead of giving the full path `molecool.functions.canvas()`.
If that's confusing, don't worry too much for now.
We will be returning to `__init__.py` in a few minutes.
For now, just note that it exists and makes our directory into a package.

### Our first module
Once inside the `molecool` folder (`molecool/molecool`), examine the files that are there.
View the module (`functions.py`) in a text editor.
We see a few things about this file.
The top begins with a description of this module surrounded by three quotations (`"""`).
Right now, that is the file name, followed by our short description,
then the sentence "Handles the primary functions".
We will change this to be more descriptive later.
CookieCutter has also created a placeholder function called `canvas`.
At the start of the `canvas` function, we have a `docstring` (more about this in [documentation]),
which describes the function.

We will be moving all of the functions we defined in the Jupyter notebook into python modules (`.py` files) like these.

````{admonition} Before proceeding, make sure your pip and setuptools packages are up-to-date
:class: alert

````{tab-set-code}
```{code-block} shell
conda update pip setuptools
```

````

### Installing from local source.

You may be accustomed to `pip` automatically retrieving packages from the internet.

To develop this package, we will want to use what is called "development mode", or an "editable install",
so that we can try out our functions and package as we develop it.
We access development mode using the `-e` option to `pip`.

#### Reviewing the generated config files
Return to the top directory (`molecool`).
Two of the files CookieCutter generated are `pyproject.toml` and `setup.cfg`.
These are the configuration files for our packaging and testing tools.
`pyproject.toml` tells [setuptools](https://packaging.python.org/key_projects/#setuptools) about your package (such as the name and version) as well as which code files to include.
We'll be using this file in the next section.

#### Installing your package
A development install will allow you to import your package and use it from anywhere on your computer.
You will then be able to import your package into scripts in the same way you import `matplotlib` or `numpy`. 

A development installation inserts a link to your project into your Python
`site-packages` folder so that updates are immediately available the next time
you launch Python, without having to reinstall your package.
To find the location of your site-packages folder, you can check your Python path.
Open Python (type `python` into your terminal window), and type


````{tab-set-code} 

```{code-block} python
>>> import sys
>>> sys.path
```
````


This will give a list of locations python looks for packages when you do an import.
One of the locations should end with `python3.11/site-packages`.
The site packages folder is where all of your installed packages for a particular environment are located.

To do a development mode install, type

````{tab-set-code} 

```{code-block} shell
pip install -e .
```
````


Here, the `-e` indicates that we are installing this project in *editable* mode
(i.e. setuptools
[*development mode*](https://setuptools.readthedocs.io/en/latest/userguide/commands.html#develop-deploy-the-project-source-in-development-mode)),
while `.` indicates to install from the local directory (you could also specify a path here).
Now, if you examine the contents of your site packages folder,
you should see a link to `molecool` (`molecool.egg-link`).
The folder has also been added to your path (check `sys.path` again.)

Now, we can use our package from any directory, similar to how we can use other installed packages like `numpy`.
Open Python, and type

````{tab-set-code} 

```{code-block} python
>>> import molecool
>>> molecool.canvas()
```
````


This should print a quote.

````{tab-set-code} 

```{code-block} output
'The code is but a canvas to our imagination.\n\t- Adapted from Henry David Thoreau'
```
````


This should work from anywhere on your computer.


````{admonition} Check Your Understanding
:class: exercise

What happens if we use `conda deactivate` and attempt to execute the code above?

What if we switch directories?

```{admonition} Solution
:class: dropdown solution

If you are in the project directory, the code will still work. However, it will not work in any other location.
```

````

:::{admonition} Final Repository State
:class: tip

You can see the final state of the repository after this section [here](https://github.com/MolSSI-Education/molecool/tree/e703f52e9381b051415264927d2bde6c1cebb52a).

You can also download a zip of the repository [here](https://github.com/MolSSI-Education/molecool/archive/refs/tags/cookiecutter-end.zip).

:::


## Key Points

```{admonition} Key Points
:class: key

* There is a common way to structure Python packages.
* You can use the CMS CookieCutter to quickly create the layout for a Python package.
```
