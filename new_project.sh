#!/bin/bash

project_name=$1

mkdir $project_name

cd $project_name

touch requirements.txt

echo "pandas" >> requirements.txt
echo "jupyter" >> requirements.txt

cp ../develop.sh .

python3 -m venv Env

pip install --upgrade pip

pip install -r requirements.txt
