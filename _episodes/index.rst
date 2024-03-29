Overview
--------

Best Practices in Python Package Development
============================================

This course by `The Molecular Sciences Software Institute <https://molssi.org/>`_ (MolSSI)
teaches users MolSSI's best practices
in Python package development.

MolSSI's best practices provide a starting point to learning software-development processes and protocols. 
Adhering to these protocols will ensure that your code is reliable and reproducible while decreasing long-term maintenance, 
increasing long-term viability, and allowing others to contribute to your code base. 
Before starting to learn the MolSSI's best practices, you should first consider your project's user and developer community. 
If your project is small with a limited number of potential contributors, 
certain topics from the best practices course may be more important to your work than others.  
However, for projects with a large user base, it is crucial to complete all components of the course.

This lesson is under continual development, please report issues to the 
`workshop repository <https://github.com/MolSSI-Education/python-package-best-practices>`_. 
If you see a subject you would like to contribute to, submit a pull request!

.. admonition:: Prerequisites
   :class: attention

   This material is best suited for people who have experience scripting in Python and are ready to learn about how to make their scripts into a software package.
   You should have experience programming Python and in using the terminal (or shell)

   You can see a tutorial on using the shell from `Software Carpentry <https://swcarpentry.github.io/shell-novice/>`_. or 
   use our :doc:`command line basics lesson<00-command-line-basics>`.

Workshop Lessons
================

The workshop lessons listed in this table below are designed to be completed sequentially. 
In this workshop sequence, we first run the CookieCutter, then use the produced repository for the lesson on version control.

If you need a refresher on the command line, see our :doc:`command line basics lesson<00-command-line-basics>`.
If you would like to do the `git` and GitHub lessons outside of the context of the CookieCutter, 
see our :doc:`standalone lesson on git<00-git-standalone>` and :doc:`standalone lesson on GitHub<00-github-standalone>`.


Set-Up
#######
.. csv-table:: 
  :file: csv_tables/setup.csv
  :header-rows: 1

git and GitHub
##############
.. csv-table:: 
  :file: csv_tables/git_and_github.csv
  :header-rows: 1

Code Style and documentation
############################
.. csv-table:: 
  :file: csv_tables/documentation.csv
  :header-rows: 1

Continuous Integration, Testing, Distribution
#############################################
.. csv-table:: 
  :file: csv_tables/ci_testing.csv
  :header-rows: 1

.. toctree::
   :maxdepth: 2
   :hidden:
   :titlesonly:

   self
   00-setup
   00-git-and-github
   00-code-organization-documentation
   00-testing-continuous-integration
   
