---
title: "Setup"
---

This setup tutorial will walk you through installing the software you will need for this workshop.

For this workshop, you will need to have Python installed. We recommend and assume you will have Python installed using Anaconda, and will be talking about package management using conda and Anaconda (see instructions below). You will also need to download workshop materials, and configure git.

We will cover the following topics. Click on a particular topic to skip to that section.

1. [Downloading workshop materials](#materials_download)
1. [Downloading a text editor](#text_editor)
2. [Installing Python using Anaconda](#python_install)
3. [Creating a Python environment using `conda`](#python_environment)
4. [Installation of cookiecutter](#cookiecutter)
5. [Creating a GitHub Account](#github_account)
6. [Installing and Configuring git](#git_configuration)

## Workshop materials <a name="materials_download"></a>

In this workshop, we will be moving code from a Jupyter notebook into a Python package that we can install and import into other scripts.

- Create a folder on your desktop called `molssi_best_practices`.
- Download the starting workshop materials [here](./data/starting_material.zip)
    - This will be a `zip` file. You should unzip this file into the folder you have created on your desktop. After downloading and unzipping, verify that you see the following directory structure.
    ~~~
    molssi_best_practices
    └── starting_material  
            ├── data
            │   ├── pdb
            │   │   ├── 1bna.pdb
            │   │   ├── benzene.pdb
            │   │   └── water.pdb
            │   └── xyz
            │       ├── 1bna.xyz
            │       ├── benzene.xyz
            │       └── water.xyz
            └── starting_notebook.ipynb
    ~~~

## Choosing a text editor <a name="text_editor"></a>
You will need an editor for Python files for this workshop. If you do not have a prefered text editor, we recommend [Visual Studio Code](https://code.visualstudio.com/)

## Installing Python Using Anaconda <a name="python_install"></a>

If you already have a Python 3 verison Anaconda or MiniConda installed, you can skip this step.

[Python][python] is a popular language for scientific computing, and great for
general-purpose programming as well.  We recommend using Python with the conda package manager. 
You can obtain Python and conda by either installing [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (minimal installer) or [Anaconda](https://www.anaconda.com/products/individual). Anaconda comes bundled with many more python packages than miniconda. Anaconda is more user-friendly. If you are uncomfortable navigating the terminal, or are unsure of which you need, install Anaconda.

The installer for Anaconda can be found on [this page](https://www.anaconda.com/products/individual). Choose the appropriate version for your Operating System.

Throughout the rest of this set-up, we will assume that you are using the `conda` package manager.

Please set up your python environment at
as far in advance as possible.  If you encounter problems with the
installation procedure, ask your workshop organizers via e-mail for assistance so
you are ready to go as soon as the workshop begins.


## Using Anaconda and conda

Use of [Anaconda] with its package manager, `conda`, greatly simplifies package installation and environment management.

`conda` is a general package manager, meaning that it can install dependencies and packages in languages besides Python, unlike `pip` (which is Python's package manager). Both `pip` and `conda` can be used to install packages.

### Python environments <a name="python_environment"></a>
A `conda` environment contains a specific collection of packages you have installed. This means that packages are isolated, and installed only for a specific environment -- you can have several environments each with different installed packages, or different versions of installed packages in different environments.

It's considered a best practice to create a new Python environment for each project you work on.

This section uses the command line interface (CLI) to create an environment using `conda`. If you are on Mac or Linux, you will type these commands into your terminal.  If you are on Windows, you should use the Anaconda Prompt. 

To create an environment for this project using `conda`,

~~~
$ conda create --name molssi_best_practices python=3.7
~~~
{: .language-bash}

For other projects, you should replace `molssi_best_practices` with a descriptive name for your project. `conda` also allows you to specify the python version to use with the environment. Here, `python=3.7` specifies that we want to use Python 3.7 in this environment. Executing this command will list the environment location and a list of Python packages to be installed. Choose `y(es)` when prompted.

Activate the environment using the command

~~~
$ conda activate molssi_best_practices
~~~
{: .language-bash}

Once you've activated an environment, the name of the environment will be in parenthesis at the front of your command line prompt.

If you wanted to create an environment for testing your code in Python 3.5, for example, you could use the command (Do not execute this, it's just an example.)

~~~
$ conda create --name molssi_35 python=3.5
~~~
{: .language-bash}

When this environment is activated, Python 3.5 will be used instead of Python 3.7.

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

~~~
$ conda activate molssi_best_practices
~~~
{: .language-bash}

To list all the Python packages installed in an environment, first activate it, then type

~~~
$ conda list
~~~
{: .language-bash}

Packages can be installed using the `conda install package_name` command. For example, to install NumPy,

~~~
$ conda install numpy
~~~
{: .language-bash}

Further, the desired version of NumPy can be specified:

~~~
$ conda install numpy=1.15
~~~
{: .language-bash}

For this workshop, you will need to install the following packages into your environment
- NumPy
- Matplotlib
- jupyter

You can install all of them in one line with

~~~
$ conda install numpy matplotlib jupyter
~~~
{: .language-bash}


## CookieCutter Installation <a name="cookiecutter"></a>

For this workshop, we will create the structure of our Python package using the [CMS CookieCutter]. Please have this package installed **in your `molssi_best_practices` environment**.

First, switch to your environment for this workshop if you are not in it.

~~~
$ conda activate molssi_best_practices
~~~
{: .language-bash}

Install the general cookiecutter with the following commands.

~~~
$ conda config --add channels conda-forge
$ conda install cookiecutter
~~~
{: .language-bash}

## Installing and configuring git <a name="git_configuration"></a>

### Installation
Install git. You can install using conda

~~~
$ conda install git
~~~
{: .language-bash}

### Configuring Git

The first time you use Git on a particular computer, you need to configure some things.

First, you should set your identity.
One of the most important things that version control like Git does is to keep track of who changes what.
This helps repository maintainers coordinate the efforts of all the people who contribute to the project.
Most importantly, it makes it easier to figure out who to blame when something goes wrong.
You can provide git your name and contact information with the following commands:

~~~
$ git config --global user.name "<Firstname> <Lastname>"
$ git config --global user.email "<email address>"
~~~
{: .bash}

Next, you might want to change the Git text editor.
As we will see later, certain Git commands will open text files.
When this happens, Git will use your environment's default text editor, which might not be the editor you are most comfortable using.
Using configuration commands, you can tell Git to use your favorite editor.

A popular chose is Vim. To use Vim, do

~~~
$ git config --global core.editor "vim"
~~~
{: .bash}

A more complete list of possible editors is available [here](http://swcarpentry.github.io/git-novice/02-setup/index.html).

You can check the configuration commands that you have set using:

~~~
$ git config --list
~~~
{: .bash}

## Create GitHub Account <a name="github_account"></a>
Create an account on [github.com]. Remember the user name and password. If you are making a GitHub account, please remember that your username should be *recognizable* and *professional*.

### Conclusion
At the end of this set-up, you should have created a Python environment (`molssi_best_practices`) which has Python 3.7, `numpy`, `matplotlib`, `jupyter`, and `cookiecutter` installed. You should also have installed and created an account on GitHub and configured git.


[anaconda]: https://www.anaconda.com
[https://www.anaconda.com/download]: https://www.anaconda.com/download
[Download and install git for your operating system.]: https://git-scm.com/downloads
[python]: https://python.org
[github.com]: https://github.coms
[video-mac]: https://www.youtube.com/watch?v=TcSAln46u9U
[video-windows]: https://www.youtube.com/watch?v=xxQ0mzZ8UvA
[wsl-windows]: https://docs.microsoft.com/en-us/windows/wsl/install-win10
[CMS CookieCutter]: https://github.com/MolSSI/cookiecutter-cms
