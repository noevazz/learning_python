```
packages
└── extra
    ├── good
    │   ├── alpha.py
    │   ├── best
    │   │   ├── sigma.py
    │   │   └── tau.py
    │   └── beta.py
    ├── __init__.py
    ├── iota.py
    └── ugly
        ├── omega.py
        └── psi.py

how do you transform such a tree (actually, a subtree) into a real Python package (in other words, how do you convince Python that such a tree is not just a bunch of junk files, but a set of modules)?
where do you put the subtree to make it accessible to Python?

    answer: packages, like modules, may require initialization.

Python expects that there is a file with a very unique name inside the package's folder: __init__.py.

The content of the file is executed when any of the package's modules is imported. If you don't want any special initializations, you can leave the file empty, but you mustn't omit it.
```