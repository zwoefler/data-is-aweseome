#!/bin/bash

# is subproject name provided?
if [ -z "$1" ]; then
    echo "Usage: $0 <subproject_name>"
    exit 1
fi

# Subproject name in lowercase with underscores
SUBPROJECT_NAME=$(echo "$1" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')

if [ -d "$SUBPROJECT_NAME" ]; then
    echo "Subproject '$SUBPROJECT_NAME' already exists."
    exit 0
else
    # Create subproject folder + necessary folders
    mkdir "$SUBPROJECT_NAME"
    cd "$SUBPROJECT_NAME" || exit
    mkdir data tests docs

    # Create README.md
    echo "# $1" > README.md

    # Create requirements.txt
    echo "requests" > requirements.txt
    echo "pandas" >> requirements.txt
    echo "matplotlib" >> requirements.txt
    echo "numpy" >> requirements.txt

    python3 -m venv Env
    source Env/bin/activate

    pip install -U pip
    pip install -r requirements.txt

    echo "Subproject '$SUBPROJECT_NAME' created"
    echo "Virutal Environment installed"
    echo "\n"
    echo "Start developing with the following instructions:"
    echo "cd '$SUBPROJECT_NAME'"
    echo "source Env/bin/activate"
fi