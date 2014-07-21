#!/usr/bin/env python3
import os
from setuptools import setup

def read(fname):
    """
    Read a file in this directory.
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="hh_mpw",
    version="0.1",
    author="Robert Tyler Stephens",
    author_email="roberttstephens@gmail.com",
    description=("Determine the miles per week for a hal higdon program."),
    license="GNU General Public License v3",
    url="https://github.com/roberttstephens/hal-higdon-miles-per-week",
    packages=['hh_mpw'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    install_requires=[
        "requests",
        "lxml",
        "cssselect",
    ],
    entry_points={
        'console_scripts': [
            'hh_mpw = hh_mpw.hh_mpw:main',
        ]
    },
)
