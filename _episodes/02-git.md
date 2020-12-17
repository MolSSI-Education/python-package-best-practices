---
title: "Intro to Version Control with Git"
teaching: 30
exercises: 5
questions:
- "How do I use git to keep a record of my project?"
objectives:
- "Explain the purpose of version control."
- "Introduce common git commands."
- "Understand how to view and check out previous versions of files."
keypoints:
- "Git provides a way to track changes in your project."
- "Git is a software for version control, and is separate from GitHub."
---

> ## Prerequisites
>
> - Created GitHub account (described in set-up)
> - Configured git (described in set-up)
> - The Python package created in Episode 1.
{: .prereq}

## Version Control

Version control keeps a complete history of your work on a given project. It
facilitates collaboration on projects where everyone can work freely on a part
of the project without overriding others’ changes. You can move between past
versions and rollback when needed. Also, you can review the
history of your project through commit messages that describe changes on the source code
and see what exactly has been modified in any given commit. You can see who made the
changes and when it happened.

This is greatly beneficial whether you are working independently or within a
team.

> ## git vs. GitHub
>
> `git` is the software used for version control, while GitHub is a hosting service. You can use `git` locally (without using an online hosting service), or you can use it with other hosting services such as GitLab or BitBucket.
> Other examples of version control software include SVN and Mercurial.
>
{: .callout}

MolSSI recommends using the software `git` for version control, and [GitHub] as a hosting service, though there are other options.

Recommended Hosting Service: [GitHub]  
Other hosting Services: [GitLab], [BitBucket]

## Making Commits

You should have git installed and configured from the [setup] instructions.

In this section, we are going to  edit files in the Python package that we created earlier, and use `git` to track those changes.

First, use a terminal to `cd` into the top directory of the local repository.

In order for git to keep track of your project, or any changes in your project, you must first tell it that you want it to do this. You must manually create check-points in your project if you wish to have points to return to. If you were not using the CookieCutter, you would first have to initialize your project (ie tell git that you were working on a project) using the command `git init`. 

When we ran the CMS CookieCutter, it actually initialized the use of `git` for us, added our files, and made a commit (how convenient!). We can see this by typing the following into the terminal on Linux or Mac

~~~
$ ls -la
~~~
{: .bash}

Here, the `-la` says that we want to list the files in long format (`-l`), and show hidden files (`-a`). 

If you are on Windows and using the Anaconda Prompt:

~~~
dir /a
~~~
{: .cmd}

If you are on Windows and using the Anaconda PowerShell Prompt:

~~~
> ls -hidden
~~~
{: .bash}

You should an output called `.git`, `.git` is a directory where `git` stores the repository data. This is one way that we are in a git repository.

Next, type

~~~
$ git status
~~~
{: .bash}

~~~
On branch master
nothing to commit, working tree clean
~~~
{: .output}

This tells us that we are on the `master` branch (more about branching later), and that no files have been changed since the last commit.

Next, type
~~~
$ git log
~~~
{: .bash}

You will get an output resembling the following. This is something called your git commit log. Whenever you make a version, or checkpoint, of your project, you will be able to see information about that checkpoint using the `git log` command. The cookie cutter has already made a commit and written a message for you, and that is what we see for this first commit in the log.

~~~
commit 25ab1f1a066f68e433a17454c66531e5a86c112d (HEAD -> master, tag: 0.0.0)
Author: Your Name <your_email@something.com>
Date:   Mon Feb 4 10:45:26 2019 -0500

    Initial commit after CMS Cookiecutter creation, version 1.0
~~~
{: .output}

Each line of this log tells you something important about the commit, or check point that exists for the project. On the first line,

~~~
commit 25ab1f1a066f68e433a17454c66531e5a86c112d (HEAD -> master, tag: 0.0.0)
~~~

You have a unique identifier for the commit (25ab1...). You can use this number to reference this checkpoint.

Then, git records the name of the author who made the change.

~~~
Author: Your Name <your_email@something.com>
~~~

This should be your information. This way, anyone who downloads this project can see who made each commit. Note that this name and email address matches what you specified when you configured git in the setup, with the name and email address you specified in the cookiecutter having no effect.

~~~
Date:   Mon Feb 4 10:45:26 2019 -0500
~~~
Next, it lists the date and time the commit was made. 

~~~

    Initial commit after CMS Cookiecutter creation, version 1.0
~~~
Finally, there will be a blank line followed by a commit message. The commit message is a message whoever made the commit chose to write, but should describe the change that took place when the commit was made. This commit message was written by the cookiecutter for you.

When we have more commits (or versions) of our code, `git log` will show a history of these commits, and they will all have the same format discussed above. Right now, we have only one commit - the one created by the CMS CookieCutter.

## The 3 steps of a commit

Now, we will change some files and use `git` to track those changes. Let's edit our README. Open `README.md` in your text editor of choice. On line 8, you should see the description of the repository we typed when running the CookieCutter. Add the following sentence to your `README` under the initial description and save the file.

~~~
This repository is currently under development. To do a developmental install, download this repository and type

`pip install -e .`

in the repository directory.
~~~

#### git add, git status, git commit

Making a commit is like making a checkpoint for a particular version of your code. You can easily return to, or revert to that checkpoint.

To create the checkpoint, we first have to make changes to our project. We might modify *many* files at a time in a repository. Thus, the first step in creating a checkpoint (or commit) is to tell `git` which files we want to include in the checkpoint. We do this with a command called `git add`. This adds files to what is called the *staging area*.

Let's look at our output from `git status` again.

~~~
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
~~~
{: .output}

Git even tells us to use `git add` to include what will be committed. Let's follow the instructions and tell `git` that we want to create a checkpoint with the current version of `README.md`

~~~
$ git add README.md
~~~
{: .language-bash}

~~~
$ git status
~~~
{: .language-bash}

~~~
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   README.md
~~~
{: .output}

We are now on the second step of creating a commit. We have `added` our files to the staging area. In our case, we only have one file in the staging area, but we could add more if we needed.

To create the checkpoint, or commit, we will now use the `git commit` command. We add a `-m` after the command for "message." Whenever you create a commit, you should write a message about what the commit does.

~~~
$ git commit -m "update readme to have instructions for developmental install"
~~~
{: .bash}


Now when we look at our log using `git log`, we see the commit we just made along with information about the author and the date of the commit.

Let's continue to edit this readme to include more information. This is a file which will describe what is in this directory. Open `README.md` in your text editor of choice and add the following to the end 

~~~
This package requires the following:
  - numpy
  - matplotlib
~~~

This file is using a language called [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). 

> ## Check your understanding
> Create a commit for these changes to your repository.
>> ## Answer
>> To add the file to the staging area and tell `git` we would like to track the changes to the file, we first use the `git add` command.
>> ~~~
>> $ git add README.md
>> ~~~
>> {: .language-bash}
>> Now the file is *staged* for a commit.
>> Next, create the commit using the `git commit` command.
>> ~~~
>> $ git commit -m "add information about dependencies to readme"
>> ~~~
>> {: .language-bash}
> {: .solution}
{: .challenge}

Once you have saved this file, type

~~~
$ git log
~~~
{: .language-bash}

Now, check `git status` and `git log`. You should see the following:

~~~
$ git status
~~~
{: .bash}

~~~
On branch master
nothing to commit, working tree clean
~~~
{: .output}

~~~
$ git log
~~~
{: .bash}

We now have a log with three commits. This means there are three versions of the repository we are working in.

`git log` lists all commits  made to a repository in reverse chronological order.
The listing for each commit includes the commit's full identifier,the commit's author, when it was created, and the commit title.

We can see differences in files between commits using git diff.

~~~
$ git diff HEAD~1
~~~
{: .language-bash}

Here HEAD refers to the point in our commit history (and current branch). When we use `~1`, we are asking git to show us the different of the current point minus one commit.

Lines that have been added are indicated in green with a plus sign next to them ('+'), while lines that have been deleted are indicated in red with a minus sign next to them ('-')

## Viewing out previous versions

If you need to check out a previous version

~~~
$ git checkout COMMIT_ID
~~~

This will temporarily revert the repository to whatever the state was at the specified commit ID.

Let's checkout the version before we made the most recent edit to the README.

~~~
$ git log --oneline
~~~

~~~
d857c74 (HEAD -> master) add information about dependencies to readme
3c0e1c6 update readme to have instructions for developmental install
116f0cf (tag: 0.0.0) Initial commit after CMS Cookiecutter creation, version 1.1
~~~
{: .output}

In this log, the commit ID is the first number on the left.

To revert to the version of the repository where we first edited the readme, use the git checkout command with the appropriate commit id.

~~~
$ git checkout 3c0e1c6
~~~
{: .language-bash}

If you now view your readme, it is the previous version of the file.

To return to the most recent point,

~~~
$ git checkout master
~~~
{: .language-bash}

> ## Exercise
> What list of commands would mimic what CMS CookieCutter did when it created the repository and performed the first commit? (hint - to initialize a repository, you use `git init`)
> > ## Solution
>> To recreate the CMS Cookiecutter's first commit exactly,
>>~~~
$ git init
$ git add .
$ git commit -m "Initial commit after CMS Cookiecutter creation, version 1.0"
>>~~~
>>{: .language-bash}
>>  
>>  
>>The first line initializes the `git` repository. The second line add all modified files in the current working directory, and the third line commits these files and writes the commit message.
> {: .solution}
{: .challenge}


## Creating new features - using branches

When you are working on a project to implement new features, it is a good practices to isolate the the changes you are making and work on one particular topic at a time. To do this, you can use something called a **branch** in git. Working on branches allows you to isolate particular changes. If you make sure that your code works before merging to your main or **master** branch, you will ensure that you always have a working version of code on your main branch.

By default, you are typically in the master branch. To create a new branch and move to it, you can use the command

~~~
$ git checkout -b new_branch_name
~~~
{: .language-bash}

The command `git checkout` switches branches when followed by a branch name. When you use the `-b` option, git will create the branch and switch to it. For this exercise, we will add a new feature - we are going to add another function to print the [Zen of Python](https://www.python.org/dev/peps/pep-0020/).

First, we'll create a new branch:

~~~
$ git checkout -b zen
~~~
{: .language-bash}

Next, add a new function to your `functions.py` module. We are going to add the ability to print "The Zen of Python". You can get the Zen of Python by typing

~~~
import this
~~~
{: .language-python}

into the interactive Python prompt

~~~
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
~~~
{: .language-python}

Verify that this function works in the interactive Python prompt. Next, commit this change:

~~~
$ git add .
$ git commit -m "add function to print Zen of Python
~~~
{: .language-bash}

Let's switch back to the master branch to see what it is like. You can see a list of all the branches in your repo by using the command

~~~
$ git branch
~~~
{: .language-bash}

This will list all of your branches. The active branch, or the branch you are on will be noted with an asterisk (`*`).

To switch back to the master branch,

~~~
$ git checkout master
~~~
{: .language-bash}

When you look at the `functions.py` module on the master branch, you should not see your most recent changes.

You can verify this by using the `git log` command.

Consider that at the same time we have some changes or features we'd like to implement. Let's make a branch to do a documentation update.

Create a new branch

~~~
$ git checkout -b doc_update
~~~
{: .language-bash}

Let's add some information about developing on branches to the README. Update your README to include this information:

~~~

Features should be developed on branches. To create and switch to a branch, use the command

`git checkout -b new_branch_name`

To switch to an existing branch, use

`git checkout new_branch_name`
~~~

Save and commit this change.

To incorporate these changes in master, you will need to do a `git merge`. When you do a merge, you should be on the branch you would like to merge into. In this case, we will first merge the changes from our `doc_update` branch, then our `zen` branch, so we should be on our `master` branch. Next we will use the `git merge` command.

The syntax for this command is 

~~~
$ git merge branch_name
~~~
{: .language-bash}

where `branch_name` is the name of the branch you would like to merge.

We can merge our `doc_update` branch to get changes on our master branch:

~~~
$ get merge doc_update
~~~
{: .language-bash}

Now our changes from the branch are on master.

We can merge our `zen` branch to get our changes on master:

~~~
$ git merge zen
~~~
{: .language-bash}

This time, you will see a different message, and a text editor will open for a merge commit message.

~~~
Merge made by the 'recursive' strategy.
~~~

This is because `master` and `zen` had development histories which have diverged. Git had to do some work in this case to merge the branches. A merge commit was created. 

Merge commits create a branched git history. We can visualize the history of our project by adding `--graph`. There are other workflows you can use to make the commit history more linear, but we will not discuss them in this course.

Once we are done with a feature branch,  we can delete it:

~~~
$ git branch -d zen
~~~
{: .language-bash}

> ## Using Branches - Exercise
> For this exercise, you will be adding all the functions from your Jupyter notebook to the package. Create a branch to add your functions. Add all of the functions from your Jupyter notebook to the module `functions.py` in your package. Verify that you can use your functions. Once the functions are added and working, merge into your master branch.
>> ## Solution
>>
>> First, create a new branch in your repository
>>
>> ~~~
>> $ git checkout -b add-functions
>> ~~~
>> {: .language-bash}
>> 
>> Next, copy all of your imports from the first cell of your Jupyter notebook and paste them into the top of your file.
>> 
>> Next, copy the function definitions from the first cell and paste them above or below the `canvas` function. 
>> 
>> Your file should look something like this.
>> ~~~
>> """
>> functions.py
>> A Python package for analyzing and visualizing xyz files. For MolSSI Workshop Python Package development workshop.
>> 
>> Handles the primary functions
>> """
>> 
>> import os
>> import numpy as np
>> import matplotlib.pyplot as plt
>> 
>> from mpl_toolkits.mplot3d import Axes3D
>> 
>> 
>> def canvas(with_attribution=True):
>>     """
>>     Placeholder function to show example docstring (NumPy format)
>> 
>>     Replace this function and doc string for your own project
>> 
>>     Parameters
>>     ----------
>>     with_attribution : bool, Optional, default: True
>>         Set whether or not to display who the quote is from
>> 
>>     Returns
>>     -------
>>     quote : str
>>         Compiled string including quote and optional attribution
>>     """
>> 
>>     quote = "The code is but a canvas to our imagination."
>>     if with_attribution:
>>         quote += "\n\t- Adapted from Henry David Thoreau"
>>     return quote
>>
>> def zen():
>>     quote = """Beautiful is better than ugly.
>>     Explicit is better than implicit.
>>     Simple is better than complex.
>>     Complex is better than complicated.
>>     Flat is better than nested.
>>     Sparse is better than dense.
>>     Readability counts.
>>     Special cases aren't special enough to break the rules.
>>     Although practicality beats purity.
>>     Errors should never pass silently.
>>     Unless explicitly silenced.
>>     In the face of ambiguity, refuse the temptation to guess.
>>     There should be one-- and preferably only one --obvious way to do it.
>>     Although that way may not be obvious at first unless you're Dutch.
>>     Now is better than never.
>>     Although never is often better than *right* now.
>>     If the implementation is hard to explain, it's a bad idea.
>>     If the implementation is easy to explain, it may be a good idea.
>>     Namespaces are one honking great idea -- let's do more of those!"""
>>     
>>     return quote
>> 
>> def calculate_distance(rA, rB):
>>     d=(rA-rB)
>>     dist=np.linalg.norm(d)
>>     return dist
>> 
>> def open_pdb(f_loc):
>>     with open(f_loc) as f:
>>         data = f.readlines()
>>     c = []
>>     sym = []
>>     for l in data:
>>         if 'ATOM' in l[0:6] or 'HETATM' in l[0:6]:
>>             sym.append(l[76:79].strip())
>>             c2 = [float(x) for x in l[30:55].split()]
>>             c.append(c2)
>>     coords = np.array(c)
>>     return sym, coords
>> 
>> atomic_weights = {
>>     'H': 1.00784,
>>     'C': 12.0107,
>>     'N': 14.0067,
>>     'O': 15.999,
>>     'P': 30.973762,
>>     'F': 18.998403,
>>     'Cl': 35.453,
>>     'Br': 79.904,
>> }
>> 
>> 
>> def open_xyz(file_location):
>>     
>>     # Open an xyz file and return symbols and coordinates.
>>     xyz_file = np.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
>>     symbols = xyz_file[:,0]
>>     coords = (xyz_file[:,1:])
>>     coords = coords.astype(np.float)
>>     return symbols, coords
>> 
>> def write_xyz(file_location, symbols, coordinates):
>>     
>>     num_atoms = len(symbols)
>>     
>>     with open(file_location, 'w+') as f:
>>         f.write('{}\n'.format(num_atoms))
>>         f.write('XYZ file\n')
>>         
>>         for i in range(num_atoms):
>>             f.write('{}\t{}\t{}\t{}\n'.format(symbols[i], 
>>                                               coordinates[i,0], coordinates[i,1], coordinates[i,2]))
>> 
>> def draw_molecule(coordinates, symbols, draw_bonds=None, save_location=None, dpi=300):
>>     
>>     # Create figure
>>     fig = plt.figure()
>>     ax = fig.add_subplot(111, projection='3d')
>>     
>>     # Get colors - based on atom name
>>     colors = []
>>     for atom in symbols:
>>         colors.append(atom_colors[atom])
>>     
>>     size = np.array(plt.rcParams['lines.markersize'] ** 2)*200/(len(coordinates))
>> 
>>     ax.scatter(coordinates[:,0], coordinates[:,1], coordinates[:,2], marker="o",
>>                edgecolors='k', facecolors=colors, alpha=1, s=size)
>>     
>>     # Draw bonds
>>     if draw_bonds:
>>         for atoms, bond_length in draw_bonds.items():
>>             atom1 = atoms[0]
>>             atom2 = atoms[1]
>>             
>>             ax.plot(coordinates[[atom1,atom2], 0], coordinates[[atom1,atom2], 1],
>>                     coordinates[[atom1,atom2], 2], color='k')
>>             
>>     plt.axis('square')
>>     
>>     # Save figure
>>     if save_location:
>>         plt.savefig(save_location, dpi=dpi, graph_min=0, graph_max=2)
>>     
>>     return ax
>> 
>> def calculate_angle(rA, rB, rC, degrees=False):
>>     AB = rB - rA
>>     BC = rB - rC
>>     theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))
>> 
>>     if degrees:
>>         return np.degrees(theta)
>>     else:
>>         return theta
>> 
>> def bond_histogram(bond_list, save_location=None, dpi=300, graph_min=0, graph_max=2):
>>     
>>     lengths = []
>>     for atoms, bond_length in bond_list.items():
>>         lengths.append(bond_length)
>>     
>>     bins = np.linspace(graph_min, graph_max)
>>     
>>     fig = plt.figure()
>>     ax = fig.add_subplot(111)
>>     
>>     plt.xlabel('Bond Length (angstrom)')
>>     plt.ylabel('Number of Bonds')
>>     
>>     
>>     ax.hist(lengths, bins=bins)
>>     
>>     # Save figure
>>     if save_location:
>>         plt.savefig(save_location, dpi=dpi)
>>     
>>     return ax
>>         
>> def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
>>     
>>     # Find the bonds in a molecule
>>     bonds = {}
>>     num_atoms = len(coordinates)
>> 
>>     for atom1 in range(num_atoms):
>>         for atom2 in range(atom1, num_atoms):
>>             distance = calculate_distance(coordinates[atom1], coordinates[atom2])
>>             if distance > min_bond and distance < max_bond:
>>                 bonds[(atom1, atom2)] = distance
>> 
>>     return bonds
>> 
>> atom_colors = {
>>     'H': 'white',
>>     'C': '#D3D3D3',
>>     'N': '#add8e6',
>>     'O': 'red',
>>     'P': '#FFA500',
>>     'F': '#FFFFE0',
>>     'Cl': '#98FB98',
>>     'Br': '#F4A460',
>>     'S': 'yellow'
>> }
>> 
>> 
>> if __name__ == "__main__":
>>     # Do something if this file is invoked on its own
>>     print(canvas())
>> 
>> ~~~
>> {: .language-python}
>> 
>> Open the interactive Python interface and try out some functions to verify that your package still works.
>>
>> Make a commit to commit this change to your branch:
>> ~~~
>> $ git add .
>> $ git commit -m "add functions to package"
>> ~~~
>> {: .language-bash}
>>
>> Next, switch back to your master branch to merge:
>> ~~~
>> $ git checkout master
>> $ git merge add-functions
>> ~~~
>> {: .language-bash}
> {: .solution}
 {: .challenge}


## More Tutorials
If you want more `git`, see the following tutorials.

### Basic git
 - [Software Carpentry Version Control with Git](http://swcarpentry.github.io/git-novice/)
 - [GitHub 15 Minutes to Learn Git](https://try.github.io/)
 - [More on branches and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
 - [Git Commit Best Practices](https://github.com/trein/dev-best-practices/wiki/Git-Commit-Best-Practices)


{% include links.md %}
[GitHub]: https://github.com
[GitLab]: https://gitlab.com/
[BitBucket]: https://bitbucket.org/
