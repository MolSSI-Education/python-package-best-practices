Python Package Best Practices
=============================

This repository contains lessons for the MolSSI Workshop "Best Practices in Python Package Development". To complete the lessons, navigate to the [website](http://education.molssi.org/python-package-best-practices/). Make sure to visit [setup] first to obtain lesson materials and install required software. 

This workshop is designed to take place in one and a half to two days. Students begin the workshop with python code stored in a Jupyter notebook. During the workshop, we refactor and format the code into a Python package. At the end, all participants should have a repository on GitHub which implements [MolSSI's Best Practices] for a Python package. Depending on the level of students taking this course, all lessons may not be accomplished in two days. Workshops should cover at least lessons 1-6 (outlined below), with more potentially being added for more advanced groups.

## Workshop Topics
This workshop walks students through setting up, writing code, and setting up multiple services (continuous integration, codecov, etc) for a Python package. When finished, this repo will include the following topics. Items which have a checkbox are (mostly) finished, and can be followed online.

- [x] Setting up a python package using the MolSSI Computational Molecular Sciences [(CMS) CookieCutter][cookiecutter]
- [x] Basic use of `git` and [GitHub].
- [x] Python coding style, docstrings.
- [x] Code collaboration on [GitHub] (Fork-PR workflow)
- [x] Unit testing using [pytest].
- [x] Continuous integration using [GitHub Actions].
- [x] Documentation using [sphinx] and [readthedocs]
- [x] Distributing packages on [PyPI] and [conda-forge]

## Contributing to these lessons
To contribute to this lesson, fork this repository and make changes on your local clone. Once you have changes you would like incorporated, create a pull request, and we will review your contributions.

All edits to lessons should be done under `_episodes` in the appropriate markdown file. We use [Sphinx] with a variation of the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) and [MyST parser](https://myst-parser.readthedocs.io/en/latest/) for lessons. 
There are custom admonitions for overviews, key points, and exercises. You can see examples of custom admonitions in the lesson files.  


[cookiecutter]: https://github.com/MolSSI/cookiecutter-cms
[setup]: https://molssi-education.github.io/python-package-best-practices/setup.html
[collections]: https://jekyllrb.com/docs/collections/
[conda-forge]: https://conda-forge.org/
[editing-config]: https://carpentries.github.io/lesson-example/03-organization/
[example-issues]: https://github.com/carpentries/lesson-example/issues/
[github-pages]: https://help.github.com/articles/creating-project-pages-manually/
[GitHub]: https://github.com
[GitHub Actions]: https://github.com/features/actions
[lesson pages]: https://molssi-education.github.io/python-package-best-practices/
[MolSSI's Best Practices]: https://molssi.org/molssis-best-practices/
[pytest]: https://pytest.org
[readthedocs]: https://readthedocs.org
[rendered]: https://carpentries.github.io/lesson-example/
[sphinx]: http://www.sphinx-doc.org/en/master/
[PyPI]: https://pypi.org/
