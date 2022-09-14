---
title: "Documentation"
teaching: 40
exercises: 20
questions:
- "How can we document our module?"
objectives:
- "Run the lesson checking script and interpret its output correctly."
- "Explain in-code documentation"
- "Explain documentation tools like Read The Docs"
keypoints:
- "Some documentation is better than no documentation"
---

This episode discusses documentation strategies. 
In particular, we will focus on how to build documentation using Sphinx and host that documentation online using [Read The Docs].

Documentation must be provided to allow for use, development, and maintenance of software. 
Documentation is often overlooked by developers since it can be tedious and boring.
However, writing good documentation is an extremely good habit to develop.

The documentation typically involves several components:

 - What your project does and why it is useful
 - Build requirements and dependencies (if applicable)
 - How to compile/build/test/install
 - How to use the software (through the API or through inputs)
 - Some examples
 - Who maintains the project

So far in our project, we have added things like installation and use instructions to our `README.md`, which is displayed on our GitHub repository. 
We have also written in-code documentation in the form of comments and function doc strings. 
These strategies work well for small projects, and may be all the documentation you need for many of your projects. 
However, if you are preparing a software package to be widely used, you may want to make a website for people to find information about your package.

## Types of Documentation

There are many types of documentation which you might find associated with a software project.
A smaller project may be fully documented in the README.
However, larger libraries may have several documentation sets, each with a different audience.
One example of this is the [NumPy library](https://numpy.org/doc/stable/).
The NumPy documentation is divided by content intended for users, and documentation meant for contributors or developers.
The NumPy documentation also has a [reference section](https://numpy.org/doc/stable/reference/) which outlines all the functions and objects in the library (also called API documentation).

Not all libraries have documentation which is this extensive.
You will have to decide what is appropriate for your project.
However, it is good to be aware of the different types of documentation you might see associated with a project.

- **README documentation** - This is the documentation which is in the `README.md` file. 
It is displayed on the GitHub page for your project. For small projects, this documentation might be sufficient. 
The README documentation should contain a short summary of the project, information on installation and basic usage, and should link out to more complex documentation if you have it.  

- **End-user documentation** - The end user documentation should explain the goal of your project and explain how to use it.
You might choose to include tutorials or text explanations in this documentation.
This type of documentation could be present on your `README.md`, or on an external documentation site.

- **Developer documentation** - Developer documentation should explain how your project works and how others can contribute to the project.

- **API documentation** - API documentation is the documentation of the modules and functions in your library. 
This is the type of documentation which in-code docstrings are used to generate.

## Sphinx for complex modules

When you want to improve your documentation strategies for Python packages, use [Sphinx]. 
Sphinx is a tool for creating documentation and was originally created for documentation of the Python programming language.

With Sphinx and some extensions, you can write documentation giving instructions and examples of your software AND pull out the in-code documentation we have already written as docstrings to document your API.
**Note** that only using Sphinx to pull out API documentation is not a best-practice and should not be considered full and complete documentation.
When documenting your project, in general, it is ideal to have accompanying end-user documentation at least as well.

The ability to pull out in-code docstrings as documentation is an advantage - you won't have to maintain documentation in more than one place. 
Later, we will see how we can automatically generate our documentation every time we push to the repository.

[Many projects you are familiar with][sphinx example] use Sphinx for documentation - including NumPy, Matplotlib, and Pytest. 

To use Sphinx, you will need to have Sphinx installed and some configuration files.
CookieCutter has already set up files which we need to get started with Sphinx.

### Using Sphinx to build documentation

The command below installs the Sphinx software and a theme for your Sphinx Documentation. 
The cookiecutter comes preconfigured to use the [Sphinx ReadTheDocs theme] (or `sphinx_rtd_theme`), but there are many themes you can choose from if you wish.
There are many themes available for Sphinx, and if you view the Sphinx [examples][sphinx example] you will see several themes you could choose from.

~~~
$ pip install sphinx sphinx_rtd_theme
~~~
{: .language-bash}

While we work with documentation, we will finally be looking at the third directory which CookieCutter created.
(Remember that we've looked at the project directory, and the `devtools` directory.)
The files which CookieCutter has set up for Sphinx are in the `docs` folder. 
Navigate to that directory.

~~~
$ cd docs
~~~
{: .language-bash}

Next, look at the files in the directory

~~~
$ ls
~~~
{: .language-bash}

~~~
Makefile            _templates          getting_started.rst requirements.yaml
README.md           api.rst             index.rst
_static             conf.py             make.bat
~~~
{: .output}

These are the files we will use to build our documentation.

The important files for you to edit in this directory end with the extension `.rst`. 
These are `reStructuredText` files, and they are what Sphinx will use to build each page or section of your documentation. 
We have three restructured text files here to begin (`index.rst`, `getting_started.rst`, `api.rst`).
The included `rst` pages were generated by the CookieCutter as a starting point for you.

When you build your documentation, the `index.rst` will be the index, or main page of your documentation. 
The other `rst` files are examples of pages you might want to have (from CookieCutter). 
Any time you want to make a new page, you can create a file with an `.rst` extension.

To build your documentation as HTML, type

~~~
$ make html
~~~
{: .language-bash}

This command tells Sphinx to generate your documentation as html pages. 
With this command, we are building HTML files from the reStructuredText files.

Now notice when you type `ls` some new directories have appeared.

~~~
ls
~~~
{: .language-bash}

~~~
Makefile            _static             autosummary         index.rst
README.md           _templates          conf.py             make.bat
_build              api.rst             getting_started.rst requirements.yaml
~~~
{: .output}

In particular, notice the `_build` directory. 
Sphinx put the HTML files it generated here. 
There should now be files in your `_build/html` folder.
You can open these files in your browser to preview what your documentation will look like.

## Adding Information to our Documentation

Now, we will have the task of actually adding information about our project to our documentation. 
This part will require us to write! 

When writing Sphinx documentation, you use an extended `reStructuredText (RST)` [syntax][rst syntax]. 
This is similar to Markdown, but has notable differences.
See this [reStructured Text Cheat Sheet] for info on reStructuredText.

Let's start by adding a simple a description to your `index.rst` under the first heading.

~~~
Welcome to molecool's documentation!
=========================================================
molecool is a Python package designed to read in, perform analysis,
and visualize molecular coordinates. The file formats `xyz` and `pdb` are
currently supported.
~~~

Next, clean your previous build and rebuild your pages.

~~~
$ make clean
$ make html
~~~
{: .language-bash}

Refresh the page in your browser to see the page with the new description.

CookieCutter has already added some other pages to our documentation: `getting_started.rst`, and `api.rst`. 
Let's tell someone how to get started on the 'Getting Started' page. 
Click the link on your HTML documentation  to see what is there already.

Right now, it says

~~~
This page details how to get started with molecool.
~~~

To change this, we will edit the content of `getting_started.rst`

> ## Exercise - Getting Started
> Using the [reStructured Text Cheat Sheet], add some information to your Getting Started page. Use the following guidelines
> 
> 1. Add a text description under "Getting Started".
> 2. Create a subheading called "installation" which contains installation instructions.
> 3. The "Installation" section should use a list for dependencies and a code block with the installation command.
>
>> ## Solution
>> Following the guidelines and using the cheat sheet may lead you to a page which looks like this:
>> ~~~
>> Getting Started
>> ===============
>>
>> This page details how to get started with molecool. Molecool is a package which was developed for the MolSSI Best Practices workshop.
>>
>> Installation
>> ------------
>> To install molecool, you will need an environment with the following packages:
>>
>> * Python 3.7
>> * NumPy
>> * Matplotlib
>>
>> Once you have these packages installed, you can install molecool in the same environment using
>> ::
>>
>>     pip install -e .
>> ~~~
>> 
>> Here, we have used asterisks (`*`) to create a non-numbered list, and `::` followed by an indented block to indicate a code block.
> {: .solution}
{: .challenge}

We can also add a Python code block, for example. 
The Sphinx RTD Theme will use syntax highlighting for Python code.
~~~
Usage
-------
Once installed, you can use the package. This example draws a benzene molecule from an xyz file.
::

    import molecool

    benzene_symbols, benzene_coords = molecool.open_xyz('benzene.xyz')
    benzene_bonds = molecool.build_bond_list(benzene_coords)
    molecool.draw_molecule(benzene_coords, benzene_symbols, draw_bonds=benzene_bonds)
~~~

## Sphinx Directives

The thing that really gives Sphinx special abilities are **directives**. 
Directives are extensions which can be used with your restructured text to add special sections, images, warnings, etc to your documentation, and are part of a package called [docutils], which Sphinx is built on top of.
You can see a general list of directives [here][rst directives], and a list of special Sphinx Directives [here][sphinx directives].

In general, the syntax for a directive is (with appropriate options and syntax)

~~~
.. directive_name::
  :option:
  :option:

  parameter
  parameter
~~~

### Code Highlight Directive
One useful directive is code highlighting. 
Previously, we automatically highlighted our code using `::` at the end of a line followed by a blank line, then an indented line with code. 
We could have alternatively used a directive and specified the language.

~~~
.. code-block:: language

  *CODE GOES HERE*
~~~

For our Python example, 

~~~
.. code-block:: python

    import molecool

    benzene_symbols, benzene_coords = molecool.open_xyz('benzene.xyz')
    benzene_bonds = molecool.build_bond_list(benzene_coords)
    molecool.draw_molecule(benzene_coords, benzene_symbols, draw_bonds=benzene_bonds)
~~~

The line `.. code-block:: python` is the line which starts the directive. 
Directives always start with two periods (`..`), followed by a space, then the directive name (`code-block` in this case), then two colons (`::`). 
Next, you press enter and add any options for the directive. 
What we want highlighted as code is indented below this directive line.

Sphinx `code-block` directive supports many languages. 
For example, we could add a C++ code block.

~~~
.. code-block:: c++

    #include <iostream>

    int main(void)
    {
        std::cout << "Hello, world!";
        return 0;
    }
~~~

### The Table of Contents Directive
The next directive we will discuss is the Table of Contents directive. 
Look at the file `index.rst`. It contains the `toctree` directive, which generates a special section called a Table of Contents which links to other parts of your projects. 
The Table of Contents on your `index.rst` file is what shows up on your main menu on the left of the page. 
It is also on your main page.

~~~
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting_started
   api
~~~

This directive has an example of directive options, namely `maxdepth` and `caption`. 
You can think of these as arguments to a function. 
We then have options for depth of the Table of Contents (what level of headers to show), as well as the "caption". 
You can see other options for this directive under "Additional options" on the [documentation page][sphinx directives]. 

After the settings for the TOC tree, you list the name of the pages you want to be included in this Table of Contents. 
Right now, we are including the 'Getting Started' page and the API page.

Note that you add the __file name__ in the TOC Tree, but the title of the page is what shows up in the TOC.
For example, for the `Getting Started` page, the page heading is 'Getting Started', but you list the file name without the extension is the TOC tree as `getting_started`.

> ## Exercise
> Create a new page with the title "About" that gives a description of the project.
> Specify that this project is for a MolSSI Best Practices Workshop, and put a link to the MolSSI homepage (molssi.org). 
> Add your new page to the Table of Contents.
>
> What happens if you remove the page from the table of contents and rebuild the documentation?
>> ## Solution
>> First, create a new file called `about.rst`. Next, create a header and write a short desciption in `about.rst`.
>> ~~~
>> About this package
>> ------------------
>> This package and documentation are a sample created for the Best Practices Workshop held by `The Molecular Sciences Software Institute <https://molssi.org>`_.
>>
>> ~~~
>> Then, in `index.rst` add the name of the file at the top of your table of contents.
>> ~~~
>> .. toctree::
>>    :maxdepth: 2
>>    :caption: Contents:
>>
>>    getting_started
>>    api
>>    about
>> ~~~
>>
>> If you remove `about` from the TOC tree and rebuild, you will see the following error
>> ~~~
>>  ...PATH_TO_DIRECTORY/molecool/docs/about.rst: WARNING: document isn't included in any toctree
>> ~~~
>> {: .error}
>> Sphinx will warn you if you've created a page and not linked to it.
>>
>{: .solution}
{: .challenge}

> ## Building documentation as a PDF
> To build a pdf version of your documentation, you use the command. Note that you must have Latex installed for this to work.
> ~~~
> make latexpdf
> ~~~
> {: .language-bash}
> This will create a folder called `pdf` in the `build` directory, and you should have a file in this directory called `molecool.pdf` containing all of your documentation. Each `rst` file is a chapter of the documentation, instead of a different page.
{: .callout}

## API Documentation

To use Sphinx to generate API documentation, you can use either [Spinx-AutoAPI]
or [Sphinx-Autodoc]. 
The cookiecutter comes bundled with Sphinx-Autodoc, so we will focus on that tool for this tutorial. 
See the Note at the end of this section for instructions on building API documentation on using AutoAPI.

AutoDoc will pull out and render your documentation strings so that they are viewable to the user. 
This makes maintaining code documentation easier on you, as you will only need to maintain documentation for usage of functions in one place (the source code.)

CookieCutter has already added a page which uses these tools. 
On your index page, click `API Documentation`, then click on the `canvas` function. 
You will see the docstring written for the function. 
If you click the green 'source' button to the right, you will be taken to a page which shows the source code for the function.

Opening, the `api.rst` file, you should see the following.

~~~
API Documentation
=================

.. autosummary::
   :toctree: autosummary

   molecool.canvas
~~~

We are using a Sphinx extension called `autosummary` which is part of AutoDoc.
This tells Sphinx to insert a table that contains links to documented items.
Autosummary will put `docstrings` out of functions and a page for each docstring.
Under that, we are starting a Table of Contents for this page.
We will list any functions we would like to have documented here.
This is useful if we would like to separate our API documentation into several pages.

For example, we can add documentation for our `calculate_distance` function.

~~~
API Documentation
=================

.. autosummary::
   :toctree: autosummary

   molecool.canvas
   molecool.calculate_distance

~~~

> ## Exercise
> Add documentation for the `calculate_angle` function.
>
>> ## Answer
>> ~~~
>> .. autosummary::
>>     :toctree: autosummary
>>
>>     molecool.canvas
>>     molecool.calculate_distance
>>     molecool.calculate_angle
>> ~~~
> {: .solution}
{: .challenge}

## Adding Docstrings to other pages

Alternatively, you could choose to break your module documentation into different pages with additional text.
To do this, you would use different directives in AutoDoc.
You may want to write documentation in addition to your docstring. 
Add a page called `measure.rst` with the following contents:

~~~
Measure module
==============

.. automodule:: molecool.measure

    This is some additional information I want to say about the measure module.

.. autofunction:: calculate_distance

I can also put additional information about a function.

.. autofunction:: calculate_angle
~~~

Using this strategy, you can selectively add documentation for functions or classes and write additional information to go with the docstrings.

> ## Structuring your documentation
> Realistically, you probably don't want just a single page for API documentation.
> You could separate your documentation by purpose.
> For example, you could have separate pages explaining visualization, calculation, and/or measurement, with an autosummary table of contents for each page that has relevant functions.
>
> Many projects are structured this way.
> Now that you know how Python documentation is built, keep an eye out for documentation you like. 
> If you find documentation you like, take a look at their files to see how they structured their project!.
{: .callout}

> ## Sphinx AutoAPI
> Another strategy for generating API documentation is using [Spinx-AutoAPI].
> 
> AutoAPI will pull documentation for all of your functions at once, rather than you having to build them manually.
> 
> To install Sphinx-AutoAPI, use `pip`:
> 
> ~~~
> pip install sphinx-autoapi
> ~~~
> {: .language-bash}
> 
> Modify your `conf.py` file to look like the following:
> 
> ~~~
> ...
> 
> extensions = [
>     'autoapi.extension',
>     #'sphinx.ext.autosummary',
>     #'sphinx.ext.autodoc',
>     'sphinx.ext.mathjax',
>     'sphinx.ext.viewcode',
>     'sphinx.ext.napoleon',
>     'sphinx.ext.intersphinx',
>     'sphinx.ext.extlinks',
> ]
>
> autoapi_dirs = ['../molecool']
> autoapi_ignore = ["*/tests/*",
>                   "*_version.py"]
>                   
> autoapi_options = ['members', 
> 		'undoc-members', 
> 		#'private-members', 
> 		#'special-members', 
> 		'show-inheritance', 
> 		'show-module-summary', 
> 		'imported-members']
>	
> # autosummary_generate = True	# or delete this
> napoleon_google_docstring = False
> napoleon_use_param = False
> napoleon_use_ivar = True
>                   
> ...
> ~~~
> {: .language-python}
> 
> You can then build your documentation to have your docstrings pulled out automatically.
> While this strategy is convenient, we consider it to be only a good first pass at creating documentation.
> Your documentation should always contain additional information on goals and usage of the project, in addition to API documentation.
{: .callout}

## Equation Directives

Our docstring for `calculate_center_of_mass` has a section where we give the formula for the center of mass. 
If you re-examine that docstring, you will see that it is actually specified using a Sphinx Directive. 
Add `calculate_center_of_mass` to your API Documentation and view the page to see the rendered equation.

## The `conf.py` file

Now that we've worked with Sphinx, let's look a little closer at what's going on. 
The file `conf.py` in your `docs` folder gives all the configuration setting we are using for Sphinx to build our documentation. 
CookieCutter has added several extensions to Sphinx to make the documentation we've built.

Open your `conf.py` file and find the `extensions` section.

You should see the following:

~~~
...

extensions = [
    'autoapi.extension',
    # 'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
]

...

# autosummary_generate = True # or delete this
napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

...
~~~
{: .language-python}

CookieCutter has added a few extensions here which will allow us to pull docstrings from our Python modules (`sphinx.ext.autosummary`, `sphinx.ext.autodoc`), and another which we use because our docstrings are `NumPy` style (`sphinx.ext.napoleon`).
The `mathjax` extension allows us to render latex into equations, and the `viewcode` extensions will add links to highlighted source code.

Previously, we have used the line `autosummary_generate = True` to allow us to pull auto summaries from our modules and functions.

## Hosting your documentation

### Read The Docs
We recommend hosting your  documentation on [Read The Docs].
With this service, you can enable the building of your documentation every time you push to your repository.

Go to the [Read The Docs] website.
Log in with your GitHub username and hook the repository to ReadTheDocs.
This is done by clicking `Import a Project` button on your dashboard.
Then on `Import a Repository` page click the `Import Manually` button and fill the form as following:
1. Use `molecool-YOUR_GITHUB_USERNAME` in the `Name` field rather than just `molecool` to create unique URL for your Read The Docs documentation,
2. Fill the `Repository URL` with your molecool repository URL,
3. Choose Git as your `Repository type`, and
4. Type `main` as your `Default branch`.

Next, trigger build by clicking the `Build version` on your Read The Docs project page.

Unfortunately, your documentation build will fail.
This is because we need our dependencies installed on RTD.
There is another file the CookieCutter has added which we must now modify.
Add your dependencies (NumPy and Matplotlib) to `docs/requirements.yaml`.
You should also add `sphinx-autoapi` under `pip only installs`.
Your `requirements.yaml` will look like this:

~~~
name: docs
channels:
dependencies:
    # Base depends
  - python
  - pip

    # Package depends
  - numpy
  - matplotlib



    # Pip-only installs
  - pip:
    - sphinx-autoapi
~~~
{: .language-yaml}

Commit and push - your documentation should build successfully and you should be able to view it!


{% include links.md %}

[Sphinx]: https://www.sphinx-doc.org/en/master/
[sphinx example]: https://www.sphinx-doc.org/en/master/examples.html
[Sphinx ReadTheDocs theme]: https://sphinx-rtd-theme.readthedocs.io/en/stable/
[rst syntax]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html
[reStructured Text Cheat Sheet]: https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html
[rst directives]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-directives
[sphinx directives]: https://www.sphinx-doc.org/en/1.8/usage/restructuredtext/directives.html
[docutils]: https://docutils.sourceforge.io/
[Sphinx-Autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[Spinx-AutoAPI]: https://github.com/readthedocs/sphinx-autoapi
[Read The Docs]: https://readthedocs.org/
