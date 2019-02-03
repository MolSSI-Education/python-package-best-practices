---
title: "Making a Open-Source Python Module"
teaching: 40
exercises: 30
questions:
- "How do I name and license a project?"
- "How do we setup a new repository?"
objectives:
- "Describe the why to use a hosted version control system such as GitHub."
- "Describe the purpose of open-source."
- "Describe what makes good and bad project names"
keypoints:
- "The importance of repository location and license choices."
---

This episode describes how to go about starting a open-source Python
module on Github. The reasons for choosing open-source, git vs. github,
and choosing an appropriate license are discussed.

## Why GitHub for a Python Module?

1. Explain role of git, and git vs. GitHub
2. Why GitHub? Why public by default?

## Project Preliminaries
This section may be made as either presentation slides or a webpage

1. **Project/Repository Name**
  - How to pick a good name
  - Uniqueness
  - Googleableness
2. **Licenses**
  - GPL vs LGPL
  - Prefer BSD-3C, but others acceptable
  - Copyright (just mention that it depends on university and employer)
3. **Programming Language**
  - How might this influence license choice

## Using Anaconda and conda

For Python development, we recommend the use of [Anaconda](https://www.anaconda.com/download/#macos). Anaconda is a free and open source distribution of Python. Use of *Anaconda* with its package manager, *conda*, greatly simplifies package installation and environment management.

*conda* is a general package manager, meaning that it can install dependicies and packages in languages besides Python, unlike *pip* (which is Python's package manager). Both *pip* and *conda* can be used within a Python environment to install packages.

### Python environments
A conda environment is a directory that contains a specific collection of conda packages you have installed. This means that packages are isolated, and installed only for a specific environment -- you can have several environments each with different installed packages, or different versions of installed packages in different environments.

To create an environment for this project using *conda*,

`conda create --name molssi_devops python=3.6`

For other projects, you should replace `molssi_devops` with a descriptive name for your project. *conda* also allows you to specify the python version to use with the environment. Here, `python=3.6` specifies that we want to use Python 3.6 in this environment. Executing this command will list the environment location and a list of Python packages to be installed. Choose *y(es)* when prompted.

Activate the environment using the command

`conda activate molssi_devops`

If you wanted to create an environment for testing your code in Python 2.7, for example, you could use the command

`conda create --name molssi_devops27 python=2.7`

When this environment is activated, Python 2.7 will be used instead of Python 3.6.

To see a list of all your environments

`conda info --envs`

To deactivate an environment, type `conda deactivate`

## Package installation using conda
Using *conda*, we can install packages to our environments. **Note**: Make sure you have activated the environment where you want to install packages.

To list all the Python packages installed in an environment, first activate it, then type

`conda list`

Packages can be installed using the `conda install package_name` command. For example, to install NumPy,

`conda install numpy`

Further, the desired version of NumPy can be specified:

`conda install numpy=1.15`

## Creating a New Repository on GitHub

1. **Project name and organization**
2. **Git Ignore**
    - Pick your programming language (important later)
3. **Public vs Private**
    - Free private for academics
    - Suggest open source
4. **Initial README**

## Initial cloning

1. Perform the initial git clone



GitHub's official [documentation](https://help.github.com/articles/create-a-repo/).




{% include links.md %}
