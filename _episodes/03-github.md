---
title: "Using GitHub"
teaching: 30
exercises: 5
questions:
- "How do I use git and GitHub?"
objectives:
- "Explain reasons to use GitHub."

keypoints:
- "You can use GitHub to store your project online where you or others can access it from a central repository."
- "You can use GitHub to store your projects so you can work on them from multiple computers."

---

## Putting your repository on GitHub.
Now, let's put this project on GitHub so that we can share it with others. In your browser, navigate to `github.com`. Log in to you account if you are not already logged in. On the left side of the page, click the green button that says `New` to create a new repository. Give the repository the name `molecool`.

Note for the last question, "Initialize this repository with a README". We will leave this unchecked in our case because we have an existing repository (as described by GitHub, "This will let you immediately clone the repository to your computer. Skip this step if you’re importing an existing repository."). If you were creating the repository on GitHub, you would select this. There are also options for adding a `.gitignore` file or a license. However, since cookiecutter created these for us, we will not add them.

Click `Create repository`.

Now, GitHub very helpfully gives us directions for how to get our code on GitHub.

Before we follow these directions, let's look at a few things in the repository. When you want to be able to put your code online in a repository, you have to add what git calls `remotes`. Currently, our repository has no remotes. See this by typing

~~~
$ git remote -v
~~~
{: .language-bash}


You should see no output. Now, follow the instructions on GitHub under "...or push an existing repository from the command line"
~~~
$ git remote add origin https://github.com/YOUR_GITHUB_USERNAME/molecool.git
dgit branch -M main
git push -u origin main
~~~
{: .language-bash}

The first command adds a remote named `origin` and sets the URL to our repository. The word `origin` here is simply a word that is a shortcut for the location of our repository. We could have called it anything (like `pickle`, or `banana`, or anything we wanted), but `origin` is used by convention. Now, whenever we say `origin`, git knows that we really mean `https://github.com/YOUR_GITHUB_USERNAME/molecool.git`. 

The second command changes our primary branch name from `master` to `main`. GitHub recently decided (as of June 2020) to switch the name of your `main` branch from `master` to `main`. However, the `git` software will still name your primary (or first) branch `master`.  After the second command, you will no longer see `master` when using the command `git branch` (instead seeing `main`). 

The third command copies (or "pushes") everything which we have tracked using git to `origin`. The word `main` means we are pushing the `main` branch. 

Now if you refresh the GitHub webpage you should be able to see all of the new files you added to the repository.

## Working With Multiple Repositories

One of the most potentially frustrating problems in software development is keeping track of all the different copies of the code.
For example, we might start a project on a local desktop computer, switch to working on a laptop during a conference, and then do performance optimization on a supercomputer.
In ye olden days, switching between computers was typically accomplished by copying files via a USB drive, or with ssh, or by emailing things to oneself.
After copying the files, it was very easy to make an important change on one computer, forget about it, and go back to working on the original version of the code on another computer.
Of course, when collaborating with other people these problems get dramatically worse.

Git greatly simplifies the process of having multiple copies of a code development project.
Let's see this in action by making another clone of our GitHub repository. For this next exercise **you must first navigate out of your project folder**.

~~~
$ cd ../
$ git status
~~~
{: .bash}

Before continuing to the next command, make sure you see the following output:

~~~
fatal: Not a git repository (or any of the parent directories): .git
~~~
{: .output}

If you do not get this message, do `cd ../` until you see it.

Next, make another copy of your repository. We'll use this to simulate working on another computer.

~~~
$ git clone https://github.com/YOUR_GITHUB_USERNAME/molecool.git molecool_friend
$ cd molecool_friend
~~~
{: .bash}

Check the remote on this repository. Notice that when you clone a repository from GitHub, it automatically has that repository listed as `origin`, and you do not have to add
the remote the way we did when we did not clone the repository.

~~~
$ git remote -v
~~~
{: .language-bash}

~~~
origin  https://github.com/YOUR_GITHUB_USERNAME/molecool.git (fetch)
origin  https://github.com/YOUR_GITHUB_USERNAME/molecool.git (push)
~~~

Create the file `testing.txt` in this new directory and make it contain the following.
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
On branch main
Your branch is up to date with 'origin/main'.

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
On branch main
Your branch is up to date with 'origin/main'.

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

Now push the commit:

~~~
$ git push
~~~
{: .bash}

If you check the GitHub page, you should see the testing.txt file.

Now change directories into the original local clone, and check if `testing.txt` is there:

~~~
$ cd ../<original clone>
$ ls -l
~~~
{: .bash}

To get the newest commit into this clone, we need to pull from the GitHub repository:

~~~
$ git pull origin main
~~~
{: .bash}

~~~
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 1), reused 3 (delta 1), pack-reused 0
Unpacking objects: 100% (3/3), done.
From https://github.com/YOUR_GITHUB_USERNAME/molecool
 * branch            main     -> FETCH_HEAD
   2ac4843..754da2b  main     -> origin/main
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
First, lets ensure that we have a few dummy files. Make empty files called `testing.txt~` and `README.md~` in your repository using your text editor of choice.


While we're at it, also make some other files that aren't important to the project. Make a file called `calculation.out` in `molecool/data` using your text editor of choice.

Now check what Git says about these files:

~~~
$ git status
~~~
{: .bash}

~~~
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	README.md~
	molecool/data/calculation.in
	molecool/data/calculation.out
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

Git looks at `.gitignore` and ignores any files or directories that match one of the lines.
Add the following to the end of `.gitignore`:

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
On branch main
Your branch is up to date with 'origin/main'.

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
$ cd ../molecool_friend
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
To https://github.com/YOUR_GITHUB_USERNAME/molecool.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/YOUR_GITHUB_USERNAME/molecool.git'
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
From https://github.com/YOUR_GITHUB_USERNAME/molecool
   754da2b..de54818  main     -> origin/main
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
On branch main
Your branch and 'origin/main' have diverged,
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

## More GitHub Features

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
