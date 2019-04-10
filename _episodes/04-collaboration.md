---
title: "Code Collaboration using GitHub"
teaching: 30
exercises: 5
questions:
- "How can others contribute to my project on GitHub?"
- "How can I contribute to the projects of others?"
objectives:
- "Learn what a fork is on GitHub"
- "Understand how to open a pull request."
keypoints:
- "To contribute to someone else's project, you should fork their repository."
- "All development work should be done on a new branch. Each branch should implement one feature."
- "Once you've implemented a new feature, push to your repository and create a pull request on the original repo."
---

## Repository collaborators

Now that we have a Python package with a function, we may want others to be able to contribute to our project. There are several ways for people to contribute to your project. If you are working with a small number of people who you know well, you may simply choose to add them as collaborators to your repo. This will give them the ability to push to your repository.

To add collaborators to your project, navigate to your repository on GitHub
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

Create a personal fork of the repository by pressing the “Fork” button near the top right of the web interface.

Then, make a clone of the fork on your personal computer.

~~~
$ cd ../
$ git clone <fork URL> fork_clone
$ cd fork_clone
~~~
{: .bash}

In a real development situation, we would also create a new `conda` environment for developing in this repository. For this workshop, we will use the same development environment. However, if we wish to test functions we are developing, we will have to do a developmental install of this package (`pip install -e .`).

## Adding an upstream to our forks
In your terminal window, type
~~~
$ git remote -v
~~~
{: .language-bash}

You should see output similar to the following

~~~
origin https://github.com/YOUR_GITHUB_USERNAME/FORKED_REPO_NAME.git (fetch)
origin https://github.com/YOUR_GITHUB_USERNAME/FORKED_REPO_NAME.git (push)
~~~
{: .language-bash}

This is similar to our own repository. However, since this is fork, we will want to add another remote to track the original repository. The standard names for remotes are `origin` for the repository we have cloned from, and `upstream` for the repository we forked from. Add an upstream using the following command

~~~
$ git remote add upstream https://github.com/YOUR_PARTNERS_GITHUB_USERNAME/ORIGINAL_REPO_NAME.git
~~~

Now, when you check the remotes (`git remote -v`), it should list both the `origin`, and `upstream` repositories. If we wanted to pull changes from the original repo, we could do `git pull upstream branch_name`

# Developing a new feature
We will implement a new module and function in our partner's package. We will be writing a function to convert a string to title case (explained below).

When creating a new feature, it is a good practice to develop each feature on a new branch in the new repository. Create a new branch in your repo called `title_case`.

~~~
$ git checkout -b title_case
~~~
{: .language-bash}

This command creates the branch and checks it out (the `-b` stands for `branch`). Alternatively, we could have used the commands `git branch title_case` and `git checkout title_case`.

You will see the output

~~~
Switched to a new branch 'title_case'
~~~
{: .language-output}

Now, create a new file called "util.py" in the same folder as our first module (molssi_math). If you are in the top level of our repository, you can do

~~~
$ touch molssi_devops/util.py
~~~
{: .language-bash}

Open this file in your text editor of choice. As discussed in the previous episode, the first thing we should do in this file is...write a docstring for the top of the file!

~~~
"""
util.py
A sample repository for the MolSSI Python package development workshop

Misc. utility functions
"""
~~~
{: .language-python}

Now, we are ready to add our title case function.

> ## Exercise
> Using the given docstring, implement a title case function. You can *not* use the .title() function.
> ~~~
> def title_case(sentence):
>   """
>   Convert a string to title case.
>
>   Title case means that the first letter of each word is capitalized, and all other letters in the word are lowercase.
>   
>   Parameters
>   ----------
>   sentence: str
>     String to be converted to title case
>   
>   Returns
>   -------
>   ret: str
>     String converted to title case.
>
>   Example
>   -------
>   >>> title_case('ThIS is a STRinG to BE ConVerTeD.')
>   'This Is A String To Be Converted.'
>   """
> ~~~
> {: .language-python}
> > ## Solution
>> This is a solution - note that there are many. This can be one you use if you don't feel like writing one.
>> ~~~
>> # Capitalize first letter
>> ret = sentence[0].upper()
>>
>> # Loop through the rest of the characters
>> for i in range(1, len(sentence)):
>>     if sentence[i - 1] == ' ':
>>         ret = ret + sentence[i].upper()
>>     else:
>>         ret = ret + sentence[i].lower()
>>
>>  return ret
>> ~~~
>> {: .language-python}
> {: .solution}
{: .challenge}

## Trying out our function

Let's test this in the command line. Open a python interpreter

~~~
$ python
~~~
{: .language-bash}

~~~
>>> import molssi_devops as md
>>> test_string = 'ThIS iS a TeSt STrinG.'
>>> md.util.title_case(test_string)
~~~
{: .language-python}

When you execute the previous code, you should get the following

~~~
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'molssi_devops_2019' has no attribute 'util'
~~~
{: .output}

This happened because we forgot to import the module in our `__init__.py` file. `__init__.py` files are required for Python packages, and tell Python to treat directories as packages. We need to import functions from our new module. Open your `__init__.py` file in a text editor. You should see the following:

~~~
"""
molssi_devops_2019
A sample repo for the 2019 MolSSI Software Fellow Bootcamp
"""

# Make Python 2 and 3 imports work the same
# Safe to remove with Python 3-only code
from __future__ import absolute_import

# Add imports here
from .molssi_math import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
~~~
{: .language-python}

> ## Lots of ways to do imports
>
> In Python, there are several ways you might choose to import packages or modules. Here are some different variations you might see.
> 1. `from module import *`
> 2. `from module import function1, function2`
> 3. `import module`  
> All of these will import functions from `module` so they can be used by the Python interpreter. Options 1 and 2 behave in similar ways, except that 1 will import everything in the module, while option 2 will only import the specified functions (`function1` and `function2`). Sometimes using option 1 is considered a bad practice, as it will import all names in a module (except those beginning with an underscore), and can introduce an unknown set of names into the interpreter, possibly hiding some of the things you have already defined. Instead, it is recommended to specify functions which should be importe (ie - option 2).
>
> If we imagine a function (`function1`) in our module (`module`), the imports above would result in the following usage of the function:
> 1. `>>> function1()`
> 2. `>>> function1()`
> 3. `>>> module.function1()`
>
{: .callout}

We are concerned with the part under `# Add imports here`. Change your section so that it looks like the following:
~~~
from .molssi_math import canvas, mean
from .util import title_case
~~~
{: .language-python}

Save your changed `__init__.py` file. If you haven't already, **close your previous Python interpreter and open a new one.** Try the above code again.

~~~
>>> import molssi_devops as md
>>> test_string = 'ThIS iS a TeSt STrinG.'
>>> md.util.title_case(test_string)
~~~
{: .language-python}

This time, you should see the following output

~~~
'This Is A Test String.'
~~~
{: .language-output}

Let's add and commit these changes (in two different commits)

~~~
$ git add molssi_devops/util.py
$ git commit -m "Add util module and title_case function"
$ git add molssi_devops/__init__.py
$ git commit -m "Add util import to __init__"
$ git push origin title_case
~~~
{: .bash}

Here, the last line indicates that we are pushing to `origin` (our fork) to the `title_case` branch.

As part of the output from this command, you should see the following:

~~~
remote:
remote: Create a pull request for 'title_case' on GitHub by visiting:
remote:      https://github.com/YOUR_GITHUB_USERNAME/FORKED_REPO_NAME/pull/new/title_case
remote:
~~~
{: .language-output}

`git` is correct. What we will want to do next is create a pull request on the original repository to get our changes incorporated.

Use your browser to confirm that this change shows up in the fork.
Have your partner check their repository - does the change appear for them?

## Pull requests

It is now time to incorporate the edits you have made in you fork into the original repository.
To do this, we must create a `Pull Request`.

Navigate to the URL of your fork. You should see a highlighted area and green button which says "Compare and Pull Request". Alternatively, you can navigate to the URL given in the message where you did a push.

Once you are on the page that says "Open a pull request", you should see fields which ask for the name of the pull request, as well as a larger text box which has space for a description. Make the title of this pull request "add util module and title_case function". Edit the description to describe what you have done in your pull request.

Submit the pull request.

Ask your partner to review the pull request. You should also have a pull request to review from your partner.
They can do this by going to the URL of their personal repository and then clicking the "Pull Requests" tab.
They should see a single pull request listed.
If they click it, they will see everything that you wrote. If you would like to pull their changes to your repo before accepting the pull request click "view command line instructions" next to the green "Merge pull request" button and follow the instructions.

They should now click the "Merge Pull Request" button, followed by "Confirm merge".

Your changes should now appear in your partner's repository.
Congratulations on your first successful pull request!

## More Tutorials
If you want more `git`, see the following tutorials.

### Branching

[Git Branching Tutorial](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

### Rebasing

[Git Rebasing Tutorial](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)
