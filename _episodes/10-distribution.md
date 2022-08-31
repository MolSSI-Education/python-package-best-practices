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

You will also eventually need to get an account on the main pypi.org,
but you can do that later.

Install some additional packages to help build and upload your distribution.
~~~
pip install build twine
~~~
{: .language-bash}

# Preparing a release

## Release notes

Make sure your README file and documentation are up to date.
Check the project description in your project's metadata, too.

Consider whether there is some announcement text that you would
want to include in a text file or in a blurb in your GitHub Releases tab.

*TODO: Do we care about GitHub's Release and Tags tabs?*


## Tagging the release

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

Build the distribution archive(s) for the packaging system you are using (see below): `PyPI` or `Conda`.


# Packages and distributions

A "distribution" is a collection of files including one (or more) Python packages that have been made portable and ready to share.

The cookiecutter template provided several additional files and metadata
to help you get your package ready for distribution,
such as the `LICENSE` file, `MANIFEST.in`, `setup.cfg`, and `pyproject.toml`.

Some of these files are essential details to make your distribution
portable or discoverable.
Others are specific to the build system (e.g. `setuptools` or `conda`).

The build system is responsible for assembling your files into a distribution
archive that can be easily placed into anyone's `site-packages` directory.
It also makes sure that various package metadata is assembled so that a
package installer like `pip` can evaluate software dependencies, and so that
your package looks good when it is shared, such as on pypi.org.

## Distributing packages for `pip install`
* Packaging standards: [Python Packaging Authority](https://packaging.python.org/en/latest/)
* Build system: `setuptools`
* Distribution network: pypi.org

### Building the distribution

We previously mentioned that `pip install .` invokes `setuptools` to build the
distribution archive for our package before installing the package in our
environment.
What does this mean?
More importantly, what does it have to do with letting other people do
`pip install molecool` and get my package automatically downloaded from
"the cloud"?

Setuptools is not the only package for configuring and building Python
distribution archives,
but it is what we will tell `pip` to use for this project.
When `pip install` is run on package sources, it notices the `pyproject.toml` file (which marks a folder as containing
buildable packages),
launches the configured build system, and then installs the resulting "wheel" (distribution archive).
Note that, if we _only_ want to prepare a distribution for sharing,
we can just use the `build` module.

~~~
pip install build
python -m build .
~~~
{: .language-bash}


Note the version string embedded in the distribution archive name.
`versioningit` (configured in `pyproject.toml`) also participated in the build process.
`versioningit` generated a `_version.py` file with a version string derived
from your most recent `git` tag. We will not add this file to our `git`
revision control, but it will be packaged in our distribution.
`versioningit` will regenerate this file as necessary and appropriate.

Note that the untagged post-release version strings
(using our formatting rules in `pyproject.toml`)
do not satisfy PEP 440 and will be rejected if we try to upload to pypi.
This is probably a good thing; it will help keep us from accidentally publishing
releases before they are ready, or messing up our versioning scheme by forgetting
a semantic versioning tag.

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
In preparation, `setuptools` no longer requires `distutils` or `setup.py`,
and can be configured entirely with `pyproject.toml`.
{: .callout}

### Building and uploading to PyPI

Refer to https://packaging.python.org/en/latest/tutorials/packaging-projects/
for build-system-agnostic tutorial on
* packaging Python projects for distribution
* publishing packages to pypi.org for automatic download with `pip install`

You will note that most of the configuration described in the packaging tutorial
has already been pre-configured by the cookiecutter.

Essentially, once you have an account on `pypi.org` and you have built
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

For more in depth documentation on packaging for PyPI specifically with setuptools,
see https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/


## Distributing packages for `conda install`

`conda` has a completely different approach to building and distributing
packages, and is not yet PEP-517 compliant.
(It does not use `pyproject.toml`.)
For information about using `conda build`,
preparing your build details and metadata with `meta.yml`,
and publishing packages through a conda channel like `conda-forge`,

*new content...*

# Preparing for future releases
 
Consider adding or updating a CHANGELOG.

## Version specifiers

Python has a strict syntax for version strings.

* Refer to [PEP 440](https://peps.python.org/pep-0440/) for constraints on Python version specifiers.
* Know how to mark versions for pre-release (or post-release) and consider
  tagging "alpha" and "beta" releases.
  
## Versioning semantics

Refer to [Semantic Versioning](https://semver.org) for guidelines on how to use versions meaningfully.

Once your package has outside users, consider how your changes affect
your users.
Avoid surprising your users by effectively supporting the package manager heuristics
(e.g. use prerelease version semantics to make a version only available when `pip install --pre` is used).
Make sure your version increments reflect the compatibilty changes
in the distributions you release.

Making these considerations may lead you to moderate the changes you make.
For instance, instead of completely changing an interface,
consider introducing a new function or module with a different name.
Or provide backwards compatible support for the old interfaces.
> ## Consider
> Is this a completely incompatible change to the interface?
>> ## Versioning strategy
>> Probably a major version increment.
> {: .solution}
 {: .challenge}
> ## Consider
> Is this a backwards compatible update, or a new feature that does not conflict with existing features?
>> ## Strategy
>> Probably a minor version increment.
> {: .solution}
 {: .challenge}
> ## Consider
>Is this an internal change or bug fix that you don't expect users to notice (but who knows? there could be a bug...)?
>> ## Strategy
>> Use a patch release version increment.
> {: .solution}
 {: .challenge}
> ## Consider
> Is this a change to documentation or something that does not affect the code at all, with no implications for compatibility, but you just need some sort of version bump so that people get your edit the next time the package is downloaded?
>> ## Strategy
>> Use a "tweak" version or post-release version. Check [PEP 440](https://peps.python.org/pep-0440/) for
>> appropriate syntax.
> {: .solution}
 {: .challenge}

{% include links.md %}
