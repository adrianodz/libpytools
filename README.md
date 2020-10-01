[![Build Status](https://travis-ci.org/adrianodz/libpytools.svg?branch=master)](https://travis-ci.org/adrianodz/libpytools)

# libpytools
Python's libs and tips

1) Git commands:

- git branch : list all local branchs

- git branch --all : list all branchs, including remote

- git remote -v: list all remote repositories connected 

- git remote add <name> <repo link> : connect to a remote repo

- git remote rm <name> : disconnect a remote repo

- git fetch --all: update all remote branchs of a remote repo

- git fetch <respository>: update all remote branchs of a specific
remote repo

- git branch <name>: create a local branch

- git checkout <name>: upload files of a specific branch

- git rm -rf .idea : remove the .idea folder from git repo

2) Tests
 - pip install pytest
 - update requirements-dev.txt with libs
 - create a folder package "test" 