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

   You can see a tutorial on using the shell from `Software Carpentry <https://swcarpentry.github.io/shell-novice/>`_.

Workshop Lessons
================

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
   
