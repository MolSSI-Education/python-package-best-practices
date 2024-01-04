# GitHub

````{admonition} Overview
:class: overview

Questions:

* How do I use GitHub to host my projects?
* How do I use git and GitHub togehter?

Objectives:

* Explain reasons to use GitHub.

````

:::{admonition} Follow Along with This Lesson
:class: tip

To follow along with this lesson, you can complete the previous lessons,
or you can download a pre-made workshop repository that is at the starting 
point.

- [Download the pre-made workshop repository as a zip file](https://github.com/MolSSI-Education/molecool/archive/refs/tags/github-start.zip)

Alternatively, download the repository using the command line:

````{tab-set-code} 
```{code-block} shell
git clone https://github.com/MolSSI-Education/molecool.git
git checkout github-start
```
````
:::

## Securely accessing GitHub
During the setup for this workshop, we generated an SSH key and added it to our GitHub account.
The SSH key will allow us to authenticate our identity to GitHub, allowing us to access our remote repositories.
For the purposes of this workshop, an SSH key is a good way to quickly and conveniently get set up using GitHub.
If you completed the [Set Up](setup.md) instructions, you will have an SSH key set up already.

If you continue further development using GitHub after this workshop, you may want to consider alternatives.

GitHub has added a feature called Personal Access Tokens (PATs) that allow for more fine-grained security control over your access.
Instead of one key that has all the permissions on your account, you can define multiple tokens that have a different set of permissions.
GitHub has good documentation for [generating and using a PAT](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token).


## Putting your repository on GitHub.
Now, let's put this project on GitHub so that we can share it with others.
In your browser, navigate to [github.com](https://www.github.com).
Log in to your account if you are not already logged in.
On the left side of the page, click the green button that says `New` to create a new repository.
Give the repository the name `molecool`.

Note for the last question, "Initialize this repository with a README".
We will leave this unchecked in our case because we have an existing repository.
(As described by GitHub, "This will let you immediately clone the repository to your computer.
Skip this step if you’re importing an existing repository.")
If you were creating the repository on GitHub, you would select this.
There are also options for adding a `.gitignore` file or a license.
However, since `cookiecutter` created these for us, we will not add them.

Click `Create repository`.

Now, GitHub very helpfully gives us directions for how to get our code on GitHub.

### Repository Remotes

Before we follow these directions, let's look at a few things in the repository.
When you want to be able to put your code online in a repository, you have to add what git calls `remotes`.
Currently, our repository has no remotes. Check this by typing:

````{tab-set-code} 

```{code-block} shell
git remote -v
```
````



you should see no output.
Now, follow the instructions on GitHub under "...or push an existing repository from the command line"
````{tab-set-code} 

```{code-block} shell
git remote add origin git@github.com:YOUR_GITHUB_USERNAME/molecool.git
git branch -M main
git push -u origin main
```
````


The first command adds a remote named `origin` and sets the URL to our repository.
The word `origin` here is simply a word that is a shortcut for the location of our repository.
We could have called it anything (like `pickle`, or `banana`, or anything we wanted), but `origin` is used by convention.
Now, whenever we say `origin`, git knows that we really mean `git@github.com:YOUR_GITHUB_USERNAME/molecool.git`. 

The second command changes our primary branch name from `master` to `main`.
GitHub recently decided (as of June 2020) to switch the name of your `main` branch from `master` to `main`.
However, the `git` software will still name your primary (or first) branch `master`. 
After the second command, you will no longer see `master` when using the command `git branch` (instead you will see `main`). 

The third command copies (or "pushes") everything which we have tracked using git to `origin`.
The word `main` means we are pushing the `main` branch. 

Now, if you refresh the GitHub webpage you should be able to see all the new files you added to the repository.

This is now an effective entry point for people discovering your project,
but you should document the URL within your repository contents, in case people
acquire your package some other way.
For now, at least, update your `pyproject.toml`, and put this GitHub repository URL
for the Source URL for your package's metadata.

## Working With Multiple Repositories

One of the most potentially frustrating problems in software development is keeping track of all the different copies of the code.
For example, we might start a project on a local desktop computer, switch to working on a laptop during a conference, and then do performance optimization on a supercomputer.
In the olden days, switching between computers was typically accomplished
by copying files via a USB drive or with `ssh` or by emailing things to oneself.
After copying files, it was very easy to make an important change on one computer,
forget about it, then resume work with the original code version on another computer
(having forgotten to reapply the important change).
Of course, when collaborating with other people such problems get dramatically worse.

Git greatly simplifies the process of maintaining multiple copies of a code development project.
Let's see this in action by making another clone of our GitHub repository.
For this next exercise **you must first navigate out of your project folder**.

````{tab-set-code} 

```{code-block} shell
cd ../
git status
```
````


Before continuing to the next command, make sure you see the following output:

````{tab-set-code} 

```{code-block} output
fatal: Not a git repository (or any of the parent directories): .git
```
````


If you do not get this message, do `cd ../` until you see it.

Next, make another copy of your repository.
We'll use this to simulate working on another computer.

````{tab-set-code} 

```{code-block} shell
git clone git@github.com:YOUR_GITHUB_USERNAME/molecool.git molecool_friend
cd molecool_friend
```
````


Check the `remote` on this repository.
Notice that when you clone a repository,
the source is automatically recorded as `origin`,
and you do not have to add the remote the way we did when we created the repository locally.

````{tab-set-code} 

```{code-block} shell
git remote -v
```
````


````{tab-set-code} 

```{code-block} output
origin  git@github.com:YOUR_GITHUB_USERNAME/molecool.git (fetch)
origin  git@github.com:YOUR_GITHUB_USERNAME/molecool.git (push)
```
````


Create the file `testing.txt` in this new directory and make it contain the following.

````{tab-set-code} 

```{code-block} testing.txt
I added this file from a new clone!
```
````

Now we will commit this new file:

````{tab-set-code}
``` shell
git status
```
````


````{tab-set-code} 

```{code-block} output
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

  testing.txt

nothing added to commit but untracked files present (use "git add" to track)
```
````


````{tab-set-code} 

```{code-block} shell
git add .
git status
```
````

```{admonition} git add .
:class: tip 

 Here, we've used `git add .` instead of `git add testing.txt`.

Using this command will add all untracked or changed files.
```

````{tab-set-code} 

```{code-block} output
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

  new file:   testing.txt

```
````


````{tab-set-code} 

```{code-block} shell
git commit -m "Adds testing.txt"
git log
```
````


Now push the commit:

````{tab-set-code} 

```{code-block} shell
git push
```
````


If you check the GitHub page, you should see the `testing.txt` file.

Now change directories into the original local clone, and check if `testing.txt` is there:

````{tab-set-code} 

```{code-block} shell
cd ../<original clone>
ls -l
```
````


To get the newest commit into this clone, we need to pull from the GitHub repository:

````{tab-set-code} 

```{code-block} shell
git pull origin main
```
````


````{tab-set-code} 

```{code-block} output
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 1), reused 3 (delta 1), pack-reused 0
Unpacking objects: 100% (3/3), done.
From github.com:YOUR_GITHUB_USERNAME/molecool
 * branch            main     -> FETCH_HEAD
   2ac4843..754da2b  main     -> origin/main
Updating 2ac4843..754da2b
Fast-forward
 testing.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 testing.txt
```
````


Now we can actually see `testing.txt` in our original repository.


## Conflict Resolution

Now we will make a few new edits to `testing.txt`:

Add a dummy header and footer for the `testing.txt`, so that it looks like this:

````{tab-set-code} 

```{code-block} testing.txt
***************************************
This is	the start of testing.txt
***************************************

I added this file from a new clone!

***************************************
This is	the end	of testing.txt
***************************************
```
````

Now commit and push this edit.

````{tab-set-code}

```{code-block}
git add testing.txt
git commit -m "Adds a new line to testing.txt"
git push
```
````


Now switch over to the `friend` clone.

````{tab-set-code} 

```{code-block} shell
cd ../molecool_friend
```
````


We are going to add another line to `testing.txt`, so that it looks like this:

````{tab-set-code} 

```{code-block} testing.txt
I added this file from a new clone!
Now I added a new line!
```
````

Now try committing and pushing the change:

````{tab-set-code} 

```{code-block} shell
git add testing.txt
git commit -m "Adds another line to testing.txt"
git push
```
````


````{tab-set-code} 

```{code-block} output
To github.com:YOUR_GITHUB_USERNAME/molecool.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'github.com:YOUR_GITHUB_USERNAME/molecool.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
````


The push failed because the `friend` clone is not up-to-date with the repository on GitHub.
We can fix this by doing a pull:

````{tab-set-code} 

```{code-block} shell
git pull
```
````


````{tab-set-code} 

```{code-block} output
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 6 (delta 3), reused 5 (delta 2), pack-reused 0
Unpacking objects: 100% (6/6), done.
From github.com:YOUR_GITHUB_USERNAME/molecool
   754da2b..de54818  main     -> origin/main
Auto-merging testing.txt
CONFLICT (content): Merge conflict in testing.txt
Automatic merge failed; fix conflicts and then commit the result.
```
````


Unfortunately, the `pull` also failed, due to a `conflict`.
To see which files have the conflict, we can do:

````{tab-set-code} 

```{code-block} shell
git status
```
````


````{tab-set-code} 

```{code-block} output
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

```
````


The conflict is in testing.txt, so let's open it up:

````{tab-set-code} 

```{code-block} testing.txt
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
```
````

The conflict is shown within the `<<<<<<<` and `>>>>>>>` bits.
The part before the `=======` is what we added in the commit in the `molecool_friend` clone,
while the part after it comes from the original local clone.
We need to decide what to do about the conflict, tidy it up, and then make a new commit.
Edit `testing.txt` so that it reads:

````{tab-set-code}
```{code-block} testing.txt
***************************************
This is the start of testing.txt
***************************************

I added this file from a new clone!
Now I added a new line!

***************************************
This is the end of testing.txt
***************************************

```
````

````{tab-set-code}

```{code-block} shell
git add .
git commit -m "Fixed merge conflicts in testing.txt"
git push
```
````


This time everything should work correctly.
Generally speaking, your procedure when ready to commit should be:

````{tab-set-code} 

```{code-block} shell
git commit -m "Commit message"
git pull
<fix any merge conflicts>
git push
```
````

## More GitHub Features

Navigate to the GitHub page for your project.
Click on `testing.txt`.
Here you can see the file and make changes to it.
Click the edit button, which looks like a small pencil near the upper right of the file text box.
Add a line that says "I added this line from the GitHub web interface!", so that the file looks like this:

````{tab-set-code}
```{code-block} testing.txt
***************************************
This is the start of testing.txt
***************************************

I added this file from a new clone!
Now I added a new line!
I added this line from the GitHub web interface!

***************************************
This is the end of testing.txt
***************************************

```
````

Scroll to the bottom of the page and write the message
"Added a line to testing.txt from the web interface." for this commit.
Then, click the green "Commit changes" button at the bottom left.
You should now see that your change appears in the text box.

Click the "Blame" button to find out who is responsible for each line of code.
Click the "History" button to see a list of all commits that affected this file.
You can click on a commit to see exactly what it did.

Go back to the main project page, and click the "commits" button.
Here you can see a list of all the commits for this project.
Clicking them reveals how they changed the code.

The "Issues" tab lets you create discussions about bugs, performance limitations,
feature requests, or ongoing work that are shared with everyone else who is working on the project.
Try filling out a quick issue now.
Then comment and close the issue.

:::{admonition} Final Repository State
:class: tip

You can see the final state of the repository after this section [here](https://github.com/MolSSI-Education/molecool/tree/efe8747f7253400d1a81354c62b4a1edc50e9ddd).

You can also download a zip of the repository [here](https://github.com/MolSSI-Education/molecool/archive/refs/tags/github-end.zip).

:::



## More Tutorials
If you want more `git`, see the following tutorials.

### Basic git
 - [Software Carpentry Version Control with Git](http://swcarpentry.github.io/git-novice/)
 - [GitHub 15 Minutes to Learn Git](https://try.github.io/)
 - [Git Commit Best Practices](https://github.com/trein/dev-best-practices/wiki/Git-Commit-Best-Practices)

## Key Points

```{admonition} Key Points
:class: key

- You can use GitHub to store your project online where you or others can access it from a central repository.
- You can use GitHub to store your projects so that you can work on them from multiple computers.

```
