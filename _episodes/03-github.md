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
Our goal in this section is to upload MODULE.py to the repository on GitHub.

First, use a terminal to cd into the top directory of the local repository.
Then, check the status of the project:

~~~
$ git status
~~~
{: .bash}


~~~
On branch master

Initial commit

Untracked files:
   (use "git add <file>..." to include in what will be committed)

	MODULE.py
nothing added to commit but untracked files present (use "git add" to track)
~~~
{: .output}

The part about "untracked files" tells you that there are certain files located within your local repository that Git is not tracking (i.e., not doing version control on).
At a minimum, you should see 'MODULE.py' listed as an untracked file.
Depending on which text editor you are using, you might also see some backup files, like 'MODULE.py~', listed here.

To tell Git to start tracking 'MODULE.py', do:

~~~
$ git add MODULE.py
~~~
{: .bash}

Then check the status again:

~~~
$ git status
~~~
{: .bash}

~~~
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   MODULE.py

~~~
{: .output}

Git now knows that it's supposed to keep track of `MODULE.py`,
but it hasn't recorded these changes as a commit yet.
To get it to do that,
we need to run one more command:

~~~
$ git commit -m "Adds MODULE.py"
~~~
{: .bash}

~~~
[master (root-commit) f22b25e] Adds MODULE.py
 1 file changed, 1 insertion(+)
 create mode 100644 MODULE.py
~~~
{: .output}

When we run `git commit`,
Git takes everything we have told it to save by using `git add`
and stores a copy permanently inside the special `.git` directory.
This permanent copy is called a [commit]({{ page.root }}/reference/#commit)
(or [revision]({{ page.root }}/reference/#revision)) and its short identifier is `f22b25e`.
Your commit may have another identifier.

We use the `-m` flag (for "message")
to record a short, descriptive, and specific comment that will help us remember later on what we did and why.
If we just run `git commit` without the `-m` option,
Git will launch `nano` (or whatever other editor we configured as `core.editor`)
so that we can write a longer message.

[Good commit messages][commit-messages] start with a brief (<50 characters) statement about the
changes made in the commit. Generally, the message should complete the sentence "If applied, this commit will" <commit message here>.
If you want to go into more detail, add a blank line between the summary line and your additional notes. Use this additional space to explain why you made changes and/or what their impact will be.

If we run `git status` now:

~~~
$ git status
~~~
{: .bash}

~~~
On branch master
nothing to commit, working directory clean
~~~
{: .output}

it tells us everything is up to date.
If we want to know what we've done recently,
we can ask Git to show us the project's history using `git log`:

~~~
$ git log
~~~
{: .bash}

~~~
commit f22b25e3233b4645dabd0d81e651fe074bd8e73b
Author: <Firstname> <Lastname> <<email address>>
Date:   Thu Aug 22 09:51:46 2013 -0400

    Adds MODULE.py
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
It should still only have the '.gitignore' and 'LICENSE' files.
This is because your local Git repository is separate from the remote GitHub repository.
To make your changes show up on GitHub, you will need to run:

~~~
$ git push
~~~
{: .bash}

This command sends all of the new commits in your local repository to the GitHub repository.
Now if you refresh the GitHub webpage you should be able to see that 'MODULE.py' has been added to the repository.

## Working With Multiple Repositories

Make another clone of the remote.

Make a change to the new clone.

Push the change, then Pull it to the first clone.

## Ignoring Files

## Conflict Resolution

Make conflicting commits in the two different repositories.

Push one, then try to push the other.

Illustrate what kinds of commits conflict and what types don't.

## Pull requests

## Branching and Forking

## Managing a Repository

Giving access to collaborators.

Evaluating pull requests.

Keeping branches under control.

## Best practices

{% include links.md %}
