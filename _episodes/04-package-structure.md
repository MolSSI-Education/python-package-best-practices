---
title: "Deciding Package Structure"
teaching: 30
exercises: 0
questions:
- "How should I break my code into modules?"
objectives:
- "Break code into modules and subpackages based on functionality."
keypoints:
- "Your package should be broken up into modules and subpackages depending on the amount of code and functionality."
---

As new features are implemented in codes, it is natural for new functions and objects to be added. In many projects, this often leads to a large number of functionalities defined within a single module. For small, single developer codes, this is not a major issue, but it can still make it difficult to work with. With large or multi-developer codes, this can slow development progress to a crawl as it is difficult to both understand and work with the code.

In this lesson, we will simulate a developing code by starting with a single python module containing all the methods we have developed, and converting it into a well structured package.

## Package Structure
Lets start by reviewing the package structure provided to us by the [CMS CookieCutter]. We have a directory containing our project with a number of additional features. Under our package directory, `molecool`, we can see our current python module `functions.py`. For a more detailed explanation of the rest of the package structure, please review the [package setup] section of the lessons.
```
.
├── LICENSE                         <- License file
├── README.md                       <- Description of project which GitHub will render
├── appveyor.yml                    <- AppVeyor config file for Windows testing (if chosen)
├── molecool
│   ├── __init__.py                 <- Basic Python Package import file
│   ├── functions.py                <- Starting package module
│   ├── data                        <- Sample additional data (non-code) which can be packaged
│   │   ├── README.md
│   │   └── look_and_say.dat
│   ├── tests                       <- Unit test directory with sample tests
│   │   ├── __init__.py
│   │   └── test_functions.py
│   └── _version.py                 <- Automatic version control with Versioneer
├── devtools                        <- Deployment, packaging, and CI helpers directory
│   ├── README.md
│   ├── conda-envs                  <- Environments for testing
│   │   └── test_env.yaml
│   ├── conda-recipe                <- Conda build and deployment skeleton
│   │   ├── bld.bat                 <- Win specific file, not present if Win CI not chosen
│   │   ├── build.sh
│   │   └── meta.yaml
│   ├── scripts
│   │   └── create_conda_env.py     <- OS agnostic Helper script to make conda environments based on simple flags
│   └── travis-ci
│       └── install.sh
├── docs                            <- Documentation template folder with many settings already filled in
│   ├── Makefile
│   ├── README.md                   <- Instructions on how to build the docs
│   ├── _static
│   ├── _templates
│   ├── conf.py
│   ├── index.rst
│   └── make.bat
├── setup.cfg                       <- Near-master config file to make house INI-like settings for Coverage, Flake8, YAPF, etc.
├── setup.py                        <- Your package's setup file for installing with additional options that can be set
├── versioneer.py                   <- Automatic version control with Versioneer
├── .github                         <- GitHub hooks for user contribution and pull request guides
│   ├── CONTRIBUTING.md
│   └── PULL_REQUEST_TEMPLATE.md
├── .codecov.yml                    <- Codecov config to help reduce its verbosity to more reasonable levels
├── .gitignore                      <- Stock helper file telling git what file name patterns to ignore when adding
└── .travis.yml                     <- Travis-CI config file for Linux and OSX testing
```
{: .output}

The easiest way to start is to see what we currently have and try and decide what is related to one another. Looking through the `functions.py` file, we see a number of different functions, we abreviate them here:
```
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
   
def open_xyz(file_location):

def write_xyz(file_location, symbols, coordinates):
    
def calculate_distance(rA, rB):

def calculate_angle(rA, rB, rC, degrees=False):

def draw_molecule(coordinates, symbols, draw_bonds=None, save_location=None, dpi=300):

def bond_histogram(bond_list, save_location=None, dpi=300, graph_min=0, graph_max=2):

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    
def calculate_molecular_mass(symbols):

def calculate_center_of_mass(symbols, coordinates):
```
{: .language-python}

Right at the start we can see two dictionaries of atom data. Clearly these are related and should probably be grouped together. Looking at the functions, we see two functions that handle opening files, `open_pdb` and `open_xyz`, and a function that writes a file, `write_xyz`. It may make sense to group these three together in a module based on input and output.

Lets start making new modules to place our related functions into.

### Atom Data
We will take the `atom_weights` and `atom_colors` dictionaries and move them into a separate module called `atom_data.py`. This is enclosing the constant data that our system is using in a single place. This allows all of the new modules we create to access the data from a single location, avoiding the need to copy the dictionaries to each module that needs them. If we have any other data, related to atoms, used by many of our functions, adding them to this module would be a good idea.
```
"""
Data used for the rest of the package.
"""

atom_weights = {
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
{: .language-python}

> ## Exercise
> Take approximately 10 minutes to look through the rest of the functions in the `functions` module and group them together. Create a module for each group with a reasonable name.
>> ## Answer
>> Here is how we decided to break up the functions:
>> - `calculate_angle` and `calculate_distance` go together in a `measure` module.
>> - `draw_molecule` and `bond_histogram` go into a `visualize` module.
>> - `build_bond_list` is placed into a `molecule` module.
>> - `open_pdb` into a `pdb` module in an `io` package.
>> - `open_xyz` and `write_xyz` are placed into an `xyz` module in an `io` package.
> {: .solution}
{: .challenge}

### Measure
Our `functions.py` file contains two functions that handle taking measurements, `calculate_distance` and `calculate_angle`. Simliar to `atom_data`, we will simply place these in a module within the main package. Since both functions are taking measurements, we will call it `measure.py`.
```
"""
This module is for functions which perform measurements.
"""
def calculate_distance(rA, rB):
    dist_vec = (rA - rB)
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
{: .language-python}

### Visualize
Similarly, we have two functions that handle visulaization of molecules. We will place them into a module called `visualize.py`.
```
"""
Functions for visualization of molecules
"""
def draw_molecule(coordinates, symbols, draw_bonds=None, save_location=None, dpi=300):
    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Get colors - based on atom name
    colors = []
    for atom in symbols:
        colors.append(atom_colors[atom])
    
    size = np.array(plt.rcParams['lines.markersize'] ** 2)*200/(len(coordinates))

    ax.scatter(coordinates[:,0], coordinates[:,1], coordinates[:,2], marker="o",
               edgecolors='k', facecolors=colors, alpha=1, s=size)
    
    # Draw bonds
    if draw_bonds:
        for atoms, bond_length in draw_bonds.items():
            atom1 = atoms[0]
            atom2 = atoms[1]
            
            ax.plot(coordinates[[atom1,atom2], 0], coordinates[[atom1,atom2], 1],
                    coordinates[[atom1,atom2], 2], color='k')
            
    plt.axis('square')
    
    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi, graph_min=0, graph_max=2)
    
    return ax

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
{: .language-python}


### Molecule
Our last function is `build_bond_list` which is not particularly related to any of our other functions. The name `functions.py` does not really give a lot of information about what is available in the module. We can rename the module to something more fitting, say `molecule.py`.
```
def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    if min_bond < 0:
        raise ValueError("Bond length can not be less than zero.")

    if len(coordinates) < 1:
        raise ValueError("Bond list can not be calculated for coordinate length less than 1.")
    
    # Find the bonds in a molecule
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds
```
{: .language-python}


### I/O Package
When looking at the three I/O functions, it may be easy to jump ahead and create an I/O module, as mentioned previously, however, what we really have is two distinct groups of functions that are related. More specifically, we have two functions that handle the input and output of a `.xyz` file and another function that handles the input of a `.pdb`. Each group is handling input and output, but are still somewhat unrelated because of their file type. Instead of making a single module, we are going to create a subpackage to handle i/o and place a module for each group within it.

Create a new directory called io within the package and create two new files (using your operating system or `touch` as prefered):
`pdb.py`
```
"""
Functions for manipulating pdb files.
"""
def open_pdb(file_location):
    with open(file_location) as f:
        data = f.readlines()
    
    coordinates = []
    symbols = []
    
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            
            coords = [float(x) for x in line[30:55].split()]
            coordinates.append(coords)
        
    coords = np.array(coordinates)
    symbols = np.array(symbols)

    return symbols, coords
```
{: .language-python}

and `xyz.py`
```
"""
Functions for manipulating xyz files.
"""
def open_xyz(file_location):
    # Open an xyz file and return symbols and coordinates.
    xyz_file = np.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coords = (xyz_file[:,1:])
    coords = coords.astype(np.float)
    return symbols, coords

def write_xyz(file_location, symbols, coordinates):
    num_atoms = len(symbols)
    
    with open(file_location, 'w+') as f:
        f.write('{}\n'.format(num_atoms))
        f.write('XYZ file\n')
        
        for i in range(num_atoms):
            f.write('{}\t{}\t{}\t{}\n'.format(symbols[i], 
                                              coordinates[i,0], coordinates[i,1], coordinates[i,2]))
```
{: .language-python}
Now any module that needs to handle input and output can import the needed module from the `io` package. Since these are currently small modules, it would not be a big deal to import all of them, but consider a large I/O suite contianing a large number of file types and functionalities, it will quickly create inefficiencies to leave them in one module.

## Fixing Imports
If you try and run some of these functions, you may find yourself with an `ImportError`. This is because the functions can only see the code that has been "loaded" into the module. Each set of functions now exists as standalones within their module. 

If we look at our original `functions.py` module, we will see that we had a number of import statements at the top of the file:
```
import os
import numpy as np
import matplotlib.pyplot as plt
```
{: .language-python}
These are modules that some of the functions need to run. Now that we have moved the functions into separate modules, we need to add in the import statements into each file where they are needed. Lets start by looking at `measure.py`. Looking through the functions, we can see that each of them has a reference to `np`, which is what we imported `numpy` as in `functions.py`. In order to make these functions work again, we need to add the import statement
```
import numpy as np
```
{: .language-python}
to the top of our file.

As a second example, let us look at the `visualize.py` module. We can quikly see that there is a reference to `np` in each of the methods, so we need to add our `numpy` import statement again. We also see references to `plt` which was the name given to `matplotlib.pyplot` when it was imported. Add both of the import statements to the top of the `visualize.py` module.
```
import numpy as np
import matplotlib.pyplot as plt
```
{: .language-python}
If you look closely at the `draw_molecule` function, you will see we have an additional problem with this module. The `draw_molecule` function uses the `atom_colors` dictionary. When all of our code was in a single module, we could simply reference the dictionary by name and use it. However, we have now moved `atom_colors` and `atom_weights` into a separate module. In order to reference the dictionaries in `visualize.py`, we need to import them using an import statement.
```
from .atom_data import atom_colors
```
{: .language-python}
This import statement looks a bit different from the other import statements in our code, we have a `.` before the name. Lets first look at the dot in a different import statement:
```
import matplotlib.pyplot as plt
```
{: .language-python}
In this case, the `.` is saying look within the package `matplotlib` and grab the subpackage (or module) `pyplot`. In our case, we are not using a name before the `.` so where is it looking? It is looking within the current package/directory, or in this case `molecool` for a module or package named `atom_data`, from which it will import the `atom_colors` dictionary.


> ## Check your understanding
> The `molecule.py` module also utilizes functions that are no longer available in the module. Correct the missing import statements in the module.
>> ## Answer
>> The `build_bond_list` functions utilizes the `calculate_distance` function, which is now in the `measure` module, so we want to create a relative import from the `measure` module.
>> ~~~
>> from .measure import calculate_distance
>> ~~~
>> {: .language-python}
> {: .solution}
{: .challenge}


[package setup]: https://molssi-education.github.io/python-package-best-practices/01-package-setup/index.html
[PEP8]: https://www.python.org/dev/peps/pep-0008/
[YAPF]: https://github.com/google/yapf
[numpy style docstrings]: https://docs.scipy.org/doc/numpy/docs/howto_document.html#numpydoc-docstring-guide
[CMS CookieCutter]: https://github.com/MolSSI/cookiecutter-cms