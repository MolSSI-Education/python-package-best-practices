# Introduction to Version Control with `git` - Standalone Lesson

````{admonition} Overview
:class: overview

Questions:
- What is version control?
- How do I use git to keep a record of my project?
- What is a branch and why would I use it?
- How do I tell `git` to ignore files?

Objectives:
- Explain the purpose of version control.
- Introduce common git commands.
- Understand how to view and check out previous versions of files.
````

```{admonition} Prerequisites
:class: caution

- Completed the previous lesson.
- Created GitHub account (described in set-up instructions)
- Configured git (described in set-up instructions)
```

## Version Control

Version control keeps a complete history of your work on a given project. 
It facilitates collaboration where everyone can work freely on different parts of a project without overriding others’ changes. 
You can move between past versions and rollback when needed.  
You can also review the history of your project through commit messages that describe changes on the source code
and see what exactly has been modified in any given commit. 

This is greatly beneficial whether you are working independently or within a team. We recommend *always* using git when working on a programming project.

```{admonition} git vs. GitHub
`git` is the software used for version control, while GitHub is a hosting service. 
You can use `git` locally (without using an online hosting service), or you can use it with other hosting services such as GitLab or BitBucket.
Other examples of version control software include SVN and Mercurial.
```

MolSSI recommends using the software `git` for version control, and [GitHub] as a hosting service, though there are other options.

## Using `git` to keep a record of your project

You should have git installed and configured from the setup instructions.

In this section, we are going to create a file with some Python functions and use `git` to track changes to our project.

First, use a terminal to `cd` into the directory where you are keeping your files for the workshop (`molssi_best_practices`). 
Then, create a folder for your git lesson.

````{tab-set-code} 

```{code-block} shell
cd molssi_best_practices
mkdir git-lesson
cd git-lesson
```
````

``````{admonition} Challenge
:class: exercise

Use the skills you used in the previous lesson to create a directory called `git-lesson`. 

Then, change directories into the folder you just created.

`````{admonition} Solution
:class: solution dropdown

````{tab-set-code} 

```{code-block} shell
mkdir git-lesson
cd git-lesson
```
````
`````
``````

**Make sure you execute the commands that are in the solution of the challenge above before continuing.**

We will do our first `git` project in this folder.

In order for git to keep track of your project, or any changes in your project, you must first tell git that you want it start a project and track your changes. 
After starting a project, you must manually create check-points if you wish to have points to return to. 
If we want to tell `git` that the folder we are working in represents a project, we do so with the command `git init`. 
In your folder, use the command

````{tab-set-code}
```{code-block}  shell
git init
```
````


You will see an output message similar to the following, except with the path to your directory

````{tab-set-code} 

```{code-block} output
Initialized empty Git repository in /PATH/TO/REPOSITORY
```
````


Now, when you check the contents of the directory using `ls`, it will still look empty. 
However, if you look at the hidden files (files or folders beginning with a dot `.`) using the `ls -a`, you will see that the directory is no longer empty

````{tab-set-code} 

```{code-block} shell
ls -a
```
````


````{tab-set-code} 

```{code-block} output
.   ..  .git
```
````


The presence of the `.git` folder indicates to us that the `git` software is now watching the folder for changes. 
`.git` is a directory where `git` stores the repository data. 
We can tell from this output that we are in a git repository.

Another way we can tell if we are in a git repository is to use the command `git status`.

````{tab-set-code} 

```{code-block} shell
git status
```
````


````{tab-set-code} 

```{code-block} output
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```
````


The command `git status` gives us the current state of our repository. 
This message tells us that we are on the `main` branch, and that we haven't yet created a checkpoint, or commit, of our project.

## The 3 steps of a commit
A particular version of your project is called a "commit". There is a very specific procedure that you should follow when making a commit. These steps are : (1) Making changes to your project. (2) Marking the changes you want to record (`git add`). (3) Creating a version, or a "commit" to the repository (you can also think of this as a project checkpoint).

Now that we've covered the steps, let's see how to make versions of our project and view the project history.

Create a file called `README.md` in your text editor of choice. 
The README file is a file which typically accompanies git repositories and gives information about that project. 
We will use [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet), which we covered in the last lesson, for the README to give it a nice formatting when viewed online. 

Add the following to your README

````{tab-set-code} 

```{code-block} README.md
# Git Lesson

This lesson covers the basics of git for version control.
```
````

Save this file an return to the terminal. 
Now that we have made a change, check the status of your project again.

````{tab-set-code} 

```{code-block} shell
git status
```
````


````{tab-set-code} 

```{code-block} output
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	README.md

nothing added to commit but untracked files present (use "git add" to track)
```
````


Notice how `git` is watching our repository!
It tells us that it sees that we have added a new file (`README.md`), but git is not actually tracking that file yet. 
Remember that `git` only watches what we tell it to watch, and only tracks changes in files we tell it to track changes in. 
Next, we will want to tell `git` to watch `README.md` and to make a version of our project which includes the file. 
In other words, we want to `commit` our changes.

#### git add, git status, git commit

Making a commit is like making a checkpoint for a particular version of your code. 
You can easily return to, or revert to that checkpoint.

To create the checkpoint, we first have to make changes to our project. 
We might modify *many* files at a time in a repository. 
Thus, the first step in creating a checkpoint (or commit) is to tell `git` which files we want to include in the checkpoint. 
We do this with a command called `git add`. 
This adds files to what is called the *staging area*.

Let's look at our output from `git status` again.

````{tab-set-code} 

```{code-block} output
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	README.md

nothing added to commit but untracked files present (use "git add" to track)
```
````


Git even tells us to use `git add` to include what will be committed. 
Let's follow the instructions and tell `git` that we want to create a checkpoint with the current version of `README.md`

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

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   README.md
```
````

We are now on the second step of creating a commit. 
We have `added` our files to the staging area. 
In our case, we only have one file in the staging area, but we could add more if we had more files.

To create the checkpoint, or commit, we will now use the `git commit` command. 
We add a `-m` after the command for "message." 
Whenever you create a commit, you should write a message about what the commit does.

````{tab-set-code} 

```{code-block} shell
git commit -m "add README with information about project."
```
````


````{tab-set-code} 

```{code-block} output
[main (root-commit) dc466ff] add README with information about project
 1 file changed, 3 insertions(+)
 create mode 100644 README.md
```
````

 Check your status after the commit

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

This message means nothing in the directory has changed since our last checkpoint, or commit.

#### git log

Next, type
````{tab-set-code} 

```{code-block} shell
git log
```
````


You will get an output resembling the following:
````{tab-set-code} 

```{code-block} output
commit dc466ff70070312b622ab0041f4d770bd37bb248 (HEAD -> main)
Author: Jessica Nash <janash@vt.edu>
Date:   Wed Jul 8 15:59:57 2020 -0400

    add README with information about project
```
````


Each line of this log tells you something important about the commit, or check point that exists for the project. 
On the first line,

```
commit dc466ff70070312b622ab0041f4d770bd37bb248 (HEAD -> main)
```

You have a unique identifier for the commit (dc466...). 
You can use this number to reference this checkpoint. 
This number is unique for every commit, meaning you will have a different number than that shown above.

Then, git records the name of the author who made the change.

```
Author: Your Name <your_email@something.com>
```

This should be your information. 
This way, anyone who is working with this project can see who made each commit. 
Note that this name and email address matches what you specified when you configured git in the setup.

```
Date:   Wed Jul 8 15:59:57 2020 -0400
```
Next, it lists the date and time the commit was made. 

```
    add README with information about project
```

Finally, there will be a blank line followed by a commit message. 
The commit message is a message whoever made the commit chose to write, but should describe the change that took place when the commit was made. 
You'll recognize this message from what you just wrote when you used the `git commit` command.

To exit the log, press the `q` key.

When we have more commits (or versions) of our code, `git log` will show a history of these commits, and they will all have the same format discussed above. 
Right now, we have only one commit.

Let's continue to edit this readme to include more information. 
This is a file which will describe what is in this directory. 
Open `README.md` in your text editor of choice and add the following to the end 

````{tab-set-code}
```{code-block} README.md
This lesson is for the MolSSI Best Practices Workshop.
```
````


Let's make another version of our file that contains this information:

````{tab-set-code} 

```{code-block} shell
git add README.md
git status
```
````


````{tab-set-code} 

```{code-block} output
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
```
````


````{tab-set-code} 

```{code-block} shell
git commit -m "add more information to README"
```
````


``````{admonition} Check your understanding
:class: exercise

Add the following information about how to make a commit to your README.md and commit the change.

````{tab-set-code}

```{code-block} README.md

To make a commit ("version" or "checkpoint") of your files, follow this procedure:

1. Make changes to your project you would like to keep.
1. When you have your changes, tell git you are ready to create a checkpoint of the files using `git add filename`
1. Create a checkpoint using `git commit -m "message about what you did"

```
````

`````{admonition} Solution
:class: solution dropdown

To add the file to the staging area and tell `git` we would like to track the changes to the file, we first use the `git add` command.

````{tab-set-code}

```{code-block} shell
git add README.md
```
````

````{tab-set-code}

Now the file is *staged* for a commit.
Next, create the commit using the `git commit` command.

```{code-block} shell
git commit -m "add more information to readme"
```
````

`````

``````


Now, check `git status` and `git log`. 
You should see the following:

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
The listing for each commit includes the commit's full identifier,the commit's author, when it was created, and the commit title.

We can see differences in files between commits using git diff.

````{tab-set-code} 

```{code-block} shell
git diff HEAD~1
```
````


Here HEAD refers to the point in our commit history (and current branch). 
When we use `~1`, we are asking git to show us the different of the current point minus one commit.

Lines that have been added are indicated in green with a plus sign next to them ('+'), while lines that have been deleted, if we had any, would be indicated in red with a minus sign next to them ('-').

## Viewing previous versions

If you need to check out a previous version

````{tab-set-code} 

```{code-block} shell
git checkout COMMIT_ID
```
````

This will temporarily revert the repository to whatever the state was at the specified commit ID.

Let's checkout the version before we made the most recent edit to the README.

````{tab-set-code} 

```{code-block} shell
git log --oneline
```
````

````{tab-set-code} 

```{code-block} output
fe357b0 (HEAD -> main) add information about how to make a commit to the readme
8c39357 add more information to README
dc466ff add README with information about project
```
````


In this log, the commit ID is the first number on the left.

To revert to the version of the repository where we first edited the readme, use the `git checkout` command with the appropriate commit id.

````{tab-set-code} 

```{code-block} shell
git checkout 8c39357
```
````


If you now view your readme, it is the previous version of the file.

To return to the most recent point,

````{tab-set-code} 

```{code-block} shell
git checkout main
```
````



## Creating new features - using branches

When you are working on a project to implement new features, it is a good practice to isolate the the changes you are making and work on one particular topic at a time. 
To do this, you can use something called a **branch** in git. 
Working on branches allows you to isolate particular changes. 
If you make sure that your code works before merging to your main or **main** branch, you will ensure that you always have a working version of code on your main branch.

By default, you are typically in the main branch. 
To create a new branch and move to it, you can use the command

````{tab-set-code} 

```{code-block} shell
git switch -c new_branch_name
```
````



The command `git switch` switches branches when followed by a branch name. 
When you use the `-c` option, git will create a branch with the specified name and switch to it. 
For this exercise, we will add a new feature - we are going to a python function to print "Hello, World!" (the famous first programming exercise).

First, we'll create a new branch:

````{tab-set-code} 

```{code-block} shell
git switch -c hello_world
```
````


Next, create a new file called `quotes.py`. 
We are going to add the ability to print "Hello, World!"

Add the function to your `quotes.py` file.

````{tab-set-code} 

```{code-block} python
"""
Some quotes.
"""

def hello_world():
    quote = "Hello, World!"
    return quote
```
````

Verify that this function works in the interactive Python prompt. 

````{tab-set-code} 

```{code-block} python
>>> import quotes
>>> print(quotes.hello_world())
```
````

Next, commit this change:

````{tab-set-code} 

```{code-block} shell
git add hello_world.py
git commit -m "add function to print Hello World"
```
````


Let's switch back to the main branch to see what it is like. 
You can see a list of all the branches in your repo by using the command

````{tab-set-code} 

```{code-block} shell
git branch
```
````


This will list all of your branches. 
he active branch, or the branch you are on will be noted with an asterisk (`*`).

To switch back to the main branch,

````{tab-set-code} 

```{code-block} shell
git switch main
```
````


On your main branch, you should see that there is no `quotes.py` module.

You can further verify this by using the `git log` command.

Consider that at the same time we have some changes or features we'd like to implement. 
Let's make a branch to do a documentation update.

Create a new branch

````{tab-set-code} 

```{code-block} shell
git switch -c doc_update
```
````


Let's add some information about developing on branches to the README. 
Update your README to include this information:

````{tab-set-code} 

```{code-block} README.md
## Adding Features
Features should be developed on branches. To create and switch to a branch, use the command

`git switch -c new_branch_name`

To switch to an existing branch, use

`git switch branch_name`
```
````

Save and commit this change.

## Getting Changes to Your main Branch

This is as far as we complete in class. 
Do not do the next sections if you want to follow along.

The portion below here should only be used if you are working on a project alone. 
Otherwise, we will discuss how to get changes all on the same branch in the lesson on collaboration using GitHb.

To incorporate these changes in main, you will need to do a `git merge`. 
When you do a merge, you should be on the branch you would like to merge into. In this case, we will first merge the changes from our `doc_update` branch, then our `hello_world` branch, so we should be on our `main` branch. 
Next we will use the `git merge` command.

The syntax for this command is 

````{tab-set-code} 

```{code-block} shell
git merge branch_name
```
````


where `branch_name` is the name of the branch you would like to merge.

We can merge our `doc_update` branch to get changes from our `doc_update` branch to our main branch:
````{tab-set-code} 

```{code-block} shell
git checkout main
git merge doc_update
```
````


Now our changes from the branch are on main.

We can merge our `hello_world` branch to get our changes on main:

````{tab-set-code} 

```{code-block} shell
git merge hello_world
```
````


This time, you will see a different message, and a text editor will open for a merge commit message.

````{tab-set-code} 

```{code-block} output
Merge made by the 'recursive' strategy.
```
````

This is because `main` and `hello_world` had development histories which have diverged (their commit histories were different). 
Git had to do some work in this case to merge the branches. A merge commit was created. 

Merge commits create a branched git history. 
We can visualize the history of our project by adding `--graph` to git log. 
There are other workflows you can use to make the commit history more linear, but we will not discuss them in this course.

````{tab-set-code} 

```{code-block} shell
git log --graph
```
````


Once we are done with a feature branch,  we can delete it:

````{tab-set-code} 

```{code-block} shell
git branch -d hello_world
git branch -d doc_update
```
````

## Ignoring Files

Sometimes while you work on a project, you may end up creating some temporary files.
For example, if your text editor is Emacs, you may end up with lots of files called `<filename>~`.
By default, Git tracks all files, including these.
This tends to be annoying, since it means that any time you do "git status", all of these unimportant files show up.

We are now going to find out how to tell Git to ignore these files, so that it doesn't keep telling us about them ever time we do "git status".
Even if you aren't working with Emacs, someone else working on your project might, so let's do the courtesy of telling Git not to track these temporary files.
First, lets ensure that we have a few dummy files. Create empty files in your text editor called `quotes.py~` and `README.md~`.

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
	quotes.py~

nothing added to commit but untracked files present (use "git add" to track)
```
````


Now we will make Git stop telling us about these files.
We do this with a file called `.gitignore`. 
A `.gitignore` does what it sounds like - it tells `git` files or directories to ignore. 
If we can created our repository on GitHub and cloned it to our computer, we could have selected to create the repository with a `.gitignore.` 
We could have told `GitHub` what language we were planning to use, and it would have given us a starting `.gitignore` with files we would be likely to want to ignore. 

Navigate [here](https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore) to get a good starting gitignore for python. 
Copy the contents of this file to a file in your repository called `.gitignore`.

Look at the contents of `.gitignore`

````{tab-set-code} 

```{code-block} .gitignore
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
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

...
```
````

Git looks at `.gitignore` and ignores any files or directories that match one of the lines.

Commit your gitignore to the repository.

````{tab-set-code}
```{code-block} shell
git add .gitignore
git commit -m "add gitignore to repository
```
````


Next, let's ignore those emacs temporary files we added.

Add the following to the end of `.gitignore`:

~~~
# emacs
*~
~~~

Now do "git status" again. 
Notice that the files we added are no longer recognized by git.

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


We want these additions to .gitignore to become a permanent part of the repository, so do

````{tab-set-code} 

```{code-block} shell
git add .gitignore
git commit -m "Ignores Emacs temporary files and data directory"
```
````

## More Tutorials
If you want more `git`, see the following tutorials.

### Basic git
 - [Software Carpentry Version Control with Git](http://swcarpentry.github.io/git-novice/)
 - [GitHub 15 Minutes to Learn Git](https://try.github.io/)
 - [More on branches and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
 - [Git Commit Best Practices](https://github.com/trein/dev-best-practices/wiki/Git-Commit-Best-Practices)


[GitHub]: https://github.com
[GitLab]: https://gitlab.com/
[BitBucket]: https://bitbucket.org/
````{admonition} Key Points
:class: key

- Git provides a way to track changes in your project.
- Making a commit (or version or checkpoint) of your project requires several steps which allow to selectively choose what files you want to include.
- Git is a software for version control, and is separate from GitHub.
````
