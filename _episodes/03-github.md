---
title: "Git and GitHub"
teaching: 90
exercises: 120
questions:
- "How do I use git and GitHub?"
objectives:
- "Explain how to use RMarkdown with the new lesson template."
- "Demonstrate how to include pieces of code, figures, and challenges."
keypoints:
- "It shouldn't be difficult"
---

> ## Prerequisites
>
> In this episode we start with the Git repositories created in Episode 1.
{: .prereq}

## Version Control

Version control keeps a complete history of your work on a given project. It
facilitates collaboration on projects where everyone can work freely on an part
of the project without overriding others’ changes. You can move between past
versions and rollback when needed, nothing is lost. Also, you can review the
history of your project through commit messages that describe each added change
and see what exactly has changed in the contents. You can see who made the
changes and when it happened.

This is greatly beneficial whether you are working independently or within a
team.

Recommended Hosting Service: [GitHub](https://github.com/)
Other hosting Services: [GitLab](https://gitlab.com/), [BitBucket](https://bitbucket.org/)

Other Tutorials:
 - [Software Carpentry Version Control with Git](http://swcarpentry.github.io/git-novice/)
 - [GitHub 15 Minutes to Learn Git](https://try.github.io/)
 - [Git Commit Best Practices](https://github.com/trein/dev-best-practices/wiki/Git-Commit-Best-Practices)


## Intoduction to Git

## Configuring Git

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

## Making Commits

Now that we have Git configured, let's try using Git do something that is actually helpful.
In this section, we are going to add the python module that we created earlier to our local Git repositories and then update GitHub to reflect this addition.

Look at your repository on GitHub.
Other than the '.gitignore' and 'LICENSE' files that were created when you first created the repository, it should be completely empty.
Our goal in this section is to upload our new module to the repository on GitHub.

First, use a terminal to cd into the top directory of the local repository.
Then, check the status of the project:

~~~
$ git status
~~~
{: .bash}

~~~
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

  modified:   .gitignore
  modified:   LICENSE
  modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

  .DS_Store
  .codecov.yml
  .github/
  .travis.yml
  devtools/
  docs/
  myexample/
  setup.cfg
  setup.py
  versioneer.py

no changes added to commit (use "git add" and/or "git commit -a")
~~~
{: .output}

The part about "Changes not staged for commit" lists all of the "tracked" files that git knows are part of your repository.
We want to tell Git to store all of the changes we have made to these files in the form of a "commit".
You can prepare these for inclusion in the next commit by doing:
~~~
$ git add -u
$ git status
~~~
{: .bash}

~~~
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

  modified:   .gitignore
  modified:   LICENSE
  modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

  .DS_Store
  .codecov.yml
  .github/
  .travis.yml
  devtools/
  docs/
  myexample/
  setup.cfg
  setup.py
  versioneer.py
~~~
{: .output}


The part about "untracked files" tells you that there are certain files located within your local repository that Git is not tracking (i.e., not doing version control on).

To tell Git to start tracking these files, do:

~~~
$ git add <filename>
~~~
{: .bash}

After adding all of the files that belong in the repository check the status again:

~~~
$ git status
~~~
{: .bash}

~~~
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

  new file:   .DS_Store
  new file:   .codecov.yml
  new file:   .github/CONTRIBUTING.md
  new file:   .github/PULL_REQUEST_TEMPLATE.md
  modified:   .gitignore
  new file:   .travis.yml
  modified:   LICENSE
  modified:   README.md
  new file:   devtools/README.md
  new file:   devtools/conda-recipe/bld.bat
  new file:   devtools/conda-recipe/build.sh
  new file:   devtools/conda-recipe/meta.yaml
  new file:   devtools/travis-ci/before_install.sh
  new file:   docs/Makefile
  new file:   docs/README.md
  new file:   docs/_static/README.md
  new file:   docs/_templates/README.md
  new file:   docs/conf.py
  new file:   docs/index.rst
  new file:   docs/make.bat
  new file:   myexample/__init__.py
  new file:   myexample/_version.py
  new file:   myexample/data/README.md
  new file:   myexample/data/look_and_say.dat
  new file:   myexample/myexample.py
  new file:   myexample/tests/__init__.py
  new file:   myexample/tests/test_ssexample.py
  new file:   setup.cfg
  new file:   setup.py
  new file:   versioneer.py

~~~
{: .output}

Git now knows which files it's supposed to keep track of, but it hasn't recorded these changes as a commit yet.
To get it to do that, we need to run one more command:

~~~
$ git commit -m "Adds initial module structure"
~~~
{: .bash}

~~~
[master f67d82f] Adds initial module structure
 30 files changed, 3107 insertions(+), 37 deletions(-)
 create mode 100644 .DS_Store
 create mode 100644 .codecov.yml
 create mode 100644 .github/CONTRIBUTING.md
 create mode 100644 .github/PULL_REQUEST_TEMPLATE.md
 create mode 100644 .travis.yml
 rewrite LICENSE (82%)
 rewrite README.md (100%)
 create mode 100644 devtools/README.md
 create mode 100644 devtools/conda-recipe/bld.bat
 create mode 100755 devtools/conda-recipe/build.sh
 create mode 100644 devtools/conda-recipe/meta.yaml
 create mode 100755 devtools/travis-ci/before_install.sh
 create mode 100644 docs/Makefile
 create mode 100644 docs/README.md
 create mode 100644 docs/_static/README.md
 create mode 100644 docs/_templates/README.md
 create mode 100644 docs/conf.py
 create mode 100644 docs/index.rst
 create mode 100644 docs/make.bat
 create mode 100644 myexample/__init__.py
 create mode 100644 myexample/_version.py
 create mode 100644 myexample/data/README.md
 create mode 100644 myexample/data/look_and_say.dat
 create mode 100644 myexample/myexample.py
 create mode 100644 myexample/tests/__init__.py
 create mode 100644 myexample/tests/test_ssexample.py
 create mode 100644 setup.cfg
 create mode 100644 setup.py
 create mode 100644 versioneer.py
~~~
{: .output}

This command tells Git to save all of our changes to a new commit.

If we run `git status` now, we see that the files we added to the last commit are no longer listed.

~~~
$ git status
~~~
{: .bash}

~~~
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

~~~
{: .output}

We can see a history of all of our changes by doing `git log`:

~~~
$ git log
~~~
{: .bash}

~~~
$ git log
commit f67d82fc72ba33aaa34a52a649fe6e0e3b831711 (HEAD -> master)
Author: Taylor Barnes <tbarnes1@vt.edu>
Date:   Mon Jul 9 01:43:15 2018 -0400

    Adds initial module structure

commit 0e6266107cf8db6034d0c0cc6695851043249e5d (origin/master, origin/HEAD)
Author: taylor-a-barnes <taylor.a.barnes@gmail.com>
Date:   Mon Jul 9 01:07:00 2018 -0400

    Initial commit
~~~
{: .output}

`git log` lists all commits  made to a repository in reverse chronological order.
The listing for each commit includes
the commit's full identifier
(which starts with the same characters as
the short identifier printed by the `git commit` command earlier),
the commit's author,
when it was created,
and the log message Git was given when the commit was created.

Now that you have commited your module, check the GitHub repository again.
It should still only have the '.gitignore', 'LICENSE', and 'README.md' files.
This is because your local Git repository is separate from the remote GitHub repository.
To make your changes show up on GitHub, you will need to run:

~~~
$ git push
~~~
{: .bash}

This command sends all of the new commits in your local repository to the GitHub repository.
Now if you refresh the GitHub webpage you should be able to see all of the new files you added to the repository.


## Working With Multiple Repositories

One of the most potentially frustrating problems in software development is keeping track of all the different copies of the code.
For example, we might start a project on a local desktop computer, switch to working on a laptop during a conference, and then do performance optimization on a supercomputer.
In ye olden days, switching between computers was typically accomplished by copying files via a USB drive, or with ssh, or by emailing things to oneself.
After copying the files, it was very easy to make an important change on one computer, forget about it, and go back to working on the original version of the code on another computer.
Of course, when collaborating with other people these problems get dramatically worse.

Git greatly simplifies the process of having multiple copies of a code development project.
Let's see this in action by making another clone of our GitHub repository.

~~~
$ cd ../
$ git clone git@github.com:git@github.com:taylor-a-barnes/git_example.git friend
$ cd friend
~~~
{: .bash}

Let's create a file in this new directory.

~~~
$ emacs testing.txt
~~~
{: .bash}

~~~
I added this file from a new clone!

~~~

Now we will commit this new file:

~~~
$ git status
~~~
{: .bash}

~~~
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

  testing.txt

nothing added to commit but untracked files present (use "git add" to track)
~~~
{: .output}

~~~
$ git add testing.txt
$ git status
~~~
{: .bash}

~~~
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

  new file:   testing.txt

~~~
{: .output}

~~~
$ git commit -m "Adds testing.txt"
$ git log
~~~
{: .bash}

~~~
commit 449f3859032a1043cb8e6c0b737c1f60317fcd65 (HEAD -> master)
Author: Taylor Barnes <tbarnes1@vt.edu>
Date:   Mon Jul 9 02:14:44 2018 -0400

    Adds testing.txt

commit f67d82fc72ba33aaa34a52a649fe6e0e3b831711 (origin/master, origin/HEAD)
Author: Taylor Barnes <tbarnes1@vt.edu>
Date:   Mon Jul 9 01:43:15 2018 -0400

    Adds initial module structure

commit 0e6266107cf8db6034d0c0cc6695851043249e5d
Author: taylor-a-barnes <taylor.a.barnes@gmail.com>
Date:   Mon Jul 9 01:07:00 2018 -0400

    Initial commit

~~~
{: .output}

Now push the commit:

~~~
$ git push
~~~
{: .bash}

If you check the GitHub page, you should see the testing.txt file.

Now change directories into the original local clone, and check if testing.txt is there:

~~~
$ cd ../<original clone>
$ ls -l
~~~
{: .bash}

~~~
total 168
-rw-r--r--@ 1 tbarnes  staff   1464 Jul  9 01:19 LICENSE
-rw-r--r--  1 tbarnes  staff    620 Jul  9 01:19 README.md
drwxr-xr-x  5 tbarnes  staff    160 Jul  9 01:19 devtools
drwxr-xr-x  9 tbarnes  staff    288 Jul  9 01:19 docs
drwxr-xr-x  8 tbarnes  staff    256 Jul  9 01:19 myexample
-rw-r--r--  1 tbarnes  staff    550 Jul  9 01:19 setup.cfg
-rw-r--r--  1 tbarnes  staff   1557 Jul  9 01:19 setup.py
-rw-r--r--@ 1 tbarnes  staff  68611 Jul  9 01:19 versioneer.py
~~~
{: .output}

To get the newest commit into this clone, we need to pull from the GitHub repository:

~~~
$ git pull
~~~
{: .bash}

~~~
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 1), reused 3 (delta 1), pack-reused 0
Unpacking objects: 100% (3/3), done.
From github.com:taylor-a-barnes/git_example
   f67d82f..449f385  master     -> origin/master
Updating f67d82f..449f385
Fast-forward
 testing.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 testing.txt
~~~
{: .output}

Now we can actually see `testing.txt`:

~~~
$ ls -l
~~~
{: .bash}

~~~
total 176
-rw-r--r--@ 1 tbarnes  staff   1464 Jul  9 01:19 LICENSE
-rw-r--r--  1 tbarnes  staff    620 Jul  9 01:19 README.md
drwxr-xr-x  5 tbarnes  staff    160 Jul  9 01:19 devtools
drwxr-xr-x  9 tbarnes  staff    288 Jul  9 01:19 docs
drwxr-xr-x  8 tbarnes  staff    256 Jul  9 01:19 myexample
-rw-r--r--  1 tbarnes  staff    550 Jul  9 01:19 setup.cfg
-rw-r--r--  1 tbarnes  staff   1557 Jul  9 01:19 setup.py
-rw-r--r--  1 tbarnes  staff     36 Jul  9 02:22 testing.txt
-rw-r--r--@ 1 tbarnes  staff  68611 Jul  9 01:19 versioneer.py
~~~
{: .output}

## Exploring History

First, let's add a line to the end of testing.txt:

~~~
$ emacs testing.txt
~~~
{: .bash}

~~~
I added this file from a new clone!
This line doesn't add any value.

~~~

When working on a project, it is easy to forget exactly what changes we have made to a file.
To check this, do

~~~
$ git diff HEAD testing.txt
~~~
{: .bash}

~~~
diff --git a/testing.txt b/testing.txt
index 166776a..bdc1cb7 100644
--- a/testing.txt
+++ b/testing.txt
@@ -1 +1,2 @@
 I added this file from a new clone!
+This line doesn't add any value.
~~~
{: .output}

"HEAD" just means the most recent commit.
To compare against the commit just before the most recent commit, add "~1" to end of "HEAD":

~~~
$ git diff HEAD~1 testing.txt
~~~
{: .bash}

~~~
diff --git a/testing.txt b/testing.txt
new file mode 100644
index 0000000..bdc1cb7
--- /dev/null
+++ b/testing.txt
@@ -0,0 +1,2 @@
+I added this file from a new clone!
+This line doesn't add any value.
~~~
{: .output}

For the commit befor that, you can do `git diff HEAD~2 MODULE.py`, and so on.

If we want to compare against a specific commit, we can first do "git log" to find the commit's ID, and then do:

~~~
$ git diff f67d82fc72ba33aaa34a52a649fe6e0e3b831711 testing.txt
~~~
{: .bash}

~~~
diff --git a/testing.txt b/testing.txt
new file mode 100644
index 0000000..bdc1cb7
--- /dev/null
+++ b/testing.txt
@@ -0,0 +1,2 @@
+I added this file from a new clone!
+This line doesn't add any value.
~~~
{: .output}

Another problem that we sometimes encounter is wanting to undo all of our changes to a particular file.
This can be done with

~~~
$ git checkout HEAD testing.txt
$ cat testing.txt
~~~
{: .bash}

~~~
I added this file from a new clone!
~~~
{: .output}

Of course, you could also replace `HEAD` here with `HEAD~1` or a specific commit ID.



## Ignoring Files

## Conflict Resolution

Make conflicting commits in the two different repositories.

Push one, then try to push the other.

Illustrate what kinds of commits conflict and what types don't.

## Pull requests

## Branching and Forking

## Using GitHub

## Pull requests

## Managing a Repository

Keeping branches under control

Giving access to collaborators.

Evaluating pull requests.

## Best practices

{% include links.md %}
