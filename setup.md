---
title: "Setup"
---

This setup tutorial will walk you through installing the software you will need for this workshop. We will cover the following topics. Click on a particular topic to skip to that section.

1. [Installing Python using Anaconda](#python_install)
2. [Creating a Python environment using `conda`](#python_environment)
3. [Installation of cookiecutter](#cookiecutter)
4. [Creating a GitHub Account](#github_account)
5. [Installing and Configuring git](#git_configuration)

## Installing Python Using Anaconda <a name="python_install"></a>

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

1. Open [https://www.anaconda.com/download] with your web browser.

2. Download the Python 3 installer for Windows.

3. Double-click the executable and install Python 3 using _MOST_ of the
   default settings. The only exception is to check the
   **Make Anaconda the default Python** option.

Alternatively, if you are running Windows 10, you can install the
[Windows Subsystem for Linux][wsl-windows]
and follow the Linux tutorial.

### Mac OS X - [Video tutorial][video-mac]

1. Open [https://www.anaconda.com/download]
   with your web browser.

2. Download the Python 3 installer for OS X.

3. Install Python 3 using all of the defaults for installation.

### Linux

Note that the following installation steps require you to work from the shell.
If you run into any difficulties, please request help before the workshop begins.

1.  Open [https://www.anaconda.com/download] with your web browser.

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

`conda` is a general package manager, meaning that it can install dependencies and packages in languages besides Python, unlike `pip` (which is Python's package manager). Both `pip` and `conda` can be used to install packages.

### Python environments <a name="python_environment"></a>
A `conda` environment contains a specific collection of packages you have installed. This means that packages are isolated, and installed only for a specific environment -- you can have several environments each with different installed packages, or different versions of installed packages in different environments.

It's considered a best practice to create a new Python environment for each project you work on.

To create an environment for this project using `conda`,

~~~
$ conda create --name molssi_devops python=3.6
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
$ conda install numpy
~~~
{: .language-bash}

Further, the desired version of NumPy can be specified:

~~~
$ conda install numpy=1.15
~~~
{: .language-bash}

## CookieCutter Installation <a name="cookiecutter"></a>

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

## Create GitHub Account <a name="github_account"></a>
Create an account on [github.com]. Remember your username and password for configuring git in the next section.

## Installing and configuring git <a name="git_configuration"></a>

### Installation
[Download and install git for your operating system.]

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
To use Emacs as your text editor, you can do:

~~~
$ git config --global core.editor "emacs"
~~~
{: .bash}

Alternatively, to use Vim as your text editor, do:

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

Finally, we want to upload an ssh key to GitHub so that it doesn't ask for our password every time we try to do something.

Check for existing keys using:

~~~
$ ls -al ~/.ssh
~~~
{: .bash}

If you see something like `id_rsa.pub`, then you don't need to generate a new key.
Otherwise, do:

~~~
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
~~~
{: .bash}

~~~
Generating public/private rsa key pair.
Enter a file in which to save the key (/Users/you/.ssh/id_rsa): (Press enter)
Enter same passphrase again: (Type passphrase again)
~~~
{: .output}

On a Mac, do:

~~~
$ eval "$(ssh-agent -s)"
~~~
{: .bash}

~~~
Agent pid 59566
~~~
{: .output}

If using macOS Sierra 10.12.2 or later, also add this to the end of ~/.ssh/config

~~~
Host *
 AddKeysToAgent yes
 UseKeychain yes
 IdentityFile ~/.ssh/id_rsa
~~~

~~~
$ ssh-add -K ~/.ssh/id_rsa
~~~
{: .bash}

On a Windows machine, do:

~~~
$ eval $(ssh-agent -s)
~~~
{: .bash}

~~~
Agent pid 59566
~~~
{: .output}

~~~
$ ssh-add ~/.ssh/id_rsa
~~~
{: .bash}


On Linux, do:

~~~
$ eval "$(ssh-agent -s)"
~~~
{: .bash}

~~~
Agent pid 59566
~~~
{: .output}

~~~
$ ssh-add ~/.ssh/id_rsa
~~~
{: .bash}

Now copy the SSH key to your clipboard:

On Mac:

~~~
$ pbcopy < ~/.ssh/id_rsa.pub
~~~
{: .bash}

On Windows:

~~~
$ clip < ~/.ssh/id_rsa.pub
~~~
{: .bash}

On Linux:

~~~
$ sudo apt-get install xclip
$ xclip -sel clip < ~/.ssh/id_rsa.pub
~~~
{: .bash}


Now we will upload the ssh key to GitHub.

Go to GitHub using a web browser, click on your user image on the top right, and then select “settings” from the drop-down menu.

Click “SSH and GPG keys” on the left.

Click “New SSH key on the top right.

Add a title that will remind you which machine this is for, then paste the key into the “Key” field.

Click “Add SSH key”

Alternatively, if you don't want to setup ssh keys, you can decrease the number of times git asks you for your password by using:

~~~
$ git config --global credential.helper cache
~~~


### Conclusion
At the end of this set-up, you should have created a Python environment (`molssi_devops`) which has Python 3.6, `numpy`, and `cookiecutter` installed. You should also have installed and created an account on GitHub and configured git.


[anaconda]: https://www.anaconda.com
[https://www.anaconda.com/download]: https://www.anaconda.com/download
[Download and install git for your operating system.]: https://git-scm.com/downloads
[python]: https://python.org
[github.com]: https://github.coms
[video-mac]: https://www.youtube.com/watch?v=TcSAln46u9U
[video-windows]: https://www.youtube.com/watch?v=xxQ0mzZ8UvA
[wsl-windows]: https://docs.microsoft.com/en-us/windows/wsl/install-win10
[CMS CookieCutter]: https://github.com/MolSSI/cookiecutter-cms
