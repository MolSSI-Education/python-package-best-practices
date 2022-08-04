---
title: "Distributing Packages"
teaching: 30
exercises: 60
questions:
- "How can you get your project out there?"
objectives:
- "Discuss community strategies"
keypoints:
- ""
---

# Preliminary

Register a test account on test.pypi.org.

Create an access token, and *don't lose it!*
(I keep a copy of the text for my token in my password manager.)

Create `$HOME/.pypirc`. It should look something like the following.

~~~
[testpypi]
  username = __token__
  password = pypi-Abunchofbase64encodedbinarydataAbunchofbase64encodedbinarydataAbunchofbase64encodedbinarydataAbunchofbase64encodedbinarydata
~~~
{: .output}

# Distributing packages for `pip install`

## Building the distribution

We previously mentioned that `pip install .` invokes `setuptools` to build the
distribution archive for our package before installing the package in our
environment.
What does this mean?
More importantly, what does it have to do with letting other people do
`pip install molecool` and get my package automatically downloaded from
"the cloud"?

Setuptools is not the only package for configuring and building Python
distribution archives,
and `pip` does not actually look at `setup.cfg` directly.
`pip` notices the `pyproject.toml` file (which marks a folder as containing
buildable packages).
Note that, if we _only_ want to prepare a distribution for sharing,
we can just use the `build` module.

~~~
pip install build
python -m build .
~~~
{: .language-bash}

Note that `versioningit` also participated in the build process.
`versioningit` generated a `_version.py` file with a version string derived
from your most recent `git` tag. We will not add this file to our `git`
revision control, but it will be packaged in our distribution.
`versioningit` will regenerate this file as necessary and appropriate.

The build system is responsible for assembling your files into a distribution
archive that can be easily placed into anyone's `site-packages` directory.
It also makes sure that various package metadata is assembled so that a
package installer like `pip` can evaluate software dependencies, and so that
your package looks good when it is shared on pypi.org.

> ## Goodbye to setup.py?
>
> Historically packages built with `setuptools` used a `setup.py` script
as the entry point to the `setuptools` build system. `setup.py` is specific
to `setuptools` and the `distutils` package it is built on.
Many tools for helping to build and test packages came to
rely on `setup.py`, which made them incompatible with non-setuptools build
systems.
> 
> In an ongoing effort at generalization, the Python community is now
encouraging package authors to use a `pyproject.toml` file to direct the build
system. `distutils` is scheduled for retirement with Python 3.12.
In preparation, `setuptools` no long requires `distutils` or `setup.py`,
and can be configured entirely with `setup.cfg` and `pyproject.toml`.
{: .callout}

## Building and uploading to PyPI

Refer to https://packaging.python.org/en/latest/tutorials/packaging-projects/
for build-system-agnostic tutorial on
* packaging Python projects for distribution
* publishing packages to pypi.org for automatic download with `pip install`

For more in depth documentation on packaging for PyPI specifically with setuptools,
see https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

Essentially, though, once you have an account on `pypi.org` and you have built
a distribution archive with `python -m build`, you can `pip install twine` and
use twine to upload your package, per the above linked tutorial.
Caution: *strongly* consider creating an account on `test.pypi.org` and uploading
an initial "alpha" or "beta" release of your package to see how it looks and to
do test installations.

Note that pypi.org enforces universal uniqueness of packages and versions.
Once you have uploaded `molecool` version `1.0.0`, you cannot replace it;
you can only upload additional versions. (You can "yank" a release, but this
only marks the package as "yanked", indicating it should not be used.
It is still out there.)
* Be tidy with your official releases.
* Be conservative with alpha and beta pre-releases.
* Test the publication of new releases on test.pypi.org before pypi.org to avoid
  cluttering your versioning scheme and your release history on pypi.

# Distributing packages for `conda install`

*beyond the scope of the present material?*

`conda` has a completely different approach to building and distributing
packages, and is not yet PEP-517 compliant.
(It does not use `pyproject.toml`.)
For information about using `conda build`,
preparing your build details and metadata with `meta.yml`,
and publishing packages through a conda channel like `conda-forge`,
see ...

# Tagging releases

Python has a strict syntax for version strings.

* Know how to mark versions for pre-release (or post-release) and consider
  tagging "alpha" and "beta" releases.
* Refer to https://semver.org for guidelines on how to use versions meaningfully.
* Refer to https://peps.python.org/pep-0440/ for constraints on Python version specifiers.

*TODO: Do we care about GitHub's Release and Tags tabs?*

## Prepare a release

~~~
git status
~~~
{: .language-bash}

Make sure that your changes are checked in and that you don't have
extra files sitting around.

Tag the latest commit with a version identifier.
Let's get ready to publish `molecool` 1.0.0a1, the first alpha release of our package.
~~~
git tag 1.0.0a1
~~~
{: .language-bash}

Build a source distribution and a wheel.

~~~
python -m build .
~~~
{: .language-bash}

Note the version string embedded in the distribution archive name.

Note that the untagged post-release version strings
(using our formatting rules in `pyproject.toml`)
do not satisfy PEP 440 and will be rejected if we try to upload to pypi.
This is probably a good thing; it will help keep us from accidentally publishing
releases before they are ready, or messing up our versioning scheme by forgetting
a semantic versioning tag.

{% include links.md %}
