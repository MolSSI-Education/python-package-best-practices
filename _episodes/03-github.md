---
title: "Git and GitHub"
teaching: 90
exercises: 120
questions:
- "How do I use git and GitHub?"
---

> ## Prerequisites
>
> We will start with the Git repositories created in Episode 1.
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

Sometimes while you work on a project, you may end up creating some temporary files.
For example, if your text editor is Emacs, you may end up with lots of files called `~<filename>`.
By default, Git tracks all files, including these.
This tends to be annoying, since it means that any time you do "git status", all of these unimportant files show up.

We are now going to find out how to tell Git to ignore these files, so that it doesn't keep telling us about them ever time we do "git status".
Even if you aren't working with Emacs, someone else working on your project might, so let's do the courtesy of telling Git not to track these temporary files.
First, lets ensure that we have a few dummy files:

~~~
$ touch testing.txt~
$ touch README.md~
$ ls -l
~~~
{: .bash}

While we're at it, also make some other files that aren't important to the project:

~~~
$ mkdir data
$ touch data/calculation.in data/calculation.out
$ ls -l
~~~
{: .bash}

~~~
total 184
-rw-r--r--@ 1 tbarnes  staff   1464 Jul  9 01:19 LICENSE
-rw-r--r--  1 tbarnes  staff    620 Jul  9 01:19 README.md
-rw-r--r--  1 tbarnes  staff      0 Jul  9 02:54 README.md~
drwxr-xr-x  4 tbarnes  staff    128 Jul  9 02:57 data
drwxr-xr-x  5 tbarnes  staff    160 Jul  9 01:19 devtools
drwxr-xr-x  9 tbarnes  staff    288 Jul  9 01:19 docs
drwxr-xr-x  8 tbarnes  staff    256 Jul  9 01:19 myexample
-rw-r--r--  1 tbarnes  staff    550 Jul  9 01:19 setup.cfg
-rw-r--r--  1 tbarnes  staff   1557 Jul  9 01:19 setup.py
-rw-r--r--  1 tbarnes  staff     36 Jul  9 02:49 testing.txt
-rw-r--r--  1 tbarnes  staff     36 Jul  9 02:54 testing.txt~
-rw-r--r--@ 1 tbarnes  staff  68611 Jul  9 01:19 versioneer.py
~~~
{: .output}


Now check what Git says about these files:

~~~
$ git status
~~~
{: .bash}

~~~
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	README.md~
	data/
	testing.txt~

nothing added to commit but untracked files present (use "git add" to track)
~~~
{: .output}

Now we will make Git stop telling us about these files.
Remember that wierd ".gitignore" file from earlier?
This is what that file is for.
If you open it up, you will see

~~~
$ emacs .gitignore
~~~
{: .bash}

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
...
~~~

Git looks at .gitignore and ignores any files or directories that match one of the lines.
Add the following to the end of .gitignore:

~~~
# emacs
*~

# temporary data files
data

~~~

Now do "git status" again:

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

no changes added to commit (use "git add" and/or "git commit -a")
~~~
{: .output}

We want these additions to .gitignore to become a permanent part of the repository, so do

~~~
$ git add .gitignore
$ git commit -m "Ignores Emacs temporary files and data directory"
$ git push
~~~
{: .bash}

One nice feature of .gitignore is that prevents us from accidentally adding a file that shouldn't be part of the repository.
For example:

~~~
$ git add data/calculation.in
~~~
{: .bash}

~~~
The following paths are ignored by one of your .gitignore files:
data/calculation.in
Use -f if you really want to add them.
~~~
{: .output}

It is possible to overide this with the "-f" option for git add.


## Conflict Resolution

Now we will make a few new edits to testing.txt:

~~~
$ emacs testing.txt
~~~
{: .bash}

Add a dummy header and footer the testing.txt, so that it looks like this:

~~~
***************************************
This is	the start of testing.txt
***************************************

I added this file from a new clone!

***************************************
This is	the end	of testing.txt
***************************************
~~~

Now commit and push this edit.

~~~
$ git add testing.txt
$ git commit -m "Adds a new line to testing.txt"
$ git push
~~~
{: .bash}

Now switch over to the `friend` clone.

~~~
$ cd ../friend
~~~
{: .bash}

We are going to add another line to testing.txt, so that it looks like this

~~~
I added this file from a new clone!
Now I added a new line!
~~~

Now try committing and pushing the change:

~~~
$ git add testing.txt
$ git commit -m "Adds another line to testing.txt"
$ git push
~~~
{: .bash}

~~~
To github.com:taylor-a-barnes/git_example.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'git@github.com:taylor-a-barnes/git_example.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
~~~
{: .output}

The push failed, because the `friend` clone is not up-to-date with the repository on GitHub.
We can fix this by doing a pull:

~~~
$ git pull
~~~
{: .bash}

~~~
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 1), reused 3 (delta 1), pack-reused 0
Unpacking objects: 100% (3/3), done.
From github.com:taylor-a-barnes/git_example
   b0b7d79..64e358f  master     -> origin/master
Auto-merging testing.txt
CONFLICT (content): Merge conflict in testing.txt
Automatic merge failed; fix conflicts and then commit the result.
~~~
{: .output}

Unfortunately, the `pull` also failed, due to a `conflict`.
To see which files have the conflict, we can do:

~~~
$ git status
~~~
{: .bash}

~~~
On branch master
Your branch and 'origin/master' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)

	both modified:   testing.txt

no changes added to commit (use "git add" and/or "git commit -a")
~~~
{: .output}

The conflict is in testing.txt, so let's open it up:

~~~
$ emacs testing.txt
~~~
{: .bash}

~~~
***************************************
This is the start of testing.txt
***************************************

I added this file from a new clone!
<<<<<<< HEAD
Now I added a new line!
=======

***************************************
This is the end of testing.txt
***************************************
>>>>>>> 12651a37de10d61d9e9eea31c260c15b7ef3b5d4
~~~

The conflict is shown within the `<<<<<<<` and '>>>>>>>' bits.
The part before the `=======` is what we added in the commit in the `friend` clone, while the part after it comes from the original local clone.
We need to decide what to do about the conflict, tidy it up, and then make a new commit.
Edit testing.txt so that it reads:

~~~
***************************************
This is the start of testing.txt
***************************************

I added this file from a new clone!
Now I added a new line!

***************************************
This is the end of testing.txt
***************************************

~~~


~~~
$ git add testing.txt
$ git commit -m "Fixed merge conflicts in testing.txt"
$ git push
~~~
{: .bash}

This time everything should work correctly.
Generally speaking, your procedure when ready to commit should be:


~~~
$ git commit -m "Commit message"
$ git pull
$ <fix any merge conflicts>
$ git push
~~~
{: .bash}



## Using GitHub

Navigate to the GitHub page for your project.
Click on "testing.txt".
Here you can see the file and make changes to it.
Click the edit button, which looks like a small pencil near the upper right of the file text box.
Add a line that says "I added this line from the GitHub web interface!", so that the file looks like:

~~~
***************************************
This is the start of testing.txt
***************************************

I added this file from a new clone!
Now I added a new line!
I added this line from the GitHub web interface!

***************************************
This is the end of testing.txt
***************************************

~~~

Scroll to the bottom of the page and write the name "Added a line to testing.txt from the web interface" for this commit.
Then, click the green "Commit changes" button at the bottom left.
You should now see that your change appears in the text box.

Click the "Blame" button to find out who is responsible for each line of code.
Click the "History" button to see a list of all commits that affected this file.
You can click on a commit to see exactly what it did.

Go back to the main project page, and click the "commits" button.
Here you can see a list of all the commits for this project.
Clicking them reveals how they changed the code.

The "Issues" tab lets you create discussions about bugs, performance limitations, feature requests, or ongoing work that are shared with everyone else who is working on the project.
Try filling out a quick issue now.
Then comment and close the issue.

Now let's look at some of your repository's settings.
Click the "Settings" button to the right of the little gear.
This will take you to some options that will help you to maintain your repository.

This page lets you do several important things, including rename, relocate, transfer, or delete your repository.

Underneath the "Features" heading you will notice an option to "Restrict editing to collaborators only".
This option prevents random strangers from being able to push changes to your repository, and should always be kept on.
To allow other people to work with you, you can assign collaborators.
Click the "Collaborators" tab on the left.
This will take you to a searchbar where you can search for the names of other github users.
By finding someone using the searchbar and then clicking "Add collaborator", you can allow specific people to contribute to your project.
Generally speaking, you should only list someone as a collaborator if you work with them closely and trust that they won't do anything especially unwise with your repository.

People you don't know very well shouldn't be listed as collaborators, but there are still ways for them to contribute improvements to your project.
In the next couple of sections, we will explore how this works in detail.



## Forks

We have seen how it is possible to allow other people to contribute to a project by listing them as collaborators.  This works fine for a project that only a handful of people work on, but what about large open-source projects that might have hundreds of people who are interested in adding their own features?  No one wants to add of those names to the list of collaborators, and giving everyone who asks the ability to push anything they want to the repository is guaranteed to lead to problems.  The solution to this question comes in the form of “forks.”

Unfortunately, the work “fork” has multiple possible meanings in the context of open-source software development.
Once upon a time, open-source software developers used the word “fork” to refer to the idea of taking an existing software project, making a copy of it, changing the name, and then developing it completely independently of the original project.
For the purpose of this discussion, every time we use the word “fork,” we mean what happens when you push the fork button in GitHub.

A fork is a copy of a repository that is largely independent of the original.
The maintainer of the original repository doesn’t have to do anything or know about the existence of the fork.
Want to make changes to an open-source project, but aren’t listed as a collaborator on the project?  Just make a fork, which you own and can manage in the same way as any other repository that you create on GitHub.
If you want to submit changes to the project’s official repository, you can create a “pull request”, which we will discuss in more detail in the next section.

For now, we will learn how to create and maintain a fork.
During this section, you will need to partner up with someone else.

From your partner, get the URL of their GitHub
This should look like `https://github.com/<username>/<repo name>`
Navigate to this URL in your web browser.

Create a personal fork of the repository by pressing the “Fork” button near the top right of the web int\
erface.

Then, make a clone of the fork:

~~~
$ cd ../
$ git clone <fork URL> fork_clone
$ cd fork_clone
~~~
{: .bash}

Open testing.txt and add a new line ("This line was added by <my username>."), so that it looks like:

~~~
***************************************
This is the start of testing.txt
***************************************

I added this file from a new clone!
Now I added a new line!
I added this line from the GitHub web interface!
This line was added by <my username>.

***************************************
This is the end of testing.txt
***************************************
~~~

Now commit and push this change:

~~~
$ git add testing.txt
$ git commit -m "Adds a line to the fork"
$ git pull
$ git push
~~~
{: .bash}

Use your browser to confirm that this change shows up in the fork.
Have your partner check their repository - does the change appear for them?

Have your partner use the web interface to create and commit a new file called `another_test.txt`.
Check the web interface for your fork.
Does `another_test.txt` appear in it?

While you work on your fork, you should keep it synced with the original repository.
To do this, you need to tell Git where to find the repository that you forked from (the `upstream`) repository.
Git tracks the remote repositories that a particular clone is associated with, which you can see by doing:

~~~
$ git remote -v
~~~
{: .bash}

~~~
origin   https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
origin   https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
~~~
{: .output}

The `origin` remote corresponds to the fork that you cloned from.
We want to tell Git where the `upstream` remote is:

~~~
git remote add upstream <original repo’s URL>
git remote -v
~~~
{: .bash}

~~~
origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)
upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)
~~~
{: .output}

~~~
git pull upstream master
git push
~~~
{: .bash}



## Pull requests

It is now time to incorporate the edits you have made in you fork into the original repository.
To do this, we must create a `Pull Request`.

Navigate to the URL of your fork.
Click the "New pull request" button that is located to the right of the "Branch" button.
You should now see a summary of what the pull request will do.
Click the green "Create pull request" button.

Add a title to the pull request.
We will go with "Improvements to testing.txt"
Underneath the title, write something like:

~~~
## Description
Adds a line to testing.txt that improves it for these specific reasons:
 - It adds a specific useful feature: _______.
 - It improves the readability of a particular part of the code by doing a specific thing.
 - It enhances the performance of a particular part of the code, which I have testing under these specific conditions.

Also, here are some details about the motivation behind the changes made by this pull request.

## Todos
 - This change is intended to be a stepping-stone towards ________.
 - I plan to submit a future pull request that builds on this one in these specific ways:

## Questions
 - Are these changes consistent with the overal goal of the project?
 - I noticed that changes recently made by _______ seem to affect similar regions of the code.  Are conflicts between our efforts likely.  What could be done to avoid this.
 - What could I do to improve the quality of my pull request?
 
## Status
 - These specific planned features: _______ are not yet fully implemented.

Thank you for taking at look at these proposed changes.  I look forward to hearing any feedback you might have.
~~~

Submit the pull request.

Ask your partner to review the pull request.
They can do this by going to the URL of their personal repository and then clicking the "Pull Requests" tab.
They should see a single pull request listed.
If they click it, they will see everything that you wrote.
They should now click the "Merge Pull Request" button, followed by "Confirm merge".

Your changes should now appear in your partner's repository.
Congratulations on your first successful pull request!


## Managing a Repository

Whenever you manage or contribute to a Git project, you will find yourself asking many practical questions, like "How big should my commits be?", “Should I make one big pull request, or lots of smaller ones?”, “How often should I sync my fork with the original project?”.

Broadly speaking, there are two main philosophies for managing a Git repo: “branching” and “continuous integration” (CI).

For many years, the prevailing opinion was that anyone working on a new feature for a code should create a development branch where they can work in isolation from the master branch.
Branches would only be merged back into the master after features were completed and thoroughly bug tested.
In principle, this meant that the master was kept “pristine,” with no partially implemented features or buggy code.
In practice, this approach tended to lead to a tedious, conflict-laden merge process that was itself prone to produce bugs.

At MolSSI, we recommend the CI approach.
The idea behind CI is that developers contribute their modifications to the code early and often – typically at least once a day.
This approach helps to ensure that merges are relatively painless, bug-free processes, while also making the code easier to maintain.
CI-based approaches also tend to emphasize the importance of regular bug testing.



