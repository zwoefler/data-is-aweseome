# Deutsche Selbstversorgung
With the agricultural sector fighting to keep all of their subsidies, some people asak why the "Selbstversorgungsgrad" aka how much stuff do we actually produce ourselves, is so low for vegetables and fruit.

Although there is much political will involved, there are many more areas where a smiliar question could be asked, but it mostly of the times skipped.

Show the "Selbstversorgungsgrad" for:
- Agricultural products
- Oil & Gas
- Electricity
- Raw materials
- etc.


| Created     | Updated | Data Collection | Data Processing | Visualization |
| ----------- | ------- | --------- | --------- | -------------- |
| 📆 09.01.24 | 📆      | 🛑 BROKEN | 🛑 BROKEN | 🛑 BROKEN |


# 🚀 Vision / Outcome
- Have datasource available as link
- Automated process to retrieve cleaned up data as dataframe
- Visualize all in same chart (percentages)

- Provide sources to explanations why the numbers are the way they are.

# 📋️ Docs
## 🛠️ Setup
Activate Python3 Environment
```BASH
python3 -m venv Env
source Env/bin/activate
pip install -U pip
pip install -r requirements.txt
```


## 🏗️ How to use / Development?
```BASH
python3 deutsche_selbstversorgung/
python3 poc_plot_selbstversorgung.py

# the plot shows up
```

## 🔍️ Dataset exploration

## Data Collection
See Links at the end of this Document

## Data Processing
Cleanup, Parsing, Cutting, Filtering

## Data Visualization
Visualizing the Data


## ❓️ Questions
- WHERE: Germany
- WHEN is the data valid?
- WHO ordered/comissioned/gathered the data?
- HOW was the data gathered?
- WHAT is the public source?



## 🚧 Problems
- Freaking `tabula-py` requres Java...



## 📚️ Resources
Selbstversorgungsgrad Obst & Gemüse 2010/11 - 2020/21 vorläufig
🔗 URL: https://www.bmel-statistik.de/fileadmin/daten/0070010-0000.pdf


Selbstversorgungsgrad - Landwirtschaftliche Erzeugnisse - Excel file
🔗 URL: https://www.bmel-statistik.de/fileadmin/daten/4010200-0000.xlsx

---

Erdöl-Förderung Deutschland:
🔗 URL: https://www.bveg.de/die-branche/erdgas-und-erdoel-in-deutschland/erdoel-in-deutschland/

Erdgasförderung Deutschland:
🔗 URL: https://www.bveg.de/die-branche/erdgas-und-erdoel-in-deutschland/erdgas-in-deutschland/
