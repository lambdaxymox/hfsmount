# HFS Mount
This repository is the source for an installable script for remounting HFS+ volumes on linux.

## Installation
There are two ways to install `hfsplus`.

### Installation From Source
To install `hfsmount`, fork the repo from github
```bash
git clone https://github.com/stallmanifold/hfsmount.git
```
and then run
```bash
python setup.py sdist
python setup.py install --user
```
to install from source.

### Installation From Pip
Run the terminal command
```bash
pip install git+https://github.com/stallmanifold/hfsmount.git
```
to install `hfsplus` via `pip`.

## Usage
Once installed, you can mount HFS+ volumes using
```bash
hfsmount /path/to/device
```
