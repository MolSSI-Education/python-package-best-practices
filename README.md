Python Package Development
==============

This repository contains lessons for the MolSSI Workshop "Best Practices in Python Package Development". To complete the lessons, navigate to the [lesson pages].

This workshop is designed to take place in two days. At the end, all participants should have a repository on GitHub which implements [MolSSI's Best Practices] for a Python package. Depending on the level of students taking this course, all lessons may not be accomplished in two days. Workshops should cover at least lessons 1-6 (outlined below), with more potentially being added for more advanced groups.

Lessons for this module were developed using the [Software Carpentry lesson template][styles],
and is itself an example of the use of that template.
Please see <https://carpentries.github.io/lesson-example/>
for a rendered version of this material,
including detailed instructions on design, setup, and formatting.

## Workshop Topics
This workshop walks students through setting up, writing code, and setting up multiple services (continuous integration, codecov, etc) for a Python package. When finished, this repo will include the following topics. Items which have a checkbox are (mostly) finished, and can be followed online.

- [x] Setting up a python package using the MolSSI Computational Molecular Sciences [(CMS) CookieCutter][cookiecutter]
- [x] Basic use of `git` and [GitHub].
- [x] Python coding style, docstrings.
- [x] Code collaboration on [GitHub] (Fork-PR workflow)
- [x] Unit testing using [pytest].
- [x] Continuous integration using [travis-ci].
- [x] Documentation using [sphinx] and [readthedocs]
- [ ] Deploying packages on [conda-forge]

## Contributing to these lessons
To contribute to this lesson, fork this repository and make changes on your local clone. Once you have changes you would like incorporated, create a pull request, and we will review your contributions.

All edits to lessons should be done under `_episodes` in the appropriate markdown file.

General instructions from software carpentry for working with this template are given below.

### Quick Instructions

1.  Please read [the episodes of this lesson][rendered] to format your material.

2.  Please keep the master copy of your lesson in your repository's `gh-pages` branch,
    since that is what is
    [automatically published as a website by GitHub][github-pages].

3.  To preview material,
    please run `make serve` from the command line
    to launch Jekyll with the correct parameters,
    or push to your repository's `gh-pages` branch
    and let GitHub take care of the rendering.

4.  Run `make lesson-check` to check that your files follow our formatting rules.

5.  If you find an error or omission in this documentation,
    please [file an issue in this repository][example-issues].
    If you find an error or omission in the lesson template,
    please [file an issue in the styles repository][styles-issues] instead.

### Layout

The layout of this repository is explained in [this site's episodes][rendered].
In brief:

1.  The source for pages that appear as top-level items in the navigation bar
    are stored in the root directory,
    including the home page (`index.md`),
    the reference page (`reference.md`),
    and the setup instructions (`setup.md`).

2.  Source files for lesson episodes are stored in `_episodes`;
    `_episodes/01-xyz.md` generates `/01-xyz/index.html`,
    which can be linked to using `/01-xyz/`.

3.  Files that appear under the "extras" menu are stored in `_extras`.

4.  Figures are stored in the `fig` directory,
    data sets in `data`,
    source code in `code`,
    and miscellaneous files in `files`.


[cookiecutter]: https://github.com/MolSSI/cookiecutter-cms
[collections]: https://jekyllrb.com/docs/collections/
[conda-forge]: https://conda-forge.org/
[editing-config]: https://carpentries.github.io/lesson-example/03-organization/
[example-issues]: https://github.com/carpentries/lesson-example/issues/
[github-pages]: https://help.github.com/articles/creating-project-pages-manually/
[GitHub]: https://github.com
[lesson pages]: https://molssi-education.github.io/python-package-best-practices/
[issues]: https://github.com/carpentries/lesson-example/issues
[MolSSI's Best Practices]: https://molssi.org/education/best-practices/
[pytest]: https://pytest.org
[readthedocs]: https://readthedocs.org
[rendered]: https://carpentries.github.io/lesson-example/
[setup]: https://carpentries.github.io/lesson-example/setup.html
[sphinx]: http://www.sphinx-doc.org/en/master/
[styles-issues]: https://github.com/carpentries/styles/issues/
[styles]: https://github.com/carpentries/styles/
[travis-ci]: https://travis-ci.org/
