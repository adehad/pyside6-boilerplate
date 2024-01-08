#!/bin/bash

 git config --global --add safe.directory /workspaces/pyside6-boilerplate

# For Windows users that have cloned into Windows' partition, we do this so that
# it doesn't show all the files as "changed" for having different line endings.
# As we use pre-commit for managing our line endings we do this to tell git we don't care
git config --global core.autocrlf input
git add .

# Install pdm and pre-commit
pipx install pre-commit
pipx install pdm

pdm install
