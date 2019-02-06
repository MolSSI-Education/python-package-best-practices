---
title: "Git and GitHub"
teaching: 30
exercises: 5
questions:
- "How do I use git and GitHub?"
objectives:
- "Explain the purpose of version control."
- "Introduce common git commands."
- "Explain use of .gitignore file"
- "Resolve a merge conflict"
keypoints:
- "Git provides a way to track changes and differences between versions."
- "git can be used with an online repository (GitHub) so that you can access a copy of your code from any machine"

---

> ## Prerequisites
>
> - Created GitHub account (described in set-up)
> - Configured git (described in set-up)
> - The Python package created in Episode 1.
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

> ## git vs. GitHub
>
> `git` is the software used for version control, while GitHub is a hosting service. You can use `git` locally (without using an online hosting service), or you can use it with other hosting services such as GitLab or BitBucket.
> Other examples of version control software include SVN, and Mercurial.
>
{: .callout}

MolSSI recommends using the software `git` for version control, and [GitHub] as a hosting service, though there are other options.

Recommended Hosting Service: [GitHub]  
Other hosting Services: [GitLab], [BitBucket]

## Making Commits

Now that we have Git configured, let's try using Git do something that is actually helpful.
In this section, we are going to  edit files in the python package that we created earlier, and use `git` to track those changes.

First, use a terminal to `cd` into the top directory of the local repository.

When we ran the CMS CookieCutter, it actually initialized the use of `git` for us, added our files, and made a commit (how convenient!). We can see this by typing

~~~
ls -la
~~~

Here, the `-la` says that we want to list the files in long format (`-l`), and show hidden files (`-a`). You should see several files starting with `.git`. In particular, `.git` is a directory where `git` stores the repository data. We can tell from this output that we are in a git repository.

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

This tells us that we are on the `master` branch, and that no files have been changed since the last commmit.

Next, type
~~~
$ git log
~~~
{: .bash}

You will get an output resembling the following:
~~~
commit 25ab1f1a066f68e433a17454c66531e5a86c112d (HEAD -> master, tag: 0.0.0)
Author: Your Name <your_email@something.com>
Date:   Mon Feb 4 10:45:26 2019 -0500

    Initial commit after CMS Cookiecutter creation, version 1.0
~~~
{: .output}

When we have more commits (or versions) of our code, `git log` will show a history of these commits. Right now, we have only one commit - the one created by the CMS CookieCutter.

Now, we will change some files and use `git` to track those changes. Let's edit our README. Open `README.md` in your text editor of choice. On line 8, you should see the description of the repository we typed when running the cookiecutter. Add the following sentence to your `README` under the initial description.

~~~
This repository is currently under development. To do a developmental install, download this repository and type

`pip install -e .`

in the repository directory.
~~~

Once you have saved this file, type

~~~
$ git status
~~~
{: .language-bash}

and you should see

~~~
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
~~~
{: .output}

This tells that since the last commit, we have modified the file `README.md`. In order to commit these changes using `git`, we first have to "stage" the changes using `git add`, then store the changes using `git commit`.

~~~
$ git add README.md
~~~
{: .language-bash}

Now, when we check the status, we should see the following:

~~~
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   README.md
~~~
{: .output}

Now, we see that we have staged this file to be committed. Commit the file

~~~
$ git commit -m "Add instructions for developmental install to README"
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

~~~
commit 2ac484309fe62f9a847a4daae1a1fa078dca306b (HEAD -> master)
Author: Jessica Nash <janash@vt.edu>
Date:   Wed Feb 6 12:47:45 2019 -0500

    Add instructions for developmental install to README

commit 25ab1f1a066f68e433a17454c66531e5a86c112d (tag: 0.0.0)
Author: Jessica Nash <janash@vt.edu>
Date:   Mon Feb 4 10:45:26 2019 -0500

    Initial commit after CMS Cookiecutter creation, version 1.0
~~~
{: .output}

Now, we have a second commit at the top of of our git log with the message we just typed. `git log` lists all commits  made to a repository in reverse chronological order.
The listing for each commit includes
the commit's full identifier
(which starts with the same characters as
the short identifier printed by the `git commit` command earlier),
the commit's author,
when it was created,
and the log message Git was given when the commit was created.

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

## Putting your repository on GitHub.
Now, let's put this project on GitHub so that we can share it with others. In your browser, navigate to `github.com`. Log in to you account if you are not already logged in. On the left side of the page, click the green button that says `New` to create a new repository. Give the repository the name `molssi_devops`.

Note for the last question, "Initialize this repository with a README". We will leave this unchecked in our case because we have an existing repository (as described by GitHub, "This will let you immediately clone the repository to your computer. Skip this step if you’re importing an existing repository."). If you were creating the repository on GitHub, you would select this. There are also options for adding a `.gitignore` file or a license. However, since cookiecutter created these for us, we will not add them.

Click `Create repository`.

Now, GitHub very helpfully gives us directions for how to get our code on GitHub.

Before we follow these directions, let's look at a few things in the repository. When you want to be able to put your code online in a repository, you have to add what git calls `remotes`. Currently, our repository has no remotes. See this by typing

~~~
$ git remote -v
~~~

You should see no output. Now, follow the instructions on GitHub under "...or push an existing repository from the command line"
~~~
$ git remote add origin https://github.com/janash/molssi_devops.git
$ git push -u origin master
~~~
{: .language-bash}

The first command adds a remote named `origin` and sets the URL to our repository. The second command pushes our repo to where we have set as origin. The word `master` means we are pushing the `master` branch.

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
$ git clone https://github.com/janash/molssi_devops.git devops_friend
$ cd devops_friend
~~~
{: .bash}

Create the file `testing.txt` in this new directory and make it contain the following.

~~~
$ touch testing.txt
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
$ git add .
$ git status
~~~
{: .bash}

> ## git add
> Here, we've used `git add .` instead of `git add testing.txt`. Using this command will add all untracked or changed files.
{: .callout}

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
commit 754da2b322d649fc358d4d85041a651337eb8241 (HEAD -> master)
Author: Jessica Nash <janash@vt.edu>
Date:   Wed Feb 6 16:29:45 2019 -0500

    Adds testing.txt

commit 2ac484309fe62f9a847a4daae1a1fa078dca306b (origin/master, origin/HEAD)
Author: Jessica Nash <janash@vt.edu>
Date:   Wed Feb 6 12:47:45 2019 -0500

    Add instructions for developmental install to README

commit 25ab1f1a066f68e433a17454c66531e5a86c112d
Author: Jessica Nash <janash@vt.edu>
Date:   Mon Feb 4 10:45:26 2019 -0500

    Initial commit after CMS Cookiecutter creation, version 1.0
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

To get the newest commit into this clone, we need to pull from the GitHub repository:

~~~
$ git pull origin master
~~~
{: .bash}

~~~
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 1), reused 3 (delta 1), pack-reused 0
Unpacking objects: 100% (3/3), done.
From https://github.com/janash/molssi_devops
 * branch            master     -> FETCH_HEAD
   2ac4843..754da2b  master     -> origin/master
Updating 2ac4843..754da2b
Fast-forward
 testing.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 testing.txt
~~~
{: .output}

Now we can actually see `testing.txt` in our original repository.

## Exploring History

In your original repository, open the `testing.txt` file and add the following line to the end of the file.

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
index 166776a..a634bfb 100644
--- a/testing.txt
+++ b/testing.txt
@@ -1 +1,3 @@
 I added this file from a new clone!
+This line doesn't add any value.
+
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
index 0000000..a634bfb
--- /dev/null
+++ b/testing.txt
@@ -0,0 +1,3 @@
+I added this file from a new clone!
+This line doesn't add any value.
+
~~~
{: .output}


If we want to compare against a specific commit, we can first do "git log" to find the commit's ID, and then do:

~~~
$ git diff *commit_id* testing.txt
~~~
{: .bash}

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
For example, if your text editor is Emacs, you may end up with lots of files called `<filename>~`.
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
$ touch molssi_devops/data/calculation.in molssi_devops/data/calculation.out
$ ls -l
~~~
{: .bash}

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
	molssi_devops/data/calculation.in
	molssi_devops/data/calculation.out
	testing.txt~

nothing added to commit but untracked files present (use "git add" to track)
~~~
{: .output}

Now we will make Git stop telling us about these files.

Earlier, when we looked at the hidden files, you may have noticed a file called `.gitignore`. Cookiecutter created this for us, however, GitHub also has built in `.gitignore` files you can add when creating an empty repository.

This file is to tell `git` which types of files we would like to ignore (thus the name `.gitignore`)

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
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

...
~~~

Git looks at .gitignore and ignores any files or directories that match one of the lines.
Add the following to the end of .gitignore:

~~~
# emacs
*~

# temporary data files
*.in
*.out

~~~

Now do "git status" again. Notice that the files we added are no longer recognized by git.

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

It is possible to override this with the "-f" option for git add.

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
$ cd ../devops_friend
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
To https://github.com/janash/molssi_devops.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/janash/molssi_devops.git'
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
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 6 (delta 3), reused 5 (delta 2), pack-reused 0
Unpacking objects: 100% (6/6), done.
From https://github.com/janash/molssi_devops
   754da2b..de54818  master     -> origin/master
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
and have 1 and 2 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Changes to be committed:

	modified:   .gitignore

Unmerged paths:
  (use "git add <file>..." to mark resolution)

	both modified:   testing.txt

~~~
{: .output}

The conflict is in testing.txt, so let's open it up:

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

The conflict is shown within the `<<<<<<<` and `>>>>>>>` bits.
The part before the `=======` is what we added in the commit in the `devops_friend` clone, while the part after it comes from the original local clone.
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
$ git add .
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

## More Tutorials
If you want more `git`, see the following tutorials.

### Basic git
 - [Software Carpentry Version Control with Git](http://swcarpentry.github.io/git-novice/)
 - [GitHub 15 Minutes to Learn Git](https://try.github.io/)
 - [Git Commit Best Practices](https://github.com/trein/dev-best-practices/wiki/Git-Commit-Best-Practices)


{% include links.md %}
[GitHub]: https://github.com
[GitLab]: https://gitlab.com/
[BitBucket]: https://bitbucket.org/
