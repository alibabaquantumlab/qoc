"""
setup.py - a module to allow package installation
"""

from setuptools import setup, find_packages


NAME = "qoc"
VERSION = "0.1alpha"
DEPENDENCIES = [
    "autograd",
    "filelock",
    "h5py",
    "matplotlib",
    "numba",
    "numpy",
    "scipy",
]
DESCRIPTION = "a package for performing quantum optimal control"
AUTHOR = "Thomas Propson"
AUTHOR_EMAIL = "tcpropson@uchicago.edu"

setup(author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      packages=find_packages(include=['qoc', 'qoc.*']),
      install_requires=DEPENDENCIES,
      name=NAME,
      version=VERSION,
)