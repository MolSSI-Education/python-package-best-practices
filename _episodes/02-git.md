# Introduction to Version Control using Git

```{admonition} Overview
:class: overview

Questions:

* How do I use git to keep a record of my project?

Objectives:

- Explain the purpose of version control.
- Introduce common git commands.
- Understand how to create a commit.
- Understand how to view diffs and see previous versions of files.

```


:::{admonition} Follow Along with This Lesson
:class: tip

To follow along with this lesson, you can complete the previous lessons,
or you can download a pre-made workshop repository that is at the starting 
point.

You will need to make sure that you have `git` installed and configured,
as described in the set-up instructions.

- [Download the pre-made workshop repository as a zip file](https://github.com/MolSSI-Education/molecool/archive/refs/tags/git-start.zip)

Alternatively, download the repository using the command line:

````{tab-set-code} 

```{code-block} shell
git clone https://github.com/MolSSI-Education/molecool.git
git checkout git-start
```
````
:::

## What is version control?

Version control keeps a complete history of your work on a given project.
It facilitates collaboration on projects where everyone can work freely on a part
of the project without overwriting others’ changes.
You can move between past versions and roll back when needed.
Also, you can review the history of your project through commit messages that describe changes in the source code,
and see what exactly has been modified in any given commit.
You can see who made the changes and when it happened.

This is greatly beneficial whether you are working independently or within a
team.

````{admonition} git vs. GitHub
:class: tip

`git` is the software used for version control, while GitHub is a hosting service.
You can use `git` locally (without using an online hosting service), or you can use it with other hosting services such as [GitLab](https://gitlab.com/) or
[BitBucket](https://bitbucket.org/).

Other examples of version control software include Subversion (`svn`) and Mercurial (`hg`).

````

## Making Commits

You should have `git` installed and configured from the setup instructions.

In this section, we are going to  edit files in the Python package that we created earlier and use `git` to track those changes.

First, use a terminal to `cd` into the top directory of the local repository (the outer molecool directory).

In order for `git` to keep track of your project, or any changes in your project,
you must first tell it that you want it to do this.
You must manually create checkpoints in your project if you wish to have points to return to.
If you were not using the CookieCutter, you would first have to initialize your project
(i.e. tell `git` that you were working on a project) using the command `git init`. 

When we ran the CMS CookieCutter, it actually initialized `git` for us,
added our files, and made a commit (how convenient!).
We can see this by typing the following into the terminal on Linux or Mac

````{tab-set-code} 

```{code-block} shell
ls -la
```
````

Here, the `-la` says that we want to list the files in long format (`-l`), and show hidden files (`-a`). 

You should see `.git` in the output. `.git` is a directory where `git` stores the repository data.
This is one way to see that we are in a git repository.

Next, type

````{tab-set-code} 

```{code-block} shell
git status
```
````


````{tab-set-code} 

```{code-block} output
On branch main
nothing to commit, working tree clean
```
````


This tells us that we are on the `main` branch (more about branching later) and that no files have been changed since the last commit.

Next, type
````{tab-set-code} 

```{code-block} shell
git log
```
````


You will get an output resembling the following.
This is something called your git *commit log*.
Whenever you make a version, or checkpoint, of your project,
you will be able to see information about that checkpoint using the `git log` command.
The CookieCutter has already made a commit and written a message for you,
and that is what we look for in this first commit in the log.

````{tab-set-code} 

```{code-block} output
commit 25ab1f1a066f68e433a17454c66531e5a86c112d (HEAD -> main, tag: 0.0.0)
Author: Your Name <your_email@something.com>
Date:   Mon Feb 4 10:45:26 2019 -0500

    Initial commit after CMS Cookiecutter creation, version X.X
```
````


Your version number for the Cookiecutter will depend on when you ran the Cookiecutter and the current released version.

Each line of this log tells you something important about the commit,
or checkpoint, that exists for the project.
In the first line,

```
commit 25ab1f1a066f68e433a17454c66531e5a86c112d (HEAD -> main, tag: 0.0.0)
```


You have a unique identifier for the commit (25ab1...).
You can use this hexadecimal number to reference this checkpoint.

Then, `git` records the name of the author who made the change.

```
Author: Your Name <your_email@something.com>
```

This should be your information.
This way, anyone who downloads this project can see who made each commit.
Note that this name and email address match what you specified when you configured `git` in the setup,
with the name and email address you specified to `cookiecutter` having no effect.

```
Date:   Mon Feb 4 10:45:26 2019 -0500
```

Next, it lists the date and time the commit was made. 

```
    Initial commit after CMS Cookiecutter creation, version 1.0
```

Finally, there will be a blank line followed by a commit message.
The commit message is a message that whoever made the commit chose to write
but should describe the change that took place when the commit was made.
This commit message was written by `cookiecutter` for you.

When we have more commits (or versions) of our code, `git log` will show a history of these commits,
and they will all have the same format discussed above.
Right now, we have only one commit: the one created by the CMS CookieCutter.

## The 3 steps of a commit

Now, we will change some files and use `git` to track those changes.

Let's edit our README file.
Open `README.md` in your text editor of choice.
On line 8, you should see the description of the repository we typed when running `cookiecutter`.

Add the following sentence to your `README.md` under the initial description and save the file.

```
This repository is currently under development. To do installation in development mode, download this repository and type

`pip install -e .`

in the repository directory.
```

### git add, git status, git commit

Making a commit is like making a checkpoint for a particular version of your code.
You can easily return to, or revert to that checkpoint.

To create the checkpoint, we first have to make changes to our project.
We might modify *many* files at a time in a repository.
Thus, the first step in creating a checkpoint (or commit) is to tell `git` which files we want to include in the checkpoint.
We do this with a command called `git add`. This adds files to what is called the *staging area*.

Let's look at our output from `git status` again.

````{tab-set-code} 

```{code-block} output
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```
````


Git even tells us to use `git add` to include what will be committed.
Let's follow the instructions and tell `git` that we want to create a checkpoint
with the current version of `README.md`.

````{tab-set-code} 

```{code-block} shell
git add README.md
```
````


````{tab-set-code} 

```{code-block} shell
git status
```
````


````{tab-set-code} 

```{code-block} output
On branch main
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   README.md
```
````


We are now on the second step of creating a commit.
We have added our files to the staging area.
In our case, we only have one file in the staging area, but we could add more if needed.

To create the checkpoint, or commit, we will now use the `git commit` command.
We add a `-m` after the command for "message".
Whenever you create a commit, you should write a message about what the commit does.

````{tab-set-code} 

```{code-block} shell
git commit -m "update readme to have instructions for developmental install"
```
````

Now when we look at our log using `git log`, we see the commit we just made along with information about the author and the date of the commit.

If you neglect the `-m` option and configure an editor during set-up,
`git` will open the editor for you to compose your commit message.

Let's continue to edit this readme to include more information.
This is a file which will describe what is in this directory.
Open `README.md` in your text editor of choice and add the following to the end.

```
This package requires the following:
  - NumPy
  - matplotlib
```

This file is using a language called
[Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). 


``````{admonition} Check Your Understanding
:class: exercise

Create a commit for the changes we've made to your repository.

`````{admonition} Solution
:class: solution dropdown

To add the file to the staging area and tell `git` we would like to track the changes to the file, we first use the `git add` command.


````{tab-set-code} 

```{code-block} shell
git add README.md
```
````

Now the file is *staged* for a commit.
Next, create the commit using the `git commit` command.

````{tab-set-code} 

```{code-block} shell
git commit -m "add information about dependencies to readme"
```
````

`````
``````

Once you have saved this file, type

````{tab-set-code} 

```{code-block} shell
git log
```
````


Now, check `git status` and `git log`. You should see the following:

````{tab-set-code} 

```{code-block} shell
git status
```
````


````{tab-set-code} 

```{code-block} output
On branch main
nothing to commit, working tree clean
```
````


````{tab-set-code} 

```{code-block} shell
git log
```
````

We now have a log with three commits.
This means there are three versions of the repository we are working in.

`git log` lists all commits  made to a repository in reverse chronological order.
The listing for each commit includes the commit's full identifier,
the commit's author, when the commit was created, and the commit title.

We can see differences in files between commits using `git diff`.

````{tab-set-code} 

```{code-block} shell
git diff HEAD~1
```
````


The argument to `git diff` refers to the comparison point in our commit history.
`HEAD` is an alias for the commit at the tip of our checked-out branch.
`~1` is a modifier that refers to the given commit minus 1.
We are asking git to show us the difference between the current files and the second most recent commit.

Lines that have been added are indicated in green with a plus sign next to them (`+`),
while lines that have been deleted are indicated in red with a minus sign next to them (`-`).

## Viewing previous versions

If you need to check out a previous version,

````{tab-set-code} 

```{code-block} shell
git checkout COMMIT_ID
```
````


This will temporarily revert the repository to whatever the state was at the specified commit ID.

Let's check out the version before the most recent edit we made to the README.

````{tab-set-code} 

```{code-block} shell
git log --oneline
```
````


````{tab-set-code} 

```{code-block} output
d857c74 (HEAD -> main) add information about dependencies to readme
3c0e1c6 update readme to have instructions for developmental install
116f0cf (tag: 0.0.0) Initial commit after CMS Cookiecutter creation, version 1.1
```
````


In this log, the commit ID is the first number on the left.

To revert to the version of the repository where we first edited the readme,
use the `git checkout` command with the appropriate commit ID.

````{tab-set-code} 

```{code-block} shell
git checkout 3c0e1c6
```
````


If you now view your `README.md`, it has reverted to the previous version of the file.

To return to the most recent point,

````{tab-set-code} 

```{code-block} shell
git checkout main
```
````

### Exercise - Creating a Repository

``````{admonition} Exercise
:class: exercise

What list of commands would mimic what the CMS CookieCutter did when it created the 
repository and made the first commit? (Hint - to initialize a repository, you use
the command `git init`.)

`````{admonition} Solution
:class: solution dropdown

To recreate the CMS CookieCutter's first commit,

````{tab-set-code} 

```{code-block} shell
git init
git add .
git commit -m "Initial commit after CMS Cookiecutter creation, version 1.0"
```
````

The first line initializes the `git` repository.
The second line adds all modified files to the current working directory, and the third line commits these files and writes the commit message.
`````
``````

## Exploring git history

When working on a project, it is easy to forget exactly what changes we have made to a file.
To check this, do

````{tab-set-code}

```{code-block} shell
git diff HEAD README.md
```

````

We should get a blank result.
"HEAD" is referencing the most recent commit.
Since we committed our changes to `README.md`, there is no difference to show.

Open your `README.md` and add the following line to the end of it.

```output
This line doesn't add any value
```

Save that file and run the same command.

````{tab-set-code} 

```{code-block} shell
git diff HEAD README.md
```
````


````{tab-set-code} 

```{code-block} output
diff --git a/README.md b/README.md
index 94e0b50..a68f349 100644
--- a/README.md
+++ b/README.md
@@ -17,6 +17,8 @@ This package requires the following:
   - numpy
   - matplotlib

+This line doesn't add any value.
+
 ### Copyright
```
````


To compare against the commit just before the most recent commit, add "~1" to the end of "HEAD":

````{tab-set-code} 

```{code-block} shell
git diff HEAD~1 README.md
```
````


````{tab-set-code} 

```{code-block} output
diff --git a/README.md b/README.md
index e778cd4..94e0b50 100644
--- a/README.md
+++ b/README.md
@@ -13,6 +13,10 @@ This repository is currently under development. To do installation in development mode, download this repository and type

`pip install -e .`

in the repository directory.

+This package requires the following:
+  - numpy
+  - matplotlib
+
 ### Copyright
```
````



If we want to compare against a specific commit, we can first do `git log` to find the commit's ID, and then do:

````{tab-set-code} 

```{code-block} shell
git diff *commit_id* README.md
```
````


Another problem that we sometimes encounter is wanting to undo all of our changes to a particular file.
This can be done with

````{tab-set-code} 

```{code-block} shell
git checkout HEAD README.md
```
````


If you open `README.md` you will see that it has reverted to the content from the most recent commit.

Of course, you could also replace `HEAD` here with `HEAD~1` or a specific commit ID.


## Creating new features - using branches

When you are working on a project to implement new features,
it is a good practice to isolate the changes you are making and work on one particular topic at a time.
To do this, you can use something called a **branch** in git.
Working on branches allows you to isolate particular changes.
If you make sure that your code works before merging to your main or master branch,
you will ensure that you always have a working version of code on your `main` branch.

If you followed the set-up instructions, you should be in the `main` branch by default.
To create a new branch and move to it, you can use the command

````{tab-set-code} 

```{code-block} shell
git checkout -b new_branch_name
```
````


The command `git checkout` switches branches when followed by a branch name.
When you use the `-b` option, git will create the branch and switch to it.
For this exercise, we will add a new feature:
We are going to add a function to print the [Zen of Python](https://www.python.org/dev/peps/pep-0020/).

First, we'll create a new branch:

````{tab-set-code} 

```{code-block} shell
git checkout -b zen
```
````


We can visualize what branching looks like with some simple figures.
Before branching, imagine a git commit history that looks like this.
In the diagram below, each circle represents a git commit.
There have been two commits, and the HEAD is currently after commit 2.

```{image} ../fig/github_workflows/git_history_0.svg
:align: center
```

After we have created a new branch and checked it out, we can imagine our git history looking like this.
The `zen` branch 'branches' starts from the point where we used the git branch command. 

```{image} ../fig/github_workflows/git_branch.svg
:align: center
```

Now, when we make a commit on the `zen` branch, our changes will continue from this point, leaving the main branch unchanged.
Note that we have not yet made a commit, but this diagram is for illustrative purposes.

```{image} ../fig/github_workflows/branch_development.svg
:align: center
```

Now that we have a better understanding of what branching looks like, let's make some changes to the `zen` branch.
Add a new function to your `functions.py` module.
We are going to add the ability to print "The Zen of Python". You can get the Zen of Python by typing

````{tab-set-code} 

```{code-block} python
import this
```
````

into the interactive Python prompt.

This will print the Zen of Python to the screen.
The Zen of Python is a collection of 19 software principles that influence the design of Python.

Let's make a function (similar to our existing `canvas` function) that prints the Zen of Python.

Add the following function to your `functions.py` module.

````{tab-set-code} 

```{code-block} python
def zen(with_attribution=True):
    quote = """Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!"""

    if with_attribution:
      quote += "\n\tTim Peters"

    return quote
```
````


Verify that this function works in the interactive Python prompt.
Next, commit this change:

````{tab-set-code} 

```{code-block} shell
git add .
git commit -m "add function to print Zen of Python"
```
````


Let's switch back to the `main` branch to see what it is like.
You can see a list of branches in your repo by using the command

````{tab-set-code} 

```{code-block} shell
git branch
```
````


This will list your local branches.
The active branch, or the branch you are on will be noted with an asterisk (`*`).

To switch back to the `main` branch,

````{tab-set-code} 

```{code-block} shell
git checkout main
```
````


When you look at the `functions.py` module on the `main` branch,
you should not see your most recent changes.

You can verify this by using the `git log` command.

Consider that at the same time we have some changes or features we'd like to implement.
Let's make a branch to do a documentation update.

Create a new branch.

````{tab-set-code} 

```{code-block} shell
git checkout -b doc_update
```
````


Let's add some information about developing branches to the README.
Update your README to include this information:

````{tab-set-code} 

```{code-block} README.md

Features should be developed on branches. 
To create and switch to a branch, use the command

`git checkout -b new_branch_name`

To switch to an existing branch, use

`git checkout new_branch_name`
```
````

Save and commit this change.

````{tab-set-code} 

```{code-block} shell
git add README.md
git commit -m "add information about branching to readme"
```
````

To incorporate these changes in `main`, you will need to do a `git merge`.
When you do a merge, you should be on the branch you would like to merge into.
In this case, we will first merge the changes from our `doc_update` branch,
then our `zen` branch, so we should be on our `main` branch.
Next, we will use the `git merge` command.

The syntax for this command is `git merge branch_name` 
where `branch_name` is the name of the branch you would like to merge.

We can merge our `doc_update` branch to get changes on our `main` branch:

````{tab-set-code} 

```{code-block} shell
git checkout main
git merge doc_update
```
````


Now our changes from the branch are on `main`.

We can merge our `zen` branch to get our changes on `main`:

````{tab-set-code} 

```{code-block} shell
git merge zen
```
````


This time, you will see a different message and a text editor will open for a merge commit message.

**Note** that if you have an older version of git, you may see `Merge made by recursive strategy.` instead 
instead of `Merge made by the 'ort' strategy.`

````{tab-set-code} 

```{code-block} output
Merge made by the 'ort' strategy.
```
````

This is because `main` and `zen` have development histories that have diverged.
`git` had to do some work in this case to merge the branches.
A *merge commit* was created. 

Merge commits create a branched git history.
We can visualize the history of our project by adding `--graph`.
There are other workflows you can use to make the commit history more linear,
but we will not discuss them in this course.

Once we are done with a feature branch, we can delete it:

````{tab-set-code} 

```{code-block} shell
git branch -d zen
```
````

### Exercise - Using Branches

``````{admonition} Using Branches - Exercise
:class: exercise

For this exercise, you will be adding all the functions from your Jupyter
Notebook to the package. Create a branch to add your functions.
Add all of the functions from your Jupyter Notebook to the module
`functions.py` in your package.
Verify that you can use your functions.
Once the functions are added and working, merge them into your `main` branch.

`````{admonition} Solution
:class: solution dropdown

First, create a new branch in your repository


````{tab-set-code} 

```{code-block} shell
git checkout -b add-functions
```
````
 
Next, copy all of your imports from the first cell of your Jupyter Notebook and paste them into the top of your file.

Next, copy the function definitions from the first cell and paste them above or below the `canvas` function. 

Your file should look something like this.

```python
"""Provide the primary functions."""

import os
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format).

    Replace this function and doc string for your own project.

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from.

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution.
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote

def zen(with_attribution=True):
    quote = """Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!"""

    if with_attribution:
      quote += "\n\tTim Peters"

    return quote

def calculate_distance(rA, rB):
    # This function calculates the distance between two points given as numpy arrays.
    d=(rA-rB)
    dist=np.linalg.norm(d)
    return dist

def open_pdb(f_loc):
    # This function reads in a pdb file and returns the atom names and coordinates.
    with open(f_loc) as f:
        data = f.readlines()
    c = []
    sym = []
    for l in data:
        if 'ATOM' in l[0:6] or 'HETATM' in l[0:6]:
            sym.append(l[76:79].strip())
            c2 = [float(x) for x in l[30:55].split()]
            c.append(c2)
    coords = np.array(c)
    return sym, coords

atomic_weights = {
    'H': 1.00784,
    'C': 12.0107,
    'N': 14.0067,
    'O': 15.999,
    'P': 30.973762,
    'F': 18.998403,
    'Cl': 35.453,
    'Br': 79.904,
}


def open_xyz(file_location):
    
    # Open an xyz file and return symbols and coordinates.
    xyz_file = np.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coords = (xyz_file[:,1:])
    coords = coords.astype(np.float)
    return symbols, coords

def write_xyz(file_location, symbols, coordinates):
    
    # Write an xyz file given a file location, symbols, and coordinates.
    num_atoms = len(symbols)
    
    with open(file_location, 'w+') as f:
        f.write('{}\n'.format(num_atoms))
        f.write('XYZ file\n')
        
        for i in range(num_atoms):
            f.write('{}\t{}\t{}\t{}\n'.format(symbols[i], 
                                              coordinates[i,0], coordinates[i,1], coordinates[i,2]))

def draw_molecule(coordinates, symbols, draw_bonds=None, save_location=None, dpi=300):
    
    # Draw a picture of a molecule using matplotlib.
    
    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Get colors - based on atom name
    colors = []
    for atom in symbols:
        colors.append(atom_colors[atom])
    
    size = np.array(plt.rcParams['lines.markersize'] ** 2)*200/(len(coordinates))

    ax.scatter(coordinates[:,0], coordinates[:,1], coordinates[:,2], marker="o",
               edgecolors='k', facecolors=colors, alpha=1, s=size)
    
    # Draw bonds
    if draw_bonds:
        for atoms, bond_length in draw_bonds.items():
            atom1 = atoms[0]
            atom2 = atoms[1]
            
            ax.plot(coordinates[[atom1,atom2], 0], coordinates[[atom1,atom2], 1],
                    coordinates[[atom1,atom2], 2], color='k')
    
    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi, graph_min=0, graph_max=2)
    
    return ax

def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta

def bond_histogram(bond_list, save_location=None, dpi=300, graph_min=0, graph_max=2):
    # Draw a histogram of bond lengths based on a bond_list (output from build_bond_list function)
    
    
    lengths = []
    for atoms, bond_length in bond_list.items():
        lengths.append(bond_length)
    
    bins = np.linspace(graph_min, graph_max)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    plt.xlabel('Bond Length (angstrom)')
    plt.ylabel('Number of Bonds')
    
    
    ax.hist(lengths, bins=bins)
    
    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi)
    
    return ax
        
def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    
    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds

atom_colors = {
    'H': 'white',
    'C': '#D3D3D3',
    'N': '#add8e6',
    'O': 'red',
    'P': '#FFA500',
    'F': '#FFFFE0',
    'Cl': '#98FB98',
    'Br': '#F4A460',
    'S': 'yellow'
}


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
```

 Open the interactive Python interface and try out some functions to verify that your package still works.

 Make a commit to commit this change to your branch:

 ````{tab-set-code} 

```{code-block} shell
git add . 
git commit -m "add functions to package"
```
````

 Next, switch back to your `main` branch to merge:

```{code-block} shell
git checkout main
git merge add-functions
```
````
`````
``````

## Adding data
We now have a package with some functions.
Let's add the data from our starting material to our package as well.
We will add this to the `molecool/testing/data` directory.
Although it would be a best practice to add these files through a branch,
we will add them directly to the `main` branch for simplicity.

Assuming that you ran the cookiecutter from the starting material directory,

````{tab-set-code} 
```{code-block} shell   
cp -r ../data molecool/tests/
```
````

Then, commit the change:

````{tab-set-code} 

```{code-block} shell   
git add .
git commit -m "add data to package"
```
````

## Ignoring files - .gitignore

Sometimes while you work on a project, you may end up creating some temporary files.
For example, if your text editor is Emacs, you may end up with lots of files called `<filename>~`.
By default, Git tracks all files, including these.
This tends to be annoying since it means that any time you do `git status`,
all of these unimportant files show up.

We are now going to find out how to tell Git to ignore these files
so that it doesn't keep telling us about them every time we do `git status`.
Even if you aren't working with Emacs, someone else working on your project might.
So let's do the courtesy of telling Git not to track these temporary files.
First, let's ensure that we have a few dummy files.
Make empty files called `testing.txt~` and `README.md~` in your repository using your text editor of choice.


While we're at it, also make some other files that aren't important to the project.
Make a file called `calculation.out` in `molecool/data` using your text editor of choice.

Now check what Git says about these files:

````{tab-set-code} 

```{code-block} shell
git status
```
````


````{tab-set-code} 

```{code-block} output
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	README.md~
	molecool/data/calculation.in
	molecool/data/calculation.out
	testing.txt~

nothing added to commit but untracked files present (use "git add" to track)
```
````


Now we will make Git stop telling us about these files.

Earlier, when we looked at the hidden files, you may have noticed a file called `.gitignore`.
Cookiecutter created this for us, however, GitHub also has built-in `.gitignore` files you can add when creating an empty repository.

This file is to tell `git` which types of files we would like to ignore (thus the name `.gitignore`).

Look at the contents of `.gitignore`

~~~
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a Python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

...
~~~

Git looks at `.gitignore` and ignores any files or directories that match one of the lines.
Add the following to the end of `.gitignore`:

~~~
# emacs
*~

# temporary data files
*.in
*.out

~~~

Now do "git status" again. Notice that the files we added are no longer recognized by Git.

````{tab-set-code} 

```{code-block} shell
git status
```
````


````{tab-set-code} 

```{code-block} output
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   .gitignore

no changes added to commit (use "git add" and/or "git commit -a")
```
````


We want these additions to `.gitignore` to become a permanent part of the repository:

````{tab-set-code} 

```{code-block} shell
git add .gitignore
git commit -m "Ignores Emacs temporary files and input/output files from calculations."
```
````


One nice feature of `.gitignore` is that prevents us from accidentally adding
a file that shouldn't be part of the repository.
For example:

````{tab-set-code} 

```{code-block} shell
git add data/calculation.in
```
````


````{tab-set-code} 

```{code-block} output
The following paths are ignored by one of your .gitignore files:
data/calculation.in
Use -f if you really want to add them.
```
````


It is possible to override this with the `-f` option for `git add`.


:::{admonition} Final Repository State
:class: tip

You can see the final state of the repository after this section [here](https://github.com/MolSSI-Education/molecool/tree/b74f9bb50e5b614d1078730aef1d4f972cbde99c).

You can also download a zip of the repository [here](https://github.com/MolSSI-Education/molecool/archive/refs/tags/git-end.zip).

:::


## More Tutorials
If you want more `git`, see the following tutorials.

### Basic git
 - [Software Carpentry Version Control with Git](http://swcarpentry.github.io/git-novice/)
 - [GitHub 15 Minutes to Learn Git](https://try.github.io/)
 - [More on branches and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
 - [Git Commit Best Practices](https://github.com/trein/dev-best-practices/wiki/Git-Commit-Best-Practices)

:::{admonition} Final Repository State
:class: tip

You can see the final state of the repository after this section [here](https://github.com/MolSSI-Education/molecool/tree/b74f9bb50e5b614d1078730aef1d4f972cbde99c).

You can also download a zip of the repository [here](https://github.com/MolSSI-Education/molecool/archive/refs/tags/git-end.zip).

:::

## Key Points
````{admonition} Key Points
:class: key

* Git provides a way to track changes in your project.
* Git is a software for version control and is separate from GitHub.
````
