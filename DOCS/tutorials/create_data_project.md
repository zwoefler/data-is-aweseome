# 🚀 Create a Data Project

So you have the idea to a new data story project?
These are the technical steps you need to follow:

You already cloned this repo and are in the root directory of this project `data-is-awesome`

```bash
# Create new Project folder
mkdir <YOUR_PROJECT_NAME>
cd <YOUR_PROJECT_NAME>

# Add necessary files
touch requirements.txt
touch README.md
mkdir data/


# Create Python Environment
python3 -m venv Env
source Env/bin/activate
pip install -r requirements.txt
```

## 🧩 Aspects of your project
All your steps must be reproducable!

**Data Collection**: A simple reproducable way to gather the data
**Data Processing**: Cleaning duplicates, usable data schema
**Visualization**: Script to load your cleaned data and visualize
