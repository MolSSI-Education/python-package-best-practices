---
title: "Git and GitHub"
teaching: 30
exercises: 5
questions:
- "How do I use git and GitHub?"
objectives:
- "Explain the purpose of version control."
- "Introduce common git commands."
- "Resolve a merge conflict"
keypoints:
- "Git provides a way to track changes and differences between versions."
- "Branches allow you to make changes without affecting the code on the master branch."
---

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

Unfortunately, the word “fork” has multiple possible meanings in the context of open-source software development.
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

## More Tutorials
If you want more `git`, see the following tutorials.

### Branching

[Git Branching Tutorial](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)


### Rebasing

[Git Rebasing Tutorial](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)
