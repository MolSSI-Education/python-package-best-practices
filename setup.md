---
title: "Setup"
---

This setup tutorial will walk you through installing the software you will need for this workshop.

For this workshop, you will need to have Python installed. We recommend and assume you will have Python installed using Anaconda, and will be talking about package management using conda and Anaconda (see instructions below). You will also need to download workshop materials, and configure git.

We will cover the following topics. Click on a particular topic to skip to that section.

1. [Downloading workshop materials](#materials_download)
1. [Installing Python using Anaconda](#python_install)
1. [Downloading a text editor](#text_editor)
1. [Creating a Python environment using `conda`](#python_environment)
1. [Installation of cookiecutter](#cookiecutter)
1. [Creating a GitHub Account](#github_account)
1. [Installing and Configuring git](#git_configuration)

## Workshop materials <a name="materials_download"></a>

In this workshop, we will be moving code from a Jupyter notebook into a Python package that we can install and import into other scripts.

## Download the starting workshop materials [here](./data/starting_material.zip)

- Create a folder on your desktop called `molssi_best_practices`.
- The file you download as starting materials will be a `zip` file. You should unzip this file into the folder you have created on your desktop. After downloading and unzipping, verify that you see the following directory structure.
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

## Installing Python Using Anaconda <a name="python_install"></a>

If you already have a Python 3 verison Anaconda or MiniConda installed, you can skip this step.

[Python][python] is a popular language for scientific computing, and great for
general-purpose programming as well.  We recommend using Python with the conda package manager. 
You can obtain Python and conda by either installing [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (minimal installer) or [Anaconda](https://www.anaconda.com/products/individual). Anaconda comes bundled with many more python packages than miniconda. Anaconda is more user-friendly. If you are uncomfortable navigating the terminal, or are unsure of which you need, install Anaconda. Anaconda will also come bundled with the text editor Visual Studio Code, so you will not need to install a text editor in the next step.

The installer for Anaconda can be found on [this page](https://www.anaconda.com/products/individual). Choose the appropriate version for your Operating System.

Throughout the rest of this set-up, we will assume that you are using the `conda` package manager.

Please set up your python environment at
as far in advance as possible.  If you encounter problems with the
installation procedure, ask your workshop organizers via e-mail for assistance so
you are ready to go as soon as the workshop begins.

> ## Windows Subsytem for Linux (WSL)
> 
> If you plan to continue developing in the future and you utilize the Windows Operating system, you may want to consider installing the WSL.
> The WSL will allow you to run a Linux based terminal from your Windows machine, which can aid in the development and running of code.
> The WSL can connect to VS code for easy development.
> You can find instructions to install the WSL on the [Windows Documentation](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
{: .callout}

## Choosing a text editor <a name="text_editor"></a>
You will need an editor for Python files for this workshop. If you do not have a prefered text editor, we recommend [Visual Studio Code](https://code.visualstudio.com/). If you installed a recent version of Anaconda, you will have VSCode installed already. You should be able to open it from the Anaconda Navigator window. If you have another prefered text editor, you should use that for the workshop.

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
- jupyter notebook

Packages available to Conda are stored within `channels`.
Some packages are not stored in the default Conda channel, so we need to specify where Conda can find the package with `-c` followed by a channel name in our install command.
The `NumPy` and `Matplotlib` packages are both stored within the default Conda channel, so we do not need to include a `-c`.
The `jupyter notebook` package is in the `conda-forge` channel, so we include the syntax `-c conda-forge` in our install command.

~~~
$ conda install numpy matplotlib
$ conda install -c conda-forge notebook
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
$ git config --global user.name "YOUR NAME"
$ git config --global user.email "YOUR_EMAIL"
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

To use VSCode as your core editor, do

~~~
$ git config --global core.editor "code --wait"
~~~
{: .language-bash}

You can check the configuration commands that you have set using:

~~~
$ git config --list
~~~
{: .bash}

## Create GitHub Account <a name="github_account"></a>
Create an account on [github.com] if you do not have one already. Remember the user name and password. If you are making a GitHub account, please remember that your username should be *recognizable* and *professional*.

The next step is to verify your email address through Github.
If you do not verify your email address, you will not be able to perform many of the actions covered in this workshop.

## Accessing GitHub through the Command Line
To utilize github from the command line, you will need to
[provide GitHub with an SSH public key](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)
or generate a GitHub Personal Access Token (PAT).


To create a PAT:
1. Click the profile photo option in the upper right hand corner of any page, then click `Settings`.
2. On the settings page, look on the left sidebar and click `Developer settings`.
3. In the new left sidebar, click `Personal access tokens`.
4. Click the `Generate new token` button to bring up the options for your token.
You can create different access tokens for different actions on Github.
For the purposes of this workshop, you should only need to select the `repo` and `workflow` options, the two at the top.
You can return to the settings page at a later time to add or remove scopes from your token.
5. Once you have checked this box, click the `Generate token` button at the bottom of the set of options.
Make sure to copy the access token as Github will not let you see it again once you have navigated from the page.
This token will be used in place of your password when you utilize the command line to access Github repositories.

By default, you will be required to enter your PAT every time you want to push to a github repository.
This can become tedious if you are making multiple pushes over a short period.
Git has options to cache your PAT in local memory for a specified time period, meaning you only have to re-enter your password if enough time has passed.
If you would like to setup caching you have to take different steps depending on your operating system.

For Linux and Windows WSL, you simply run
```
git config --global credential.helper cache
```
which will cache your token in memory for 15 minutes after it has been entered.

If you would like to modify the length of time a token is cached, you can use the command:
```
git config --global credential.helper 'cache --timeout=3600'
```
where the value after timeout is the length of time to cache in seconds (1 hour in this example).

For Mac OS, you need a separate tool, `osxkeychain` to cache your token.
You can check if you have it installed already by running
```
git credential-osxkeychain
```
If you do not have it installed, you should be prompted to install it by the console.
Then run
```
git config --global credential.helper osxkeychain
```
to setup caching for your operating system.
Your PAT will be stored locally on your machine and encrypted by the operating system.

If you would like to store the PAT locally and have git automatically reference it on Linux/WSL, you can specify that git should store your PAT.
This can be done through the command
```
git config --global credential.helper 'store --file ~/.my-credentials'
```
where `~/.my-credentials` is a filepath to a file git should store your PAT in.
Note that this is stored as plain text on your machine.

### Conclusion
At the end of this set-up, you should have created a Python environment (`molssi_best_practices`) which has Python 3.7, `numpy`, `matplotlib`, `jupyter`, and `cookiecutter` installed. You should also have downloaded starting material, installed and created an account on GitHub, and configured git.


[anaconda]: https://www.anaconda.com
[https://www.anaconda.com/download]: https://www.anaconda.com/download
[python]: https://python.org
[github.com]: https://github.coms
[CMS CookieCutter]: https://github.com/MolSSI/cookiecutter-cms
