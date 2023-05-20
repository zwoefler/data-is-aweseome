#!/bin/bash

project_name=$1

mkdir $project_name

cd $project_name

touch requirements.txt

echo "pandas" >> requirements.txt
echo "jupyter" >> requirements.txt
echo "requests" >> requirements.txt
echo "python-dotenv" >> requirements.txt

cp ../develop.sh .

python3 -m venv Env

source Env/bin/activate

pip install --upgrade pip

pip install -r requirements.txt
