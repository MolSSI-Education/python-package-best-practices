
# Deciding Package Structure

```{admonition} Overview
:class: overview

Questions:

* How should I organize my code?

* How can I handle imports in my package?

Objectives:

* Break code into modules and subpackages based on functionality.

* Understand how the `__init__.py` file affects your Python package.

```
:::{admonition} Follow Along with This Lesson
:class: tip

To follow along with this lesson, you can complete the previous lessons,
or you can download a pre-made workshop repository that is at the starting 
point.

- [Download the pre-made workshop repository as a zip file](https://github.com/MolSSI-Education/molecool/archive/refs/tags/deciding-package-structure-start.zip)

Alternatively, download the repository using the command line:

````{tab-set-code} 
```{code-block} shell
git clone https://github.com/MolSSI-Education/molecool.git
git checkout deciding-package-structure-start
```
````
:::

As new features are implemented in codes, it is natural for new functions and objects to be added.
In many projects, this often leads to a large number of functionalities defined within a single module.
For small, single developer codes, this is not a major issue, but it can still make code difficult to work with.
With large or multi-developer codes, this can slow development progress to a crawl as it is difficult both to understand and work with the code.

In this lesson, we will simulate a developing piece of software.
We will start with a single python module containing all the methods we have developed,
and convert it into a well-structured package.

## Package Structure
Let's start by reviewing the package structure provided to us by the [CMS CookieCutter].
We have a directory containing our project with a number of additional features.
Under our package directory, `molecool`, we can see our current python module `functions.py`.
For a more detailed explanation of the rest of the package structure,
please review the [package setup] section of the lessons.

```{code-block}
.
├── CODE_OF_CONDUCT.md              <- Code of Conduct for developers and users
├── LICENSE                         <- License file
├── MANIFEST.in                     <- Packaging information for pip
├── README.md                       <- Description of project which GitHub will render
├── molecool                        <- Basic Python Package import file
│   ├── __init__.py                 <- Basic Python Package import file
│   ├── functions.py                <- Starting package module
│   ├── data                        <- Sample additional data (non-code) which can be packaged. Just an example, delete in production
│   │   ├── README.md
│   │   └── look_and_say.dat
│   └── tests                       <- Unit test directory with sample tests
│       ├── __init__.py
│       └── test_molecool.py
├── devtools                        <- Deployment, packaging, and CI helpers directory
│   ├── README.md
│   ├── conda-envs                  <- Conda environments for testing
│   │   └── test_env.yaml
│   └── scripts
│       └── create_conda_env.py     <- OS agnostic Helper script to make conda environments based on simple flags
├── docs                            <- Documentation template folder with many settings already filled in
│   ├── Makefile
│   ├── README.md                   <- Instructions on how to build the docs
│   ├── _static
│   │   └── README.md
│   ├── _templates
│   │   └── README.md
│   ├── api.rst
│   ├── conf.py
│   ├── getting_started.rst
│   ├── index.rst
│   ├── make.bat
│   └── requirements.yaml           <- Documenation building specific requirements. Usually a smaller set than the main program
├── readthedocs.yml
├── pyproject.toml                  <- Generic Python build system configuration (PEP-517).
├── setup.cfg                       <- Near-master config file to make house INI-like settings for Coverage, Flake8, YAPF, etc.
├── setup.py                        <- Your package's setup file for installing with additional options that can be set
├── .codecov.yml                    <- Codecov config to help reduce its verbosity to more reasonable levels
├── .github                         <- GitHub hooks for user contribution, pull request guides and GitHub Actions CI
│   ├── CONTRIBUTING.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows
│       └── CI.yaml
├── .gitignore                      <- Stock helper file telling git what file name patterns to ignore when adding files
└── .lgtm.yml
```

The easiest way to start is to see what we currently have and try to decide which parts are related to one another.
Looking through the `functions.py` file, we see a number of different functions,
and for the sake of simplicity we abbreviate and rearrange them here:

````{tab-set-code} 

```{code-block} functions.py
atomic_weights = {
    'H': 1.00784,
    'C': 12.0107,
    'N': 14.0067,
    'O': 15.999,
    'P': 30.973762,
    'F': 18.998403,
    'Cl': 35.453,
    'Br': 79.904,
}

atom_colors = {
    'H': 'white',
    'C': '#D3D3D3',
    'N': '#add8e6',
    'O': 'red',
    'P': '#FFA500',
    'F': '#FFFFE0',
    'Cl': '#98FB98',
    'Br': '#F4A460',
    'S': 'yellow'
}

def open_pdb(file_location):
    ...
   
def open_xyz(file_location):
    ...

def write_xyz(file_location, symbols, coordinates):
    ...
    
def calculate_distance(rA, rB):
    ...

def calculate_angle(rA, rB, rC, degrees=False):
    ...

def draw_molecule(coordinates, symbols, draw_bonds=None, save_location=None, dpi=300):
    ...

def bond_histogram(bond_list, save_location=None, dpi=300, graph_min=0, graph_max=2):
    ...

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    ...
    
def calculate_molecular_mass(symbols):
    ...

def calculate_center_of_mass(symbols, coordinates):
    ...
```
````


Right at the start we can see two dictionaries of atom data. Clearly these are related and should probably be grouped together.
Looking at the functions, we see two functions that handle opening files, `open_pdb` and `open_xyz`, and a function that writes a file, `write_xyz`.
It may make sense to group these three together in a module based on input and output.

Let's start making new modules to place our related functions into.

### Atom Data
We will take the `atomic_weights` and `atom_colors` dictionaries and move them into a separate module called `atom_data.py`.
This is enclosing the constant data that our system is using in a single place.
This allows all the new modules we create to access the data from a single location, avoiding the need to copy the dictionaries to each module that needs them.
If we have any other data, related to atoms, used by many of our functions, adding them to this module would be a good idea.

````{tab-set-code} 

```{code-block} atom_data.py
"""
Data used for the rest of the package.
"""

atomic_weights = {
    'H': 1.00784,
    'C': 12.0107,
    'N': 14.0067,
    'O': 15.999,
    'P': 30.973762,
    'F': 18.998403,
    'Cl': 35.453,
    'Br': 79.904,
}

atom_colors = {
    'H': 'white',
    'C': '#D3D3D3',
    'N': '#add8e6',
    'O': 'red',
    'P': '#FFA500',
    'F': '#FFFFE0',
    'Cl': '#98FB98',
    'Br': '#F4A460',
}
```
````


## Exercise - Grouping into Modules

``````{admonition} Exercise - Grouping into Modules
:class: exercise

Take approximately 10 minutes to look through the rest of the functions in the `functions` module and group them together.
Create a module for each group with a reasonable name.

`````{admonition} Solution
:class: solution dropdown

Here is how we decided to break up the functions:
- `calculate_angle` and `calculate_distance` go together in a `measure` module.
- `draw_molecule` and `bond_histogram` go into a `visualize` module.
- `build_bond_list` is placed into a `molecule` module.
- `open_pdb` go into a `pdb` module in an `io` subpackage.
- `open_xyz` and `write_xyz` are placed into an `xyz` module in an `io` subpackage.
`````
``````

### Measure Module
Our `functions.py` file contains two functions that handle taking measurements:
`calculate_distance` and `calculate_angle`.
Similar to `atom_data`, we will simply place these in a module within the main package.
Since both functions are taking measurements, we will call it `measure.py`.

````{tab-set-code} 

```{code-block} measure.py

"""
This module is for functions that perform measurements.
"""

def calculate_distance(rA, rB):
    """Calculate the distance between two points.

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between the two points.

    Examples
    --------
    >>> r1 = np.array([0, 0, 0])
    >>> r2 = np.array([0, 0.1, 0])
    >>> calculate_distance(r1, r2)
    0.1
    """

    dist_vec = rA - rB
    distance = np.linalg.norm(dist_vec)

    return distance

def calculate_angle(rA, rB, rC, degrees=False):
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
```
````


### Visualize Module
Similarly, we have two functions that handle visualization of molecules.
We will place them into a module called `visualize.py`.

````{tab-set-code} 

```{code-block} visualize.py
"""
Functions for visualization of molecules
"""

def draw_molecule(coordinates, symbols, draw_bonds=None, save_location=None, dpi=300):

    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Get colors - based on atom name
    colors = []
    for atom in symbols:
        colors.append(atom_colors[atom])

    size = np.array(plt.rcParams["lines.markersize"] ** 2) * 200 / (len(coordinates))

    ax.scatter(
        coordinates[:, 0],
        coordinates[:, 1],
        coordinates[:, 2],
        marker="o",
        edgecolors="k",
        facecolors=colors,
        alpha=1,
        s=size,
    )

    # Draw bonds
    if draw_bonds:
        for atoms, bond_length in draw_bonds.items():
            atom1 = atoms[0]

def bond_histogram(bond_list, save_location=None, dpi=300, graph_min=0, graph_max=2):
    lengths = []
    for atoms, bond_length in bond_list.items():
        lengths.append(bond_length)
    
    bins = np.linspace(graph_min, graph_max)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    plt.xlabel('Bond Length (angstrom)')
    plt.ylabel('Number of Bonds')
    
    ax.hist(lengths, bins=bins)
    
    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi)
    
    return ax
```
````



### Molecule Module
Our last function is `build_bond_list`, which is not particularly related to any of our other functions.
The name `functions.py` does not really give a lot of information about what is available in the module.
We can rename the module to something more fitting, say `molecule.py`.
We also add a docstring.

````{tab-set-code} 

```{code-block} molecule.py
"""
Functions for molecule analysis
"""

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    """
    Build a list of bonds in a set of coordinates based on a distance criteria.

    Parameters
    ----------
    coordinates: np.ndarray
        The coordinates of the atoms to analyze in an (natoms, ndim) array.

    max_bond: float, optional
        The maximum distance for two atoms to be considered bonded.

    min_bond: float, optional
        The minimum distance for two atoms to be considered bonded.

    Returns
    -------
    bonds: dict
        A dictionary containing bonded atoms with atom pairs as keys and the distance between the atoms as the value.
    """

    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds
```
````



### I/O Subpackage
When looking at the three I/O functions,
it may be easy to jump ahead and create an I/O module, as mentioned previously.
However, what we really have is two distinct groups of functions that are related.
More specifically,
we have two functions that handle the input and output of a `.xyz` file
and another function that handles the input of a `.pdb`.
Each group is handling input and output,
but are still somewhat unrelated because of their file type.
Instead of making a single module,
we are going to create a subpackage to handle i/o and place a module for each group within it.

Create a new directory called "io" within the package (using the command 'mkdir directory_name') and create two new files `pdb.py` and `xyz.py` (using the command `touch file_name`):


````{tab-set-code} 

```{code-block} io/pdb.py
"""
Functions for manipulating pdb files.
"""

def open_pdb(file_location):
    """Open and read coordinates and atom symbols from a pdb file.

    The pdb file must specify the atom elements in the last column, and follow
    the conventions outlined in the PDB format specification.

    Parameters
    ----------
    file_location : str
        The location of the pdb file to read in.

    Returns
    -------
    coords : np.ndarray
        The coordinates of the pdb file.
    symbols : list
        The atomic symbols of the pdb file.

    """

    with open(file_location) as f:
        data = f.readlines()

    coordinates = []
    symbols = []
    for line in data:
        if "ATOM" in line[0:6] or "HETATM" in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coords = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coords)

    coords = np.array(coordinates)
    symbols = np.array(symbols)

    return symbols, coords
```
````

````{tab-set-code} 

```{code-block} io/xyz.py
"""
functions for manipulating xyz files.
"""

def open_xyz(file_location):

    # Open an xyz file and return symbols and coordinates.
    xyz_file = np.genfromtxt(fname=file_location, skip_header=2, dtype="unicode")
    symbols = xyz_file[:, 0]
    coords = xyz_file[:, 1:]
    coords = coords.astype(float)
    return symbols, coords


def write_xyz(file_location, symbols, coordinates):

    num_atoms = len(symbols)

    if num_atoms != len(coordinates):
        raise ValueError(
            f"write_xyz : the number of symbols ({num_atoms}) and number of coordinates ({len(coordinates)}) must be the same to write xyz file!"
        )

    with open(file_location, "w+") as f:
        f.write("{}\n".format(num_atoms))
        f.write("XYZ file\n")

        for i in range(num_atoms):
            f.write(
                "{}\t{}\t{}\t{}\n".format(
                    symbols[i], coordinates[i, 0], coordinates[i, 1], coordinates[i, 2]
                )
            )
```
````


Now any module that needs to handle input and output can import the needed module from the `io` subpackage.
Since these are currently small modules, it would not be a big deal to import all of them.
But, consider a large I/O suite containing a large number of file types and functionalities.
It will quickly create inefficiencies to leave them in one module.

Now that we've organized and changed the structure in our project,
we should commit our changes and push to GitHub.

````{tab-set-code} 

```{code-block} shell
git add .
git commit -m "organize molecool into modules and subpackage"
git push origin main
```
````

## Fixing Imports
When we first copied the functions from the Jupyter Notebook into `functions.py`,
we were able to import `molecool` package and access the functions within `functions.py`.
After we extracted the functions from that file, we won't be able to import those functions in the same way.
In fact, we won't be able to access them at all.
Every time we restructure our code or create new folders we have to be careful and modify the `__init__.py` accordingly.
Let us then add the new functions into the `__init__.py`.

````{tab-set-code} 

```{code-block} __init__.py
# Add imports here
from .functions import *
from .measure import calculate_distance, calculate_angle
from .molecule import build_bond_list
from .visualize import draw_molecule, bond_histogram
```
````


In this way, we should be able to call each of the functions after importing our module.

````{tab-set-code} 

```{code-block} python
>>> import molecool
>>> molecool.build_bond_list()
```
````


Even with the imports fixed, if you try to run some of these functions,
you may find yourself with an `ImportError`.
This is because the functions can only see the code that has been "loaded" into their module.
Each set of functions now exist in the context of their module "namespace".

If we look at our original `functions.py` module,
we will see that we had a number of import statements at the top of the file:

````{tab-set-code} 

```{code-block} original_functions.py
import os
import numpy as np
import matplotlib.pyplot as plt
```
````


These are modules that are needed by some functions.
Now that we have moved the functions into separate modules,
we need to add the `import` statements into each file where they are needed.
Let's start by looking at `measure.py`.
Looking through the functions, we can see that each of them has a reference to `np`,
which is what we imported `numpy` as in `functions.py`. 

Aside from visual inspection,
you could have also seen these missing imports by using `flake8` on the modules.

````{tab-set-code} 

```{code-block} shell
flake8 measure.py
```
````


You will see a message which says "undefined name np".

In order to make these functions work again, we need to add the following `import` statement.

````{tab-set-code} 

```{code-block} python
import numpy as np
```
````


to the top of our file.

As a second example, let us look at the `visualize.py` module.
We can quickly see that there is a reference to `np` in each of the methods,
so we need to add our `numpy` import statement again.
We also see references to `plt` which was the name given to `matplotlib.pyplot` when it was imported.
Add imports of the external libraries to the top of the `visualize.py` module.
Of course, don't forget our "unused import" for 3D axes.

````{tab-set-code} 

```{code-block} visualize.py
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
```
````


If you use `flake8` (or if you carefully inspect), you will also see that `atom_colors` is missing.
The `draw_molecule` function uses the `atom_colors` dictionary.
When all of our code was in a single module, we could simply reference the dictionary by name and use it.
However, we have now moved `atom_colors` and `atomic_weights` into a separate module.
In order to reference the dictionaries in `visualize.py`, we need to import them using an import statement.
This is an intra-package import, meaning that we are importing modules from within our packages to other imports in our package (see intra package imports [here](https://docs.python.org/3/tutorial/modules.html))

````{tab-set-code} 

```{code-block} visualize.py
from .atom_data import atom_colors
```
````


This import statement looks a bit different from the other import statements in our code, we have a `.` before the name.
This is because it is a *relative import*. Just like when using bash, a dot (`.`) means to look in the current folder. 

To think about this more, let's first look at the dot in a different `import` statement:

````{tab-set-code} 

```{code-block} python
import matplotlib.pyplot as plt
```
````


In this case, the `.` is saying look within the package `matplotlib` and grab the subpackage (or module) `pyplot`.
In our case, we are not using a name before the `.` so where is it looking?
It is looking within the current package/directory, or in this case `molecool` for a module or package named `atom_data`, from which it will import the `atom_colors` dictionary.

### Check your Understanding - Relative Imports

``````{admonition} Check your Understanding
:class: exercise

The `molecule.py` module also utilizes functions that are no longer available in the module.
Correct the missing import statements in the module.

`````{admonition} Solution
:class: solution dropdown

The `build_bond_list` functions utilizes the `calculate_distance` function, which is now in the `measure` module, so we want to create a relative import from the `measure` module.
````{tab-set-code} 

```{code-block} molecule.py

from .measure import calculate_distance
```
````
`````
``````

### Using `import *`

We have moved all of our functions into modules and we've updated our `__init__.py` file.
If you use a Python interpreter in a directory which is not directly above your project, you can see the consequences of this.
We can use the `dir` functions to see what is available in a particular module or object:

````{tab-set-code}
```{code-block} python
>>> import molecool
>>> dir(molecool)
```
````

You should see something similar to the following

````{tab-set-code} 

```{code-block} output
['__builtins__', '__cached__', '__doc__', '__file__', '__git_revision__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_version', 'functions', 'np', 'plt', 'calculate_distance', 'calculate_angle,
'build_bond_list', 'draw_molecule', 'bond_histogram' ]
```
````

These are all the things available to us from importing `molecool`.
You will see your `functions` module, but you will also see `np` and `plt`.
This comes from using `from .functions import *` and is why using `import *` is usually considered a bad practice.

Since we are no longer using any code from `functions.py`, we will remove the statement importing it from `__init__.py`.

### IO Subpackage

We haven't yet included our `io` subpackage, meaning that the user would have to import this package if they wanted to use it.
For example, to use the xyz functions,

````{tab-set-code} 

```{code-block} python
>>> import molecool.io.xyz
>>> dir(molecool.io.xyz.open_xyz)
```
````


This will work, however, the main reason we broke up the modules within the `io` package was for development convenience.
Right now this has come at the cost of slightly more complicated import statements to get access to any function.

We can, of course, edit our `__init__.py` file to make this simpler.
At this point, the way we actually do this import is going to be stylistic - how do you want people to interact with your package?

The goal we are going for is to call an IO function using

````{tab-set-code} 

```{code-block} python
molecool.io.IO_FUNCTION
```
````


where `IO_FUNCTION` is any function relating to IO.

Within the `io` directory, create a new file called `__init__.py`.
Open that file with your desired editor and add the following two lines.

````{tab-set-code} 

```{code-block} __init__.py
from .pdb import open_pdb
from .xyz import open_xyz, write_xyz
```
````

These lines are relative import statements to the functions within the `io` package.
Think of them as pointers to the functions.
When we look at the `io` package, it directs us to the location of the underlying functions,
so we do not need to look within each submodule.
This allows us to use the following `import` statement to our top level `__init__.py` to access the functions:

````{tab-set-code} 

```{code-block} __init__.py
from . import io
```
````


We can now call our I/O functions using our target syntax.

````{tab-set-code} 

```{code-block} python
>>> molecool.io.open_pdb()
```
````


If we wanted the I/O functions to mimic the imports from the rest of the modules,
we could modify our top level `__init__.py` file to reflect that.

````{tab-set-code} 

```{code-block} __init__.py
from .measure import calculate_distance, calculate_angle
from .molecule import build_bond_list
from .visualize import draw_molecule, bond_histogram
from .io import open_pdb, open_xyz, write_xyz
```
````



We could even make these functions more accessible by removing the need for the  `io` module.

This would allow us to call functions by simply typing the following.

````{tab-set-code} 

```{code-block} python
>>> molecool.open_pdb()
```
````


You can now appreciate how the `__init__.py` file plays such an important role in defining how the user imports the functions in the package. 

Now that we've made some changes to `__init__.py`,
we should commit our changes and push to GitHub.

````{tab-set-code} 

```{code-block} shell
git add .
git commit -m "fixing imports"
git push origin main
```
````

:::{admonition} Final Repository State
:class: tip

You can see the final state of the repository after this section [here](https://github.com/MolSSI-Education/molecool/tree/5b7642b7fa140a833bc618a1561bc4a08d433257).

You can also download a zip of the repository [here](https://github.com/MolSSI-Education/molecool/archive/refs/tags/deciding-package-structure-end.zip).

:::

## Key Points

```{admonition} Key Points
:class: key

- Your package should be broken up into modules and subpackages depending on the amount of code and functionality.
- You can use the `__init__.py` file to define what packages are imported with your package, and how the user interacts with it.
```


[package setup]: https://molssi-education.github.io/python-package-best-practices/01-package-setup/index.html
[PEP8]: https://www.python.org/dev/peps/pep-0008/
[YAPF]: https://github.com/google/yapf
[numpy style docstrings]: https://docs.scipy.org/doc/numpy/docs/howto_document.html#numpydoc-docstring-guide
[CMS CookieCutter]: https://github.com/MolSSI/cookiecutter-cms
