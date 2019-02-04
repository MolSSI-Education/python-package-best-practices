---
title: "Setup"
---

## Installing Python Using Anaconda

[Python][python] is a popular language for scientific computing, and great for
general-purpose programming as well. Installing all of its scientific packages
individually can be a bit difficult, however, so we recommend the all-in-one
installer [Anaconda][anaconda].

Throughout the rest of this set-up, we will assume that you are using [Anaconda] and the `conda` package manager.

Please set up your python environment at
least a day in advance of the workshop.  If you encounter problems with the
installation procedure, ask your workshop organizers via e-mail for assistance so
you are ready to go as soon as the workshop begins.

### Windows - [Video tutorial][video-windows]

1. Open [http://continuum.io/downloads][continuum-windows]
   with your web browser.

2. Download the Python 3 installer for Windows.

3. Double-click the executable and install Python 3 using _MOST_ of the
   default settings. The only exception is to check the
   **Make Anaconda the default Python** option.

Alternatively, if you are running Windows 10, you can install the
[Windows Subsystem for Linux][wsl-windows]
and follow the Linux tutorial.

### Mac OS X - [Video tutorial][video-mac]

1. Open [http://continuum.io/downloads][continuum-mac]
   with your web browser.

2. Download the Python 3 installer for OS X.

3. Install Python 3 using all of the defaults for installation.

### Linux

Note that the following installation steps require you to work from the shell.
If you run into any difficulties, please request help before the workshop begins.

1.  Open [http://continuum.io/downloads][continuum-linux] with your web browser.

2.  Download the Python 3 installer for Linux.

3.  Install Python 3 using all of the defaults for installation.

    a.  Open a terminal window.

    b.  Navigate to the folder where you downloaded the installer

    c.  Type

    ~~~
    $ bash Anaconda3-
    ~~~
    {: .bash}

    and press tab.  The name of the file you just downloaded should appear.

    d.  Press enter.

    e.  Follow the text-only prompts.  When the license agreement appears (a colon
        will be present at the bottom of the screen) hold the down arrow until the
        bottom of the text. Type `yes` and press enter to approve the license. Press
        enter again to approve the default location for the files. Type `yes` and
        press enter to prepend Anaconda to your `PATH` (this makes the Anaconda
        distribution the default Python).

## Using Anaconda and conda

Use of [Anaconda] with its package manager, `conda`, greatly simplifies package installation and environment management.

`conda` is a general package manager, meaning that it can install dependicies and packages in languages besides Python, unlike `pip` (which is Python's package manager). Both `pip` and `conda` can be used to install packages.

### Python environments
A `conda` environment contains a specific collection of packages you have installed. This means that packages are isolated, and installed only for a specific environment -- you can have several environments each with different installed packages, or different versions of installed packages in different environments.

It's considered a best practice to create a new Python environment for each project you work on.

To create an environment for this project using `conda`,

~~~
conda create --name molssi_devops python=3.6
~~~
{: .language-bash}

For other projects, you should replace `molssi_devops` with a descriptive name for your project. `conda` also allows you to specify the python version to use with the environment. Here, `python=3.6` specifies that we want to use Python 3.6 in this environment. Executing this command will list the environment location and a list of Python packages to be installed. Choose `y(es)` when prompted.

Activate the environment using the command

~~~
$ conda activate molssi_devops`
~~~
{: .language-bash}

Once you've activated an environment, the name of the environment will be in parenthesis at the front of your command line prompt.

If you wanted to create an environment for testing your code in Python 2.7, for example, you could use the command

~~~
$ conda create --name molssi_devops27 python=2.7
~~~
{: .language-bash}

When this environment is activated, Python 2.7 will be used instead of Python 3.6.

To see a list of all your environments

~~~
$ conda info --envs
~~~
{: .language-bash}

To deactivate an environment, type

~~~
$ conda deactivate
~~~
{: .language-bash}

### Package installation using conda
Using `conda`, we can install packages to our environments. **Note**: Make sure you have activated the environment where you want to install packages.

To list all the Python packages installed in an environment, first activate it, then type

~~~
$ conda list
~~~
{: .language-bash}

Packages can be installed using the `conda install package_name` command. For example, to install NumPy,

~~~
conda install numpy
~~~
{: .language-bash}

Further, the desired version of NumPy can be specified:

~~~
conda install numpy=1.15
~~~
{: .language-bash}

## CMS CookieCutter Installation

For this workshop, we will create the structure of our Python package using the [CMS CookieCutter]. Please have this package installed **in your `molssi_devops` environment**.

First, switch to your environment for this workshop if you are not in it.

~~~
$ conda activate molssi_devops
~~~
{: .language-bash}

Install the general cookiecutter with the following commands.

~~~
$ conda config --add channels conda-forge
$ conda install cookiecutter
~~~
{: .language-bash}

At the end of this set-up, you should have created a Python environment (`molssi_devops`) which has Python 3.6, `numpy`, and `cookiecutter` installed.



[anaconda]: https://www.continuum.io/anaconda
[continuum-mac]: http://continuum.io/downloads#_macosx
[continuum-linux]: http://continuum.io/downloads#_unix
[continuum-windows]: http://continuum.io/downloads#_windows
[gapminder]: http://gapminder.org
[jupyter]: http://jupyter.org/
[jupyter-install]: http://jupyter.readthedocs.io/en/latest/install.html#optional-for-experienced-python-developers-installing-jupyter-with-pip
[python]: https://python.org
[video-mac]: https://www.youtube.com/watch?v=TcSAln46u9U
[video-windows]: https://www.youtube.com/watch?v=xxQ0mzZ8UvA
[wsl-windows]: https://docs.microsoft.com/en-us/windows/wsl/install-win10
[CMS CookieCutter]: https://github.com/MolSSI/cookiecutter-cms
