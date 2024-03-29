# Introduction to the Command Line

````{admonition} Overview
:class: overview

Questions:
- What is the command line?
- How can I navigate files and directories on the command line?

Objectives:
- Learn basic shell commands for navigating and creating directories.
````

## Opening the Terminal

In this workshop, we will be navigating files and using git (a software for version control) using the command line. 
The Linux command line is a text interface to your computer. 
When you use the command line, you use something called a shell.
You can access the command line, or shell, using a *terminal*. 
If you are using WSL, the only type of interface you have to your Linux operating system is a command line, or terminal.

In scientific computing, you will need to use the Linux command line on high performance computing (HPC) servers.
Knowing the command line will also allow you to perform repetitive tasks quickly through shell scripting.
For this course, we will focus on basic navigation, file creation, and using git from the command line.

Most modern operating systems have graphical user interfaces, or GUIs (often pronounced "gooey"), that are used to interact with the computer.
However, you can also interact with the computer using text only.

[Open your terminal](https://towardsdatascience.com/a-quick-guide-to-using-command-line-terminal-96815b97b955). 
On Mac, you should be able to find a terminal application.
If you are using WSL, open your Linux distribution.
You can use this interface to issue commands to your computer using text.

## Viewing Directory Contents

The first command we will discuss is the command `pwd`. 
`pwd` stands for "**p**rint **w**orking **d**irectory." 
This command gives the name of the folder you are currently in.
In Linux, "directory" means the same thing as "folder".

````{tab-set-code} 

```{code-block} shell
pwd
```
````


````{tab-set-code} 

```{code-block} output
/YOUR/PATH
```
````


When you open a terminal initially, you will be in your home directory. 
The path displayed as your output will be whatever your home directory is if you type `pwd` immediately after opening your terrminal.

The `ls` command shows you the contents of the directory you are in. 
`ls` stands for "list", and the command shows you the contents of the directory you are in.

````{tab-set-code} 

```{code-block} shell
ls
```
````


If you want to see contents of another directory, you can follow `ls` with the path to that directory. 
In the command below, you should substitute a directory you can see from the previous `ls` command.

````{tab-set-code} 

```{code-block} shell
ls DIRECTORY_NAME
```
````

```{admonition} Clearing the screen
:class: note

If you'd like to make room on your screen, you can use the `clear` command too get a fresh terminal.
Pressing `ctrl+L` on your keyboard will also clear the screen.
```

## Creating and navigating directories
We will make a directory to keep our work in for the course.
For the sake of uniformity, these directions will tell you how to create a folder in your home directory.
If you have another preference for where you would like to store your files and you are able to navigate files, you can use that location.

The command to **m**a**k**e a **dir**ectory is `mkdir`.

````{tab-set-code} 

```{code-block} shell
mkdir command_line_lesson
```
````

``````{admonition} Check Your Understanding
:class: exercise

What command that you have learned so far could you use to see that your newly created folder is in your current location?

````{admonition} Solution
:class: solution dropdown

You could use the `ls` command to confirm that there is now a folder called `command_line_lesson` in your home directory.

``````


This has created an empty folder, or directory, named `command_line_lesson` in your home directory.
To navigate to be inside of that directory, we need to **c**hange the **d**irectory we are in using the `cd` command.

```{admonition} Spaces in file and directory names
:class: note

In general, you will notice that most file and directory names created on systems where the command line is used do not contain spaces.

On the command line, many applications and scripts may not work with file names or directories containing spaces. 
It is best to use underscores `_` or dashes `-` to separate words in file names.

```


````{tab-set-code} 

```{code-block} shell
cd command_line_lesson
```
````


We will create a file that has a description of what is in this folder. 

You can verify what folder you are in using the `pwd` command.

````{tab-set-code} 

```{code-block} shell
pwd
```
````


Open a text file in your text editor of choice. 
If you installed [VSCode](https://code.visualstudio.com/download)  you will be able to open a file called `README.md` using VSCode with the following command. **Note** If you are on MacOS it will be necessary to [add VSCode to your path manually](https://code.visualstudio.com/docs/setup/mac).

````{tab-set-code} 

```{code-block} shell
code README.md
```
````


The Visual Studio Code text editor will open with a file called `README.md`. 
Type some information in the file and save it.

````{tab-set-code} 

```{code-block} README.md
# MolSSI Best Practices - Command Line
This folder contains files and directories associated with the MolSSI Best Practices Workshop.
```
````


This file uses something called [Markdown](https://www.markdownguide.org/), which a mark-up, or text formatting language.
This is often used for README files, and we will use `Markdown` throughout the bootcamp. 
The hashtag (`#`) followed by the space results indicates a title.
Save this file and exit.

Now, when you type `ls`, you will see that you have a file called `README.md` in your directory.

To navigate out of this folder, you can use `..` as the file location. 

````{tab-set-code} 

```{code-block} shell
cd ..
```
````


This will move you back to your home directory. 

```{admonition} Changing to the home directory from anywhere
:class: note

If you use the `cd` command followed by no path, you will always be returned to your home directory.
```

Other commands which will be useful to you are `mv` which is used for moving files from one place to another, and `cp` for copying files from one place to another. For example, you can create a copy of your README.md file:

````{tab-set-code} 

```{code-block} shell
cp command_line_lesson/README.md .
```
````


This command will create a copy of the README.md file in your current directory. 
The dot (`.`) is a short-cut for your current directory. 
In this case, the created file will have the same name as the one you copied it from.
You could also give the file another name:

````{tab-set-code} 

```{code-block} shell
cp command_line_lesson/README.md README_copy.md
```
````


The `mv` command behaves the same way except that the original file is removed.

You can remove a file using the `rm` command.
Let's get rid of those copies we just made:

````{tab-set-code} 

```{code-block} shell
rm README.md
rm README_copy.md
```
````

``````{admonition} Challenge
:class: exercise

Navigate to your `command_line_lesson` directory and list the directory contents.

`````{admonition} Solution
:class: dropdown solution

The commands you should execute are

````{tab-set-code} 
```{code-block} shell
cd command_line_lesson
ls
```
````
`````
``````


````{admonition} Key Points
:class: key

- The terminal or "command line" is a text interface to your computer.
- You can use text commands in the command line to navigate directories and change files.
- We will use a text mark-up notation called "markdown". This will be in text files and doesn't directly have to do with the terminal.
````
