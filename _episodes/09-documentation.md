---
title: "Documentation"
teaching: 40
exercises: 20
questions:
- "How can we document out module?"
objectives:
- "Run the lesson checking script and interpret its output correctly."
- "Explain in-code documentation"
- "Explain documentation tools like Read The Docs"
keypoints:
- "Some documentation is better than no documentation"
---

This episode discusses documentation strategies. In particular, we will focus on how to build documentation using Sphinx and host that documentation online using ReadTheDocs.

Documentation must be provided to allow for use, development, and maintenance
of software. Documentation is often overlooked by developers since it is
tedious and boring, however good documentation is an extremely good habit to
develop.

The documentation typically involves several components:

 - Build requirements and dependencies (if applicable)
 - How to compile/build/test/install
 - How to use the software (through the API or through inputs)
 - Some examples
 

## README documentation

So far in our project, we have added things like installation and use instructions to our `README.md` which is displayed on our GitHub repository. This works well for small projects, and may be all of the documentation you need for many of your projects. 

## Sphinx for complex modules

When you want to improve your documentation strategies for Python packages, use [Sphinx](https://www.sphinx-doc.org/en/master/). Sphinx is a tool for creating documentation, and was originally created for documentation of the Python programming language. 

With Sphinx and some extensions, you can write documentation giving instructions and examples of your software, AND pull out the in code documentation we have already written as docstrings. The ability to pull out in-code doc-strings as documentation is an advantage - you won't have to maintain documentation in two places. Later, we will see how we can automatically generate our documentation every time we push to the repository.

Many projects you are familiar with use Sphinx for documentation - including numpy, matplotlib, and pytest. To see a list of project that use Sphinx, click [here](https://www.sphinx-doc.org/en/master/examples.html).

CookieCutter has already set up files which we need to get started with Sphinx.

### Using Sphinx to build documentation

To build your Sphinx documentation locally, you will first need to install Sphinx. This command installs Sphinx, and the Sphinx Read The Docs theme (the theme you use defines the style of your pages). There are many themes available for Sphinx, and if you view the Sphinx [examples](https://www.sphinx-doc.org/en/master/examples.html) you will see several themes you could choose from.

~~~
$ conda install sphinx sphinx_rtd_theme 
~~~
{: .language-bash}

While we work with documentation, we will finally be looking at the third directory which CookieCutter created (remember that we've looked at the project directory, and the `devtools` directory). The files which CookieCutter has set up for Sphinx are in the `docs` folder. Navigate to that directory.

~~~
$ cd docs
~~~
{: .langauge-bash}

Next, look at the files in the directory

~~~
$ ls
~~~
{: .bash}

~~~
Makefile            _templates          getting_started.rst
README.md           api.rst             index.rst
_static             conf.py             make.bat
~~~
{: .output}

These are the files we will use to build our documentation.

The important files for you to edit in this directory end with the extension `.rst`. These are `reStructured text` files, and they are what Sphinx will use to build each page or section of your documentation. We have three restructured text files here to begin (`index.rst`, `getting_started.rst`, `api.rst`). 

When you build your documentation, the `index.rst` will be the index, or main page of your documentation. The other `rst` files are examples of pages you might want to have (from CookieCutter). Any time you want to make a new page, you can create a file with an `.rst` extension.

To build your documentation, type

~~~
$ make html
~~~
{: .language-bash}

This command tells Sphinx to generate your documentation as html pages. With this command, we are building HTML files from the reStructured text files. 

Now notice when you type `ls` a some new directories have appeared.

~~~
ls
~~~
{: .language-bash}

~~~
Makefile            _static             autosummary         index.rst
README.md           _templates          conf.py             make.bat
_build              api.rst             getting_started.rst
~~~
{: .output}

In particular, notice the `_build` directory. Sphinx put the HTML files it generated here. There should now be files in your `_build/html` folder. You can open these files in your browser to preview what your documentation will look like.

You can change the content of these files by editing the rst files and rebuilding your documentation. Add a description to your `index.rst` under the first heading.

~~~
Welcome to molecool's documentation!
=========================================================
molecool is a Python package designed to read in, perfom analysis,
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

CookieCutter has already added some other pages to our documentation, `getting_started.rst`, and `api.rst`. Let's tell someone how to get started on the 'Getting Started' page. Click the link on your HTML documentatio to see what is there already.

Right now, it says

~~~
This page details how to get started with molecool.
~~~

To changed this, we will edit the content of `getting_started.rst`

~~~
Getting Started
=============================

molecool is currently under development, and can not yet be installed from PyPI
or conda. 

Installation
------------
**These instructions assume you have the python package manager `conda` installed.**

To install molecool, navigate to the GitHub repository and clone it.

Naviate to the project directory. To do a developmental install, type

``pip install -e .``

Dependencies
^^^^^^^^^^^^^^^
You need to install `numpy` and `matplotlib`
~~~

We have subheaders indicated with `---` and `^^^`.  The sections surrounded by `` are in-line code blocks.

### Adding links

We could improve our documentation page by adding an external link to the repository. The syntax for adding a link in restructured text is

~~~
`Link Name <link location>`_.
~~~

Add a link to your GitHub repository

~~~
To install molecool, navigate to the `GitHub <https://www.github.com/YOUR_GITHUB_USERNAME/molecool>`_.
~~~

If you use Sphinx extensively, you will want to take some time to learn more about [restructured text](http://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html).


### Adding More Sections and Highlighting Code

Let's add a quick code example to our getting started page. First, we create a new subsection at the same level as "Installation". We know it is the same level because it has the same type of underline.

~~~
Usage
--------
~~~

To add a code block, you end your paragraph with `::`, then indent what you intend to be the code block.

~~~
Usage
-------
Once installed, you can use the package. This example draws a benzene molecule from an xyz file.::

    import molecool
    
    benzene_symbols, benzene_coords = molecool.open_xyz('benzene.xyz')
    benzene_bonds = molecool.build_bond_list(benzene_coords)
    molecool.draw_molecule(benzene_coords, benzene_symbols, draw_bonds=benzene_bonds)
~~~

### The Table of Contents
The `index.rst` file contains a special section called a Table of Contents which links to other parts of your projects. The Table of Contents on your `index.rst` file is what shows up on your main menu on the left of the page. It is also on your main page.

~~~
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting_started
   api
~~~

The first three lines in this highlighted section give the settings for the Table of Contents. The first line is how you start a Table of Contents section (`. toctree ::`). The `maxdepth` refers to the number of subheadings you will see in the menu on the page(if your page has subheadings).

After the settings for the TOC tree, you list the name of the pages you want to be included in this Table of Contents. Right now, we are including the 'Getting Started' page and the API page.

Note that you add the __file name__ in the TOC Tree, but the title of the page (For example, for the `Getting Started` page, the page heading ('Getting Started') is what shows up in the TOC, but you list the file name without the extension is the TOC tree `getting_started`.)

> ## Exercise
> Create a new page with the title "About" that gives a description of the project. Specify that this project is for a MolSSI Best Practices Workshop, and put a link to the molssi homepage (molssi.org). Add your new page to the Table of Contents.
>
> What happens if you remove the page from the table of contents and rebuild the documentation.
>> ## Solution
>> First, create a new file called `about.rst`. Next, create a header and write a short desciption in `about.rst`.
>> ~~~
>> About this package
>> ----------------
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
> To build a pdf version of your documentation, you use the command
> ~~~
> make latexpdf
> ~~~
> {: .language-bash}
> This will create a folder called `pdf` in the `build` directory, and you should have a file in this directory called `molecool.pdf` containing all of your documentation. Each `rst` file is a chapter of the documentation, instead of a different page.
{: .callout}

## Using AutoDoc

To generate your documentation with the modules documented from your docstrings, we will use Sphinx autodoc. AutoDoc will pull out and render your documentation strings so that they are viewable to the user. This makes maintaining code documentation easier on you, as you will only need to maintain documentation for usage of functions in one place (the source code.)

CookieCutter has already added a page which uses these tools. On your index page, click `API Documentation`, then click on the `canvas` function. You will see the docstring written for the function. If you click the green 'source' button to the right, you will be taken to a page which shows the source code for the function.


Opening, the `api.rst` file, you should see the following.

~~~
API Documentation
=================

.. autosummary::
   :toctree: autosummary

   molecool.canvas
~~~

We are using a Sphinx extension called autosummary.  This tells Sphinx to insert a table that contains links to documented items.  Autosummary will put `docstrings` out of functions and a page for each docstring. Under that, we are starting a Table of Contents for this page. We will list any functions we would like to have documented here.

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

### Rendering equations

Our docstring for `calculate_center_of_mass` has a section where we give the formula for the center of mass. Our Sphinx set-up allows us to render that equation. Add `calculate_center_of_mass` to your API Documentation and view the page to see the rendered equation.

> ## Structuring your documentation
> Realistically, you probably don't want just a single page for API documentation. You could separate your documentation by purpose. For example, you could have separate pages explaining visualization, calculation, and/or measurement, with an autosummary table of contents for each page that has relevant functions.
{: .callout}

## The `conf.py` file

Now that we've worked with Sphinx, let's look a little closer at what's going on. The file `conf.py` in your `docs` folder gives all of the configuration setting we are using for Sphinx to build our documentation. CookieCutter has added several extensions to Sphinx to make the documentation we've built.

Open your `conf.py` file and find the `extensions` section.

You should see the following:

~~~
extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
]

autosummary_generate = True
napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True
~~~
{: .language-python}

CookieCutter has added a few extensions here which will allow us to pull doc strings from our Python modules (`sphinx.ext.autosummary`, `sphinx.ext.autodoc`), and another which we use because our docstrings are `NumPy` style (`sphinx.ext.napoleon`).  The `mathjax` extension allows us to render latex into equations, and the `viewcode` extensions will add links to highlighted source code.

Next, we have added the line `autosummary_generate = True` to allow us to pull auto summaries from our modules and functions.

## Hosting your documentation

### Read The Docs
We recommend hosing your  documentation on [Read The Docs](https://readthedocs.org/). With this service, you can enable the building of your documentation every time you push to your repository.

Go to the [Read the Docs](https://readthedocs.org/) website. Log in with your GitHub username and hook the repository to read the docs. Push to the repository, or trigger a build on the site. You should see you documentation. However, you will not see your docstring information.

#### Using autodoc and autosummary on RTD
If you would like to use `autodoc` on Read the Docs, you will need a configuration file and an environment file specifically for documentation. In order for the RTD site to build your auto documentation, it has to build and import your module. Since we have dependencies, we will need provide an environment file and a configuration file.

Copy the environment file we use for testing. From your `docs` folder, type

~~~
$ cp ../devtools/conda-envs/test_env.yaml doc_env.yaml
~~~
{: .language-bash}

Edit the `doc_env.yaml` file to only have the packages we need for installing and using the package.

Contents of `doc_env.yaml`

~~~
name: documentation
channels:
dependencies:
    # Base depends
  - python
  - pip

  # Dependencies
  - numpy
  - matplotlib

    # Pip-only installs
  #- pip:
  #  - codecov
~~~

Next, we will create the configuration file for Read the Docs.

~~~
cd ../
touch .readthedocs.yml
~~~

Add to .readthedocs.yml

~~~
# .readthedocs.yml

version: 2

build:
  image: latest

python:
  version: 3.7
  install:
    - method: pip
      path: .

conda:
  environment: docs/doc_env.yaml
~~~

Commit to these changes and push to your repository. You should now see your documentation strings.


{% include links.md %}