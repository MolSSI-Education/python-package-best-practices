Best Practices in Python Package Development
---------------------------------------------

This course by `The Molecular Sciences Software Institute <https://molssi.org/>`_ (MolSSI)
teaches users MolSSI's best practices
in Python package development.

MolSSI best practices provides a starting point to get into software
development operations to ensure that your code is reliable and reproducible
while decreasing long-term maintenance requirements, increasing long-term
viability, and allow others to work on your code base to assist your own
efforts. Before starting into MolSSI best practice one must first think about
the user base of a given project whether this is a project only used by
yourself, within a small group, or a large community project. If your project
is small and personal you may want to consider each topic in detail before
implementing while for large community projects each topic is quite crucial.

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

   setup
   01-package-setup
   00-git-and-github
   00-code-organization-documentation
   00-testing-continuous-integration
   
